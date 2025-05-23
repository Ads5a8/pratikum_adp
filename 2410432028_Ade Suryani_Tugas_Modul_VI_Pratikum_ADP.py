# Input Banyak Persamaan Linear dan Banyak Variabel dalam Persamaan Linearnya
n = int(input("Banyak Persamaan Linear (2/3) : "))
m = int(input("Banyak Variabel dalam Persamaan Linear (1/2/3) : "))

#Input Koefisien dari Setiap Variabel (Matriks A), dan Nilai konstantanya (Matriks B) 
A = []
for i in range(n):
    print(f"\ninput koefisien dari persamaan {i+1} :")
    baris = []
    for j in range(m):
        baris.append(float(input()))
    A.append(baris)
    i += 1
    print()

B = []
for i in range(n) :
    print(f"input konstanta dari persamaan {i+1}")
    B.append(float(input()))

print("\nMatriks A :")
for baris in A :
    print(baris)
print("\nMatriks B :")
for angka in B :
    print([angka])

while True :
    if n > m :
        print("\nSPL tidak memiliki solusi")
        break
    elif n < m :
        print("\nSPL memiliki banyak solusi (tak hingga)")
        break
    else :
        print("SPL memiliki solusi tunggal yaitu :")
        #buat Matriks Identitas I untuk membantu mencari Invers Matriks A
        I = []
        for i in range(n) :
            baris = []
            for j in range(n) :
                if i == j :
                    entri = 1
                else :
                    entri = 0
                baris.append(entri)
            I.append(baris)

        # Gabungkan Matriks A dengan Matriks Identitas
        for i in range(n) :
            A[i] += I[i]

        # Gunakan MEG untuk mendapatkan Invers Matriks A 
        for i in range(n) :
            pembagi = A[i][i]  #ambil pembaginya yaitu elemen diagonal   
            for j in range(2*n) :    #j mempresentasikan semua kolom, kenapa range-nya 2*n ? karena Matriks A dan Matriks Identitas tadikan digabung, jadi ukuran matriksnya menjadi 2 kali ukuran matriks awal 
                A[i][j] = A[i][j] / pembagi
            for k in range(n) :      # k mempresentasikan baris yang mau di eliminasi, oleh karna itu range-nya n 
                if k != i :
                    faktor = A[k][i]   
                    for j in range(2*n) :
                        A[k][j] -= faktor * A[i][j]

        # Ambil invers dari Matriks A
        a_invers = []
        for i in range(n) :
            a_invers.append(A[i][n:])

        # Kalikan invers Matriks A dengan Matriks B
        X = []
        for i in range(n) :
            hasil = 0
            for j in range(n) :
                hasil += a_invers[i][j] * B[j]
            X.append(hasil)

        
        for i in range(n) :
            print(f"X{i+1} = {X[i] : 4f}")
        break
    
