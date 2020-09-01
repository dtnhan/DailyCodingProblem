def check(list, k):
    for i in range(len(list)):
        if k - list[i] in list:
            print("True")
            return True
    print("False")
    return False
    
list1 = [1, 2, 5, 7, 9]
keys = 5

check(list1, keys)
