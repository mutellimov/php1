list1 = []
for i in range(10):
    say = int(input(f"{i+1}eded daxil edilir:"))
    list1.append(say)
cut_ededlerin_sayi  = 0
for i in list1:
    if i % 2 == 0:
        cut_ededlerin_sayi += 1
print(cut_ededlerin_sayi)


