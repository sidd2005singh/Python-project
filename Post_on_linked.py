from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import time 

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
         
u = "rsurendrasen90@gmail.com" 
# p= input("Enter User Password") 
p = "Rakhirahul@1343" 
# r=input("Enter receiver profile url") 
r = "https://www.linkedin.com/in/rahul-sain-88a963288/" 

send_linkedin_message( 
    username=u, 
    password=p, 
    recipient_profile_url=r, 
    message_text="Hello from automated Selenium script!" 
) 
