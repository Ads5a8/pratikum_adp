#form penilaian calon penerimaan tim pengajar Himatika

n = int(input("Masukkan jumlah pendaftar: "))
print("")

i = 0

for i in range(n) :
    print("Data pendaftar ke-",i+1)
    nama = str(input("Nama: "))
    matkul = str(input("Mata kuliah yang diminati: "))

    while True :
        nilai_wawancara = float(input("Penilaian wawancara: "))
        if 1 <= nilai_wawancara <= 100 :
            break
        print("Penilaian harus berada pada range 1 sampai 100.")

    while True :
        nilai_tes_tulis = float(input("Penilaian tes tulis: "))
        if 1 <= nilai_tes_tulis <= 100 :
            break
        print("Penilaian harus berada pada range 1 sampai 100.")

    while True :    
        nilai_mengajar = float(input("Penilaian mengajar: "))
        if 1 <= nilai_mengajar <= 100 :
            break
        print("Penilaian harus berada pada range 1 sampai 100.")

    nilai_rata_rata = (nilai_wawancara + nilai_tes_tulis + nilai_mengajar)/3
    print("Nilai rata-rata: ",nilai_rata_rata)

    if nilai_rata_rata > 80 :
        Prediket = "LULUS"
        print("Prediket: ",Prediket)
    else :
        Prediket = "TIDAK LULUS"
        print("Prediket: ",Prediket)
    print("")

