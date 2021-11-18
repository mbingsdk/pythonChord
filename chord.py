#chord main
from func import *

while True:
    print("\nKetik !exit untuk keluar")
    test = input("\nPenyanyi: ")
    if test == "!exit":
        exit()
    else:
        a = chord()
        a.menu(test)
        a.showChord()
