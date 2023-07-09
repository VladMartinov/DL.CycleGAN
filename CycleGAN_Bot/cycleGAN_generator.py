#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn

class ConvBlock(nn.Module):
  def __init__(self, input_chanels, out_chanels, is_down=True, is_act=True, **kwargs):
    super().__init__()

    self.conv_block = nn.Sequential(
        nn.Conv2d(input_chanels, out_chanels, padding_mode="reflect", **kwargs)
        if is_down
        else nn.ConvTranspose2d(input_chanels, out_chanels, **kwargs),
        nn.ReLU(inplace=True) if is_act else nn.Identity(),
    )

  def forward(self, x):
    return self.conv_block(x)

class ResidualBlock(nn.Module):
    def __init__(self, chanels):
      super().__init__()

      self.res_block = nn.Sequential(
          ConvBlock(chanels, chanels, kernel_size=3, padding=1),
          ConvBlock(chanels, chanels, is_act=False, kernel_size=3, padding=1),
      )

    def forward(self, x):
      return x + self.res_block(x)


# GAN Generator #
class Generator(nn.Module):
    def __init__(self, input_channels=3, num_features=[64, 128, 256, 512], num_residual_blocks=9):
        super().__init__()
        #---------------------------------------------------
        # We create the generator with the next arhitecture:
        # Conv2d -> ReLU
        # 2 * ConvBlock(down)
        # num_residual_blocks * ResidualBlock
        # 2 * ConvBlock(up)
        # Conv2d -> tanh
        #---------------------------------------------------

        # Convolution Layears
        self.initial_blocks = nn.Sequential(
            nn.Conv2d(input_channels, num_features[0], kernel_size=7, stride=1, padding=3, padding_mode="reflect"),
            nn.ReLU(inplace=True),
        )

        self.down_blocks = nn.ModuleList(
            [
                ConvBlock(num_features[0], num_features[1], kernel_size=3, stride=2, padding=1),
                ConvBlock(num_features[1], num_features[2], kernel_size=3, stride=2, padding=1),
            ]
        )

        self.res_blocks = nn.Sequential(
            *[ResidualBlock(num_features[2]) for _ in range(num_residual_blocks)]
        )

        self.up_blocks = nn.ModuleList(
            [
                ConvBlock(num_features[2], num_features[1], is_down=False, kernel_size=3, stride=2, padding=1, output_padding=1),
                ConvBlock(num_features[1], num_features[0], is_down=False, kernel_size=3, stride=2, padding=1, output_padding=1),
            ]
        )

        self.last_layer = nn.Conv2d(num_features[0], input_channels, kernel_size=7, stride=1, padding=3, padding_mode="reflect")

    def forward(self, x):
        x = self.initial_blocks(x)

        for layer in self.down_blocks:
          x = layer(x)

        for layer in self.res_blocks:
          x = layer(x)

        for layer in self.up_blocks:
          x = layer(x)

        x = self.last_layer(x)

        return torch.tanh(x)

