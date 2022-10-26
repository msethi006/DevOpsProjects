import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
s = requests.session()
try:
    page_res = s.get('http://18.222.67.133:8501/', headers = headers)
    if page_res.status_code == 200:
        print("WEbsite is working fine",flush= True)
except Exception as e:
    print(e)
    print('Website is not working',flush= True)
