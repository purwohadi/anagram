def anagram(s1,s2):
    c1 = [0] * 27
    c2 = [0] * 27
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] +1 
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] +1 

    j = 0
    valid = True
    while j < 26 and valid :
        if c1[j] == c2[j]:
            j = j + 1
        else:
            valid = False
            
    return valid
    
print(anagram("purwo","owrup"))


==============================
result :
True