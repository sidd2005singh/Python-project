import Client 

def Make_Call(): 
        # Replace these with your Twilio account credentials 
        account_sid = 'ACbca2f4aa500aac75286c5a1416f4cd' # Your Twilio account SID   
        auth_token = 'b8ad753475828cba9fab67b811cedf'   # Your Twilio auth token 
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
    
Make_Call() 
