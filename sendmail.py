import webbrowser 
import urllib.parse 
 
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
 
sendGmail()
