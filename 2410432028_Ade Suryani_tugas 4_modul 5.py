#inisiasi variabel list 
no_pelanggan = []
nama_pelanggan = []
total_belanja = []

while True :
    print("\nMenu Utama : ")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Cetak data")
    print("4. Keluar")
    
    pilihan = input("\nPilih Menu : ")

    if pilihan == "1" :
        print("\nTambahkan Data Pelanggan!\n")
        nomor = input("Nomor Pelanggan : ")
        nama = input("Nama Pelanggan : ")
        total = float(input("Total Belanja : "))

        no_pelanggan.append(nomor)
        nama_pelanggan.append(nama)
        total_belanja.append(total)

        print("\nData telah ditambahkan!\n")
        
    
    elif pilihan == "2" :
        hapus_no = input("\nNomor pelanggan yang mau di hapus : ")

        i = 0 
        while i < len(no_pelanggan) :
            if no_pelanggan[i] == hapus_no :
                del no_pelanggan[i]
                del nama_pelanggan[i]
                del total_belanja[i]
                print("\nData telah dihapus!\n")
                break
            else :
                i += 1
            
        else :
            print("\nData pelanggan tidak dapat ditemukan!")
    
    elif pilihan == "3" :
        print("\nData Pelanggan : \n")
        print(f"{"No.":<8} {"Nama":<15} {"Total":<15}")
        for i in range(len(no_pelanggan)):
            print(no_pelanggan[i],"\t",nama_pelanggan[i],"\t",total_belanja[i])
        
        
    elif pilihan == "4" :
        print("\nTerimakasih telah menggunakan program ini!")
        break

    else :
        print("\nPilihan tidak valid, silahkan coba lagi!")
