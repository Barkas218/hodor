import requests
import sys

# level 3
# proxies are not required

def get_proxies():
    ip_list = []
    with open('index.html') as fhand:
        for line in fhand:
            line = line.strip()            
            ip_list.append(line)
    return ip_list        


def send_votes():
    url = 'http://158.69.76.135/level4.php'
    captcha_url = 'http://158.69.76.135/captcha.php'
    string_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    referer_string = 'http://158.69.76.135/level3.php'
    id = 2500
    times = 1024

    for i in range(times):

        with requests.Session() as s:
            r = s.get(url, headers={'User-Agent': string_agent})
            i = s.get(captcha_url, headers={'User-Agent': string_agent})
            image_file = open('captcha.png', 'wb')
            image_file.write(i.content)
            image_file.close()
            c = r.cookies
            key_form = ""
            for cookie in c:
                if cookie.name == 'HoldTheDoor':
                    key_form = cookie.value
                    break

            l = s.post(url, data={'id': id, 'holdthedoor': 'Enviar', 'key': key_form}, headers={'User-Agent': string_agent, 'referer': referer_string}, cookies = c)

send_votes()
