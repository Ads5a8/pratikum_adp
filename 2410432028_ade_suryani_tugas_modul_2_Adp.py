daftar_barang = {
    "nissin wafer chocolate kaleng": 79900,
    "beras pulen premium          ": 98999,
    "nescafe classic              ": 51300,
    "vaseline Gluta-hya serum     ": 55600,
    "kopi espresso arabika papua  ": 67500,
    "kurma khalas                 ": 87250,
    "kanzler sosis sapi           ": 91800,
    "nugget kanzler chicken crispy": 93700,
    "bebelac kaleng               ": 98750,
    "khong guan biscuits kaleng   ": 68500
}


print("====================================Daftar Barang===================================")
for barang in daftar_barang :
    print("Daftar barang : ", barang, "\t   harga : ", daftar_barang[barang])
print("====================================================================================")
print("untuk pembelian kurang dari Rp. 1000000, tidak mendapatkan diskon")
print("untuk pembelian antara Rp. 1000000  sampai dengan Rp.1500000 mendapat diskon 10%")
print("untuk pembelian diatas Rp. 1500000 mendapat diskon 20%")
print("====================================================================================")

barang = str(input("barang yang dibeli             = "))
jumlah = int(input("jumlah barang yang dibeli      = "))
harga = int(input("masukkan harga barang          = "))
bayar = harga *  jumlah 

if bayar < 1000000 :
    print("pembeli tidak mendapat diskon")
elif 1000000 < bayar < 1500000 :
    diskon = 10/100
else :
    diskon = 20/100

potongan_harga = bayar * diskon
total_bayar = bayar - potongan_harga

#menampilkan detail pembayaran
print("harga total                    =", bayar)
print("potongan harga                 = ", potongan_harga)
print("total yang harus dibayar       = ", total_bayar)

print("=====================================================================================")

