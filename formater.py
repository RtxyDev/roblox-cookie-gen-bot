cookies = open('generated_cookies.txt', 'r').read().splitlines()

for x in cookies:
    cookie = '_|' + x.split(':_|')[1] 
    print(cookie)
    open('formated.txt', 'a').write(cookie+'\n')
input()
