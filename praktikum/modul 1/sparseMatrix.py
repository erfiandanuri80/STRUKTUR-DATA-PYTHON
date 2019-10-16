def createspmatrix():
    mat={}
    numbar=int(input("jumlah baris: "))
    numkol=int(input("jumlah kolom: "))
    numdat=int(input("jumla elemen: "))
    for i in range(numdat):
        bar = int(input("baris ke: ?"))
        kol = int(input("kolom ke: ?"))
        if bar >= numbar:
            print("ERROR","masukkan baris dengan benar bro")
        elif kol >= numkol:
            print("ERROR","masukkan kolom dengan benar bro")
        else:
            data = int(input("data[" + str(bar) + "," + str(kol) + "]="))
            mat[bar, kol] = data
    return mat,numbar,numkol

def multspmatrix(mat1,mat2,bar,kol):
    mat = {}
    for x in range(bar):
        for y in range(bar):
            s = 0
            for z in range(kol):
                s = s + (mat1.get((x,z),0) * mat2.get((z,y),0))
            mat[x,y]=s
    return mat

def displayData(mat,bar,kol):
    for r in range(bar):
        print("|",end="")
        for s in range(kol):
            cek=mat.get((r,s),0)
            data=str(cek)
            print(" "*(4-len(data)) + data, end="")
        print(" |")
