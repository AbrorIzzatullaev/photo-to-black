from aiogram import  types
from loader import dp, bot
import cv2
from io import BytesIO
import aiohttp


@dp.message_handler(content_types='photo')
async def photo_handler(message: types.Message):
	imggg = message.photo[-1].file_id
	file = await bot.get_file(imggg)

	await bot.download_file(file.file_path, "images/text.jpg")
	img = cv2.imread("images/text.jpg")
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('images/image.png',img)	
	# cat = FSInputFile('images/image.png')
	photo=open('images/image.png','rb')
	# await message.reply_photo(document=photo, caption="Bu fayl")
	await message.reply_photo(photo, caption="Black photo")	
