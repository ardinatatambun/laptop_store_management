from tabulate import tabulate

# def tam
database_item = [
    {'Nama': 'Asus VivoBook 14 A416MA', 'Storage' : '256GB', 'Layar' :'14' , 'Processor' : 'Intel Celeron N4020', 'Ram' : '4GB ', 'Harga' : 5199000},
    {'Nama': 'Lenovo IdeaPad Slim 3 15ADA6', 'Storage' : '512GB', 'Layar' :'15.6' , 'Processor' : 'AMD Ryzen 3 5300U', 'Ram' : '8GB', 'Harga' : 6999000},
    {'Nama': 'HP 14s-dq2608TU', 'Storage' : '512GB ', 'Layar' :'14' , 'Processor' : 'Intel Core i3-1115G4', 'Ram' : '8GB', 'Harga' : 7499000},
    {'Nama': 'Acer Aspire 5 A514-54G', 'Storage' : '512GB', 'Layar' :'14' , 'Processor' : 'Intel Core i5-1135G7', 'Ram' : '8GB', 'Harga' : 8799000},
    {'Nama': 'Asus TUF Gaming F15 FX506HF', 'Storage' : '512GB', 'Layar' :'15.6' , 'Processor' : 'Intel Core i5-11400H', 'Ram' : '8GB', 'Harga' : 12999000},
    {'Nama': 'Lenovo Legion 5 15ACH6H', 'Storage' : '1TB', 'Layar' :'15.6' , 'Processor' : 'AMD Ryzen 7 5800H', 'Ram' : '16GB', 'Harga' : 17499000},
    {'Nama': 'Apple MacBook Air M1', 'Storage' : '256GB', 'Layar' :'13.3' , 'Processor' : 'Apple M1', 'Ram' : '8GB', 'Harga' : 13999000}
]

# database admin
database_recycle = []
database_add = []

# database customer
database_cart = []
database_cart_bin = []

# MENAMPILKAN DATABASE ITEM / CART (menambah nomor index)
def display_list(x):
    item_with_index = []
    for i in range(len(x)):
        add_index_item = {'No': i + 1, **x[i]}  
        item_with_index.append(add_index_item)
    table = (tabulate(item_with_index, headers='keys', tablefmt='rounded_outline'))
    print(table)

# Menampilkan database (admin/customer)
def display_database():
    display_list(database_item)
    while True:
        confirm_back = input('[1] Kembali ke Menu Utama (ketik back atau kembali): ')
        if confirm_back.lower() in ('back', 'kembali', 'b'):
            break
        elif confirm_back.isdigit():
            confirm_back = int(confirm_back)
            if confirm_back != 1:
                print('Input tidak valid!')
            else:
                break
        else:
            print('Input tidak valid!')
            continue

# ------------------------------------FITUR ADMIN----------------------------------

# Tampilan login awal (admin) (B)
def login_admin():
    while True:
        print('\nAnda telah login sebagai Admin\n')
        user_admin = input('Silakkan masukkan username atau (b/back untuk kembali): ')
        if user_admin in ('b', 'back'):
            break
        pass_admin = input('Silakkan masukkan password atau (b/back untuk kembali): ')
        if pass_admin in ('b', 'back'):
            break
        elif user_admin == 'admin' and pass_admin == '123':
            menu_admin()
        else:
            print('\nLogin gagal. Tolong masukkan username dan password yang benar!')
            print('(Jika memilih tidak, anda akan dikembalikan ke menu awal)')
            retry_login = input('Apakah anda masih ingin mencoba lagi ? (Y/N): ')
            retry_login = retry_login.lower()
            while True:
                if retry_login in ('y', 'ya', 'yes'):
                    break
                elif retry_login in ('n', 'tidak', 'no'):
                    return
                else:
                    print('Pilihan tidak valid!')

# Tampilan utama (admin) (G)
def menu_admin():
    while True:
        print('\n---------------------------MENU ADMIN---------------------------')
        print('''
[1] Menampilkan list barang
[2] Menambahkan barang
[3] Menghapus barang
[4] Mengupdate barang
[5] List Barang Yang Dihapus
[6] Keluar
              ''')
        print('----------------------------------------------------------------')
        admin_input = input('Masukkan perintah yang ingin anda jalankan: ')
        if admin_input.isdigit():
            admin_input = int(admin_input)
        if admin_input == 1:
            display_database()
        elif admin_input == 2:
            add_database()
        elif admin_input == 3:
            remove_database()
        elif admin_input == 4:
            update_database()
        elif admin_input == 5:
            show_delete_item()
        elif admin_input == 6:
            break
        else: 
            print('Pilihan tidak Valid! Harus berupa angka!')
            continue

# MENAMBAH DATABASE ITEM (admin) (H)
def add_database():
    while True:
        display_list(database_item)
        name_item = input('Masukkan nama item yang ingin ditambahkan (ketik "back" atau "b" untuk kembali): ')
        if name_item.lower() in ('b', 'kembali', 'back'):
            break
        storage_item = input('Masukkan ukuran storage dari item (ketik "back" atau "b" untuk kembali): ')
        if storage_item.lower() in ('b', 'kembali', 'back'):
            break
        screen_item = input('Masukkan ukuran layar dari item (ketik "back" atau "b" untuk kembali): ')
        if screen_item.lower() in ('b', 'kembali', 'back'):
            break
        processor_item = input('Masukkan jenis processor dari item (ketik "back" atau "b" untuk kembali): ')
        if processor_item.lower() in ('b', 'kembali', 'back'):
            break
        ram_item = input('Masukkan ukuran RAM dari item (ketik "back" atau "b" untuk kembali): ')
        if ram_item.lower() in ('b', 'kembali', 'back'):
            break
        price_item = input('Masukkan harga dari item yang ingin ditambahkan (ketik "back" atau "b" untuk kembali): ')
        while True:
            if not price_item.isdigit():
                print('Input harus berupa angka!')
                price_item = input('Masukkan harga dari item yang ingin ditambahkan (ketik "back" atau "b" untuk kembali): ')
                if ram_item.lower() in ('b', 'kembali', 'back'):
                    break
                continue
            elif price_item.isdigit():
                price_item = int(price_item)
                break
    
        for item in database_item:
            if (
            item['Nama'].lower() == name_item.lower() and 
            item['Storage'].lower() == storage_item.lower() and 
            item['Layar'].lower() == screen_item.lower() and 
            item['Processor'].lower() == processor_item.lower() and 
            item['Ram'].lower() == ram_item.lower() and 
            item['Harga'] == price_item
            ):
                print('Data sudah ada')
                return    
        database_item.append({
            'Nama': name_item.title(), 
            'Storage': storage_item.upper(), 
            'Layar': screen_item, 
            'Processor': processor_item.title(), 
            'Ram': ram_item.upper(), 
            'Harga': price_item
            })
        print('Data barang berhasil ditambahkan')
        database_add.append({
            'Nama': name_item.title(), 
            'Storage': storage_item.upper(), 
            'Layar': screen_item, 
            'Processor': processor_item.title(), 
            'Ram': ram_item.upper(), 
            'Harga': price_item
            })
        display_list(database_add)
        database_add.clear()
        break

# MENGHAPUS DATABASE ITEM (admin) (I)
def remove_database():
    display_list(database_item)
    while (True):
        item_delete = input('Masukkan nomor item yang ingin anda hapus (b/back untuk kembali): ')
        if item_delete.lower() in ('b', 'kembali', 'back'):
            break
        elif not item_delete.isdigit():
            print('Input tidak valid! Mohon masukkan nomor item yang ingin diubah')
            continue
        item_delete = int(item_delete)
        if not 0 < item_delete < len(database_item) + 1:
            print('Input tidak boleh melebihi nomor item yang tersedia!')
            continue
        database_recycle.append(database_item[item_delete - 1])
        print('Barang berhasil dihapus :')
        display_list(database_recycle)
        del database_item[item_delete - 1]
        print("Daftar barang yang siap dijual:")
        display_list(database_item)
        while (True):
            confirm = input("Apakah masih ingin menghapus stok ? (ya/tidak) : ")
            if confirm in ('tidak', 't', 'no'):
                return
            elif confirm.isdigit():
                print('Input tidak boleh angka!')
                continue
            elif confirm in ('yes', 'y','ya'):
                break
            else:
                print('Input tidak valid!')

# MENGUPDATE DATABASE ITEM (admin) (J)
def update_database():
    while True:
        display_list(database_item)
        item_update = (input('Masukkan nomor item yang ingin anda ubah (b/back untuk kembali): '))
        if item_update in ('b', 'kembali', 'back'):
            break
        elif not item_update.isdigit():
            print('Input harus berupa angka! Mohon masukkan nomor item yang ingin diubah')
            continue
        item_update = int(item_update)
        if 0 < item_update < len(database_item) + 1:
            data_update_success = 'Data barang berhasil diubah!'
            item_update = database_item[item_update - 1]
            print('[1] Ubah keseluruhan data\n[2] Nama\n[3] Ukuran Storage\n[4] Ukuran Layar\n[5] Jenis Processor\n[6] Ukuran Ram\n[7] Harga Barang\n[8] Kembali Menu Utama')
            update_value = int(input('Pilih bagian mana yang ingin anda ubah: '))
            if update_value == 1:
                name_item = input('Masukkan nama baru item yang ingin diubah: ')
                storage_item = input('Masukkan ukuran storage dari item: ')
                screen_item = input('Masukkan ukuran layar dari item: ')
                processor_item = input('Masukkan jenis processor dari item: ')
                ram_item = input('Masukkan ukuran RAM dari item: ')
                price_item = input('Masukkan harga dari item yang ingin ditambahkan: ')
                while True:
                    if not price_item.isdigit():
                        print('Input harus berupa angka!')
                        price_item = input('Masukkan harga dari item yang ingin ditambahkan: ')
                        continue
                    elif price_item.isdigit():
                        price_item = int(price_item)
                        break
                item_update['Nama'] = name_item.title() 
                item_update['Storage'] = storage_item.upper() 
                item_update['Layar'] = screen_item 
                item_update['Processor'] = processor_item.title() 
                item_update['Ram'] = ram_item.upper() 
                item_update['Harga'] = price_item
                print(data_update_success)
            elif update_value == 2:
                name_item = input('Masukkan nama baru item yang ingin diubah: ')
                item_update['Nama'] = name_item.title()
                print(data_update_success)
            elif update_value == 3:
                storage_item = input('Masukkan ukuran storage baru dari item: ')
                item_update['Storage'] = storage_item.upper()
                print(data_update_success)
            elif update_value == 4:
                screen_item = input('Masukkan ukuran layar baru dari item: ')
                item_update['Layar'] = screen_item
                print(data_update_success)
            elif update_value == 5:
                processor_item = input('Masukkan jenis processor baru dari item: ')
                item_update['Processor'] = processor_item.title()
                print(data_update_success)
            elif update_value == 6:
                ram_item = input('Masukkan ukuran RAM baru dari item: ')
                item_update['Ram'] = ram_item.upper()
                print(data_update_success)
            elif update_value == 7:
                price_item = input('Masukkan harga dari item yang ingin ditambahkan: ')
                while True:
                    if not price_item.isdigit():
                        print('Input harus berupa angka!')
                        price_item = input('Masukkan harga dari item yang ingin ditambahkan: ')
                        continue
                    elif price_item.isdigit():
                        price_item = int(price_item)
                        break
                item_update['Harga'] = price_item
                print(data_update_success)
            elif update_value == 8:
                break
        else:
            print('Input tidak boleh melebihi nomor item yang tersedia!')
            continue

# MELIHAT DATABASE YANG DIHAPUS (admin) (K)
def show_delete_item():
    while True:
        if database_recycle == []:
            print('Belum ada data barang yang dihapus!')
            break
        else: 
            display_list(database_recycle)
            recycle_item = input('Apakah anda ingin mengembalikan barang ke dalam stok ? (Ya/Tidak) (B/Back untuk kembali): ')
        if recycle_item.lower() in ('tidak', 'b', 'back'):
            return
        elif recycle_item.isdigit():
            print('Input harus berupa ya/tidak/kembali')
            continue
        elif recycle_item.lower() in ('ya', 'y', 'yes'):
            confirm_recycle = input('Ingin mengembalikan seluruh item ?\n[1] Seluruh Item\n[2] Sesuai nomor\n'
        'Masukkan pilihan: ')
        else:
            print('Input tidak valid!')
            continue
        while True:
            if not confirm_recycle.isdigit:
                print('Input harus berupa angka!')
                confirm_recycle = input('Ingin mengembalikan seluruh item ?\n[1] Seluruh Item\n[2] Sesuai nomor\n')
                continue
            else:
                confirm_recycle = int(confirm_recycle)
                break
        if confirm_recycle == 1:
            database_item.extend(database_recycle)
            database_recycle.clear()
            print('Seluruh barang sudah dikembalikan ke dalam stok!')
            break
        elif confirm_recycle == 2:
            recycle_index = input('Masukkan nomor yang ingin dikembalikan: ')
            while True:
                if not recycle_index.isdigit:
                    print('Input harus berupa angka!')
                    recycle_index = input('Masukkan nomor yang ingin dikembalikan: ')
                    continue
                else:
                    recycle_index = int(recycle_index)
                    break
            database_item.append(database_recycle[recycle_index - 1])
            del database_recycle[recycle_index - 1]
            print('Barang sudah dikembalikan ke dalam stok!\nList barang di recycle bin')
            continue

# ------------------------------------FITUR CUSTOMER----------------------------------

# Tampilan awal (customer) (A)
def login_buyer():
    while True:
        print('\n---------------------------MENU PEMBELI---------------------------')
        print('''
[1] Tampilkan data laptop yang dijual
[2] Menambah Keranjang Belanja
[3] Melihat/Mengurangi Keranjang Belanja
[4] Pembayaran
[5] Keluar
              ''')
        print('-----------------------------------------------------------------')
        admin_input = input('Masukkan perintah yang ingin anda jalankan: ')
        if admin_input.isdigit():
            admin_input = int(admin_input)
            if admin_input == 1:
                display_database()
            elif admin_input == 2:
                add_cart()
            elif admin_input == 3:
                show_cart_item()
            elif admin_input == 4:
                payment_info(database_cart)
            elif admin_input == 5:
                break
            else:
                print('Pilihan tidak Valid! Harap masukkan sesuai opsi yang ada!')
        else: 
            print('Pilihan tidak Valid! Harus berupa angka!')
            continue

# Menambah barang ke dalam keranjang (customer) (C)
def add_cart():
    while (True):
        display_list(database_item)
        add_item = input("Masukkan nomor barang yang ingin dibeli (b/back untuk kembali): ")
        if add_item.lower() in ('b', 'kembali', 'back'):
            break
        elif not add_item.isdigit():
            print('Input tidak valid! Mohon masukkan nomor item yang ingin beli')
            continue
        add_item = int(add_item)
        if not 0 < add_item < len(database_item) + 1:
            print('Input tidak boleh melebihi nomor item yang tersedia!')
            continue
        while True:
            amount_item = input('Jumlah barang yang ingin anda beli (b/back untuk kembali): ')
            if amount_item.lower() in ('b', 'kembali', 'back'):
                break
            elif not amount_item.isdigit():
                print('Input tidak valid! Mohon jumlah barang yang ingin anda tambahkan')
                continue
            amount_item = int(amount_item)
            cart_item = dict(database_item[add_item-1])
            cart_item['Jumlah'] = amount_item
            duplicate_item = False
            for item in database_cart:
                if (
                    item['Nama'] == cart_item['Nama'] and 
                    item['Storage'] == cart_item['Storage'] and 
                    item['Layar'] == cart_item['Layar'] and 
                    item['Processor'] == cart_item['Processor'] and
                    item['Ram'] == cart_item['Ram'] and 
                    item['Harga'] == cart_item['Harga']
                    ):
                    print('Data barang sudah ada, jika ingin mengubah stok harap menggunakan pilihan 4')
                    duplicate_item = True
                    break
            if duplicate_item == True:
                break
            elif not duplicate_item:
                database_cart.append(cart_item)
                print('Barang sudah berhasil ditambahkan kedalam keranjang')
                display_list(database_cart)
                break
        break

# Menampilkan keranjang (customer) (D)
def show_cart_item():
    while True:
        if database_cart == []:
            print('Belum ada barang di keranjang Anda!')
            break
        else: 
            display_list(database_cart)
            print('[1] Melanjutkan pembayaran\n[2] Menghapus/mengurangi barang dari keranjang\n[3] Kembali')
            buy_item = (input('Pilihan anda ?: '))
            if buy_item.isdigit():
                buy_item = int(buy_item)
                if buy_item == 1:
                    payment_info(database_cart)
                elif buy_item == 3:
                    break
                elif buy_item == 2:
                    change_input = input('[1] Menghapus barang\n[2] Mengatur jumlah barang\n[3] Kembali\nPilihan anda: ')
                    if not change_input.isdigit():
                        print('Input harus berupa angka!')
                    else:
                        change_input = int(change_input)
                    if change_input == 1:
                        remove_cart()
                    elif change_input == 2:
                        update_cart()
                    elif change_input == 3:
                        break
                else:
                    print('Input tidak valid, mohon masukkan input dalam opsi yang tertera')
                    continue
            else:
                print('Input harus berupa angka!')
                continue

# Proses pembayaran (customer) (E)
def payment_info(cart):
    while True:
        if cart == []:
            print('Belum ada data barang yang bisa dibayar!')
            break
        else: 
            final_payment = 0
            for item in cart:
                total_payment = item['Harga'] * item['Jumlah']
                payment_item = dict(item)
                payment_item['Total'] = total_payment
                final_payment += payment_item['Total']
        print(f"Total belanja yang harus dibayarkan : Rp {final_payment:,}")
        money_total = 0
        while (True) :
            money = input("Masukkan jumlah uang yang Anda miliki (b untuk kembali): ")
            if money.lower() in ('b', 'back', 'kembali'):
                return
            elif not money.isdigit():
                print('Mohon masukkan uang dalam angka!')
                continue
            else:
                money = int(money)
            money_total += money 
            if money_total > final_payment:
                change_money = money_total - final_payment
                print("\nTERIMA KASIH")
                print("Pembelian Anda Berhasil! Mohon ambil barang di counter depan")
                print(f"Uang kembali anda : Rp{change_money:,}")
                database_cart.clear()
                return
            elif money_total < 0:
                print("Uang Anda tidak valid. Silakan masukkan jumlah uang yang benar.")
            elif money_total < final_payment:
                minus_money = final_payment - money_total
                print(f"Uang Anda tidak cukup. Kekurangan sebesar : Rp{minus_money:,}")
                continue
            else :
                print("Uang Anda pas. TERIMA KASIH.")
                return

# Menghapus data di keranjang customer (customer) (F)
def remove_cart():
    display_list(database_cart)
    while (True):
        item_delete = input('Masukkan nomor item yang ingin anda hapus (b/back untuk kembali): ')
        if item_delete.lower() in ('b', 'kembali', 'back'):
            break
        elif not item_delete.isdigit():
            print('Input tidak valid! Mohon masukkan nomor item yang ingin diubah')
            continue
        item_delete = int(item_delete)
        if not 0 < item_delete < len(database_item) + 1:
            print('Input tidak boleh melebihi nomor item yang tersedia!')
            continue
        database_cart_bin.append(database_item[item_delete - 1])
        print('Barang berhasil dihapus!')
        del database_cart[item_delete - 1]
        if database_cart == []:
            break
        else:
            print("Daftar barang yang dikeranjang:")
            display_list(database_cart)
        while (True):
            confirm = input("Apakah masih ingin menghapus stok ? (ya/tidak) : ")
            if confirm.lower() in ('tidak', 't', 'no'):
                return
            elif confirm.lower() in ('yes', 'y','ya'):
                break
            elif confirm.isdigit():
                print('Input tidak boleh angka!')
                continue
            else:
                print('Input tidak valid!')

# Mengupdate database keranjang (customer) (F)
def update_cart():
    while True:
        display_list(database_cart)
        item_update = (input('Masukkan nomor item yang ingin anda ubah (b/back untuk kembali): '))
        if item_update in ('b', 'kembali', 'back'):
            break
        elif not item_update.isdigit():
            print('Input harus berupa angka! Mohon masukkan nomor item yang ingin diubah')
            continue
        item_update = int(item_update)
        if 0 < item_update < len(database_cart) + 1:
            data_update_success = 'Data barang berhasil diubah!'
            item_update = database_cart[item_update - 1]
            print('\nApakah anda masih ingin mengubah barang?\n[1] Ubah stok barang\n[2] Kembali menu sebelumnya')
            update_value = int(input('Pilih 1 untuk tetap mengubah atau 2 untuk kembali: '))
            if update_value == 1:
                stock_item = input('Masukkan jumlah baru dari item yang ingin diubah: ')
                while True:
                    if not stock_item.isdigit():
                        print('Input harus berupa angka!')
                        stock_item = input('Masukkan jumlah dari item yang ingin diubah: ')
                        continue
                    elif stock_item.isdigit():
                        stock_item = int(stock_item)
                        break
                item_update['Jumlah'] = stock_item
                print(data_update_success)
            elif update_value == 2:
                break
        else:
            print('Input tidak boleh melebihi nomor item yang tersedia!')
            continue

# ------------------------------------MENU UTAMA----------------------------------
# Tampilan awal Menu Utama (START)
def menu_utama():
    while (True):
        print('''
Selamat Datang di Toko Laptop Elon Musk
Apakah anda ingin masuk sebagai : 
1. Pembeli (atau ketik "pembeli")
2. Admin (atau ketik "admin")
3. Keluar (atau ketik "keluar" atau "exit")
''')
        login_input = input('Pilih (1/2/3): ')
        if login_input.isdigit():
            login_input = int(login_input)
            if not (1 <= login_input <= 3):
                print('Pilihan tidak valid!\nJika ingin keluar dari program anda dapat memilih "exit" atau "keluar"')
                continue
            if login_input == 1:
                login_buyer()
            elif login_input == 2:
                login_admin()
            elif login_input == 3:
                break
        else:
            login_input = login_input.lower()
            if login_input == 'pembeli':
                login_buyer()
            elif login_input == 'admin':
                login_admin()
            elif login_input in ('keluar', 'exit'):
                break
            else: 
                print('Pilihan tidak valid!\nJika ingin keluar dari program anda dapat memilih "exit" atau "keluar"')

menu_utama()