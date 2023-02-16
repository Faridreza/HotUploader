from pyrogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

if __name__!="__main__":

    def KeyBoardAdministrator():
        KeyBoard=[
            [KeyboardButton("آپلود فایل🗃️")],
            [KeyboardButton("حذف قفل🗑️"),KeyboardButton("ثبت قفل🔒")],
            [KeyboardButton("لیست لینک ها⚙️")],
            [KeyboardButton("تعداد کاربران🔢")],
            [KeyboardButton("ارسال پیام همه گانی📩")],
            [KeyboardButton("حذف ادمین🗑️"),KeyboardButton("افزودن ادمین👤")],
        ]
        return ReplyKeyboardMarkup(KeyBoard,resize_keyboard=True)
    
    def KeyBoardAdmin():
        KeyBoard=[
            [KeyboardButton("آپلود فایل🗃️")],
            [KeyboardButton("حذف قفل🗑️"),KeyboardButton("ثبت قفل🔒")],
            [KeyboardButton("لیست لینک ها⚙️")],
            [KeyboardButton("تعداد کاربران🔢")],
            [KeyboardButton("ارسال پیام همه گانی📩")],
            [KeyboardButton("حذف ادمین🗑️"),KeyboardButton("افزودن ادمین👤")],
        ]
        return ReplyKeyboardMarkup(KeyBoard,resize_keyboard=True)

    def InlineChanell(getlist:list,keyfilename:str):
        KeyBoard=[]
        for i in getlist:
                KeyBoard.append([InlineKeyboardButton(i[1],url=f"https://t.me/{i[2]}")])
        KeyBoard.append([InlineKeyboardButton("عضو شدم",url=f"https://t.me/Horneylover_bot?start={keyfilename}")])
        return InlineKeyboardMarkup(KeyBoard)