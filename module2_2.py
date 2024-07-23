first=int(input('a: '))
second = int(input('b: '))
third=int(input('c: '))
if third == first == second and second == third:
    print(3)
elif second != first and first == third or first == second or second == third:
    print(2)
elif first != second and first != third:
    print(0)
