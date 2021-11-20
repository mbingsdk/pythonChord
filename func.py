# chord guitar module
# by Vx6-CT
import requests, re, enquiries

class chord:
    def __init__(self):
        self.url = "http://sergcat.xssemble.com/service-v2.php"
        self.headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0; ASUS-X008DA Build/MRA58K",
            "Host":"sergcat.xssemble.com",
            "Connection":"Keep-Alive",
            "Accept-Encoding":"gzip",
            "Content-Lenght":"0"
        }
        self.data = {
            "cc":"0",
            "ci":"5",
            "lc":"in",
            "vc":"9093"
        }
        self.lagu = {}
        self.penyanyi = ""
        self.judul = ""
        self.choice = ""
        self.result = ""

    def getChord(self, mode, args):
        self.data["a"] = args
        if mode == "getList":
            self.data["name"] = "a"
        elif mode == "getChord":
            self.data["name"] = "i"
        else:
            exit()
        self.result = requests.get(url=self.url, headers=self.headers, params=self.data).json()
        if self.result == []:
            print("\n" + args + " Tidak ditemukan!")
            exit()
        else:
            return self.result

    def listReplace(self, args1, args2):
        if isinstance(args1, str):
            if isinstance(args2, str):
                self.result = self.result.replace(args1, args2)
            else:
                pass
        elif isinstance(args1, list):
            if isinstance(args2, str):
                for i in args1:
                    self.result = self.result.replace(i, args2)
            elif isinstance(args2, list):
                a = len(args1)
                b = len(args2)
                if a == b:
                    for i in range(a):
                        self.result = self.result.replace(args1[i], args2[i])
            else:
                pass
        else:
            pass
        return self.result

    def cleanhtml(self):
        self.result = re.sub(re.compile('<.*?>'), '', self.result)
        return self.result

    def rebuild(self):
        x = ""
        self.result = self.listReplace(["<sup>", "</sup>"], ["((sup))", "((!sup))"])
        self.result = self.cleanhtml()
        a = self.result.split("\n")
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
        self.result = x
        return self.result

    def menu(self, args):
        self.result = self.getChord("getList", args)
        #print(self.result)
        for i in range(len(self.result)):
            self.lagu[self.result[i][2]] = str(self.result[i][0])
        self.choice = enquiries.choose("\nLagu "+self.result[0][1], list(self.lagu))
        print(self.choice, "\n")
        return self.choice, self.lagu

    def showChord(self):
        self.result = self.getChord("getChord", self.lagu[self.choice])
        self.penyanyi = self.result[0][0]
        self.judul = self.result[0][1]
        self.result = self.result[0][2]
        self.result = self.rebuild()
        return self.result, self.penyanyi, self.judul
