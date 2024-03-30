def akkerman (m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return akkerman(m - 1, 1)
    else:
        return akkerman(m - 1, akkerman(m, n - 1))


m = int(input('Число m: '))
n = int(input('Число n: '))
print(akkerman(m, n))