from pathlib import Path
from PyQt6 import QtWidgets, uic

class HistoryWindow(QtWidgets.QDialog):
    def __init__(self, history, parent=None):
        super().__init__(parent)
        uic.loadUi(Path(__file__).parent / "history.ui", self)

        self.btnTutup.clicked.connect(self.close)

        if not history:
            self.listHistory.addItem("Belum ada transaksi belum laku sabar!")
            return

        for i, t in enumerate(history, 1):
            self.listHistory.addItem(f"----------Transaksi {i}----------    ")
            for item in t.items:
                self.listHistory.addItem(f"  {item}")
            self.listHistory.addItem(f"  Total    : Rp {t.total:,}")
            self.listHistory.addItem(f"  Bayar    : Rp {t.bayar:,}")
            self.listHistory.addItem(f"  Kembalian: Rp {t.kembalian:,}")
            self.listHistory.addItem("")