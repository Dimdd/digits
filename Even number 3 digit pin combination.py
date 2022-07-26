first_digit_max = int(input())
second_digit_max = int(input())
third_digit_max = int(input())
combination_counter = 0
for a in range(2, first_digit_max + 1):
    for b in range(2, second_digit_max + 1):
        for c in range(2, third_digit_max + 1):
            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                combination_counter += 1
                print(f"{a} {b} {c}", end=" ")
                print()

print(f"Number of combination {combination_counter}")