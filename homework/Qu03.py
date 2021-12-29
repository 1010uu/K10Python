star="*"
blank=" "
for i in range(5):
    for j in range(5):
        if i>=j:
            print(star, end='')
        else:
            print(blank, end='')
    print()