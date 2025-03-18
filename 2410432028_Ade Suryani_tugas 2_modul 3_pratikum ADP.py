# f(x) =  x^2 + 2x
# batas atas (b) dan batas bawah kurva (a)

a = 1
b = 3

n = int(input("jumlah partisi yang diinginkan : "))
dx = (b-a)/n

estimasi_luas_daerah = 0

for i in range(n) :
    xi = 1 + i*dx
    estimasi_luas_daerah += (xi**2 + 2*xi) * dx

print("luas daerah dari fungsi x^2 + 2x dengan batas x = 1 dan x = 3 dan jumlah partisi n =", (n), "adalah", estimasi_luas_daerah)


