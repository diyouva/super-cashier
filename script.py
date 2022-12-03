import pandas as pd

class Transaction:
    def __init__(self):
        """
        fungsi menginisialisasi dictionary
        """
        self.data_item = dict()
        self.daftar_belanja = dict()

    def add_item(self, item, jumlah, harga):
        """
        fungsi menambahkan item belanja dan menghitung total belanja

        parameters
        item    : str   nama item yang akan ditambahkan
        jumlah  : int   jumlah item yang akan ditambahkan
        harga   : int   harga item yang akan ditambahkan

        output: daftar item yang dibeli
        """
        self.data_item.update({item: [jumlah, harga]})
        return f'Item yang dibeli adalah {self.data_item}'

    def update_item_name(self, item, item_baru):
        """
        fungsi untuk memperbaharui item

        parameters
        item        : str   item yang ingin diganti
        item_baru   : str   item baru

        output: daftar item yang dibeli
        """
        temp = self.data_item[item]
        self.data_item.pop(item)
        self.data_item.update({item_baru: temp})
        return f'Item yang dibeli adalah {self.data_item}'
    
    def update_item_qty(self, item, jumlah_baru):
        """
        fungsi untuk memperbaharui jumlah item dan total belanja

        parameters
        item        : str   item yang ingin diubah jumlahnya
        jumlah_baru : str   jumlah baru item

        output: daftar item yang dibeli
        """
        self.data_item[item][0] = jumlah_baru
        return f'Item yang dibeli adalah {self.data_item}'

    def update_item_price(self, item, harga_baru):
        """
        fungsi untuk memperbaharui harga item dan total belanja

        parameters
        item        : str   item yang ingin diubah harganya
        harga_baru  : str   harga baru item

        output: daftar item yang dibeli
        """
        self.data_item[item][1] = harga_baru
        return f'Item yang dibeli adalah {self.data_item}'
    
    def index_item(self, item):
        """
        fungsi mengembalikan nilai index dari baris yang mengandung value 'item'

        parameters
        item    : str   item yang mau dicari

        return
        i       : int   index dari baris yang mengandung item
        """
        for i in range(len(self.data_item)):
            if item == self.data_item[i][0]:
                return i
    
    def delete_item(self, item):
        """
        fungsi untuk menghapus item

        parameters
        item        : str   item yang ingin dihapus

        output: daftar item yang dibeli
        """
        self.data_item.pop(item)
        return f'Item yang dibeli adalah {self.data_item}'
    
    def reset_transaction(self):
        """
        fungsi untuk menghapus seluruh record transaksi

        output: str    keterangan tidak ada item yang dibeli
        """
        self.data_item.clear()
        return f'Semua item berhasil dihapus!'

    def check_order(self):
        """
        fungsi untuk melihat pesanan dan mengecek pesanan apa ada yang bernilai nol

        output : print data item yang dipesan
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 0:
                data = pd.DataFrame(self.data_item).T
                data.columns = ['jumlah', 'harga', 'total']
                print(data.to_markdown())
                print('Pemesanan sudah benar')
            else:
                print('Tidak terdapat pesanan')
        except:
            print('harap melakukan reset transaksi')
    
    def total_price(self):
        """
        fungsi mengecek total belanja dan menghitung diskon

        output: keterangan persentase diskon dan total belanja
        """
        value_item = [i for i in self.data_item.values()]
        total_belanja = sum([a[0]*a[1] for a in value_item])
        try:
            if total_belanja > 200_000:
                total_belanja = total_belanja - (0.05*total_belanja)
                return f'Item yang dibeli adalah {self.data_item}. Anda Mendapat Diskon 5%, total belanja anda: {total_belanja}'
            elif total_belanja > 300_000:
                total_belanja = total_belanja - (0.08*total_belanja)
                return f'Item yang dibeli adalah {self.data_item}. Anda Mendapat Diskon 8%, total belanja anda: {total_belanja}'
            elif total_belanja > 500_000:
                total_belanja = total_belanja - (0.1*total_belanja)
                return f'Item yang dibeli adalah {self.data_item}. Anda Mendapat Diskon 10%, total belanja anda: {total_belanja}'
            elif total_belanja <= 200_000:
                return f'Item yang dibeli adalah {self.data_item}. Anda Tidak Mendapat Diskon, total belanja anda: {total_belanja}'
        except:
            print('harap memeriksa daftar belanja')