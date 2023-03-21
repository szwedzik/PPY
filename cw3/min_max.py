numbers = input("Podaj liczby oddzielone przecinkami: ")
number_list = numbers.split(",")

max_num = int(number_list[0])
min_num = int(number_list[0])

for num in number_list:
    if int(num) > max_num:
        max_num = int(num)
    if int(num) < min_num:
        min_num = int(num)

print("Największa liczba to:", max_num)
print("Najmniejsza liczba to:", min_num)
