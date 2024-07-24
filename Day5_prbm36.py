#36
#input:ABC
#output:EFG

inp=input()
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(chr(ord(i)+4),end="")
    
#hw:cyclic
'''xyz
X=120+3=123 ----->a=97
chr(123)=|
y=121+3=124 ------->b=98
chr(124)=}
z=122+3=125 -------->c=99
chr(125)=~'''