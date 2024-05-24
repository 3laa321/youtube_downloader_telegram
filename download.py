from lib import *

@bot.message_handler(func=lambda message: True)
def handle_message(message):
		url = message.text
		user_id = str(message.from_user.id)
		file_path = os.path.join("user_data", user_id)

		try:
				with open(file_path, "r", encoding="utf-8") as file:
						file_content = file.read()
						# التحقق من صحة الرابط
						if file_content == 'ar':
								text_loading = "⏳جار التحميل..."
								text_caption = "يرجي الانضمام للقناة 🩵."
								text_find_error = "عذرًا، لم يتم العثور على مقطع صوتي في الرابط المُرسل."
								text_download_error = "حدث خطأ أثناء التحميل. الرجاء المحاولة مرة أخرى."
								text_url_error = "الرجاء إرسال رابط يوتيوب صحيح."
						elif file_content == 'en':
								text_loading = "⏳Loading..."
								text_caption = "Please join the channel 🩵."
								text_find_error = "Please send a valid YouTube link."
								text_download_error = "An error occurred while downloading. Please try again."
								text_url_error = "Sorry, no audio clip was found in the sent link."

				if "youtube.com" in url or "youtu.be" in url:
						loading_message = bot.reply_to(message, text_loading)
						unique_id = str(uuid.uuid4())
						try:
								yt = YouTube(url)
								title = yt.title
								safe_title = "".join(x for x in title if (x.isalnum() or x in "._- ")).strip()  # إزالة الأحرف غير الصالحة
								audio_stream = yt.streams.filter(only_audio=True).first()
								if audio_stream:  # التحقق من وجود مقطع صوتي
										output_file = audio_stream.download(filename=unique_id)

										# تحويل الملف إلى صيغة MP3 باستخدام pydub وffmpeg
										audio = AudioSegment.from_file(output_file)
										new_file = safe_title + '.mp3'
										audio.export(new_file, format='mp3')
										os.remove(output_file)

										# التأكد من وجود علامة ID3
										try:
												audio_tags = ID3(new_file)
										except error:
												audio_tags = MP3(new_file)
												audio_tags.add_tags()

										# تعديل بيانات الملف الصوتي
										audio_tags = EasyID3(new_file)
										audio_tags['title'] = title
										audio_tags['artist'] = '@YTDY_bot'
										audio_tags.save()

										# إضافة صورة الألبوم
										audio_tags = MP3(new_file, ID3=ID3)
										with open(ICON_PATH, 'rb') as albumart:
												audio_tags.tags.add(
														APIC(
																encoding=3,  # 3 is for utf-8
																mime='image/jpeg',  # image/jpeg or image/png
																type=3,  # 3 is for the cover(front) image
																desc=u'Cover',
																data=albumart.read()
														)
												)
										audio_tags.save()

										with open(new_file, 'rb') as audio_file:
												thumb_image = open('Base/icon.jpg', 'rb')
												bot.send_audio(message.chat.id, audio_file, caption=text_caption, title=safe_title, thumb=thumb_image, reply_markup=markup_inline_help())
												thumb_image.close()
										os.remove(new_file)
								else:
										bot.reply_to(message, text_find_error)
						except Exception as e:
								bot.reply_to(message, text_download_error)
								print(e)
						finally:
								bot.delete_message(chat_id=message.chat.id, message_id=loading_message.message_id)
				else:
						bot.reply_to(message, text_url_error)

		except FileNotFoundError as e:
				print(e)
		except Exception as e:
				print(e)
