def checkPalindromeNumber(num):
    rev = 0
    tmp = num
    while tmp:
        last = tmp % 10
        rev = rev*10 + last
        tmp = int(tmp/10)
    print(num, rev)
    if num == rev:
        return True
    return False

checkPalindromeNumber(1012332101)