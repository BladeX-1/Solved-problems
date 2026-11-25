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
        # p1@lambda=0  p2@lambda=1
        # p3@lambda=lambdaP3 p4@lambda=lambdaP4
        # line = p1 + lambda*gradient
        lambdaP3 = (x3-x1)/gradientX1 if gradientX1 else (y3-y1)/gradientY1
        lambdaP4 = (x4-x1)/gradientX1 if gradientX1 else (y4-y1)/gradientY1

        lambda2min = min(lambdaP3,lambdaP4)
        lambda2max = max(lambdaP3,lambdaP4)

        if lambda2max<0:
            return False
        elif 1<lambda2min:
            return False
        return True


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