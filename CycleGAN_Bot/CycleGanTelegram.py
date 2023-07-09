#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install torchvision --user


# In[ ]:


import telebot

import numpy as np
from cycleGAN_generator import Generator

import io
import os

# For generative model
import torch
import torch.nn as nn

from PIL import Image
import torchvision.transforms as transforms


# In[ ]:


# Получаем токен API для бота
bot_token = '6131296601:AAGz_jpnZ4LLvHpOjKmDW1hW0GqUYxYOjXA'
bot = telebot.TeleBot(token=bot_token)

# Использование GPU если оно есть
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device: {device}.")


# In[ ]:


transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(size = (256,256)),
        ])


# In[ ]:


genM = Generator(input_channels=3, num_residual_blocks=9).to(device)

# Загружаем генеративную модель GAN
checkpoint = torch.load('genm.pth.tar', map_location=device)
genM.load_state_dict(checkpoint["state_dict"])


# In[ ]:


# Обработчик запросов от бота
@bot.message_handler(content_types=['photo'])
def bot_handler(message):   
    # Получаем входное фото, сохраняем его
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    file_path = file.file_path

    file = bot.download_file(file.file_path)
    
    src = 'photo_input.' + file_path.split('.')[-1];
    with open(src, 'wb') as new_file:
        new_file.write(file)
        
    # Переводим его в тензор, ресайзим, отправляем генератору
    photo_img = np.array(Image.open(src).convert("RGB"))
    
    generated_monet_image = genM(transform(photo_img))

    # Преобразуем выходной тензор в изображение
    image = generated_monet_image.squeeze().permute(1, 2, 0).clamp(0, 1).detach().numpy()
    image = (image * 255).astype('uint8')
    pil_image = Image.fromarray(image)
    
    # Отправляем сгенерированное изображение в ответ на запрос от бота
    bio = io.BytesIO()
    pil_image.save(bio, format='PNG')
    bio.seek(0)
    
    text = "Сгенерированное Monet фото для вас " + message.from_user.username
    
    bot.send_photo(message.chat.id, photo=bio, caption=text)

    return 'ok'


# In[ ]:


def main():
    bot.polling()


# In[ ]:


if __name__ == '__main__':
    main()

