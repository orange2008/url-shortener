
import requests
import datetime
def apikey():
    addr = "https://cdn.jsdelivr.net/gh/orange2008/postitem@master/APIKey/suo.im"
    get = requests.get(addr)
    ret = get.text
    return ret

def save(raw, surl):
    n = datetime.datetime.now()
    y = n.year
    m = n.month
    d = n.day
    h = n.hour
    mi = n.minute
    s = n.second
    da = "-"
    string = str(y)+da+str(m)+da+str(d)+da+str(h)+da+str(mi)+da+str(s)+" "+str(raw)+" -> "+str(surl)
    string = str(string)
    with open("history.txt", 'a') as f:
        f.write(string)
        f.write("\n")

print("Welcome to url shortener!")
print("We used suo.im's api!")

while True:
    raw = input("URL: ")
    print("Running quietly..")
    sapikey = apikey()
        # if "http" in url:
        #     pass
        # else:
        #     print("The URL must include http:// or https://")
        #     return False
    address = "http://suo.im/api.htm?url=" + raw + "&key=" + sapikey + "&format=json&expireDate=2099-12-31"
    req = requests.get(address)
    res = req.json()
    err = res['err']
    surl = res['url']
    if err == '':
        pass
    else:
        print("Something went wrong...")
        print(err)
        continue
    if surl == raw:
        print("Shorten failed.")
        print("Check your URL exist or this URL didn't supported.")
        continue
    else:
        pass
    
    save(raw, surl)

    print("Shorten successful!")
    print("\n\n\n")
    print(surl)
    print("\n\n\n")
    opt = input("Do you want to short another link?(yes/no): ")
    if opt == "yes":
        continue
    else:
        print("Thanks for using!")
        break

print("Quitting..")
