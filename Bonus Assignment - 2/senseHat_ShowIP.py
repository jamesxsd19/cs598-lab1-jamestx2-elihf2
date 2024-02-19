from sense_hat import SenseHat
import urllib.request

def get_ip_address():
    
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')
    
BPIP = get_ip_address()
print(BPIP)

sense=SenseHat()
sense.clear()


white= (255,255,255)
#red=(255,0,0)
for i in range(0,2):

    sense.show_message(BPIP, text_colour=white, scroll_speed=0.05)
    
sense.clear()
