import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
 
api_id="8058651"
api_hash="8860db996ef04daf58e511634525519c"
token="2026206234:AAE4ydg6a8koQnYpjzTmEhl_O6V8AL-D2-s"
message="hello brother"

phone='+917004983927'

client= TelegramClient('session',api_id,api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)

    client.sign_in(phone,input('Enter the code: '))


try:

     receiver= InputPeerUser(1269603873, 8058651)    

     client.send_message(receiver,message,parse_mode='html')

except Exception as e:
     print(e);     


client.disconnect()

