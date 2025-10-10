n = int(input("Введите сторону квадрата: "))

print("\n1) два треугольника:")
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()
for i in range(1, n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

print("\n2) Бабочка:")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n - 1):
    for j in range(n - i - 1):
        print("*", end=" ")
    for j in range(2 * (i + 1)):
        print(" ", end=" ")
    for j in range(n - i - 1):
        print("*", end=" ")
    print()

print("\n3) Ромб:")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(2 * (n - i - 1) - 1):
        print("*", end=" ")
    print()