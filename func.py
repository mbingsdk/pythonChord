#chord guitar modules
import requests, re, enquiries


def cleanhtml(raw_html):
    cleantext = re.sub(re.compile('<.*?>'), '', raw_html)
    return cleantext
    
def listReplace(text, args1, args2):
    if isinstance(args1, str):
        if isinstance(args2, str):
            text = text.replace(args1, args2)
        else:
            pass
    elif isinstance(args1, list):
        if isinstance(args2, str):
            for i in args1:
                text = text.replace(i, args2)
        elif isinstance(args2, list):
            a = len(args1)
            b = len(args2)
            if a == b:
                for i in range(a):
                    text = text.replace(args1[i], args2[i])
        else:
            pass
    else:
        pass
    return text

def getChord(mode, args):
    url = "http://sergcat.xssemble.com/service-v2.php"
    header = {
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0; ASUS-X008DA Build/MRA58K",
        "Host":"sergcat.xssemble.com",
        "Connection":"Keep-Alive",
        "Accept-Encoding":"gzip",
        "Content-Lenght":"0"
    }
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
    args = listReplace(args, ["<sup>", "</sup>"], ["((sup))", "((!sup))"])
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

def menu(args):
    lagu = {}
    out = getChord("getList", args)
    for i in range(len(out)):
        lagu[out[i][2]] = str(out[i][0])
    choice = enquiries.choose("\nLagu "+out[0][1], list(lagu))
    print(choice, "\n")
    return [lagu, choice]

def showChord(args1, args2):
    ret = getChord("getChord", args1[args2])
    penyanyi = ret[0][0]
    judul = ret[0][1]
    chordLagu = ret[0][2]
    result = rebuild(chordLagu)
    print(result)
