import sys
from pathlib import Path
from PyQt6 import QtWidgets, uic
from kasir import Produk, Keranjang, Transaksi
from bayar_window import BayarWindow
from history_window import HistoryWindow

class KasirApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).parent / "kasir.ui", self)

        self.keranjang = Keranjang()
        self.history = []

        self.daftar_produk = [
            Produk("Nasi Goreng", 18000),
            Produk("Mie Ayam", 10000),
            Produk("Es Teh", 3000),
            Produk("Jus Jeruk", 5000),
            Produk("Ayam Goreng", 20000),
        ]

        for p in self.daftar_produk:
            self.cmbProduk.addItem(str(p))

        self.btnTambah.clicked.connect(self.tambah_item)
        self.btnHapus.clicked.connect(self.hapus_item)
        self.btnBayar.clicked.connect(self.bayar)
        self.btnHistory.clicked.connect(self.lihat_history)

        self.lblTotal.setText("Total : Rp 0")

    def refresh_keranjang(self):
        self.listKeranjang.clear()
        for item in self.keranjang.semua_item():
            self.listKeranjang.addItem(str(item))
        self.lblTotal.setText(f"Total : Rp {self.keranjang.total():,}")

    def tambah_item(self):
        index = self.cmbProduk.currentIndex()
        jumlah = self.spnJumlah.value()
        if jumlah <= 0:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Jumlah harus lebih dari 0!")
            return
        produk = self.daftar_produk[index]
        self.keranjang.tambah(produk, jumlah)
        self.refresh_keranjang()

    def hapus_item(self):
        index = self.listKeranjang.currentRow()
        if index == -1:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Pilih item dulu!")
            return
        self.keranjang.hapus(index)
        self.refresh_keranjang()

    def bayar(self):
        if not self.keranjang.semua_item():
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Keranjang masih kosong!")
            return

        dialog = BayarWindow(self.keranjang.total(), self)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            transaksi = Transaksi(self.keranjang, dialog.jumlah_bayar)
            self.history.append(transaksi)
            QtWidgets.QMessageBox.information(self, "Struk Belanja", transaksi.struk())
            self.keranjang.kosongkan()
            self.refresh_keranjang()

    def lihat_history(self):
        dialog = HistoryWindow(self.history, self)
        dialog.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = KasirApp()
    window.show()
    sys.exit(app.exec())