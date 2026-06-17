def countZerosBinary(num):
    count = 0
    while num:
        if not num&1:
            count += 1
        num >>= 1
    return count
