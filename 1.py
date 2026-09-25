from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFrame,
    QWidget,
    QTableView,
    QApplication
)
from PyQt6.QtCore import Qt

class Queue(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Electronic queue system")
        self.setGeometry(500, 500, 500, 500)

        self.ticketlabel = QLabel("Ticket")
        self.windowlabel = QLabel("Window")

        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Raised)
        frame.setLineWidth(2)

        vlayout = QVBoxLayout(frame)

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.ticketlabel)
        hlayout1.addWidget(self.windowlabel)

        vlayout.addLayout(hlayout1)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(QLabel("A123"))
        hlayout2.addWidget(QLabel("02"))

        vlayout.addLayout(hlayout2)

        hlayout3 = QHBoxLayout()
        hlayout3.addWidget(QLabel("A777"))
        hlayout3.addWidget(QLabel("03"))

        vlayout.addLayout(hlayout3)

        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

app = QApplication([])

window = Queue()
window.show()

app.exec()
