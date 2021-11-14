#chord guitar

import requests, urllib, re

link = "http://sergcat.xssemble.com/service-v2.php"
head = {
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0; ASUS-X008DA Build/MRA58K",
    "Host":"sergcat.xssemble.com",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "Content-Lenght":"0"
}
lagu = {}
CLEANR = re.compile('<.*?>')

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def getChord(mode, url, args, header):
    data = {
        "a":args,
        "cc":"0",
        "ci":"5",
        "lc":"in",
        "vc":"9093"
    }
    
    if mode == "getList":
        data["name"] = "a"
    elif mode == "getChord":
        data["name"] = "i"
    else:
        exit()
        
    r = requests.get(url=url, headers=header, params=data)
    return r.json()

def rebuild(args):
    x = ""
    args = args.replace("<sup>", "((sup))")
    args = args.replace("</sup>", "((!sup))")
    args = cleanhtml(args)
    a = args.split("\n")
    for i in a:
        y = ""
        z = ""
        if "((sup))" in i:
            k = i.split("((sup))")
            for j in range(len(k)):
                y += " "*len(k[j]) if j==0 else k[j].split("((!sup))")[0]+(" "*len(k[j].split("((!sup))")[1]))
                z += k[j] if j == 0 else k[j].split("((!sup))")[1]
            y += "\n"
            z += "\n"
            x += y+z
        else:
            x += i+"\n"
    return x