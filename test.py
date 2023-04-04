import requests,time,random
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
         "Cookie": "your cookie"} 
while 1:
    res = requests.get('https://pointsprizes.com/r/3551888/17/blog',headers=header)
    res2 = requests.get('https://pointsprizes.com/r/3551888',headers=header)
    print(res.text) 
    print(type(res))
    print(res2.text) 
    print(type(res2))
    r=random.randint(1,25)
    time.sleep(r)
