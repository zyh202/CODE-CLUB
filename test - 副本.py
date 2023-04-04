import requests,time
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36", 
         "Cookie": "your cookie"} 
while 1:
    res = requests.get('http://www.fzcangshan.gov.cn/xjwz/xxgk/gzdt/csxw/202211/t20221119_4467576.htm',headers=header)
    print(res) 
    print(type(res))
    time.sleep(2)
