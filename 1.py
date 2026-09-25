from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QWidget,
    QTableView,
    QApplication
)
from PyQt6.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

class Queue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Electronic queue system")
        self.setGeometry(500, 500, 500, 500)

        self.ticketlabel = QLabel("Ticket")
        self.windowlabel = QLabel("Window")

        vlayout = QVBoxLayout()

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.ticketlabel)
        hlayout.addWidget(self.windowlabel)

        vlayout.addLayout(hlayout)

        hlayout = QHBoxLayout()
        hlayout.addWidget(QLabel("A123"))
        hlayout.addWidget(QLabel("02"))

        vlayout.addLayout(hlayout)

        widget = QWidget()
        widget.setLayout(vlayout)

        self.table = QTableView()

        data = [
            [0, 1],
            ['a', 'a']
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

app = QApplication([])

window = Queue()
window.show()

app.exec()


