# 4 eded daxil edilir bu ededlerden necesinin tek necesinin cut olduqnu cap eden
a=int(input("1 eded daxil edilir "))
b=int(input("2 eded daxil edilir "))
c=int(input("3 eded daxil edilir "))
d=int(input("4 eded daxil edilir "))
tek=0
sifir=0
cut=0
if(a==0):
    sifir=sifir+1
elif(a%2==0):
    cut=cut+1
else:
    tek=tek+1
if(b==0):
    sifir=sifir+1
elif(b%2==0):
    cut=cut+1
else:
    tek=tek+1
if(c==0):
    sifir=sifir+1
elif(c%2==0):
   cut=cut+1
else:
   tek=tek+1
if(d==0):
    sifir=sifir+1
elif(d%2==0):
    cut=cut+1
else:
    tek=tek+1 
print("tek ededler",tek)
print("cut ededler",cut)
print("sifirlar",sifir)




