import os 
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException, NoSuchElementException 

def post_to_facebook(username, password, message=None, image_path=None): 
        """ 
        Posts a message or image to Facebook using Selenium automation 
        
        Args: 
            username (str): Facebook username/email 
            password (str): Facebook password 
            message (str): Text message to post 
            image_path (str): Path to image file 
        """ 
        # Configure browser options 
        options = webdriver.ChromeOptions() 
        options.add_argument("--disable-notifications") 
        options.add_argument("--disable-infobars") 
        options.add_argument("--disable-extensions") 
        options.add_argument("--disable-dev-shm-usage") 
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized") 
        
        # Initialize WebDriver (ensure you have chromedriver in PATH) 
        driver = webdriver.Chrome(options=options) 
        driver.implicitly_wait(10) 
        
        try: 
            # Navigate to Facebook 
            driver.get("https://www.facebook.com/") 
            print("    Loading Facebook...") 
            
            # Login 
            print("     Logging in...") 
            email_field = WebDriverWait(driver, 20).until( 
                EC.presence_of_element_located((By.ID, "email")) 
            ) 
            email_field.send_keys(username) 
            
            password_field = driver.find_element(By.ID, "pass") 
            password_field.send_keys(password) 
            password_field.send_keys(Keys.RETURN) 
            
            # Wait for login to complete 
            WebDriverWait(driver, 20).until( 
                EC.presence_of_element_located((By.XPATH, '//div[@role="navigation"]')) 
            ) 
            print("   Login successful") 
            
            # Navigate to profile 
            profile_link = WebDriverWait(driver, 20).until( 
                EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Profile"]')) 
            ) 
            profile_link.click() 
            print("     Navigated to profile") 
            
            # Wait for profile page to load 
            WebDriverWait(driver, 20).until( 
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Create a post"]')) 
            ) 
            
            # Create a post 
            create_post_button = driver.find_element(By.XPATH, '//div[@aria-label="Create a post"]') 
            create_post_button.click() 
            print("          Creating post...")
            
            # Wait for post dialog to appear 
            post_dialog = WebDriverWait(driver, 20).until( 
                EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]')) 
            ) 
            
            # Add message if provided 
            if message: 
                post_field = post_dialog.find_element(By.XPATH, './/div[@role="textbox"]') 
                post_field.send_keys(message) 
                print(f"      Added message: {message[:20]}...") 
                time.sleep(1)  # Allow text to appear 
            
            # Add image if provided 
            if image_path: 
                if not os.path.exists(image_path): 
                    print(f"  Image not found: {image_path}") 
                    return 
                
                # Click photo/video button 
                photo_button = post_dialog.find_element(By.XPATH, '//div[@aria-label="Photo/Video"]') 
                photo_button.click() 
                time.sleep(1) 
                
                # Upload file (using native file input) 
                file_input = driver.find_element(By.XPATH, '//input[@type="file"]') 
                file_input.send_keys(os.path.abspath(image_path)) 
                print(f"           Uploading image: {image_path}") 
                
                # Wait for upload to complete 
                WebDriverWait(driver, 30).until( 
                    EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Remove"]')) 
                ) 
                print("   Image uploaded") 
            
            # Post the content 
            post_button = post_dialog.find_element(By.XPATH, '//div[@aria-label="Post" and @role="button"]') 
            post_button.click() 
            print("        Post published!") 
            
            # Wait for post to appear 
            WebDriverWait(driver, 20).until( 
                EC.presence_of_element_located((By.XPATH, '//div[@data-pagelet="ProfileTimeline"]')) 
            ) 
            print("   Post confirmed on timeline") 
            
        except TimeoutException: 
            print("       Timed out waiting for element. Facebook UI might have changed.") 
        except NoSuchElementException as e: 
            print(f"    Element not found: {e}") 
        except Exception as e: 
            print(f"  An error occurred: {str(e)}") 
        finally: 
            # Clean up 
            print("   Closing browser in 5 seconds...") 
            time.sleep(5) 
            driver.quit() 
    
if __name__ == "__main__": 
        # Configuration - Replace with your credentials 
        USERNAME = "Rahul Sain" 
        PASSWORD = "" 
        MESSAGE = "Posted automatically with Python!                   " 
        IMAGE_PATH = "path/to/your/image.jpg"  # Set to None for text-only post 
        
        post_to_facebook(USERNAME, PASSWORD, MESSAGE, IMAGE_PATH) 
