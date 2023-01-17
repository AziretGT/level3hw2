from aiogram import Bot, Dispatcher, types, executor
import config 

bot = Bot(token=config.token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','go'])
async def start(message:types.Message):
    await message.answer(f"здравствуйте {message.from_user.full_name}. Вас приветствует IT компания GekTek. Наш курс имеет 5 напрвлений. Чтобы получит больше информации пожалуйста введите /backend, /frontend, /uxui, /android, /ios.  ")


@dp.message_handler(commands=['backend', 'Backend', 'BACKEND', 'bACKEND','иаслутв','Ифслутв', 'ИФСЛУТВ'])
async def backend(message:types.Message):
    await message.reply("Бэкенд-разработчик (с англ. back-end (дословно «задняя часть») developer) занимается программно-административной частью веб-приложения, внутренним содержанием системы, серверными технологиями — базой данных, архитектурой, программной логикой.")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")


@dp.message_handler(commands=['frontend', 'Frontend', 'FRONTEND', 'fRONTEND','АКЩТЕУТВ','Акщтеутв', 'акщтеутв'])
async def frontend(message:types.Message):
    await message.reply("Вёрстка веб-страниц – создание структуры гипертекстового документа на основе HTML-разметки, как правило, при использовании таблиц стилей и клиентских сценариев, таким образом, чтобы элементы дизайна выглядели аналогично макету.")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")


@dp.message_handler(commands=['uxui', 'UxUi', 'Uxui', 'UXUI','ГЧГШ','ГчГш', 'гчгш'])
async def frontend(message:types.Message):
    await message.reply("Дизайн взаимодействия с пользователем включает в себя традиционное взаимодействие человека с компьютером, в том числе все аспекты продукта, как они воспринимаются пользователями.")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 3 месяц")


@dp.message_handler(commands=['Android', 'android', 'aNDROID', 'ANDROID','ФТВКЩШВ','Фтвкщшв', 'фтвкщшв'])
async def frontend(message:types.Message):
    await message.reply("Android разработка это разработка прилоожений для android")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 9 месяц")


@dp.message_handler(commands=['Ios', 'ios', 'iOS', 'IOS','шщы','Шщы', 'ШЩЫ'])
async def frontend(message:types.Message):
    await message.reply("Ios разработка это разработка прилоожений для Ios")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 9 месяц")


executor.start_polling(dp)