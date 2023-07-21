import redis, requests
from pyrogram import Client, filters
from pyrogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove, Message
from helper import get_audio

#os.system("pip install -U pyrogram")
#os.system("apt install update")

redis_url = "redis://default:ETw7er7MYHFCWvHIdi8c0BvfKtJKyqSD@redis-16065.c278.us-east-1-4.ec2.cloud.redislabs.com:16065"
r = redis.from_url(redis_url, encoding="utf-8",decode_responses=True)

BOT_TOKEN = "5851051301:AAG7Lh2uLioHYqkiQoDyhYc4EE9ohZQVaUY"
CHANNELS = ["i88Y8"]
BOT_ID = int(BOT_TOKEN.split(":")[0])

# Client

app = Client(
     name = "ClientBot",
     api_id = 9398500,
     api_hash = "ad2977d673006bed6e5007d953301e13",
     bot_token = BOT_TOKEN,
     #plugins = dict(root="plugins_bot")
 )


################### START MESSAGE ########################

@app.on_message(filters.command(commands="start", prefixes=['!','/',''], case_sensitive=False) & filters.private)
async def command_start(client, message):

    if not str(message.from_user.id) in r.smembers(f'{BOT_ID}Users'):
        r.sadd(f"{BOT_ID}Users", message.from_user.id)
        await client.send_message(5719372657, f"مستخدم جديد دخل بوتـ {len(r.smembers(f'{BOT_ID}Users'))} ـك 🕺", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton(message.from_user.first_name, url=f"tg://openmessage?user_id={message.from_user.id}")],
            ])
        )

    for i in CHANNELS:
        check_member = requests.get('https://api.telegram.org/bot' + str(BOT_TOKEN) + '/getchatmember?chat_id=@' + str(i) + '&user_id=' + str(message.from_user.id)).json()
        if check_member['result']['status'] not in ["creator", "member", "administrator"]:
            return await message.reply_text(f"- لطفاً اشترك بالقناة واستخدم البوت . \n- ثم اضغط /start \n- @{i} 👾" , quote=True)

    if message.text == "/start" or len(message.command) == 2 and message.command[1] == "start":
        await message.reply_text("مرحبا بك معنا في منصة القرآن الكريم على التيليجرام .\n\n[للملاحظات و الاقتراحات](tg://user?id=5719372657) , ولا تتردد في زيارة [قناتنا](t.me/i88Y8) .", disable_web_page_preview=True)
        await message.reply_text("كيف تفضل طريقة الاختيار ؟", reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("🤍")]], resize_keyboard=True))

    if len(message.command) == 2 and message.command[1] == "set_reader":
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("ابراهيم الأخضر"), KeyboardButton("أحمد العجمي"), KeyboardButton("خالد الجليل")],
            [KeyboardButton("بندر بليلة"), KeyboardButton("خليفة الطنيج"), KeyboardButton("حاتم فريد الواعر")],
            [KeyboardButton("سعود الشريم"), KeyboardButton("سعد الغامدي"), KeyboardButton("صلاح بو خاطر")],
            [KeyboardButton("ابو بكر الشاطري"), KeyboardButton("عبد الرحمن العوسي"), KeyboardButton("عبد الباسط عبد الصمد")],
            [KeyboardButton("عبد العزيز الزهراني"), KeyboardButton("عبد الرشيد صوفي"), KeyboardButton("عبد الله عواد الجهني")],
            [KeyboardButton("عبد الله بصفر"), KeyboardButton("علي جابر"), KeyboardButton("علي الحذيفي")],
            [KeyboardButton("فارس عباد"), KeyboardButton("غسان الشوربجي"), KeyboardButton("ماهر المعيقلي")],
        ],
            resize_keyboard=True, one_time_keyboard=False
        )
        await message.reply_text("اختر القارئ المراد الاستماع له ...", quote=True, reply_markup=keyboard)


################### START MESSAGE ########################

@app.on_message(filters.command(commands='القائمة الرئيسية', prefixes=['!','/',''], case_sensitive=False) & filters.private)
async def shoice_reader(client, message):
    await message.reply_text("كيف تفضل طريقة الاختيار ؟", quote=True, reply_markup=ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton("🤍")]], resize_keyboard=True))
            
################### START MESSAGE ########################

@app.on_message(filters.command(commands='🤍', prefixes=['!','/',''], case_sensitive=False) & filters.private)
async def shoice_reader(client, message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("القائمة الرئيسية")],
        [KeyboardButton("ابراهيم الأخضر"), KeyboardButton("أحمد العجمي"), KeyboardButton("خالد الجليل")],
        [KeyboardButton("بندر بليلة"), KeyboardButton("خليفة الطنيج"), KeyboardButton("حاتم فريد الواعر")],
        [KeyboardButton("سعود الشريم"), KeyboardButton("سعد الغامدي"), KeyboardButton("صلاح بو خاطر")],
        [KeyboardButton("ابو بكر الشاطري"), KeyboardButton("عبد الرحمن العوسي"), KeyboardButton("عبد الباسط عبد الصمد")],
        [KeyboardButton("عبد العزيز الزهراني"), KeyboardButton("عبد الرشيد صوفي"), KeyboardButton("عبد الله عواد الجهني")],
        [KeyboardButton("عبد الله بصفر"), KeyboardButton("علي جابر"), KeyboardButton("علي الحذيفي")],
        [KeyboardButton("فارس عباد"), KeyboardButton("غسان الشوربجي"), KeyboardButton("ماهر المعيقلي")],
        ],
        resize_keyboard=True, one_time_keyboard=False
    )
    await message.reply_text("فضلا اختر القارئ المراد الاستماع له ...", quote=True, reply_markup=keyboard)


################### CHOOSE A READER  ########################

readers = ["احمد العجمي", "أحمد العجمي", "ابراهيم الأخضر", "ابراهيم الاخضر", "بندر بن عبد العزيز", "بندر بليلة", "خالد الجليل", "حاتم فريد الواعر", "خليفة الطنيجي", "سعد الغامدي", "سعود الشريم", "ابو بكر الشاطري", "صلاح بو خاطر", "صلاح ابو خاطر", "عبد الباسط عبد الصمد", "عبد الرحمن العوسي", "عبد الرشيد صوفي", "عبد العزيز الزهراني", "عبد الله بصفر", "عبدالله عواد الجهني", "عبد الله عواد الجهني", "علي الحذيفي", "علي جابر", "غسان الشوربجي", "فارس عباد", "ماهر المعيقلي"]
@app.on_message(filters.command(commands=readers, prefixes=['!','/',''],case_sensitive=False) & filters.private)
async def shoice_surah(client, message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("القائمة الرئيسية")],
        [KeyboardButton("النساء"), KeyboardButton("آل عمران"), KeyboardButton("البقرة"), KeyboardButton("الفاتحة")],
        [KeyboardButton("التوبة"), KeyboardButton("الأنفال"), KeyboardButton("الأعراف"), KeyboardButton("الأنعام")],
        [KeyboardButton("إبراهيم"), KeyboardButton("الرعد"), KeyboardButton("يوسف"), KeyboardButton("هود")],
        [KeyboardButton("مريم"), KeyboardButton("الكهف"), KeyboardButton("الإسراء"), KeyboardButton("النحل")],
        [KeyboardButton("النور"), KeyboardButton("المؤمنون"), KeyboardButton("الحج"), KeyboardButton("الأنبياء")],
        [KeyboardButton("العنكبوت"), KeyboardButton("القصص"), KeyboardButton("النمل"), KeyboardButton("الشعراء")],
        [KeyboardButton("سبأ"), KeyboardButton("الأحزاب"), KeyboardButton("السجدة"), KeyboardButton("لقمان")],
        [KeyboardButton("الزمر"), KeyboardButton("ص"), KeyboardButton("الصافات"), KeyboardButton("يس")],
        [KeyboardButton("الدّخان"), KeyboardButton("الزخرف"), KeyboardButton("الشورى"), KeyboardButton("فصلت")],
        [KeyboardButton("الحجرات"), KeyboardButton("الفتح"), KeyboardButton("محمد"), KeyboardButton("الأحقاف")],
        [KeyboardButton("القمر"), KeyboardButton("النجم"), KeyboardButton("الطور"), KeyboardButton("الذاريات")],
        [KeyboardButton("الحشر"), KeyboardButton("المجادلة"), KeyboardButton("الحديد"), KeyboardButton("الواقعة")],
        [KeyboardButton("التغابن"), KeyboardButton("المنافقون"), KeyboardButton("الجمعة"), KeyboardButton("الصف")],
        [KeyboardButton("الحاقة"), KeyboardButton("القلم"), KeyboardButton("الملك"), KeyboardButton("التحريم")],
        [KeyboardButton("المدثر"), KeyboardButton("المزمل"), KeyboardButton("الجن"), KeyboardButton("نوح")],
        [KeyboardButton("النازعات"), KeyboardButton("النبأ"), KeyboardButton("المرسلات"), KeyboardButton("الإنسان")],
        [KeyboardButton("الإنشقاق"), KeyboardButton("المطففين"), KeyboardButton("الإنفطار"), KeyboardButton("التكوير")],
        [KeyboardButton("الفجر"), KeyboardButton("الغاشية"), KeyboardButton("الأعلى"), KeyboardButton("الطارق")],
        [KeyboardButton("الشرح"), KeyboardButton("الضحى"), KeyboardButton("الليل"), KeyboardButton("الشمس")],
        [KeyboardButton("الزلزلة"), KeyboardButton("البينة"), KeyboardButton("القدر"), KeyboardButton("العلق")],
        [KeyboardButton("الهمزة"), KeyboardButton("العصر"), KeyboardButton("التكاثر"), KeyboardButton("القارعة")],
        [KeyboardButton("الكافرون"), KeyboardButton("الكوثر"), KeyboardButton("الماعون"), KeyboardButton("قريش")],
        [KeyboardButton("الناس"), KeyboardButton("الفلق"), KeyboardButton("الإخلاص"), KeyboardButton("المسد")],
    ],
        resize_keyboard=True, one_time_keyboard=False
    )
    r.hset("QURAN-Reader", message.from_user.id, message.text)
    await message.reply_text("فضلا اختر السورة المراد الاستماع لها ...", quote=True, reply_markup=keyboard)


################### CHOOSE THE SURAH ########################

surahs = ["الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس", "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه", "الأنبياء", "الحج", "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم", "لقمان", "السجدة", "الأحزاب", "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر", "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق", "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة", "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج", "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس", "التكوير", "الانفطار", "المطففين", "الانشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد", "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات", "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر", "المسد", "الإخلاص", "الفلق", "الناس"]
surahss = ["سورة الفاتحة", "سورة البقرة", "سورة آل عمران", "سورة النساء", "سورة المائدة", "سورة الأنعام", "سورة الأعراف", "سورة الأنفال", "سورة التوبة", "سورة يونس", "سورة هود", "سورة يوسف", "سورة الرعد", "سورة إبراهيم", "سورة الحجر", "سورة النحل", "سورة الإسراء", "سورة الكهف", "سورة مريم", "سورة طه", "سورة الأنبياء", "سورة الحج", "سورة المؤمنون", "سورة النور", "سورة الفرقان", "سورة الشعراء", "سورة النمل", "سورة القصص", "سورة العنكبوت", "سورة الروم", "سورة لقمان", "سورة السجدة", "سورة الأحزاب", "سورة سبأ", "سورة فاطر", "سورة يس", "سورة الصافات", "سورة ص", "سورة الزمر", "سورة غافر", "سورة فصلت", "سورة الشورى", "سورة الزخرف", "سورة الدخان", "سورة الجاثية", "سورة الأحقاف", "سورة محمد", "سورة الفتح", "سورة الحجرات", "سورة ق", "سورة الذاريات", "سورة الطور", "سورة النجم", "سورة القمر", "سورة الرحمن", "سورة الواقعة", "سورة الحديد", "سورة المجادلة", "سورة الحشر", "سورة الممتحنة", "سورة الصف", "سورة الجمعة", "سورة المنافقون", "سورة التغابن", "سورة الطلاق", "سورة التحريم", "سورة الملك", "سورة القلم", "سورة الحاقة", "سورة المعارج", "سورة نوح", "سورة الجن", "سورة المزمل", "سورة المدثر", "سورة القيامة", "سورة الإنسان", "سورة المرسلات", "سورة النبأ", "سورة النازعات", "سورة عبس", "سورة التكوير", "سورة الانفطار", "سورة المطففين", "سورة الانشقاق", "سورة البروج", "سورة الطارق", "سورة الأعلى", "سورة الغاشية", "سورة الفجر", "سورة البلد", "سورة الشمس", "سورة الليل", "سورة الضحى", "سورة الشرح", "سورة التين", "سورة العلق", "سورة القدر", "سورة البينة", "سورة الزلزلة", "سورة العاديات", "سورة القارعة", "سورة التكاثر", "سورة العصر", "سورة الهمزة", "سورة الفيل", "سورة قريش", "سورة الماعون", "سورة الكوثر", "سورة الكافرون", "سورة النصر", "سورة المسد", "سورة الإخلاص", "سورة الفلق", "سورة الناس"]
@app.on_message(filters.command(commands=surahs, prefixes=['!','/',''],case_sensitive=False))
@app.on_message(filters.command(commands=surahss, prefixes=['!','/',''],case_sensitive=False))
async def send_audio(client, message):
    reader = r.hget("QURAN-Reader", message.from_user.id)
    if reader:
        await message.reply_text(f"`لقد اخترت سورة {message.text.replace('سورة ', '')} من القارئ {reader} برواية حفص عن عاصم - مرتل , ستصل لك في لحظات ..`")
        await message.reply_audio(audio=f"https://t.me/TheHolyQuranIsAudible/{get_audio(reader, message.text)}")
    else:
        await message.reply_text("فضلا اختر القارئ المراد الاستماع له ...", quote=True, reply_markup=InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton(text = "🤍", url = f"https://t.me/{client.me.username}?start=set_reader")],
            ])
        )

        
app.run()
