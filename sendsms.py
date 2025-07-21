from twilio.rest import Client 
 
def send_sms(): 
    # Replace with your Twilio credentials 
    account_sid = ''  # use your  
    auth_token = '' 
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
 
send_sms() 
