import re
import os
import random
import subprocess
import time
from datetime import datetime
import pyautogui
from PIL import Image
import pytesseract
import base64
import requests

BotName = "PonyTown"
Admin_name = ['admin1', 'admin2']
prefix = ['+', '.', '-']
apikey="YOUR GEMINI API KEY HERE"

def press_arrow_key(direction):
    pyautogui.keyDown(direction)
    time.sleep(0.1)
    pyautogui.keyUp(direction)

def handle_command(text_cmd, command, direction, kmna):
    match = re.search(r'\[(.*?)\](?: whispers:)? .*?' + command + r'\s+(\d+)', text_cmd)
    if match:
        username = match.group(1)
        if username in Admin_name:
            value = int(match.group(2))
            
            kirim_pesan(f"{value} langkah ke {kmna}")
            for _ in range(value):
                press_arrow_key(direction)
            kirim_pesan("")
        else:
            kirim_pesan("SIAPA LU NYURUH NYURUH??")
def split_text(text, max_length=70):
    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += word + ' '
        else:
            lines.append(current_line.rstrip())
            current_line = word + ' '

    if current_line:
        lines.append(current_line.rstrip())

    return lines

def gemini(meseg):
    api_key = "RGV2ZWxvcGVyIFBUIGF0YXUgUG9ueSBUb3duOiBBZ2FtbmVudHphciwgU3RhcmJvdywgUGxleGF1cmUsIFNtaWxleSwgRmlzaEJlYW0sIEluZHVzdHJpYWxpY2UsIENoaXJhQ2hhbiwgU3R1YmVuaG9ja2VyLCBPcmNoaWRQb255LCBXYW5kZXJpbmcgQXJ0aXN0LCBQb2x5ZXRoeWxlbmUsIExpdHRsZUZhaXRoOSwgVGlvUmFmYUpQLCBEYW1pYW4sIE9jdGF2aWFQb25lLCBNZXdpbywgRGVlcmF3LCBBbm4sIFJhbmRTZmssIE1lbm8sIFJKLCBNYWR6LCBLc2VuLCBTY2F0dGVyLCBTaGVsZg=="
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"""**Database :**
                        {datetime.now().strftime('Tanggal:%Y-%m-%d Jam:%H:%M')}
                        {base64.b64decode(api_key.encode('utf-8')).decode('utf-8')}
                        """
                    }
                ]
            },
            {
                "role": "model",
                "parts": [
                    {
                        "text": "Saved in Database"
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "text": meseg
                    }
                ]
            }
        ]
    }
    response = requests.post("https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent", headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        candidates = response_data.get("candidates", [])
        if candidates:
            content_parts = candidates[0].get("content", {}).get("parts", [])
            text_parts = [part["text"] for part in content_parts if "text" in part]
            response_text = " ".join(text_parts)
            if len(response_text) > 70:
                b = split_text(response_text)
                return b
            else:
                
                return response_text
        else:
            print("No candidates found.")
            
def command(cmd, run):
    pattern = r'\[(.*?)\](?: whispers:)? ([' + ''.join(re.escape(p) for p in prefix) + '])' + re.escape(cmd) + r'(?: (.+))?'
    if re.search(pattern, text_cmd.lower()):
        match = re.search(pattern, text_cmd)
        if match:
            run(match)
    elif ".up" in text_cmd.lower():
        handle_command(text_cmd, ".up", 'up', "atas")
    elif ".dn" in text_cmd.lower():
        handle_command(text_cmd, ".dn", 'down', "bawah")
    elif ".kn" in text_cmd.lower():
        handle_command(text_cmd, ".kn", 'right', "kanan")
    elif ".kr" in text_cmd.lower():
        handle_command(text_cmd, ".kr", 'left', "kiri")

def kirim_pesan(message):
    print(message)

class Cmd:
    def menu(self, match):
        username = match.group(1)
        current_time = time.localtime()
        current_hour = str(current_time.tm_hour) 
        current_minute = str(current_time.tm_min)
        def adminmenu():
            kirim_pesan("> thr ")
            kirim_pesan("> give <nama>")
            kirim_pesan('> nama_keren')
            kirim_pesan('> skin_cl')
            kirim_pesan("> day")
            kirim_pesan("> (calculator)")
            kirim_pesan("> quotes")
            kirim_pesan("> puja")
            kirim_pesan("> owner")
            kirim_pesan("> ai")
            kirim_pesan("> py!!<python code>!!")
            kirim_pesan("> dice <value>")
            kirim_pesan("< hunt")
            kirim_pesan("< stats")
            kirim_pesan("< buy")
            kirim_pesan("< gacha")
            kirim_pesan("< inven")
            kirim_pesan("< use")

        def menu():
            pesan_salam = f"Hai [{username}] Time: {current_hour}:{current_minute}"
            kirim_pesan(pesan_salam)
            kirim_pesan(f"I'm a {BotName}")
            time.sleep(4)
            kirim_pesan("Available menus:")
            time.sleep(2)
            kirim_pesan("> thr ")
            kirim_pesan("> give <nama>")
            kirim_pesan('> nama_keren')
            kirim_pesan('> skin_cl')
            kirim_pesan("> day")
            kirim_pesan("> (pertambahan)")
            kirim_pesan("> quotes")
            kirim_pesan("> puja")
            kirim_pesan("> owner")
            kirim_pesan("> ai")
            kirim_pesan("> py!!<python code>!!")
            kirim_pesan("> dice <value>")

        if username in Admin_name: 
            pesan_salam = f"Hallo Tuan [{username}], Sekarang Jam: {current_hour}:{current_minute}"
            kirim_pesan(pesan_salam)
            kirim_pesan(f"Apa yang tuan {username} inginkan?")
            time.sleep(4)
            kirim_pesan("Menu yang saya bisa:")
            time.sleep(2)
            adminmenu()
        
        else:
            menu()
            
    def day(self, match):
        username = match.group(1)
        now = datetime.now()
        day_index = now.weekday()
        day_name = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][day_index]


        kirim_pesan("Sekarang adalah hari "+day_name+" "+username)
        
    def nama_keren(self, match):
        username=match.group(1)

        adjectives = ['Mighty', 'Sleek', 'Shadow', 'Blaze', 'Thunder', 'Eternal', 'Epic', 'Ninja', 'Alpha', 'Omega']
        nouns = ['Phoenix', 'Dragon', 'Wolf', 'Storm', 'Tiger', 'Sword', 'Warrior', 'Legend', 'Hero', 'Knight']
        
        name_parts = username.split()
        
        num_adjectives = random.randint(1, min(len(name_parts), 2))
        selected_adjectives = random.sample(adjectives, num_adjectives)
        
        cool_name = ' '.join(selected_adjectives + name_parts)
        kirim_pesan(f"Nama keren Anda: {cool_name}")
        
    def dice(self, match):
        username = match.group(1)
        tebakan = match.group(3)
        print(tebakan)
        dice = random.randint(0, 9)
        if username == "RandSfk":
            kirim_pesan(f" 🎲 Tebakanmu adalah {str(tebakan)} of 9")
            time.sleep(4)
            kirim_pesan("hasilnya: "+str(tebakan))
            kirim_pesan(f"Selamat {username} Kamu Menang")
            kirim_pesan('/roll 999999999')
        else:
            try:
                if int(tebakan) > 9:
                    kirim_pesan('Maaf angka terlalu tinggi')
                else:
                    kirim_pesan(f"🎲🎲🎲🎲Tebakanmu adalah {str(tebakan)} of 9 {username}")
                    time.sleep(4)
                    kirim_pesan("hasilnya: "+str(dice))
                    time.sleep(2)
                    if int(dice) == int(tebakan):
                        kirim_pesan(f"Selamat {username} Kamu Menang")
                        kirim_pesan('/roll 999999999')
                    else:
                        kirim_pesan(f"Coba Lagi nanti {username}")
            except:
                kirim_pesan("Harap gunakan angka dan bukan huruf")
    
    def owner(self, match):
        kirim_pesan("Username: RandSfk")
        kirim_pesan("Instagram: rand_sfk")
        kirim_pesan("Github  : RandSfk")
        kirim_pesan("Facebook: RandSfk Remastered")
        
    def quotes(self, match):
        quotes = [
        "Jangan menyerah, karena saat menyerah, itu adalah awal dari kegagalan.",
        "Hidup adalah apa yang terjadi saat kamu sibuk membuat rencana lain.",
        "Satu-satunya cara untuk melakukan pekerjaan besar adalah mencintai apa yang kamu lakukan.",
        "Di akhir, bukanlah tahun dalam hidupmu yang penting. Tetapi hidup dalam tahun-tahunmu.",
        "Hanya ada satu hal yang harus kita takuti, yaitu ketakutan itu sendiri.",
        "Anda akan melewatkan 100% dari tembakan yang tidak anda ambil.",
        "Jadilah dirimu sendiri; orang lain sudah terlalu tersita.",
        "Masa depan milik mereka yang percaya pada keindahan mimpinya.",
        "Berjuang bukanlah untuk sukses, tetapi lebih baik untuk memberi nilai.",
        "Saya tidak gagal. Saya hanya menemukan 10.000 cara yang tidak akan berhasil."
        ]
        kirim_pesan(random.choice(quotes))

    def puja(self, match):
        username = match.group(1)
        pujian = [
        f"Terima kasih atas kontribusi Anda, {username}!",
        f"{username}, Anda luar biasa!",
        f"{username}, Anda membuat komunitas menjadi lebih baik.",
        f"{username}, Anda inspiratif!",
        f"{username}, Anda berharga!",
        f"{username}, Anda adalah motivasi bagi kita semua.",
        f"{username}, Kami menghargai Anda!",
        f"{username}, Anda membuat perbedaan!",
        f"{username}, Terus berikan yang terbaik!",
        f"{username}, Anda adalah sumber inspirasi!",
        f"{username}, Jangan pernah menyerah!",
        f"{username}, Anda adalah teladan yang baik!",
        f"{username}, Hidup Anda berharga!",
        f"{username}, Anda hebat!",
        f"{username}, Dunia ini lebih baik dengan Anda!",
        f"{username}, Anda pantas mendapat pujian!",
        f"{username}, Selamat! Anda luar biasa!",
        f"{username}, Anda menakjubkan!",
        f"{username}, Anda memberikan energi positif!",
        f"{username}, Anda layak mendapat penghargaan!",
        f"{username}, Anda mencerahkan hari saya!",
        f"{username}, Anda membuat perbedaan yang nyata!",
        f"{username}, Anda adalah inspirasi bagi banyak orang!",
        f"{username}, Anda sangat berarti bagi kami!",
        f"{username}, Anda adalah pahlawan sejati!",
        f"{username}, Keren sekali!",
        f"{username}, Anda luar biasa hari ini!",
        f"{username}, Terima kasih telah menjadi bagian dari tim kami!",
        f"{username}, Karya Anda sangat dihargai!",
        f"{username}, Anda adalah contoh yang baik untuk diikuti!",
        f"{username}, Anda adalah aset berharga!",
        f"{username}, Selamat atas pencapaian Anda!",
        f"{username}, Anda membuat kami bangga!",
        f"{username}, Anda adalah sumber inspirasi yang tak terelakkan!"
        ]
        kirim_pesan(random.choice(pujian))
        
    def py(self, match):
        if  match.group(3) == None:
            kirim_pesan("Contoh penggunaan: .py print(123)")
        else:
            code = match.group(3).replace(" ", "\n")
            banned = ['os', 'sys']
            if any(word in code for word in banned):
                kirim_pesan(f"Terdapat Syntak yang tidak diperbolehkan {banned}")
            else:
                try:
                    print(code)
                    with open("temp.py", "w") as f:
                        f.write(code)
                    result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
                    kirim_pesan(f"Output: {result.stdout}")
                except Exception as e:
                    kirim_pesan("Error executing Python code:", e)
                finally:
                    os.remove("temp.py")
                    
    def ai(self, match):
        if match.group(3) == None:
            kirim_pesan("Cara penggunaan: .ai <teks>")
        else:
            username = match.group(1)
            question = match.group(3)
            ceks = gemini(question)
            if username in Admin_name:
                if isinstance(ceks, list):
                    for item in ceks:
                        kirim_pesan(item)
                        time.sleep(7)
                elif ceks == None:
                    kirim_pesan("terlalu banyak permintaan")
                    gemini(question)
                else:
                    kirim_pesan(ceks)
            elif username not in Admin_name:
                kirim_pesan(ceks)
while True:
    screen = pyautogui.screenshot().save("temp.png")
    img = Image.open("temp.png")
    text_cmd = pytesseract.image_to_string(img)
    run = Cmd()
    command('menu', run.menu)
    command('nama_keren', run.nama_keren)
    command('day', run.day)
    command('dice', run.dice)
    command('owner', run.owner)
    command('quotes', run.quotes)
    command('puja', run.puja)
    command('py', run.py)
    command('ai', run.ai)
    os.remove("temp.png")
