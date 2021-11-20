#chord main
from func import *

def run():
    a = chord()
    while True:
        print("\nKetik !exit untuk keluar")
        test = input("\nPenyanyi: ")
        if test == "!exit":
            exit()
        else:
            a.lagu = {}
            a.menu(test)
            a.showChord()
            print(a.result)

run()
