import sys
listanditemnumber = []
shopinglists = []
frequentItems = []
firstList = []
lists = []
inorder = []
counter = 0
# for items in sys.stdin:
#     if 'q' == items.rstrip():
#         break
#     lists.append(items)
#     print(f"this is {lists}")
# print('EXIT')


class Error(Exception):
    pass


class UpperError(Exception):
    pass


while True:
    try:
        listanditemnumber = [int(i) for i in sys.stdin.readline().split()]
        if len(listanditemnumber) > 2:
            raise Error
        if listanditemnumber[0] not in range(1, 100):
            raise Error
        if listanditemnumber[1] not in range(1, 5000):
            raise Error
    except ValueError:
        print("Numbers only ! \n")
    except Error:
        print("Invalid input! \n")
    else:
        break
while True:
    try:
        for i in range(listanditemnumber[0]):
            lists = [str(elem).lower()
                     for elem in sys.stdin.readline().split()]
            if not len(lists) == listanditemnumber[1]:
                raise Error
            else:
                shopinglists.append(lists)
            for j in range(listanditemnumber[1]):
                if not len(shopinglists[i][j]) < 11 or not shopinglists[i][j].isalpha():
                    shopinglists = []
                    raise UpperError
    except Error:
        print("Invalid input! \n")
    except UpperError:
        print("Items must be less then 11 characters and must be lowercase")
    except IndexError:
        print("Item missing")
    else:
        break

firstList = shopinglists[0]
for item in firstList:
    for row in range(listanditemnumber[0]):
        for col in range(listanditemnumber[1]):
            if item == shopinglists[row][col]:
                counter += 1
                if counter == listanditemnumber[0]:
                    frequentItems.append(item)
    counter = 0

print(int(len(frequentItems)))

frequentItems.sort()
for items in frequentItems:
    print(items)
