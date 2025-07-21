import tweepy 
    
import os 
import requests 
import base64 
from dotenv import load_dotenv 
    
    # Load environment variables 
load_dotenv() 
    
def post_to_twitter(text=None, image_path=None): 
        """ 
        Posts a tweet with optional image to Twitter 

        Args: 
            text (str): Text content of the tweet (280 char max) 
            image_path (str): Path to image file 
        """ 
        # Get credentials from environment 
        # Twitter Developer API credentials (keep these secret!) 
        API_KEY = "LPC9SMgXRSKR4UrkyShQ5A" #  Use Your API Key 
        API_SECRET = "PZ0ukcIrve3T03VyRN4CzCEUCDOt3mNLx3TYYgxK" # Use Your API Secret 
        ACCESS_TOKEN = "1946137468639592448-ekZQOnZV9kiuDqw8I" # Use Your Access Token 
        ACCESS_SECRET = "N6WyQyPIAH7p7qkIHqyFEjXxF3Mojo29cGaml" # Use Your Access Secret 
        BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIV73AEAAAAAn8%2BKqptYwCbEeN" # Use Your Bearer Token 
    
        # Validate credentials 
        if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, BEARER_TOKEN]): 
            print("  Missing Twitter credentials in .env file") 
            return 
    
        # Step 1: Get OAuth 2.0 Access Token (for media upload) 
        auth_url = "https://api.twitter.com/oauth2/token" 
        credentials = base64.b64encode(f"{API_KEY}:{API_SECRET}".encode()).decode() 
        auth_headers = { 
            "Authorization": f"Basic {credentials}", 
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" 
        } 
        auth_data = {"grant_type": "client_credentials"} 
        
        try: 
            auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data) 
            auth_response.raise_for_status() 
            app_access_token = auth_response.json()["access_token"] 
        except Exception as e: 
            print(f"  Failed to get access token: {str(e)}") 
            return
        
        # Step 2: Upload media (if provided) 
        media_id = None 
        if image_path: 
            try: 
                # Check file exists 
                if not os.path.exists(image_path): 
                    print(f"  Image not found: {image_path}") 
                    return 
                
                # Upload image 
                media_url = "https://upload.twitter.com/1.1/media/upload.json" 
                with open(image_path, 'rb') as file: 
                    media_data = {"media": file} 
                    media_headers = {"Authorization": f"Bearer {app_access_token}"} 
                    media_response = requests.post(media_url, headers=media_headers, files=media_data)
                    media_response.raise_for_status() 
                    media_id = media_response.json()["media_id_string"] 
                    print(f"           Image uploaded successfully! Media ID: {media_id}") 
            except Exception as e: 
                print(f"  Media upload failed: {str(e)}") 
                return 
    
        # Step 3: Post tweet 
        tweet_url = "https://api.twitter.com/2/tweets" 
        tweet_headers = { 
            "Authorization": f"Bearer {BEARER_TOKEN}", 
            "Content-Type": "application/json" 
        } 
        tweet_data = {} 
        
        if text and media_id: 
            tweet_data["text"] = text 
            tweet_data["media"] = {"media_ids": [media_id]} 
        elif text: 
            tweet_data["text"] = text 
        elif media_id: 
            tweet_data["media"] = {"media_ids": [media_id]} 
        else: 
            print("    Nothing to post. Provide text or image") 
            return
        
        try: 
            tweet_response = requests.post(tweet_url, headers=tweet_headers, json=tweet_data) 
            tweet_response.raise_for_status() 
            tweet_id = tweet_response.json()["data"]["id"] 
            print(f"   Tweet posted successfully! Tweet ID: {tweet_id}") 
            return tweet_id 
        except Exception as e: 
            print(f"  Failed to post tweet: {str(e)}") 
            if tweet_response: 
                print(f"Twitter API response: {tweet_response.text}") 
    
if __name__ == "__main__": 
        # ===== CONFIGURE THESE ===== 
        # Create .env file with: 
        #   TWITTER_API_KEY=your_api_key 
        #   TWITTER_API_SECRET=your_api_secret 
        #   TWITTER_ACCESS_TOKEN=your_access_token 
        #   TWITTER_ACCESS_SECRET=your_access_secret 
        #   TWITTER_BEARER_TOKEN=your_bearer_token 
        
        # Post example 
        post_to_twitter( 
            text="Hello Twitter from Python!                  ", 
            # image_path="path/to/your/image.jpg" 
        ) 
