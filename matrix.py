def add(fD, sD, fM, sM):
# . . .[[1,1,1],[1,1,1][1,1,1]]
    res=[]
    for i in range(fD[0]):
        res.append([])
        for j in range(fD[1]):
            res[i].append(fM[i][j]+sM[i][j])
  
    return res

#test
def sub(fD, sD, fM, sM): #вычитание
# . . .[[1,1,1],[1,1,1][1,1,1]]
    res=[]
    for i in range(fD[0]):
        res.append([])
        for j in range(fD[1]):
            res[i].append(fM[i][j]-sM[i][j])
  
    return res


def mult(fD,sD,fM,sM): #умножение
    res=[]
    for i in range(fD[0]):
        res.append([])
        for j in range(sD[1]):
            res[i].append(cell(fM[i],column(sM,j)))
  
    return res

def cell(line, column): #вычисление элемента при умножении
    cell=0
    for i in range(len(line)):
        cell=cell+line[i]*column[i]
    return(cell) 

def column(sM,j):
    column=[]
    for i in range(len(sM)):
        column.append(sM[i][j])
    return(column)

def det(size, gmatr):
    deter=0
    if size>2:
        curentMS=size-1#размер минора на еденицу меньше
        for i in range(0,size): #разбор по итой строке
            curentM=buildM(curentMS,gmatr,i)#построение нового минора
            deter=deter+(-1)**(1+i)*gmatr[1][i]*det(curentMS,curentM)#формула, 
            #где используем рекурсиию, вычисляя опр.минора
    else:
        deter=gmatr[1][1]*gmatr[2][2]-gmatr[1][2]*gmatr[2][1]
    return(det)

def buildM(S,matr,ej):
    newM=[[0 for i in range(0,S)] for j in range(0,S)]
    for i in range(0,S):
        for j in range(0,S):
            if j<=ej:
                newM[i][j]=matr[i+1][j]
            if j>ej:
                newM[i][j]=matr[i+1][j+1]
    return(newM)        
    
