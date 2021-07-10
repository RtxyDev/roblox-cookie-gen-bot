import requests, threading, random, subprocess, string, time

proxies = []


def rotate_proxies():
    global proxies
    while True:
        proxi_ = ''
        for chunk in requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').iter_content(chunk_size=5000):
            if chunk:
                proxi_ += chunk.decode()
        proxies +=  proxi_.splitlines()
        time.sleep(1000)

def generate_username():
    while True:
        user = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + '_', k=random.randint(4, 7)))
        username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={user}')
        if username.json()['message'] == "Username is valid":
            return user

def generate_cookie():
    try:
        with requests.session() as session:
            proxy = {
                'http':random.choice(proxies),
                'https':random.choice(proxies)
            }
            agents = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36', 'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4']
            session.headers['user-agent'] = random.choice(agents)
            session.headers['x-csrf-token'] = session.post(f"https://auth.roblox.com/v2/signup", proxies=proxy).headers['x-csrf-token']
            gender = random.randint(1,3)
            username = generate_username()
            password = f''.join(random.choices(string.ascii_letters, k=10))
            forum = {'birthday':'21 Oct 2006', 'captchaProvider':'', 'captchaToken':'', 'isTosAgreementBoxChecked':True, 'gender':gender, 'displayAvatarV2':False, 'displayContextV2':False, 'password':password, 'username':username}
            create = session.post('https://auth.roblox.com/v2/signup', data=forum, proxies=proxy)
            if create.status_code == 200:
                cookie = session.cookies['.ROBLOSECURITY']
                with open('generated_cookies.txt', 'a') as gen:
                    gen.write(f'{username}:{password}:{cookie}\n')
                print(f'- Generated Cookie | {create.status_code} | {username} | {proxy}')
    except:
        pass

threading.Thread(target=rotate_proxies,).start()
time.sleep(3)
while True:
    threading.Thread(target=generate_cookie,).start()