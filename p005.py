ans = 1
flag = False

while not flag:
    ans += 1
    flag = True

    for x in range(1, 21)[::-1]:
        if not ans % x == 0:
            flag = False
            break

    # print(f'{ans} is not solution')

print(ans)
