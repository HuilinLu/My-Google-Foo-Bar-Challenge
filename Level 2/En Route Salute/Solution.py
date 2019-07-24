  
### Level 2
"""  Level 2: En_route_salute """
s = input('Put the road here: ')
string = list(s)
sum = 0
for strings in string:
    if str(strings)  == '>' :
        atpos = s.find(strings)
        remain=list(s[atpos+1:])
        count = 0
        for remains in remain:
            if str(remains) == '<' :
                count = count + 1
        sum = sum + count
print(2*sum)

