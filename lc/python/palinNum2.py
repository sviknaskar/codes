def isPalin(num):
    rev = 0
    while num:
        rev = 10 * rev + num%10
        num = num//10

    if rev == num:
        return True
    return False