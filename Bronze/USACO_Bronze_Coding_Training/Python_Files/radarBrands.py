motherBrand = int(input())
def reverseNum(num):
    array = str(num)
    array = list(array)
    newArray = []
    for i in range(len(array)-1,-1,-1):
        newArray.append(array[i])
    newArray = "".join(newArray)
    return int(newArray)
def checkPalindrome(num):
    if num == reverseNum(num):
        return True
    else:
        return False
add = reverseNum(motherBrand)
iterations = 0
sum = reverseNum(motherBrand) + motherBrand
while checkPalindrome(sum) == False:
    sum = motherBrand + reverseNum(motherBrand)
    motherBrand = sum
    iterations += 1
if iterations == 0:
    print (1,end=" ")
    print (sum)
else:
    print (iterations,end=" ")
    print (sum)
