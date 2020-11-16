import numpy as np
import random
#1 farakhni ktabkhane random
# 2 skht arye 101 tayy bekhter ziba namysh dadn 101 shod
a=np.arange(101)
a=[' ' for x in range(101)]
# 3 sakht halgh for 11tayy  barya in ke goft shode 11 ta az harkodom
for i in range(11):
    # 4 sakht add random 1 ta 100 
            r2=random.randint(1,100)
# 5 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
                r2=random.randint(1,100)
# 6 agr bod s ro bezar
            a[r2]="s"
# 7 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
# 8 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 9 agr bod c ro bezar
            a[r2]="c"
# 10 ta vagh barabar nabod ' ' dar jayy halgh  
            while a[r2]!=' ':
# 11 sakht add random 1 ta 100 
                r2=random.randint(1,100)
# 12 agr bod R ro bezar
            a[r2]="R"
            # print(a)
#13 sakht skht string bary rekhtan arrye vorodi braye namayesh
ss=""
#14 sakht halgh bar mortb rikhtn arrey be string
for s in range(1,101):
#15 bary in ke 10 dar 10 besh age halge be s%10==0 rsid ber khat bad ba ezaf kardn \n
            if s%10==0:
                ss+="\t"+a[s]
                ss+="\n"
#16 dar gher in sorat ba \t ezafe kone 
            else: 
                ss+="\t"+a[s]
#17 dar akharm nmaysh
print(ss)
#18sakht method save file
# try:
#     with open("test.bat","w") as f:
#                 f.write(ss)
# except TypError:
#     print("There was a type error!")



# a=np.array([1,2,3])
# print (a)











