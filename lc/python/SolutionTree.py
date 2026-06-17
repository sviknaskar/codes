def SolutionSpace(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []
    def backtrack(path, idx):
        if idx == len(digits):
            result.append(path)
            return

        for i in phone[digits[idx]]:
            backtrack(path+i, idx+1)


    if digits:
        backtrack("", 0)
    print(result)




def SolutionTreeTest():
    SolutionSpace("234")


SolutionTreeTest()