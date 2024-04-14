from PIL import Image
from datetime import datetime
import time, random, re, pyautogui, pytesseract, os, requests, subprocess, rpg,sys

apikey = "Your GEMINI APIKEY here"
Admin_name = ['RandSfk', 'Selvi']
valid_username = rpg.read_usernames()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cooldowns = {}

def read_usernames():
    with open('name.txt', 'r') as file:
        usernames = [line.strip() for line in file]
    return usernames

def add_username(username):
    with open('name.txt', 'r') as file:
        usernames = [line.strip() for line in file]
    if username.strip() not in usernames:
        with open('name.txt', 'a') as file:
            file.write(username.strip() + '\n')
        return(f"Username '{username}' has been added successfully.")
    else:
        return(f"Username '{username}' already exists.")
        
def remove_username(username):
    temp_file = 'name.txt'
    with open('name.txt', 'r') as file, open(temp_file, 'w') as temp:
        for line in file:
            if line.strip() != username:
                temp.write(line)
    return(f"Username '{username}' has been removed.")

def is_on_cooldown(username):
    if username in Admin_name:
        return False
    if username in cooldowns:
        current_time = time.time()
        cooldown_time = cooldowns[username]
        if current_time - cooldown_time < 3600: 
            return True
        else:
            del cooldowns[username] 
    return False
def process_uang_kaget_command(username):
    if not is_on_cooldown(username):
        kirim_pesan(f"Selamat {username}, anda mendapat uang sebesar:")
        kirim_pesan("/roll 100000000")
        cooldowns[username] = time.time()
    else:
        kirim_pesan(f"{username}, Anda masih dalam cooldown. Silakan coba lagi nanti.")

def process_thr_command(username, target):
    if not is_on_cooldown(username):
        kirim_pesan(f"Selamat {target}, anda mendapat uang dari {username}, sebesar:")
        kirim_pesan("/roll 100000000")
        cooldowns[username] = time.time()
    else:
        kirim_pesan(f"{username}, Anda masih dalam cooldown. Silakan coba lagi nanti.")
        
def process_quotes_command():
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

def klik():
    time.sleep(1)
    pyautogui.click(40, pyautogui.size()[1] - 70)
    pyautogui.click(230, pyautogui.size()[1] - 70)

def kirim_pesan(message):
    pyautogui.typewrite('/')
    pyautogui.press('backspace')
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    pyautogui.typewrite('/clearchat')
    pyautogui.press('enter')

def read_usernames():
    with open('name.txt', 'r') as file:
        usernames = [line.strip() for line in file]
    return usernames

def menu(username):
    usernames = read_usernames()
    current_time = time.localtime()
    current_hour = str(current_time.tm_hour) 
    current_minute = str(current_time.tm_min)

    def adminmenu():
        kirim_pesan("> thr")
        kirim_pesan("> give")
        kirim_pesan('> nama_keren')
        kirim_pesan('> skin_cl')
        kirim_pesan("> day")
        kirim_pesan("> (pertambahan)")
        kirim_pesan("> quotes")
        kirim_pesan("> puja")
        kirim_pesan("> owner")
        kirim_pesan("> ai")
        kirim_pesan("> py!!")
        kirim_pesan("< hunt")
        kirim_pesan("< stats")
        kirim_pesan("< buy")
        kirim_pesan("< gacha")

    def menu():
        pesan_salam = f"Hai [{username}] Jam: {current_hour}:{current_minute}"
        kirim_pesan(pesan_salam)
        kirim_pesan("Saya adalah Joseph")
        kirim_pesan("Mafia bot dari Party Keluarga Hamburg")
        time.sleep(4)
        kirim_pesan("Menu yang tersedia :")
        time.sleep(2)
        kirim_pesan("> thr ")
        kirim_pesan("> give")
        kirim_pesan('> nama_keren')
        kirim_pesan('> skin_cl')
        kirim_pesan("> day")
        kirim_pesan("> (pertambahan)")
        kirim_pesan("> quotes")
        kirim_pesan("> puja")
        kirim_pesan("> owner")
        kirim_pesan("> ai")
        kirim_pesan("> py!!")

    if username in usernames: 
        pesan_salam = f"Hallo Tuan [{username}], Sekarang Jam: {current_hour}:{current_minute}"
        kirim_pesan(pesan_salam)
        kirim_pesan(f"Apa yang tuan {username} inginkan?")
        time.sleep(4)
        kirim_pesan("Menu yang saya bisa:")
        time.sleep(2)
        adminmenu()

    elif username == "Selvi":
        pesan_salam = f"Hallo Nyonya agung [{username}], Sekarang Jam: {current_hour}:{current_minute}"
        kirim_pesan(pesan_salam)
        kirim_pesan(f"Apa yang nyonya {username} inginkan?")
        time.sleep(4)
        kirim_pesan("Menu yang tersedia:")
        time.sleep(2)
        adminmenu()
    else:
        menu()
        

def generate_cool_name(name):
    adjectives = ['Mighty', 'Sleek', 'Shadow', 'Blaze', 'Thunder', 'Eternal', 'Epic', 'Ninja', 'Alpha', 'Omega']
    nouns = ['Phoenix', 'Dragon', 'Wolf', 'Storm', 'Tiger', 'Sword', 'Warrior', 'Legend', 'Hero', 'Knight']
    
    name_parts = name.split()
    
    num_adjectives = random.randint(1, min(len(name_parts), 2))
    selected_adjectives = random.sample(adjectives, num_adjectives)
    
    cool_name = ' '.join(selected_adjectives + name_parts)
    
    return cool_name

def warna_skin():
    skin_colors = {
        "Fair": "#F8E5DA",
        "Light": "#F2D5BB",
        "Medium": "#E5B887",
        "Olive": "#B28D6A",
        "Tan": "#8A694B",
        "Deep": "#634834",
        "Ebony": "#3C281D",
        "Pale": "#FFE4C4",
        "Caramel": "#FFA07A",
        "Chestnut": "#CD5C5C",
        "Mahogany": "#8B4513",
        "Sable": "#705040",
        "Mocha": "#462E1B",
        "Honey": "#DAA520",
        "Amber": "#FFBF00",
        "Bronze": "#CD7F32",
        "Cocoa": "#D2691E",
        "Sienna": "#A0522D",
        "Copper": "#B87333",
        "Sepia": "#704214"
    }
    return skin_colors

def nama_keren(username):
    cool_name = generate_cool_name(username)
    kirim_pesan(f"Nama keren Anda: {cool_name}")

def get_indonesian_day(day_num):
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    return days[day_num]

def process_puji_command(username):
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
def gemini(meseg):
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": meseg+" dalam 60 huruf"
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
            return(response_text)
        else:
            print("No candidates found.")

while True:
##########//////////// [ENGINE] //////////////////####################################################
    screen = pyautogui.screenshot()
    screen.save("screenshot.png")
    img = Image.open("screenshot.png")
    text_cmd = pytesseract.image_to_string(img)
    ### (Opsional)
    #print(text_cmd)

#########//////////////// [BASIC COMMAND] /////////////////########################################################

    if ".menu" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .menu', text_cmd)
        if match:
            username = match.group(1)
            print(username)
            if "[say]" in text_cmd.lower():
                menu(username)
            else:
                menu(username)

    elif ".thr" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .thr ', text_cmd)
        if match:
            username = match.group(1)
            if username not in Admin_name and not is_on_cooldown(username):
                process_uang_kaget_command(username)
            elif username not in Admin_name:
                kirim_pesan(f"{username}, Anda masih dalam cooldown. Silakan coba lagi nanti.")
            elif username in Admin_name:
                kirim_pesan(f"Selamat tuan {username}, anda mendapat uang sebesar:")
                kirim_pesan("/roll 9999999999")

    elif ".give" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .give \[(.*?)\]', text_cmd)
        if match:
            username = match.group(1)
            target = match.group(2)
            if username not in Admin_name and not is_on_cooldown(username):
                process_thr_command(username=username, target=target)
            elif username not in Admin_name:
                kirim_pesan(f"{username}, Anda masih dalam cooldown. Silakan coba lagi nanti.")

    elif ".nama_keren" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .nama_keren', text_cmd)
        if match:
            username = match.group(1)
            nama_keren(username)

    elif re.search(r'\(\d+\+\d+\)', text_cmd):
        matches = re.findall(r'\((\d+)\+(\d+)\)', text_cmd)
        for match in matches:
            angka1 = int(match[0])
            angka2 = int(match[1])
            total = angka1 + angka2
            print("Pola ditemukan dalam teks.")
            print("Angka pertama:", angka1)
            print("Angka kedua:", angka2)
            kirim_pesan(f"Total pertambahan dari {str(angka1)} + {str(angka2)} = {str(total)}")

    elif re.search(r'\(\d+\-\d+\)', text_cmd):
        matches = re.findall(r'\((\d+)\-(\d+)\)', text_cmd)
        for match in matches:
            angka1 = int(match[0])
            angka2 = int(match[1])
            total = angka1 - angka2
            print("Pola ditemukan dalam teks.")
            print("Angka pertama:", angka1)
            print("Angka kedua:", angka2)
            kirim_pesan(f"Total pengurangan dari {str(angka1)} - {str(angka2)} = {str(total)}")

    elif re.search(r'\(\d+\*\d+\)', text_cmd):
        matches = re.findall(r'\((\d+)\*(\d+)\)', text_cmd)
        for match in matches:
            angka1 = int(match[0])
            angka2 = int(match[1])
            total = angka1 * angka2
            print("Pola perkalian ditemukan dalam teks.")
            print("Angka pertama:", angka1)
            print("Angka kedua:", angka2)
            kirim_pesan(f"Total perkalian dari {str(angka1)} * {str(angka2)} = {str(total)}")

    elif re.search(r'\(\d+/\d+\)', text_cmd):
        matches = re.findall(r'\((\d+)/(\d+)\)', text_cmd)
        for match in matches:
            angka1 = int(match[0])
            angka2 = int(match[1])
            total = angka1 / angka2
            print("Pola pembagian ditemukan dalam teks.")
            print("Angka pertama:", angka1)
            print("Angka kedua:", angka2)
            kirim_pesan(f"Total pembagian dari {str(angka1)} / {str(angka2)} = {str(total)}")

    elif ".skin_cl" in text_cmd.lower():
        skin_colors = warna_skin()
        warna = random.choice(list(skin_colors.keys()))
        kirim_pesan("Berikut adalah kode warna kulit:")
        kirim_pesan(f"{warna}: {skin_colors[warna]}")

    elif ".owner" in text_cmd.lower():
        kirim_pesan("username: Rand Sfk")
        kirim_pesan("instagram: rand_sfk")
        kirim_pesan("github  : RandSfk")
        kirim_pesan("facebook: RandSfk Remastered")

    elif ".day" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .day', text_cmd)
        if match:
            username = match.group(1)
            now = datetime.now()
            day_index = now.weekday()
            day_name = get_indonesian_day(day_index)
            kirim_pesan("Sekarang adalah hari "+day_name+" "+username)

    elif ".quotes" in text_cmd.lower():
        process_quotes_command()

    elif ".puja" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .puja', text_cmd)
        if match:
            username = match.group(1)
            process_puji_command(username)

    elif ".ai" in text_cmd.lower():
        match = re.search(r'.ai \[(.*?)\]', text_cmd)
        if match:
            question = match.group(1)
            ceks = gemini(question)
            kirim_pesan(ceks)
    elif '.py!!' in text_cmd:
        match = re.search(r'\.py!!(.*?)!!', text_cmd)
        if match:
            code = match.group(1).replace("\\n", "\n")
            try:
                print(code)
                with open("temp.py", "w") as f:
                    f.write(code)
                result = subprocess.run(["python", "temp.py"], capture_output=True, text=True)
                kirim_pesan(f"Eksekusi Python: {result.stdout}")
            except Exception as e:
                print("Error executing Python code:", e)
            finally:
                os.remove("temp.py")
#######################//////////////////////////////////// [RPG] /////////////////////////////////################################

    elif ".hunt" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .hunt', text_cmd)
        if match:
            username = match.group(1)
            if username in valid_username:
                hasil_hunt = rpg.hunt(username)
                kirim_pesan(hasil_hunt) 
    elif ".gacha" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .gacha', text_cmd)
        if match:
            username = match.group(1)
            if username in valid_username:
                hasil_gacha = rpg.gacha(username)
                kirim_pesan(hasil_gacha)

    elif ".stats" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .stats', text_cmd)
        if match:
            username = match.group(1)
            if username in valid_username:
                print(username)
                character_info = rpg.view_status(username)
                kirim_pesan(character_info)

    elif ".inven" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .inven', text_cmd)
        if match:
            username = match.group(1)
            if username in valid_username:
                print(username)
                character_info = rpg.view_inventory(username)
                kirim_pesan(character_info)

    elif ".buy" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .buy (\w+)', text_cmd)
        if match:
            username = match.group(1)
            item = match.group(2)
            if username in valid_username:
                hasil_pembelian = rpg.buy(username, item)  
                kirim_pesan(hasil_pembelian)
    elif ".use" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .use (\w+)', text_cmd)
        if match:
            username = match.group(1)
            item = match.group(2)
            if username in valid_username:
                hasil_pembelian = rpg.use(username, item)  
                kirim_pesan(hasil_pembelian)
#//////// ADMIN TOOL ////////////////////////////////////////////////////////////////////////////////////////////

    elif "msih mau bandel ga?" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] msih mau bandel ga?', text_cmd)
        if match:
            username = match.group(1)
            if username == 'RandSfk':
                kirim_pesan("Ampun tidak tuan")
            else:
                kirim_pesan("Siapalu??")
    elif ".add" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] whispers: .add \[(.*?)\]', text_cmd)
        if match:
            username = match.group(1)
            command = match.group(2)
            if username in Admin_name:
                n = add_username(command)
                kirim_pesan(str(n))
    elif ".rm" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] whispers: .rm \[(.*?)\]', text_cmd)
        if match:
            username = match.group(1)
            command = match.group(2)
            if username in Admin_name:
                b = remove_username(command)
                kirim_pesan(str(b))
    elif ".cek" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] whispers: .cek', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                h = read_usernames()
                kirim_pesan("RPG Acoount: ")
                for name in h:
                    kirim_pesan("- "+str(name))
    elif ".sit" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .sit', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('/sit')
                pyautogui.press('enter')
                kirim_pesan('saya duduk tuan')
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".stand" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .stand', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('/stand')
                pyautogui.press('enter')
                kirim_pesan("saya berdiri tuan")
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".lambai" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .lambai', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('1')
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".back" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .back', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('4')
                kirim_pesan('')
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".sleep" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .sleep', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('6')
                kirim_pesan("Turu")
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".laugh" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .laugh', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('/laugh')
                pyautogui.press('enter')
                kirim_pesan("wkwk")
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
    elif ".kiss" in text_cmd.lower():
        match = re.search(r'\[(.*?)\] .kiss', text_cmd)
        if match:
            username = match.group(1)
            if username in Admin_name:
                pyautogui.typewrite('/kiss')
                pyautogui.press('enter')
                kirim_pesan("MUACHH")
            else:
                kirim_pesan("SIAPA LU NYURUH NYURUH??")
#//////// RPG ////////////////////////////////////////////////////////////////////////////////////////////





    os.remove("screenshot.png")
