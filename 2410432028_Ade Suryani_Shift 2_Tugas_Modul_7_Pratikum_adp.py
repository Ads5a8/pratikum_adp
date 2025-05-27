#Program menghitung tagihan listrik
def tagihan_listrik(pemakaian_kwh, golongan = 3): 
    if golongan == 1 :
        tarif_pertama = 1500
        tarif_selanjutnya =  2000
    elif golongan == 2 :
        tarif_pertama = 2500
        tarif_selanjutnya = 3000
    elif golongan == 3 :
        tarif_pertama =  4000
        tarif_selanjutnya = 5000
    elif golongan == 4 :
        tarif_pertama = 5000
        tarif_selanjutnya = 7000
    else :
        tarif_pertama = 4000
        tarif_selanjutnya = 5000

#Hitung besar tagihan yang akan dibayar
    if pemakaian_kwh <= 100 :
        tagihan = pemakaian_kwh * tarif_pertama
    else :
        tagihan = 100*tarif_pertama + (pemakaian_kwh -  100)*tarif_selanjutnya

    return tagihan


a = float(input("Pemakaian kwh : "))
b = float(input("Golongan tarif (1-4), input selain 1-4 jika tidak ada informasi golongan tarif : "))


print("\nTagihan listrik sebesar : Rp.",tagihan_listrik(a, b))
print()

