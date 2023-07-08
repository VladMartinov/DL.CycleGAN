<h1 align="middle">Проект по реализации <b>генеративной модели (CycleGAN)</b>.</h1>
<ul>
  <li><h4>Выполнил: Мартынов Владислав</h4></li>
  <li><h4>Поток: Продвинутый</h4></li>
  <li><h4>StepikID: 596247708</h4></li>
  <li><h4>GitHub: <a href=""https://github.com/VladMartinov>VladMartinov</a></h4></li>
</ul>
<h2 align="middle">Решаемая задача:</h2>
<ul>
  <li><h4>Monet2Photo</h4></li>
  <li><h4>Photo2Anime (Comming soon)</h4></li>
</ul>
<h2 align="middle">Пояснение:</h2>
<p>В данной проекте была реализована задача стилизации из обычной фотографии в монет и обратно при помощи возможностей Cycle GAN. А именно была решена задача Monet2Photo.</p>
<h2 align="middle">Кратко про модели и обучение:</h2>
<p>Все модели были основаны на основной документации и слегка модернезированы. Генераторы состоят из 9-и residual-блоков и down/up convolution layears, а так же активацией ReLU.</p>
<p>Дискриминаторы же в свою очередь состоит из Instance Block's а так же convolution layears, активация применяется LeakyReLU, а на выходе применяется sigmoid (архитектура напоминающая PathGAN).</p>
<p>Модель обучалась на датасете из 6 тыс. картинок около 200 эпох.</p>
<p>Так же был реализован дополнительный буфер для дискриминатора (количество изображений в буфере = 100).</p>
<h2 align="middle">Процесс обучения.</h2>
<p>На вход подаются изображения размерностью 256 x 256. Выходные изображение будут иметь такую же размерность.</p>
<p>Присутствует возможность обучения уже как существующих моделей так и обучение новых. Так же можно сохронять прогресс после каждой эпохи (как изображений, так и моделей).</p>
<hr>
<p>Таким образом для обучения необходим датасет с изображениями 256 x 256 (другие не тестировались), желательно чтобы датасет был сбалансирован (не было такого, что допустим monet было в 2-а раза больше photo или наоборот).</p>
<p>На выходе у нас могут сохранятся изображения в ходе обучения, а так же весы моделей.</p>
<p>Пути к датасетам можно прописать в .ipynb файле где можно и настроить обучение (количество эпох, лямбды, пути к датасету и многое др.)</p>
<h2 align="middle">Примеры получившихся результатов:</h2>
<ul>
  <li>
		<h4 align="middle">Monet2Photo:</h4>
		<table align="center">
			<thead>
				<tr>
					<th>Исходная:</th>
					<th>Результата преобразования:</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Body content 1</td>
					<td>Body content 2</td>
				</tr>
			</tbody>
		</table>
	</li>
  <li>
		<h4 align="middle">Photo2Anime (Comming soon)</h4>
		<table align="center">
			<thead>
				<tr>
					<th>Исходная:</th>
					<th>Результата преобразования:</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Empty...</td>
					<td>Empty...</td>
				</tr>
			</tbody>
		</table>
	</li>
</ul>
<hr>
<h2>Используемая литература:</h2>
<ol>
  <li><h4><a href="https://arxiv.org/pdf/1703.10593.pdf">Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.</a></h4></li>
  <li><h4><a href="https://www.youtube.com/watch?v=5jziBapziYE&list=PLhhyoLH6IjfwIp8bZnzX8QR30TRcHO8Va&index=8">CycleGAN Paper Walkthrough.</a></h4></li>
  <li><h4><a href="https://hannibunny.github.io/mlbook/gan/GAN.html">HOCHSCHULE DER MEDIEN. Generative Adversarial Nets (GAN)</a></h4></li>
  <li><h4><a href="https://nn.labml.ai/gan/cycle_gan/index.html">labml.ai. Cycle GAN</a></h4></li>
  <li><h4><a href="https://blog.paperspace.com/unpaired-image-to-image-translations-with-cycle-gans/">Unpaired Image to Image Translations with Cycle GANs</a></h4></li>
</ol>
<h2>Ссылка на весы и примеры фото в процессе обучения:</h2>
<ul>
  <li><h4><a href="https://drive.google.com/drive/folders/1OJRgLQmvXJTDdMa-OWqW0_k0EuaMxK7c?usp=sharing">Папка на Google Drive со всеми файлами и весами.</a></h4></li>
  <li><h4><a href=""></a></h4></li>
</ul>
<hr>
