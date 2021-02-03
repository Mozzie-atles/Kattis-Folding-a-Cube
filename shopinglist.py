shopinglistNumber = 0
itemsNumber = 0
shopinglists = []
frequentItems = []
firstList = []
lists = []
counter = 0


class Error(Exception):
    pass


class RangeError(Exception):
    pass


class UpperError(Exception):
    pass


while True:
    try:
        shopinglistNumber, itemsNumber = map(int, input().split())
        if shopinglistNumber not in range(1, 100):
            raise Error
        if itemsNumber not in range(1, 5000):
            raise Error
    except ValueError:
        print("Numbers only ! \n")
    except Error:
        print("Number of lists can't pass 100 and numver or items can't pass 5000! \n")
    else:
        break
while True:
    try:
        for i in range(shopinglistNumber):

            lists = list(map(str, input().split()))
            shopinglists.append(lists)
            for j in range(itemsNumber):
                if not len(shopinglists[i][j]) < 11:
                    raise UpperError
            if len(shopinglists) > itemsNumber:
                raise RangeError
    except UpperError:
        print("Items must be less then 11 characters and must be lowercase")
    except RangeError:
        print("Can't have more then:{itemsNumber} items")
    else:
        break

firstList = shopinglists[0]
for item in firstList:
    for row in range(shopinglistNumber):
        for col in range(itemsNumber):
            if item == shopinglists[row][col]:
                counter += 1
                if counter == shopinglistNumber:
                    frequentItems.append(item)
    counter = 0
print(len(frequentItems))
for items in frequentItems:
    print(items)
