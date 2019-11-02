print("Amicable numbers")

for i in range(1, 10):
    print("\nDividers for number=" + str(i) + "\n")
    for j in range (1, 10):
        if (i % j == 0 and i > j):
            print(j, end=', ')