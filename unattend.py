import json
import requests
import datetime
import time

print("This is unattend program.")
sn = input("Script name(without file extension): ")

addr = "https://raw.githubusercontent.com/orange2008/postitem/master/APIKey/suo.im"
get = requests.get(addr)
sapikey = get.text
fn = sn + ".json"
with open(fn) as ff:
    d = json.load(ff)

def tim():
    n = datetime.datetime.now()
    y = n.year
    m = n.month
    d = n.day
    h = n.hour
    mi = n.minute
    s = n.second
    da = "-"
    string = str(y)+da+str(m)+da+str(d)+da+str(h)+da+str(mi)+da+str(s)
    string = str(string)
    return string

while True:
    print("Processing...")
    print("You can drink a cup of coffee or eat some lunch.")
    print("All logs and result will output to a name called " + sn + "-result.txt")
    re = sn + "-result.txt"
    time.sleep(3)
    print("Running...")
    for urls in d:
        print("Processing URL: " + str(urls))
        address = "http://suo.im/api.htm?url=" + urls + "&key=" + sapikey + "&format=json&expireDate=2099-12-31"
        print("API Request: " + address)
        req = requests.get(address)
        res = req.json()
        err = res['err']
        surl = res['url']
        if err == '':
            err = "N"
        else:
            err = "Y"
        
        tm = tim()
        with open(re, 'a') as fi:
            print("Saving..")
            fi.write(tm)
            fi.write(" ")
            fi.write(urls)
            fi.write(" -> ")
            fi.write(surl)
            fi.write("     Error: ")
            fi.write(err)
            fi.write("\n")
    print("All done!")
    break

quit = input("Press any key to continue.")