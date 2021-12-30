total = 0
def sum(arg1, arg2):
    total = arg1+arg2
    print("지역변수 total=", total)
    return total

print("전역변수 total=", total)
print("sum(10,20)호출 후 반환 값=", sum(10,20))

print("========================================")

def  commander(saying):
    def inner(quote):
        return "조선의 위대한 장군 = '%s'" % quote
    return inner(saying)
print(commander("이순신"))
print("========================================")

def printme(str1, str2):
    print(str1, str2)
    return
