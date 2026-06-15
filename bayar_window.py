from pathlib import Path
from PyQt6 import QtWidgets, uic

class BayarWindow(QtWidgets.QDialog):
    def __init__(self, total, parent=None):
        super().__init__(parent)
        uic.loadUi(Path(__file__).parent / "bayar.ui", self)

        self.total = total
        self.jumlah_bayar = 0
        self.lblTotal.setText(f"Rp {total:,}")
        self.lblKembalian.setText("Rp 0")

        self.inputBayar.textChanged.connect(self.hitung_kembalian)
        self.btnProses.clicked.connect(self.proses)
        self.btnBatal.clicked.connect(self.reject)

    def hitung_kembalian(self):
        try:
            bayar = int(self.inputBayar.text())
            kembalian = bayar - self.total
            if kembalian >= 0:
                self.lblKembalian.setText(f"Rp {kembalian:,}")
            else:
                self.lblKembalian.setText("Uang kurang!")
        except ValueError:
            self.lblKembalian.setText("Rp 0")

    def proses(self):
        try:
            bayar = int(self.inputBayar.text())
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Masukkan angka yang valid jangan pake koma atau titik!")
            return
        if bayar < self.total:
            QtWidgets.QMessageBox.warning(self, "Peringatan", "Uang tidak cukup!")
            return
        self.jumlah_bayar = bayar
        self.accept()