#2 eded daxil edilir bu ededlerden 1 cisi axdarilan eded 2 cisi  saydir qeyd edilen say qeder eded daxil edib axtarilan ededden bu ededler icerisinde nece dene olduqnu cap eden kodu yazin 
a=int(input("axdaracaqim eded: "))
b=int(input("say"))
count=0
for i in range (b):
    num=int(input(f"{i+1}-ci ededi daxil edin:"))
    if num == a:
        count += 1
print(f"axtarilan ededden {count} dene tapildi.")


 