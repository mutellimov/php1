#list1 = []
#for i in range (10):
  #  a=int(input(f"{i+1} eded daxil edilir "))
   # list1.append(a)
#print(list1)




list1 = []
a = int(input("say "))
for i in range(1, a + 1):
    ədəd = int(input(f"{i}. ədədi daxil edin: "))
    list1.append(ədəd)
print("Cut :")
for ədəd in list1:
    if ədəd % 2 == 0:
        print(ədəd)
