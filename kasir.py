class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama} - Rp{self.harga:,}"


class ItemKeranjang:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah

    def subtotal(self):
        return self.produk.harga * self.jumlah

    def __str__(self):
        return f"{self.produk.nama} x{self.jumlah} = Rp{self.subtotal():,}"


class Keranjang:
    def __init__(self):
        self._items = []

    def tambah(self, produk, jumlah=1):
        # Cek kalau produk udah ada, tambah jumlahnya aja
        for item in self._items:
            if item.produk.nama == produk.nama:
                item.jumlah += jumlah
                return
        self._items.append(ItemKeranjang(produk, jumlah))

    def hapus(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)

    def total(self):
        return sum(item.subtotal() for item in self._items)

    def semua_item(self):
        return self._items.copy()

    def kosongkan(self):
        self._items.clear()


class Transaksi:
    def __init__(self, keranjang, bayar):
        self.items = keranjang.semua_item()
        self.total = keranjang.total()
        self.bayar = bayar
        self.kembalian = bayar - self.total

    def struk(self):
        baris = ["=" * 30, "       STRUK BELANJA", "=" * 30]
        for item in self.items:
            baris.append(str(item))
        baris.append("-" * 30)
        baris.append(f"Total    : Rp{self.total:,}")
        baris.append(f"Bayar    : Rp{self.bayar:,}")
        baris.append(f"Kembalian: Rp{self.kembalian:,}")
        baris.append("=" * 30)
        return "\n".join(baris)