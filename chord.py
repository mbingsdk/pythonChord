from func import *
import enquiries

lagu = {}
test = input("\nPenyanyi: ")
out = getChord("getList", test)

for i in range(len(out)):
    lagu[out[i][2]] = str(out[i][0])

choice = enquiries.choose("\nLagu "+out[0][1], list(lagu))
print(choice, "\n")

ret = getChord("getChord", lagu[choice])
penyanyi = ret[0][0]
judul = ret[0][1]
chordLagu = ret[0][2]

result = rebuild(chordLagu)
print(result)
#print(chordLagu)
