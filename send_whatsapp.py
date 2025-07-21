import pywhatkit 
from datetime import datetime, timedelta 

def sendWhatsApp(): 
    now = datetime.now() 
    future_time = now + timedelta(seconds=50) 
    hours = future_time.hour 
    minutes = future_time.minute 
    message = "Hi Sidharth I am good \n" 
    pywhatkit.sendwhatmsg("+91 8079018281", f"{message}", hours, minutes) 
 
sendWhatsApp() 
