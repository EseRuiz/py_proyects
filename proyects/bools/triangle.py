def equilateral(sides):
    if 0 in sides:
        return False
    if len(set(sides)) == 1:
        return True
    return False

def isosceles(sides):
    if 0 in sides:
        return False
    a,b,c= sorted(sides)
    if len(set(sides))==2 and a+1==b or a-1==b or len(set(sides)) == 1 or len(set(sides))==2 and a<b or a>b :
        return True
    return False


def scalene(sides):
    if 0 in sides or len(set(sides))==2 or len(set(sides)) == 1:
        return False
    a,b,c=sorted(sides)
    if a+b > c and a+c > b and b+c >a:
        return True
    return False

