    # some method -> compreheprint(a)
    #        # different methodnsions
a = [] # it is a list
for z in range(0 , 10):                    #|
     a.append(z)                           #|-> a = [z for z in rang(0,10)]
     print(a)                              #|   print(a)
         # differents look likes that               |
    # some method                                   |--|
a = [] # it is a list                      #|          | other way
for z in range(0 , 10):                    #|-> a = [z for z in rang(0,10)]
     a.append(z)                           #|   for z in a:
                                           #|       print(z,end=",")
print(a)

a = [z for z in range(0,10)]
for z in a:
    print(z, end=",")
     # others->user_defined function
def add(d, f):
  return d +f        # other method #  sum = d + f
                                    #   return sum
print(add(4,4))
     # lambda function
k =lambda a , d : a + d
print(k(6,8))
           # other method -> dif in lamdba
def myfun(n):
    return lambda a : a + n
mynum = myfun(8)
print(mynum(4))
      # file handling
           # open key
# ->f = open("loge.txt","x")
# ->f.close()
      # other method for FH->use the  write key
#->with open("loge.txt","w") as f:
#->    f.write("hi loge\nhow are u ")
      # use the append key
#->with open("loge.txt","a") as f:
#->    f.write("hay\n")
      # use to read key
#->  with open("loge.txt","r") as f:
#->      for l in f.readlines(): print(l , end="")



