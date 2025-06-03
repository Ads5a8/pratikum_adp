#buat text file nya terlebih dahulu
file = open("Catatan.txt", "w")
file.write(" ")
file.close()

# baca dan simpan file
file = open("Catatan.txt", "r")
isi = file.read()
file.close()

data = isi.strip()
catatan = {}

for item in data :
    bagian = item.strip().split("\n")
    if len(bagian) == 2 :
        judul = bagian[0].strip()
        isi_catatan = bagian[1].strip()
        catatan[judul] = isi_catatan

            

def tambah_catatan() :
    judul = input("Masukkan Judul Catatan : ")
    isi = input("Masukkan Isi Catatan : ")
    catatan[judul] = isi

    file = open("Catatan.txt", "a")
    file.write(f"| {judul :<35} | {isi: <150} | \n ")
    file.close()

    print("Catatan berhasil disimpan!\n")

def lihat_catatan() :
    if not catatan :
        print("Belum ada catatan \n")
        return
    print("\n===DAFTAR JUDUL CATATAN===\n")
    for judul in catatan :
        print(f"- {judul}")

    pilih = input("\nMasukkan judul catatan yang ingin dibaca: ")
    if pilih in catatan:
        print("\nIsi Catatan:")
        print(catatan[pilih])
    else:
        print("Data tidak ditemukan.")
    print()
    print()


def menu() :
    while True :
        print("========MENU========")
        print("1. Lihat Catatan")
        print("2. Tambah Catatan")
        print("3. Exit")
        pilihan = input("\nPilih Menu : ")

        if pilihan == "1" :
            lihat_catatan()
        elif pilihan == "2" :
            tambah_catatan()
        elif pilihan == "3" :
            print("Terima kasih telah menggunakan program isi. Program selesai.")
            break
        else :
            print("Pilihan tidak valid!")
        
menu()
        
