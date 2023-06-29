print("Введите число А")
a=int(input())
print("Введите число B, больше либо равном А")
b=int(input())
kolvo=0
for i in range(a,b+1):
    if i%2==0:
        kolvo+=1

print("Количество четных чисел на данном отрезке:",kolvo)


