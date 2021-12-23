def inversePyramid(pyramidLength = 4):
    if(pyramidLength <= 0):
        print('Negative')
        return(0)
    k = []
    for i in range(pyramidLength):
        k.append(1)
    print(k)
    inversePyramid(pyramidLength - 1)