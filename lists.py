# list1=[2,2,6,4,5,6,8,41,60]
# for i in range(len(list1)):
#     flag=False
#     for j in range(len(list1)):
#         if list1[i]==list1[j]:
#             flag=True
#             break
#     if flag:
#         for j in range(i):
#             if list1[i]==list1[j]:
#                 flag=False
#                 break
#     if flag:
#         print(list1[i], end= ' ')


# list1 = [2, 2, 6, 4, 5, 6, 8, 41, 60]
# list2 = [1, 3, 5, 6, 8, 9, 41]

# combined_list = list1 + list2

# ("Первый список:", list1)
# print("Второй список:", list2)
# print("Уникальные элементы из двух списков:")

# for i in range(len(combined_list)):
#      is_unique = True
#     for j in range(len(combined_list)):
#         if i != j and combined_list[i] == combined_list[j]:
#            is_unique = False
#             break
#     if is_unique:
#         already_printed = False
#         for k in range(i):
#             if combined_list[i] == combined_list[k]:
#                 already_printed = True
#                 break
#         if not already_printed:
#             print(combined_list[i], end=' ')

# list1 = [2, 2, 6, 4, 5, 6, 8, 41, 60]
#
# print("Исходный список:", list1)
#
# for i in range(len(list1)):
#     is_duplicate = False
#     for j in range(len(list1)):
#         if i != j and list1[i] == list1[j]:
#             is_duplicate = True
#             break
#
#     if is_duplicate:
#         list1[i] = 0
#
# print("Список после замены:", list1)

# list1 = [2, 2, 6, 4, 5, 6, 8, 41, 60]
# list2 = [1, 3, 5, 6, 8, 9, 41]
# avg1 = sum(list1) / len(list1)
# avg2 = sum(list2) / len(list2)
# if avg1 > avg2:
#     print("Среднее значение ПЕРВОГО списка больше")
# elif avg2 > avg1:
#     print("Среднее значение ВТОРОГО списка больше")
# else:
#     print("Средние значения списков РАВНЫ")

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
for i in range(len(list1)):
    list1[i], list2[i] = list2[i], list1[i]

print("\nПосле обмена:")
print("list1 =", list1)
print("list2 =", list2)
