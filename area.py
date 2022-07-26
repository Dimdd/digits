first = int(input())
second = int(input())
third = int(input())
for a in range(2, first + 1):
    for b in range(2, second + 1):
        for c in range(2, third + 1):
            if a % 2 == 0 and c % 2 == 0:
                if b == 3 or b == 5 or b == 7 or b == 2:
                    print(f"{a} {b} {c}", end=" ")
                    print()
