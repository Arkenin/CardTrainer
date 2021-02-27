#%% Tests function for dobble
from dobble import dobble

print("start")

a = dobble (8)
set(a[0])&set(a[1])

for i in a:
    if len(set(i)) != 8 and True:
            print (len(set(i)))
          
for i in a:
    for j in a:
        if i is j:
            continue
        if len (set(i)&set(j)) >1:
            print(set(i)&set(j))