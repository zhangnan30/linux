"""
i = 0
while i<100:
    if i // 10 % 2 == 0:
        print("A",end="")
    else:
        print("B",end="")
    if i % 10 == 9:
        print()
    i+=1
print()


i = 0
while i < 10:
    a=0
    while a < 10:
        if i % 2  == 0:
           print("A",end="")
        else:
            print("B",end="")
        a+=1
    print()
    i+=1
"""
###反向口诀
""""
a = 1
while a <= 9:
    c = 9-a
    while c > 0:
        print("        ",end="")
        c-=1
    b = 1
    while b <= a:
        print("%d*%d=%2d " %(a,b,a*b),end=" ")
        b+=1
    print()
    a+=1

"""
'''
fp = open("12-26.txt",mode="w",encoding="utf-8")
fp.write("你好")
fp.close()

fp = open("12-26.txt",mode="r",encoding="utf-8")
res = fp.read()
fp.close
print(res)

a = { 1 ,"r","哈哈",0.4,0 }
print(a,type(a))
'''
lstvar = [1,2,3,]
lstvar.append(9)
print(lstvar)
lstvar.insert(0,66)
print(lstvar)
lstvar.extend("小米")
print(lstvar)
lstvar.pop(0)
print(lstvar)
lstvar.remove("小")
print(lstvar)
lstvar.clear()
print(lstvar)
lstvar = [1,2,3,]
lstvar[1]=(8)
print(lstvar)
c=lstvar.count(1)
print(lstvar)
lstvar.sort(reverse=True)
print(lstvar)
lstvar.reverse()
print(lstvar)
print("______________________________________________")

import copy
a = 3
b = a
a = 5
print(b)
a = [1,5,[9]]
b = copy.deepcopy(a) 
a[2].append(0)
print(b)

print("______________________________________________")

a = {"lisi","张三","王二麻子"}
b = {"张三"}
res = a & b
print(res)
res = a-b 
print(res)
res = a|b
print(res)
res = a^b 
print(res)
res = a<b 
print(res)
print("_______________")
"""
图片复制
fp = open("1.png",mode="rb")
res=fp.read()
fp.close

fp = open("5.png",mode="wb")
fp.write(res)
fp.close

"""

fp = open("11.txt",mode="w+",encoding="utf-8")
res=fp.write("我就是我，不一样的烟火。\n本来无一物，何处惹尘埃\n美丽的姑娘是我的向往")
print(res)

fp.close



fp = open("11.txt",mode="w+",encoding="utf-8")
fp.seek(0,2)
fp.write("hahah")
fp.seek(0)
a = fp.read()

print(a)
fp.close

a = {"name":"张三","age":"18","addr":"北京"}
for i,j in a.items():
    print(i)
print("___________________________________")

def func():
   print("111111111111")
   print("22222222")
   return 1
   print("333333333333")
   print("44444444444444")
   return 9
   
   
res=func()
print(res)




















































































































	
    



