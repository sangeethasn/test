import random

upper_case =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
random.shuffle(upper_case)
uc=list(upper_case[0])


lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y','z']
random.shuffle(lower_case)
lc = list(lower_case[0])


num= ['0','1','2','3','4','5','6','7','8','9']
random.shuffle(num)
n = list(num[0])

special_chara= ['!','@','#','$','%','^','*']
random.shuffle(special_chara)
sc= list(special_chara[0])


password=[]
user_input=raw_input("Type 'Y' to generate new password")

if user_input=='Y' :
    print ''.join(lc+sc+n+uc+n+lc+sc)
