def findPath(M):
    idX,idY=[0,0]
    sizeX,sizeY= M.shape
    res=""
    while idX+1<sizeX or idY+1<sizeY:
        if idX+1<sizeX and M[idX+1,idY]==1:
            res+="D"
            idX+=1
        elif idY+1<sizeY and M[idX,idY+1]==1:
            res+="R"
            idY+=1
    return res
    