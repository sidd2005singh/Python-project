import os 
from instagrapi import Client 
from instagrapi.exceptions import LoginRequired, ChallengeRequired 
 
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
 
# Example usage 
if __name__ == "__main__": 
    USERNAME = "rahul_sen1251" 
    PASSWORD = "trikal@134344" 
    MESSAGE = "Automated post via Python    " 
    IMAGE_PATH = "D://lw classes//IMG-20240820-WA0000.jpg"  # or None for text-based story 
 
    post_to_instagram(USERNAME, PASSWORD, MESSAGE, IMAGE_PATH) 
