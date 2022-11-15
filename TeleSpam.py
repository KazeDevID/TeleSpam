from telethon import TelegramClient
from telethon.errors import rpcerrorlist, FloodWaitError, ChatWriteForbiddenError
import time
import os
try:
    import progressbar
except ModuleNotFoundError:
    print("Install ini dulu brey > pip install progressbar2") 


if os.path.isfile('spamer.txt'):
    with open('spamer.txt', 'r') as r:
        data = r.readlines()
    api_id = int(data[0])
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('spamer.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('spamer', api_id, api_hash)


async def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    global target
    print(''' _____    _      _____                       
|_   _|  | |    /  ___|                      
  | | ___| | ___\ `--. _ __   __ _ _ __ ___  
  | |/ _ \ |/ _ \`--. \ '_ \ / _` | '_ ` _ \ 
  | |  __/ |  __/\__/ / |_) | (_| | | | | | |
  \_/\___|_|\___\____/| .__/ \__,_|_| |_| |_|
                      | |                    
                      |_| by KazeDevID''')
    print('\n\nPilih Targetnya...')
    i = 0
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(i, ':', dialog.name, 'has ID', dialog.id)
        i = i + 1

    confirm = False
    max = len(dialogs) - 1

    while confirm == False:
        target_index = -1

        # Get target chat
        while target_index < 0 or target_index > max:
            print('Silakan masukkan pilihan antara 0 dan ', max)
            target_index = int(input())
            if target_index < 0 | target_index > max:
                print('target out of range')

        target = dialogs[target_index]
        print('Target adalah ', target.name, 'Id', target.id)

        # Wait for confirm
        print('Benar? Y/N')
        reply = input()[0]
        if reply == 'Y' or reply == 'y':
            confirm = True

    message = input("Masukkan pesan untuk dikirim di sini: ")
    Several = int(input("Berapa banyak pesan yang ingin Anda kirim?\n"))

    print("Jika Anda Salah memilih target, atau ingin memberhentikan tools ini silakan Ctrl-Z")
     print('Mulai spam dalam 3 detik...')
    time.sleep(3)
    print("[+] Spam Di mulai")
    bar = progressbar.ProgressBar(
        widgets=[progressbar.SimpleProgress()],
        max_value=Several,
    ).start()
    try:
        for i in range(int(Several)):
            await client.send_message(target.id, message)
            bar.update(i + 1)
        bar.finish()
        print("[+] spam sukses")
    except rpcerrorlist.ChatAdminRequiredError:
        print("[!] Anda tidak memiliki izin untuk memposting pesan dalam obrolan ini!")
    except ChatWriteForbiddenError:
        print("[!] Anda telah dibatasi untuk menulis pesan dalam obrolan ini...!")
    except FloodWaitError:
        print("[!] coba lagi setelah satu jam")


with client:
    client.loop.run_until_complete(main())
