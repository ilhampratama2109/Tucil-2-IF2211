def Det(A,B,C):
    #menghitung determinan / garis yang digunakan untuk membagi titik menjadi 2 bagian
    det = A[0]*B[1] + B[0]*C[1] + C[0]*A[1] - A[0]*C[1] - B[0]*A[1] - C[0]*B[1]
    return det

def rekursiv(Points, P, Q):
    #fungsi rekursive untuk convexHull
    if(len(Points) == 0):
        #basis
        return [Q]
    else:
        hull = []
        detMaximum = 0 # inisiasi determinan
        for i in Points:
            determinant = Det(P, Q, i)
            if(determinant > detMaximum):
                detMaximum = determinant
                hull = i

        #bagi jadi 2 bagian, kanan dan kiri
        Bagiankanan = []
        BagianKiri = []
        for j in Points:
            detKanan = Det(hull, Q, j)
            detKiri = Det(P, hull, j)
            if(detKanan > 0.000000001):
                Bagiankanan.append(j)
            if(detKiri > 0.000000001):
                BagianKiri.append(j)
        
        #ulangi terus sampai menemui basis
        BagianKanan = rekursiv(Bagiankanan, hull, Q)
        BagianKiri = rekursiv(BagianKiri, P, hull)
        return BagianKanan + BagianKiri

#fungsi utama
def ConvexHull(Points):
    if(len(Points) < 2): #minimal harus 2 titik untuk membentuk baris
        return Points
    else:
        Points.sort()
        P = Points[0] # ambil bagian paling kiri
        Q = Points[len(Points)-1] #ambil bagian paling kanan
        BagianKanan = []
        BagianKiri = []
        for i in Points:
            determinant = Det(P, Q, i)
            if(determinant > 0.000000001):
                #jika positif masukkan ke dalam bagian kiri
                BagianKiri.append(i)
            if(determinant < -0.000000001):
                #Jika negatif masukkan ke dalam bagian kanan
                BagianKanan.append(i)

        #ulangi terus sampai ketemu basis, isi elemen dari points kurang dari 2
        BagianKanan = rekursiv(BagianKanan, Q, P)
        BagianKiri = rekursiv(BagianKiri, P, Q)
        return BagianKanan+BagianKiri