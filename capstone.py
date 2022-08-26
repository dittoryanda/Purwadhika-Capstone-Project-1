# Ditto Ryanda
# JCDSVL07
# Capstone Project 1
# Gudang - Data Stok

i_kode = 2 #karena ada 2 data dummy
dataStok = [
    {
        'kode': 'KD1',
        'nama': 'buku',
        'jumlah': 60,
        'modal' : 50000,
        'harga' : 75000
    },
    {
        'kode': 'KD2',
        'nama': 'pensil',
        'jumlah': 60,
        'modal' : 5000,
        'harga' : 7500
    }
]

#READ
def menampilkanData() : #menampilkan seluruh data
    print('Daftar Stok Barang\n')
    print('Kode\t\tNama\t\tJumlah\t\tHargaPokok\tHargaJual')
    for i in range(len(dataStok)) :
        print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(dataStok[i]['kode'],dataStok[i]['nama'],dataStok[i]['jumlah'],dataStok[i]['modal'],dataStok[i]['harga']))

def menampilkanDataSpef(kodeBrg): #menampilkan data pada barang spesifik
    list_kode = [barang['kode'] for barang in dataStok] #list kode barang
    if (kodeBrg.upper() in list_kode) :
        idxBrg = list_kode.index(kodeBrg.upper())
        print('Kode\t\tNama\t\tJumlah\t\tHargaPokok\tHargaJual')
        print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(dataStok[idxBrg]['kode'],dataStok[idxBrg]['nama'],dataStok[idxBrg]['jumlah'],dataStok[idxBrg]['modal'],dataStok[idxBrg]['harga']))
    else :
        print('Data yang Anda cari tidak ada')

#CREATE
def menambahBarang() :
    namaBarang = input('Nama Barang : ')
    cek_existance = [True for barang in dataStok if namaBarang.lower() in barang.values()]
    if(any(cek_existance)) : #cek apakah ada True value di list cek_existance
        print('Barang sudah ada')
    else :
        global i_kode 
        i_kode += 1 #increment untuk kode barang
        jumlah = int(input('Jumlah : '))
        hargaPokok = int(input('Modal : '))
        hargaJual = int(input('Harga Jual : '))
        while True :
            try :
                konfirmasi = int(input('''Apakah anda yakin ingin menambahkan data ini?
                1. Ya
                2. Cancel
                
                Silahkan pilih instruksi yang ingin dijalankan : '''))
            except ValueError :
                print('Input salah')
                continue
            else :
                if (konfirmasi == 1) :
                    dataStok.append({
                        'kode': 'KD'+str(i_kode),
                        'nama': namaBarang,
                        'jumlah': jumlah,
                        'modal': hargaPokok,
                        'harga': hargaJual
                    })
                    print('Data Tersimpan')
                    break
                elif (konfirmasi == 2) :
                    break
                else :
                    print('Instruksi tidak tersedia')
        
#DELETE
def menghapusBarang() :
    menampilkanData() #menampilkan data stok barang
    kodeHapus = input('Masukkan kode barang yang ingin dihapus : ')
    list_kode = [barang['kode'] for barang in dataStok] #list kode barang
    if(kodeHapus.upper() in list_kode) :
        while True :
            try :
                konfirmasi = int(input('''
                Apakah anda yakin ingin menghapus data ini?
                1. Ya
                2. Cancel
                
                Silahkan pilih instruksi yang ingin dijalankan : '''))
            except ValueError :
                print('Input salah')
                continue
            else :
                if (konfirmasi == 1) :
                    del dataStok[list_kode.index(kodeHapus.upper())]
                    print('Data Deleted')
                    break
                elif (konfirmasi == 2) :
                    break
                else :
                    print('Instruksi tidak tersedia')              
    else :
        print('Data yang Anda cari tidak ada')

#UPDATE
def update() :
    kodeBrg = input('''
    Silahkan masukkan kode barang yang ingin di-update : ''')
    list_kode = [barang['kode'] for barang in dataStok] #list kode barang
    if (kodeBrg.upper() in list_kode) :
        idxBrg = list_kode.index(kodeBrg.upper())
        while True:
            try :
                kolom = int(input('''
                1. Nama
                2. Jumlah
                3. Modal/Harga Pokok
                4. Harga Jual

                Silahkan pilih kolom yang ingin diubah : '''))
            except ValueError :
                print('Input salah')
                continue
            else :
                if (kolom == 1) :
                    valueBaru = input('''
                    Masukkan nilai baru : ''')
                    while True:
                        try :
                            konfirmasi = int(input('''
                            Apakah Anda yakin ingin mengubah data ini?
                            1. Ya
                            2. Cancel
                            
                            Silahkan pilih instruksi yang ingin dijalankan : '''))
                        except ValueError :
                            print('Input salah')
                            continue
                        else :
                            if (konfirmasi == 1) :
                                dataStok[idxBrg]['nama'] = valueBaru
                                print('''
                                Data Terupdate''')
                                break
                            elif (konfirmasi == 2) :
                                break
                            else :
                                print('Instruksi tidak tersedia')
                    break
                elif (kolom == 2) :
                    while True :
                        try :
                            valueBaru = int(input('Masukkan nilai baru : '))
                        except ValueError :
                            print('Mohon masukkan angka: ')
                            continue
                        else :  
                            while True:
                                try :
                                    konfirmasi = int(input('''
                                    Apakah Anda yakin ingin mengubah data ini?
                                    1. Ya
                                    2. Cancel
                                    
                                    Silahkan pilih instruksi yang ingin dijalankan : '''))
                                except ValueError :
                                    print('Input salah')
                                    continue
                                else :
                                    if (konfirmasi == 1) :
                                        dataStok[idxBrg]['jumlah'] = valueBaru
                                        print('''
                                        Data Terupdate''')
                                        break
                                    elif (konfirmasi == 2) :
                                        break
                                    else :
                                        print('Instruksi tidak tersedia')
                            break
                elif (kolom == 3) :
                    while True :
                        try :
                            valueBaru = int(input('Masukkan nilai baru : '))
                        except ValueError :
                            print('Mohon masukkan angka: ')
                            continue
                        else :  
                            while True:
                                try :
                                    konfirmasi = int(input('''
                                    Apakah Anda yakin ingin mengubah data ini?
                                    1. Ya
                                    2. Cancel
                                    
                                    Silahkan pilih instruksi yang ingin dijalankan : '''))
                                except ValueError :
                                    print('Input salah')
                                    continue
                                else :
                                    if (konfirmasi == 1) :
                                        dataStok[idxBrg]['modal'] = valueBaru
                                        print('''
                                        Data Terupdate''')
                                        break
                                    elif (konfirmasi == 2) :
                                        break
                                    else :
                                        print('Instruksi tidak tersedia')
                            break
                elif (kolom == 4) :
                    while True :
                        try :
                            valueBaru = int(input('Masukkan nilai baru : '))
                        except ValueError :
                            print('Mohon masukkan angka: ')
                            continue
                        else :  
                            while True:
                                try :
                                    konfirmasi = int(input('''
                                    Apakah Anda yakin ingin mengubah data ini?
                                    1. Ya
                                    2. Cancel
                                    
                                    Silahkan pilih instruksi yang ingin dijalankan : '''))
                                except ValueError :
                                    print('Input salah')
                                    continue
                                else :
                                    if (konfirmasi == 1) :
                                        dataStok[idxBrg]['harga'] = valueBaru
                                        print('''
                                        Data Terupdate''')
                                        break
                                    elif (konfirmasi == 2) :
                                        break
                                    else :
                                        print('Instruksi tidak tersedia')    
                            break      
                break               
    else :
        print('Data yang Anda cari tidak ada')

while True :
    try :
        instruksi = int(input('''
            Halo Admin Gudang 

            1. Menampilkan Data 
            2. Menambah Barang
            3. Menghapus Barang
            4. Update Data Barang
            5. Exit Program

            Silahkan pilih instruksi yang ingin dijalankan : '''))
    except ValueError :
        print('Input salah')
        continue
    else :
        if(instruksi == 1) :
            while True:
                try:
                    pilihanData = int(input('''
                        1. Data Stok Barang
                        2. Data Barang Spesifik
                        3. Cancel
                        
                        Silahkan pilih data yang ingin ditampilkan : '''))
                except ValueError:
                    print('Input salah')
                    continue
                else:
                    if (pilihanData == 1) :
                        menampilkanData() #data stok barang
                    elif (pilihanData == 2) :
                        kodeBrg = input('Silahkan masukkan kode barang yang ingin dicari : ')
                        menampilkanDataSpef(kodeBrg)
                    elif (pilihanData == 3) :
                        break
                    else :
                        print('Instruksi tidak tersedia')
        elif(instruksi == 2) :
            menambahBarang()
        elif(instruksi == 3) :
            menghapusBarang()
        elif(instruksi == 4) :
            update()
        elif(instruksi == 5) :
            break
        else :
            print('Instruksi tidak tersedia')