
def getLambda(x1,y1,x2,y2,x3,y3,x4,y4):
    # line1 = point1 + lambda*gradient  0<=lambda<=1
    # line2 = point3 + phi*gradient
    # 
    # line1 = line2
    # phi*gradient2-lambda*gradient1 = point1 - point3

    gradientY1 = y2-y1
    gradientX1 = x2-x1

    gradientY2 = y4-y3
    gradientX2 = x4-x3

    # 1 is x, 2 is y
    # a is phi, b is lambda

    a1 = gradientX2
    b1 = -gradientX1
    c1 = x1-x3

    a2 = gradientY2
    b2 = -gradientY1
    c2 = y1-y3

    denominator = a1*b2-a2*b1

    phiNum = c1*b2-c2*b1
    lambdaNum = c2*a1-c1*a2

    if denominator!=0:
        # print('den!=0')
        phi = phiNum/denominator
        lambda_ = lambdaNum/denominator
        return 0<=lambda_<=1 and 0<=phi<=1

    elif phiNum!=0 and lambdaNum!=0: # denominator == 0
        # print('den==0 and num!=0')
        # hence parallel lines with distance between them
        return False
    elif phiNum==0 and lambdaNum==0:# 0/0 form
        # overlapping lines
        # print('den==0 and num==0')
        if x1!=x2 and (min(x1,x2)<=x3<=max(x2,x1) or min(x1,x2)<=x4<=max(x2,x1)):
            return True
        elif x3!=x4 and (min(x3,x4)<=x1<=max(x4,x3) or min(x3,x4)<=x2<=max(x4,x3)):
            return True
        elif y1!=y2 and (min(y1,y2)<=y3<=max(y2,y1) or min(y1,y2)<=y4<=max(y2,y1)):
            return True
        elif y3!=y4 and (min(y3,y4)<=y1<=max(y4,y3) or min(y3,y4)<=y2<=max(y4,y3)):
            return True
        elif x1==x2==x3==x4 and y1==y2==y3==y4: ## invalid input
            return True
        else:
            return False
    elif phiNum==0 or lambdaNum==0:
        assert False, "something is wrong with my logic"

    assert False, "it should not trigger"


# fl = open('inp.txt','r')
def inputmethod():
    return input()
    return fl.readline().strip()

t = int(inputmethod())
for _ in range(t):
    xyAll4 = [*map(int,inputmethod().split(' '))]
    if getLambda(*xyAll4):
        print('YES')
    else:
        print('NO')