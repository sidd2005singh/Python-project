import os 
import time 
import psutil 
import urllib.parse 
import webbrowser 
import requests 
import pandas as pd 
from PIL import Image, ImageDraw 
from bs4 import BeautifulSoup 
from datetime import datetime, timedelta 
from twilio.rest import Client 
from googlesearch import search 
import pywhatkit 
import serial 
import serial.tools.list_ports  # For GSM or COM port-based communication 
 
# Selenium for browser automation 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager 
 
print("Using serial module from:", serial.__file__) 
 
def Mak_Call(): 
    # Replace these with your Twilio account credentials 
    account_sid = 'ACbca2f4aa500aac75286c5a1416f4cd9c' 
    auth_token = 'b8ad753475828cba9fab67b811cedfd6' 
    twilio_number = '+12708354429'  # Your Twilio phone number 
    to_number = '+918079018281'   # The phone number you want to call 
 
    # Message or URL to read aloud 
    twiml_url = 'http://demo.twilio.com/docs/voice.xml'  # Twilio XML with message 
 
    client = Client(account_sid, auth_token) 
 
    call = client.calls.create( 
        to=to_number, 
        from_=twilio_number, 
        url=twiml_url 
    ) 
     
    print(f"   Call initiated: SID {call.sid}") 
 
# Auto-detect and list available COM ports 
def list_available_ports(): 
    ports = list(serial.tools.list_ports.comports()) 
    print("\nAvailable COM Ports:") 
    for i, port in enumerate(ports): 
        print(f"{i + 1}. {port.device} ({port.description})") 
    return ports 
 
# WhatsApp sender 
def sendWhatsApp(): 
    now = datetime.now() 
    future_time = now + timedelta(seconds=50) 
    hours = future_time.hour 
    minutes = future_time.minute 
    message = "This my message\n" * 4 
    pywhatkit.sendwhatmsg("+91 9782815557", f"{message}", hours, minutes) 
 
# Gmail (opens in browser) 
def sendGmail(): 
    to = "rsurendra90@gmail.com" 
    subject = "Hello from Python" 
    body = "This is a test message written in Python, sent manually." 
    params = urllib.parse.urlencode({ 
        'to': to, 
        'subject': subject, 
        'body': body 
    }) 
    url = f"https://mail.google.com/mail/?view=cm&fs=1&{params}" 
    webbrowser.open(url) 
 
# RAM usage checker 
def checkram(): 
    memory = psutil.virtual_memory() 
    print("RAM Details:") 
    print(f"Total     : {memory.total / (1024 ** 3):.2f} GB") 
    print(f"Available : {memory.available / (1024 ** 3):.2f} GB") 
    print(f"Used      : {memory.used / (1024 ** 3):.2f} GB") 
    print(f"Free      : {memory.free / (1024 ** 3):.2f} GB") 
    print(f"Percent   : {memory.percent}%") 
 
# Image maker 
def makeImg(): 
    width, height = 300, 300 
    image = Image.new("RGB", (width, height), "red") 
    draw = ImageDraw.Draw(image) 
    center = (width // 2, height // 2) 
    radius = 80 
    draw.ellipse([ 
        (center[0] - radius, center[1] - radius), 
        (center[0] + radius, center[1] + radius) 
    ], fill="blue") 
    image.save("my_image.png") 
    image.show() 
 
def search_on_google(): 
    """ 
    Perform Google search, display top 10 results with titles, 
    and open each in a new browser tab. 
    Requires: googlesearch-python, requests, beautifulsoup4 
    """ 
    from googlesearch import search 
    import requests 
    from bs4 import BeautifulSoup 
    import webbrowser 
    import time 
 
    query = input("    Enter search query: ").strip() 
    if not query: 
        print("Query cannot be empty.") 
        return 
 
    urls = [] 
    print(f"\n    Searching Google for: {query!r} ...\n") 
 
    for idx, url in enumerate(search(query, num_results=10), start=1): 
        try: 
            response = requests.get(url, timeout=5) 
            soup = BeautifulSoup(response.text, "html.parser") 
            title = soup.title.string.strip() if soup.title else url 
        except Exception: 
            title = url 
        print(f"{idx}. {title}\n   {url}\n") 
        urls.append(url) 
 
    print("  Opening each result in a new browser tab...\n") 
    time.sleep(2) 
    for url in urls: 
        webbrowser.open_new_tab(url) 
        time.sleep(1) 
 
def send_linkedin_message(username, password, recipient_profile_url, message_text): 
    # 1) create driver correctly 
    service = Service(ChromeDriverManager().install()) 
    driver  = webdriver.Chrome(service=service) 
     
    try: 
        driver.get("https://www.linkedin.com/login") 
        time.sleep(4) 
 
        # 2) log in 
        driver.find_element(By.ID, "username").send_keys(username) 
        driver.find_element(By.ID, "password").send_keys(password) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click() 
        time.sleep(5) 
 
        # 3) go to profile & click “Message” 
        driver.get(recipient_profile_url) 
        time.sleep(4) 
 
        message_btn = driver.find_element( 
            By.XPATH, "//button[contains(., 'Message')]" 
        ) 
        message_btn.click() 
        time.sleep(4) 
 
        # 4) write & send text 
        textbox = driver.find_element(By.XPATH, "//div[@role='textbox']") 
        textbox.send_keys(message_text) 
        time.sleep(4) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click() 
        time.sleep(5) 
        print("    Message sent.") 
    except Exception as e: 
        print(f"   Error: {e}") 
    finally: 
        time.sleep(5) 
 
from twilio.rest import Client 
    
    def send_sms(): 
        # Replace with your Twilio credentials 
    account_sid = 'YOUR_TWILIO_SID'
    auth_token = 'YOUR_TWILIO_TOKEN'
        twilio_number = '+12708354429'  # Your Twilio phone number 
        recipient_number = '+918079018281'  # Destination phone number 
    
    # Create the client 
    client = Client(account_sid, auth_token) 

    # Send the SMS 
    message = client.messages.create( 
        body="Hello from Python via Twilio        ", 
        from_=twilio_number, 
        to=recipient_number 
    ) 
    return message.sid 

    def dwnweb_Data(): 
        headers = {"User -Agent": "Mozilla/5.0"} 

    def download_tables(url): 
        print("      Extracting tables...") 
        folder = "tables" 
        os.makedirs(folder, exist_ok=True) 
 
        response = requests.get(url, headers=headers) 
        response.raise_for_status() 
        html = response.text 
 
        # Save page plain text (optional) 
        with open(os.path.join(folder, "page_text.txt"), "w", encoding="utf-8") as f: 
            f.write(BeautifulSoup(html, "html.parser").get_text()) 
        print("   Saved plain text of page.") 
 
        try: 
            tables = pd.read_html(html) 
            for i, table in enumerate(tables, start=1): 
                filename = os.path.join(folder, f"table_{i}.xlsx") 
                table.to_excel(filename, index=False) 
                print(f"   Saved table -> {filename}") 
            if not tables: 
                print("    No tables found on this page.") 
        except ValueError: 
            print("  No readable tables found.") 
 
    def download_images(url): 
        print("            Downloading images...") 
        folder = "images" 
        os.makedirs(folder, exist_ok=True) 
 
        response = requests.get(url, headers=headers) 
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, "html.parser") 
 
        downloaded = 0 
        for img in soup.find_all("img"): 
            src = img.get("src") 
            if not src: 
                continue 
 
            img_url = urljoin(url, src) 
            if img_url.startswith("//"): 
                img_url = "https:" + img_url 
 
            parsed = urlparse(img_url) 
            filename = os.path.basename(parsed.path) 
            if not filename: 
                continue 
            filepath = os.path.join(folder, filename) 
 
            if os.path.exists(filepath): 
                continue 
 
            try: 
                img_resp = requests.get(img_url, headers=headers, timeout=15) 
                img_resp.raise_for_status() 
                with open(filepath, "wb") as f: 
                    f.write(img_resp.content) 
                downloaded += 1 
                print(f"     Saved -> {filepath}") 
            except requests.RequestException as e: 
                print(f"  Could not download {img_url}: {e}") 
 
        if downloaded == 0: 
            print("    No images downloaded.") 
        else: 
            print(f"   Downloaded {downloaded} images into '{folder}/'") 
 
# ── Example usage ── 
url = "https://en.wikipedia.org/wiki/Krishna" 
 
# Call what you need: 
print("""Enter 1 to Download video 
      Enter 2 for download image""") 
if int(input("Enter Number: ")) == 1:  
    download_tables(url) 
elif int(input("Enter Number: ")) == 2: 
    download_images(url) 
else: 
    print("Wrong Choice") 
 
# Example usage: 
def post_to_instagram(username, password, message, image_path=None): 
    """ 
    Posts an image or video to Instagram feed, or a text-based story if no media is provided. 
 
    Args: 
        username (str): Instagram username 
        password (str): Instagram password 
        message (str): Caption for the media or text for story 
        image_path (str, optional): Path to the image/video file. If None, a text story is posted. 
    """ 
    cl = Client() 
    session_file = f"{username}_session.json" 
 
    try: 
        # Load existing session 
        if os.path.exists(session_file): 
            cl.load_settings(session_file) 
 
        # Login (always attempt fresh login) 
        cl.login(username, password) 
 
        # Save session to file 
        cl.dump_settings(session_file) 
 
        # Post content 
        if image_path: 
            extension = image_path.lower().split('.')[-1] 
            if extension in ['mp4', 'mov']: 
                cl.video_upload(image_path, caption=message) 
                print("   Video posted successfully!") 
            elif extension in ['jpg', 'jpeg', 'png']: 
                cl.photo_upload(image_path, caption=message) 
                print("   Photo posted successfully!") 
            else: 
                print(f"  Unsupported file type: {extension}") 
        else: 
            # Posting a simple text story (not supported natively without media) 
            # Instead, we create a white background image and post as story 
            from PIL import Image, ImageDraw, ImageFont 
            temp_image = "temp_story.jpg" 
            img = Image.new("RGB", (720, 1280), color="white") 
            draw = ImageDraw.Draw(img) 
            draw.text((50, 600), message, fill="black") 
            img.save(temp_image) 
            cl.photo_upload_to_story(temp_image) 
            os.remove(temp_image) 
            print("   Text story posted as image!") 
 
    except (LoginRequired, ChallengeRequired) as e: 
        print("    Login failed. Possible reasons:") 
        print("- Invalid or expired session") 
        print("- 2FA enabled or suspicious login detected") 
        print(f"Details: {e}") 
 
    except Exception as e: 
        print(f"  Unexpected error: {e}") 
 
    finally: 
        password = None  # Clear password for security 
 
# === MENU === 
print(""" 
Enter your choice: 
      1 for WhatsApp 
      2 for Email  
      3 for Read RAM 
      4 for Make Image 
      5 for send sms 
      6 for call 
      7 for search on google 
      8 for downloadTable 
      9 for Linkedin Automation 
      10 for Instagram Post 
""") 
 
choice = int(input("Enter a number: ")) 
 
if choice == 1: 
    sendWhatsApp() 
elif choice == 2: 
    sendGmail() 
elif choice == 3: 
    checkram() 
elif choice == 4: 
    makeImg() 
elif choice == 5: 
    send_sms() 
elif choice == 6: 
    Mak_Call() 
elif choice == 7: 
    search_on_google() 
elif choice == 8: 
    dwnweb_Data() 
elif choice == 9: 
    # u= input("Enter User Mail") 
    u = "rsurendrasen90@gmail.com" 
    # p= input("Enter User Password") 
    p = "Rakhirahul@1343" 
    # r=input("Enter receiver profile url") 
    r = "https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAA Dv5QuoBL56nbv3mGBMbLNfVu3vs6iEhZS0&keywords=Siddharth%20singh&origin=ENTITY_SEARC H_HOME_HISTORY&sid=AYm" 
    send_linkedin_message( 
        username=u, 
        password=p, 
        recipient_profile_url=r, 
        message_text="Hello from automated Selenium script!" 
    ) 
elif choice == 10: 
    USERNAME = "rahul_sen1251" 
    PASSWORD = "trikal@134344" 
    MESSAGE = "Automated post via Python    " 
    IMAGE_PATH = "D://lw classes//IMG-20240820-WA0000.jpg"  # or None for text-based story 
 
    post_to_instagram(USERNAME, PASSWORD, MESSAGE, IMAGE_PATH) 
else: 
    print("Invalid choice.") 
