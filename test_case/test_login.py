import requests
import xlrd
from config.conf import *
from  config.get_user_message import *

def test_login():
 url=ip_addres()+"/api/v1/user/login"
 print(url)
 username,passwrod=get_xlsx(1)
 print(username,passwrod)
 json={
    "authRequest": {
        "userName": username,
        "password": passwrod
    }
 }

 r=requests.post(url=url,json=json)
 print(r.json())