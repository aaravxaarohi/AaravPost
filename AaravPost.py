import mechanize
import json
from time import sleep
from datetime import datetime
import os
import sys
import random
import time
import urllib.error

# Color codes and other constants
P = "\x1b[38;5;231m"  # Putih (White)
M = "\x1b[38;5;196m"  # Merah (Red)
H = "\x1b[38;5;46m"   # Hijau (Green)
A = '\x1b[38;5;248m'  # Abu-Abu (Grey)
B = '\x1b[38;5;33m'   # Biru (Blue)
BOLD = "\033[1m"

# Additional headers
g_headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'www.google.com',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
    'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
}

# Function to load cookies from file
def load_cookies_from_file(file_path, cookies):
    with open(file_path, 'r') as f:
        cookies_data = json.load(f)
        for key, value in cookies_data.items():
            c = mechanize.Cookie(
                version=0, name=key, value=value,
                port=None, port_specified=False,
                domain='facebook.com', domain_specified=True, domain_initial_dot=False,
                path='/', path_specified=True,
                secure=False, expires=None,  # No 'secure' attribute in the JSON
                discard=True, comment=None, comment_url=None, rest={}
            )
            cookies.set_cookie(c)

def extract_profile_ids(cookies):
    profile_ids = []
    for cookie in cookies:
        if cookie.name == 'c_user':
            profile_ids.append(cookie.value)
    return profile_ids    

os.system('clear')
def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]
    
    x = """
   


       d8888                                                        
      d88888                                                        
     d88P888                                                        
    d88P 888       8888b.       888d888       8888b.       888  888 
   d88P  888          "88b      888P"            "88b      888  888 
  d88P   888      .d888888      888          .d888888      Y88  88P 
 d8888888888      888  888      888          888  888       Y8bd8P  
d88P     888      "Y888888      888          "Y888888        Y88P   
                                                                    
                                                                    
                                                                                                                                              
                                        
                                                                                                                                            
                                                                          
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()

def logo2():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    Y = """
   

        d8888                                                        
      d88888                                                        
     d88P888                                                        
    d88P 888       8888b.       888d888       8888b.       888  888 
   d88P  888          "88b      888P"            "88b      888  888 
  d88P   888      .d888888      888          .d888888      Y88  88P 
 d8888888888      888  888      888          888  888       Y8bd8P  
d88P     888      "Y888888      888          "Y888888        Y88P   
                                                                    
                                                                    
                                                                    
                                                     
                                                     
                                                     

"""
    for N, line in enumerate(Y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
os.system('clear')
logo()
print('%s\n   ╟─ %sCOOKIES LOADER TOOL ➟ BY AARAV SHRIVASTAVA %s ─╢ %s'%(B,P,B,P))
print('%s  »»───────────────── %s• %s★ %s• %s────────────────««%s\n'%(A,B,A,B,A,A))
print('\x1b[1;37m\x1b[1;41m SCRIPT CREATED BY \x1b[1;0m\x1b[1;37m')
print ('%s└─★ %sAAROHI X3 AARAV ( AARAV  SHRIVASTAVA)%s ★─┘ %s\n'%(B,P,B,P))
print ('»»———————————————————————————　★　——————————————————————————««')

def openlink(browser, msg4):
    try:
        r = browser.open(msg4)
    except urllib.error.URLError as e:
        print("Error: No internet connectivity. Please check your network connection.")
        return None
    return r

def pawanXD(browser, comment):
    try:
        browser.select_form(nr=0)
        browser.form['comment_text'] = comment
        r = browser.submit()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(B + "Comment Done ✔ => \n" + BOLD + f"[{current_time}]\n{comment}")
        print(BOLD + "\u001b[37m" + "[>==============>  RUNNING SOJ9 9B J9K3  <==============<]")
    except Exception as e:
        print(f"Error occurred while commenting: {str(e)}")
        # You might want to handle the error here, such as logging it or retrying the operation 

def main():
     # Print the logo at the beginning

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)

    # Add the headers to your mechanize browser instance
    for key, value in g_headers.items():
        browser.addheaders.append((key, value))

    browser.set_handle_refresh(False)

    cookie_file = input("[+]3NT3R JSON C00KI3S FIL3 P9TH : ")
    load_cookies_from_file(cookie_file, cookies)  
    print ('[>===========>  C00KI3S L09D3D ✔  <===========<]\n')

    profile_ids = extract_profile_ids(cookies)
    print("|=> Profile ID <=|")
    for profile_id in profile_ids:
        print(f"[{profile_id}]\n")
    print ('[>===========>  YOUR PROFIL3 ID ✔ <===========<]')

    msg4 = input("[+]3NT3R P0ST LINK : ")
    print ('[>===========>  P0ST L09D3D ✔  <===========<]\n')
    msg5 = input("[+]3NT3R NOT3P9D P9TH : ")
    f = open(msg5, 'r')
    lines = f.readlines()
    f.close()
    print ('[>===========>  N0D3P9D L09D3D ✔  <===========<]\n')
    msg6 = int(input("[+]3NT3R T1M3 : "))
    print ('[>===========>  TIM3 L09D3D ✔ <===========<]\n')
    os.system('clear')
    print('%s _______ _     _ _     _ _     _ %s_____'%(P,B))
    print('%s |______ |     | |____/  |_____| %s  |  '%(P,B))
    print('%s ______| |_____| |    \_ |     | %s__|__'%(P,B))
    print('\n')

    print('[>==============>C0MM3NT ST9RT3D<==============<]')
    while True:  # Infinite loop
        try:
            for line in lines:
                if len(line) > 3:
                    r = openlink(browser, msg4)
                    if r is not None:
                        pawanXD(browser, line)
                        sleep(msg6)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue  # Continue with the next iteration of the loop even if an error occurs

        sleep(1)  # Add a delay before looping to prevent excessive requests

if __name__ == "__main__":
    main()
