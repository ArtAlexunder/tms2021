# Cjnditions

for i, j in enumerate(range(1, 10)):

    if i == 5:
        continue
    elif j > 6:
        j -= 1
        pass
        # break
    print(i, ":", j)

else:
    print('Else after for')

print('End of program!')
