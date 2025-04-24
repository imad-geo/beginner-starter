import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QWidget


class SumCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 200)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()

        # Number 1 input
        self.label_num1 = QLabel("Enter first number:")
        self.input_num1 = QLineEdit()
        layout2.addWidget(self.label_num1)
        layout2.addWidget(self.input_num1)
        self.input_num1.setPlaceholderText("Number 1")
        

        # Number 2 input
        self.label_num2 = QLabel("Enter second number:")
        self.input_num2 = QLineEdit()
        layout2.addWidget(self.label_num2)
        layout2.addWidget(self.input_num2)
        self.input_num2.setPlaceholderText("Number 2")

        # set spaces between number 1 and number 2
        layout2.setSpacing(50)

        # arrange the HZ layout

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        # Calculate buttons

        self.calculate_button = QPushButton("Sum")
        self.calculate_button.clicked.connect(self.calculate_sum)   #this for sum
        layout3.addWidget(self.calculate_button)

        self.calculate_button = QPushButton("sub")
        self.calculate_button.clicked.connect(self.calculate_sub) #this for subestraction
        layout3.addWidget(self.calculate_button)

        self.calculate_button = QPushButton("mult")
        self.calculate_button.clicked.connect(self.calculate_mult) #this for multiplication
        layout3.addWidget(self.calculate_button)

        self.calculate_button = QPushButton("div")
        self.calculate_button.clicked.connect(self.calculate_div) #this for devision
        layout3.addWidget(self.calculate_button)

        # set spaces between buttons
        layout3.setSpacing(20)

        #Result display

        self.result_label = QLabel("result will appear here")
        layout1.addWidget(self.result_label)
        central_widget.setLayout(layout1)

        # the methods of calcualtion

    def calculate_sum(self):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())
            total = num1 + num2
            self.result_label.setText(f"Sum: {total}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers!")

    def calculate_sub(self):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())
            total = num1 - num2
            self.result_label.setText(f"subestraction: {total}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers!")
        
    def calculate_mult(self):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())
            total = num1 * num2
            self.result_label.setText(f"multiplication: {total}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers!")

    def calculate_div(self):
        try:
            num1 = float(self.input_num1.text())
            num2 = float(self.input_num2.text())
            total = num1 / num2
            self.result_label.setText(f"devision: {total}")
        except ValueError:
            self.result_label.setText("Please enter valid numbers!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SumCalculator()
    window.show()
    sys.exit(app.exec_())