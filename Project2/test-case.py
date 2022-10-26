import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
s = requests.session()
page_res = s.get('http://18.191.246.46:8501/', headers = headers)
if page_res.status_code == 200:
    print("WEbsite is working fine",flush= True)
else:
    print('Website is not working',flush= True)
