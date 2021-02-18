def makebricks(goal,small,large):

    xgoal = large*5

    if large*5 >= goal:
        xgoal = (goal//5)*5
    if xgoal + small >= goal:
        return True
    else:
        return False


print(makebricks(10,2,1))
print(makebricks(12,1,10))
print(makebricks(10,10,1))
print(makebricks(20,0,5))


def rotate(lst):
    result = []
    result.append(lst[-1])
    for i in range(len(lst),-1):

        result.append(lst[i])
    return result


def rotates(lst):
    return lst[-1:] + lst[0:-1]


def string_matching(a,b):

    count = 0

    if len(a) < len(b):

        length = len(a)
    else:

        length = len(b)

    for i in range(length-1):

        if a[i:1+2] == b[i+i+2]:

            count+=1
    return count