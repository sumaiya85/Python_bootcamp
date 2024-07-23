#password verifier Mr.x is trying to create a new password for his instagram account
#this are the required conditions for creating a new password
#condition 1:Minimum length is 8 max length is 15
#condition 2: only @,/ is allowed in a password
#condition 3: no spaces are allowed
#condition 4:only alpha numerics are allowed
#u r supposed to print weak if length is exact 8,medium length is between 8 to 12
#strong if length is between 12 to 15

str=input()
a="@"
b="/"
if( a or b in str):
    if " " not in str:
        if(len(str) == 8):
            print("weak password")
        elif(len(str)>8 and len(str)<=12):
            print("medium password")
        elif(len(str)>12 and len(str)<=15):
            print("strong password")
    else:
        print("please follow the conditions")
else:
    print("please follow the conditions")