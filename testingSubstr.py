ini_str = "ababababab"
sub_str = 'ab'

hd = 0
cnt =0

while hd<len(ini_str):
    print(hd)
    pos = ini_str.find(sub_str,hd)
    
    print(pos)

    if pos !=-1:
        hd = pos+1 
        cnt = cnt+1
    else:
        break

print("substr count "+str(cnt))        
    