import data 


def get_audio(reciter, surah):
    if reciter == "أحمد العجمي" or reciter == "احمد العجمي":
        return data.ajami[surah]
    elif reciter == "ابراهيم الاخضر" or reciter == "ابراهيم الأخضر":
        return data.alakhdar[surah]
    elif reciter == "بندر بن عبد العزيز" or reciter == "بندر بليلة":
        return data.balilah[surah]
    elif reciter == "خالد الجليل":
        return data.aljalil[surah]
    elif reciter == "حاتم فريد الواعر":
        return data.hatem[surah]
    elif reciter == "خليفة الطنيجي":
        return data.khalifa[surah]
    elif reciter == "سعد الغامدي":
        return data.alghamdi[surah]
    elif reciter == "سعود الشريم":
        return data.alshuraim[surah]
    elif reciter == "ابو بكر الشاطري":
        return data.shatri[surah]
    elif reciter == "صلاح بو خاطر" or reciter == "صلاح ابو خاطر":
        return data.bukhatir[surah]
    elif reciter == "عبد الباسط عبد الصمد":
        return data.abdulbaset[surah]
    elif reciter == "عبد الرحمن العوسي":
        return data.al3osy[surah]
    elif reciter == "عبد الرشيد صوفي":
        return data.soufi[surah]
    elif reciter == "عبد العزيز الزهراني":
        return data.alzahrani[surah]
    elif reciter == "عبد الله بصفر":
        return data.bsfr[surah]
    elif reciter == "عبدالله عواد الجهني" or reciter == "عبد الله عواد الجهني":
        return data.aljahani[surah]
    elif reciter == "علي الحذيفي":
        return data.alhuthaifi[surah]
    elif reciter == "علي جابر":
        return data.jaber[surah]
    elif reciter == "غسان الشوربجي":
        return data.ghassan[surah]
    elif reciter == "فارس عباد":
        return data.fares[surah]
    elif reciter == "ماهر المعيقلي":
        return data.maher[surah]

#print(get_audio("خالد الجليل", "الفاتحة"))