# Find the missing set of letters in the series,  HF, AY,  …,  JH,  ZX,  OM

import string 

letters = string.ascii_lowercase

series = []

for i in range(6):
    
    if i != 0:
        x = letters.index(l2)-(4+i)
    else:
        x = 7+i
    l1 = letters[x]
    l2 = letters[x-2]
    
    pair = [l1,l2]
    series.append(pair)
    print(series)

