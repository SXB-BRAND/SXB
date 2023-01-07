import os,time,platform
os.system('clear')
print('[•] Checking New Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')


bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{green}[•] Join Over Facebook Group {white}')
    os.system('xdg-open https://facebook.com/groups/1582618178844097//')
    import pro
    time.sleep(2.05)
