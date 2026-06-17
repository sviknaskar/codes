def revInteger(num):
    res = 0
    while num !=0 :
        res += num % 10
        if num%10 != num:
            res *= 10
        num /= 10
        num = int(num)
    return res


def ReverseIntTest():
    print(f"Test name: {__name__}")
    num = 65487889159
    res = revInteger(num)
    print(f"{res}")

