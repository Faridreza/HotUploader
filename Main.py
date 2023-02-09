from pyrogram import Client,filters,types
from KeyBoard import KeyBoardAdmin,KeyBoardAdministrator,InlineChanell
from pyrogram.types import ReplyKeyboardRemove
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from random import choice
from string import ascii_lowercase
from random import choice
from os import rename,chdir
from asyncio import sleep
from glob import glob
from DataBase import *
from pyromod import listen
from re import findall

HotUploader=Client("Session\\HotUploader",1070574,"b23074812559269d941253103c948eff",bot_token="5895402771:AAHyCHX28l8Q0wFf2FhMyMRzQ8818UxYl4s")
GetIdUploader=Client("Session\\IdUploader",1070574,"b23074812559269d941253103c948eff")
InsertAdmin(5456444873,"Amy",0)
@GetIdUploader.on_message(filters.private & filters.chat(5456444873))
async def ReturnId(_:GetIdUploader,e:types.Message):
    Text=e.text
    IsCheckPrivate=findall("t.me/.*",Text)
    IsCheckPublic=findall("@(\w+)",Text)
    if IsCheckPrivate!=[] or IsCheckPublic!=[]:
        GetId=await GetIdUploader.join_chat(Text)
        await GetIdUploader.send_message(e.from_user.id,GetId.id)
        await GetIdUploader.leave_chat(Text,True)

global AccsessAdmin
AccsessAdmin=0

async def Check_Join(userid: int) -> bool:
    NotJoin=[]
    for Link in FetchLocksLink():
        try:
            User = await HotUploader.get_chat_member(int(Link[0]),userid)
        except UserNotParticipant:
            NotJoin.append(Link)
    return NotJoin

@HotUploader.on_message(filters.text & filters.command("start"))
async def Start(_:HotUploader,e:types.Message):
    global AccsessAdmin
    UserId=e.from_user.id
    Text=e.text
    Any=AnyAdmin(UserId)
    if Any!=404 and Any[0]==200:
        Info=InfoAdmin(UserId)
        if Info[2]==0:
            AccsessAdmin=0
            await HotUploader.send_message(UserId,"سلام🙋‍♂️\nمیتونی از طریق دکمه های زیر با من در ارتباط باشی🗿",reply_markup=KeyBoardAdministrator())
        else:
            AccsessAdmin=1
            await HotUploader.send_message(UserId,"سلام🙋‍♂️\nمیتونی از طریق دکمه های زیر با من در ارتباط باشی🗿",reply_markup=KeyBoardAdmin())
    else:
        if AnyUser(UserId)==404:
            InsertUser(UserId,e.from_user.first_name)
        if Text=="/start":
            await HotUploader.send_message(UserId,"اینجا چیزی برات نداریم میتونی عضو چنلمون بشی بتونی دسترسی به فیلما و نودا داشته باشی🗿\n@Nudestoooon")
        else:
            StateJoin= await Check_Join(UserId)
            if StateJoin==[]:
                FileCurrentName=Text.split(" ")[-1]
                File=glob(f"DataFile\\{FileCurrentName}.*")[0].replace("DataFile\\","").split(".")
                if File[1]=="jpg":
                    if FileCurrentName==File[0]:
                        SendFile=await HotUploader.send_media_group(UserId,[types.InputMediaPhoto(f"DataFile\\{File[0]}.jpg",caption="توجه فایل بالا به مدت 30 ثانیه در دسترس شماست لطفا اون رو در پیام های ذخیره شده نگه دارید⚠️")])
                        await sleep(30)
                        await HotUploader.delete_messages(UserId,e.id+1)
                elif File[1]=="mp4":
                    if FileCurrentName==File[0]:
                        SendFile=await HotUploader.send_media_group(UserId,[types.InputMediaVideo(f"DataFile\\{File[0]}.mp4",caption="توجه فایل بالا به مدت 30 ثانیه در دسترس شماست لطفا اون رو در پیام های ذخیره شده نگه دارید⚠️")])
                        await sleep(30)
                        await HotUploader.delete_messages(UserId,e.id+1)
            else:
                await HotUploader.send_message(UserId,"شیطون داخل کانالای زیر جوین بده تا فایلو بفرستم برات ⚠️",reply_markup=InlineChanell(StateJoin))

global STEP
STEP=''

@HotUploader.on_message(filters.text)
async def Command(_:HotUploader,e:types.Message):
    UserId=e.from_user.id
    Any=AnyAdmin(UserId)
    if Any!=404:
        Text=e.text
        global STEP
        if Text=="آپلود فایل🗃️":
            STEP='UpFile'
            await HotUploader.send_message(UserId,"خیلی یاواش فایلو بفرست برام 🗿")
        elif Text=="ثبت قفل🔒":
            Link=await HotUploader.ask(UserId,"لینک رو بدون @ اگه خصوصیه بدون لینک قبلش بفرست 🔐\nIdNumber\nTitle\nLink Not @")
            LinkText=Link.text.split("\n")
            if LinkText!='':
                if InsertLocksLink(str(LinkText[0]),str(LinkText[1]),str(LinkText[2]))==200:
                    if Any[1][0]==0:
                        await HotUploader.send_message(UserId,"لینک ثبت شد✅",reply_markup=KeyBoardAdministrator())
                    else:
                        await HotUploader.send_message(UserId,"لینک ثبت شد✅",reply_markup=KeyBoardAdmin())
                else:
                    if Any[1][0]:
                        await HotUploader.send_message(UserId,"لینک قبلا قفل شده ⚠️",reply_markup=KeyBoardAdministrator())
                    else:
                        await HotUploader.send_message(UserId,"لینک قبلا قفل شده ⚠️",reply_markup=KeyBoardAdmin())
            else:
                if Any[1][0]:
                        await HotUploader.send_message(UserId,"لینک درست نیست ❌",reply_markup=KeyBoardAdministrator())
                else:
                        await HotUploader.send_message(UserId,"لینک درست نیست ❌",reply_markup=KeyBoardAdmin())
        elif Text=="حذف قفل🗑️":
            Link=await HotUploader.ask(UserId,"لینک رو بفرست 🔐")
            LinkText=Link.text
            if LinkText!='':
                if DeleteLocksLink(str(LinkText))==200:
                    if Any[1][0]==0:
                        await HotUploader.send_message(UserId,"لینک حذف شد✅",reply_markup=KeyBoardAdministrator())
                    else:
                        await HotUploader.send_message(UserId,"لینک حذف شد✅",reply_markup=KeyBoardAdmin())
                else:
                    if Any[1][0]:
                        await HotUploader.send_message(UserId,"لینک وجود ندارد ⚠️",reply_markup=KeyBoardAdministrator())
                    else:
                        await HotUploader.send_message(UserId,"لینک وجود ندارد ⚠️",reply_markup=KeyBoardAdmin())
            else:
                if Any[1][0]:
                        await HotUploader.send_message(UserId,"لینک درست نیست ❌",reply_markup=KeyBoardAdministrator())
                else:
                        await HotUploader.send_message(UserId,"لینک درست نیست ❌",reply_markup=KeyBoardAdmin())
        elif Text=="لیست لینک ها⚙️":
            Links=FetchLocksLink()
            if Links==[] or Links==None:
                if Any[1][0]:
                        await HotUploader.send_message(UserId,"لینکی وجود ندارد ❌",reply_markup=KeyBoardAdministrator())
                else:
                    await HotUploader.send_message(UserId,"لینکی وجود ندارد ❌",reply_markup=KeyBoardAdmin())
            else:
                LinkMessage='لینک های قفل شده 🔐\n'
                for i in Links:
                    LinkMessage+=f"⚙️ `{i[0]}`\n"
                if Any[1][0]:
                     await HotUploader.send_message(UserId,LinkMessage,reply_markup=KeyBoardAdministrator())
                else:
                     await HotUploader.send_message(UserId,LinkMessage,reply_markup=KeyBoardAdmin())
        elif Text=="تعداد کاربران🔢":
            Users=FetchUsers()
            if Users==[] or Users==None:
                await HotUploader.send_message(UserId,"یوزری وجود ندارد ❌",reply_markup=KeyBoardAdmin())
            else:
                CountUsers='👤تعداد یوزر ها : {0}'.format(len(Users))
                if Any[1][0]:
                     await HotUploader.send_message(UserId,CountUsers,reply_markup=KeyBoardAdministrator())
                else:
                     await HotUploader.send_message(UserId,CountUsers,reply_markup=KeyBoardAdmin())
        elif Text=="ارسال پیام همه گانی📩":
            Link=await HotUploader.ask(UserId,"متنو بده تا بدم بشون 🗿")
            LinkText=Link.text
            Users=FetchUsers()
            for i in Users:
                await HotUploader.send_message(i[1],LinkText)
            await HotUploader.send_message(UserId,"به همشون دادم سید 🗿",reply_markup=KeyBoardAdministrator())
        elif Text=="افزودن ادمین👤":
            Info=await HotUploader.ask(UserId,"آیدیشو بده بکنمش ادمین🗿\n1212-Ali")
            Info=str(Info.text).split("-")
            if InsertAdmin(int(Info[0]),Info[1],1)==200:
                await HotUploader.send_message(UserId,"کردمش ادمین سید 🗿💦")
            else:
                await HotUploader.send_message(UserId,"وجود نداره یا یجاشو ریدی ❌")
        elif Text=="حذف ادمین🗑️":
            Info=await HotUploader.ask(UserId,"آیدیشو بده بکنمش ادب\n1212")
            Info=str(Info.text)
            if DeleteAdmin(Info)==200:
                await HotUploader.send_message(UserId,"حذفش کردم تا بشه ادب سید 💦")
            else:
                await HotUploader.send_message(UserId,"وجود نداره یا یجاشو ریدی ❌")
        else:
            await HotUploader.send_message(UserId,"نکن جیزه بچه 🗿")

def RandomName(length=8):
   letters = ascii_lowercase
   return ''.join(choice(letters) for i in range(length))

@HotUploader.on_message(filters.photo | filters.video)
async def DownloadPhotoFile(_:HotUploader,e:types.Message):
    if STEP=='UpFile':
        UserId=e.from_user.id
        RandomFileName=RandomName()
        await HotUploader.send_message(UserId,"صبر کن تا لینک دانلود درسته شه🥺",reply_markup=ReplyKeyboardRemove())
        InfoFile=await HotUploader.download_media(e,"DataFile\\")
        CurrentFileName=InfoFile.split("\\")[-1]
        FormatFile=CurrentFileName.split(".")[-1]
        rename(f"DataFile\\{CurrentFileName}",f"DataFile\\{RandomFileName}.{FormatFile}")
        await HotUploader.delete_messages(UserId,e.id+1)
        if AccsessAdmin==0:
            await HotUploader.send_message(UserId,f"⚙️لینک فایل شما\nt.me/NudestoooonBot?start={RandomFileName}",reply_markup=KeyBoardAdministrator())
        else:
            await HotUploader.send_message(UserId,f"⚙️لینک فایل شما\nt.me/NudestoooonBot?start={RandomFileName}",reply_markup=KeyBoardAdmin())

GetIdUploader.start()
HotUploader.run()