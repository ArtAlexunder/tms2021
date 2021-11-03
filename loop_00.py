# Loop while

n = int(input("Enter number of iterations: "))
i = 1
while i <= n:
    if i > 8:
        break
    elif i == 4:
        i += 1
        continue
    print(i, end=') ')
    print('Silence is golden')
    i += 1


print('End of loop')
