StrVowel=input("String: ")
v='aeiou'
x=0
string1=""
newstr=""
for i in StrVowel:
    if i==v[x]:
        string1=string1+i
    if x<(len(v)-1):
        if i==v[x+1]:
            string1=string1+i
            x=x+1
for i in StrVowel:
    if i not in newstr:
        newstr=newstr+i
if newstr!=v:
    print(0)
else:
    print(len(string1))
