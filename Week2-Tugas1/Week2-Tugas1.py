# Nama: Nurhayati Ningsih
# NIM : F1D02410085
# Kelas: 6C
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
from PySide6.QtCore import Qt

class BiodataForm(QWidget):
    def __init__(self):
        super().__init__()
       
        self.LIGHT_GREEN = "#e6ffed"  
        self.BLUE = "#007bff"         
        self.GRAY = "#6c757d"         
        self.LIGHT_RED_BORDER = "#f8d7da"

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(350, 510)

        self.header_frame = QFrame()
        self.header_frame.setFixedHeight(50)
        self.header_frame.setStyleSheet("background-color: #f0f0f0; border-bottom: 1px solid #ccc;")

        circle_style = "font-size: 15px; font-weight: bold;"
        self.red_circle = QLabel("●")
        self.red_circle.setStyleSheet(f"color: #ff5f56; {circle_style}")
        self.yellow_circle = QLabel("●")
        self.yellow_circle.setStyleSheet(f"color: #ffbd2e; {circle_style}")
        self.green_circle = QLabel("●")
        self.green_circle.setStyleSheet(f"color: #27c93f; {circle_style}")

        self.header_title = QLabel("Form Biodata Mahasiswa")
        self.header_title.setAlignment(Qt.AlignCenter)
        self.header_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")

        header_layout = QHBoxLayout(self.header_frame)
        header_layout.setContentsMargins(15, 0, 15, 0)
        header_layout.addWidget(self.red_circle)
        header_layout.addWidget(self.yellow_circle)
        header_layout.addWidget(self.green_circle)
        header_layout.addStretch()
        header_layout.addWidget(self.header_title)
        header_layout.addStretch()

        self.main_widget = QFrame()
        self.main_widget.setStyleSheet("background-color: white;")
        input_style = "background-color: white; border: 1px solid #ccc;"
        
        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Masukkan Nama Lengkap")
        self.nama_input.setStyleSheet(input_style)

        self.nim_input = QLineEdit()
        self.nim_input.setPlaceholderText("Masukkan NIM")
        self.nim_input.setStyleSheet(input_style)

        self.kelas_input = QLineEdit()
        self.kelas_input.setPlaceholderText("Contoh: TI-2A")
        self.kelas_input.setStyleSheet(input_style)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Pilih Jenis Kelamin", "Laki - laki", "Perempuan"])
        self.gender_combo.setStyleSheet(input_style)

        self.tampilkan_btn = QPushButton("Tampilkan")
        self.tampilkan_btn.setStyleSheet(
            f"QPushButton {{ background-color: {self.BLUE}; color: white; font-weight: bold; border-radius: 5px; padding: 8px; }}"
            f"QPushButton:hover {{ background-color: #0056b3; }}" 
        )

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setStyleSheet(
            f"QPushButton {{ background-color: {self.GRAY}; color: white; font-weight: bold; border-radius: 5px; padding: 8px; }}"
            f"QPushButton:hover {{ background-color: #5a6268; }}" 
        )

        self.hasil_frame = QFrame()
        self.hasil_frame.setFrameShape(QFrame.StyledPanel)
        self.hasil_frame.setStyleSheet("padding: 8px;")

        self.data_biodata_label = QLabel("DATA BIODATA")
        self.data_biodata_label.setAlignment(Qt.AlignJustify)
        self.data_biodata_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.hasil_label = QLabel()
        self.hasil_label.setWordWrap(True)

        hasil_layout = QVBoxLayout(self.hasil_frame)
        hasil_layout.addWidget(self.data_biodata_label)
        hasil_layout.addWidget(self.hasil_label)
        content_layout = QVBoxLayout(self.main_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)

        row_nama_layout = QVBoxLayout()
        label_nama = QLabel("Nama Lengkap")
        label_nama.setAlignment(Qt.AlignJustify)
        row_nama_layout.addWidget(label_nama)
        row_nama_layout.addWidget(self.nama_input)
        content_layout.addLayout(row_nama_layout)

        row_nim_layout = QVBoxLayout()
        label_nim = QLabel("NIM")
        label_nim.setAlignment(Qt.AlignJustify)
        row_nim_layout.addWidget(label_nim)
        row_nim_layout.addWidget(self.nim_input)
        content_layout.addLayout(row_nim_layout)

        row_kelas_layout = QVBoxLayout()
        label_kelas = QLabel("Kelas")
        label_kelas.setAlignment(Qt.AlignJustify)
        row_kelas_layout.addWidget(label_kelas)
        row_kelas_layout.addWidget(self.kelas_input)
        content_layout.addLayout(row_kelas_layout)

        row_gender_layout = QVBoxLayout()
        label_gender = QLabel("Jenis Kelamin")
        label_gender.setAlignment(Qt.AlignJustify)
        row_gender_layout.addWidget(label_gender)
        row_gender_layout.addWidget(self.gender_combo)
        content_layout.addLayout(row_gender_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.tampilkan_btn)
        button_layout.addWidget(self.reset_btn)
        content_layout.addLayout(button_layout)

        content_layout.addWidget(self.hasil_frame)
        content_layout.addStretch()

        main_window_layout = QVBoxLayout(self)
        main_window_layout.setContentsMargins(0, 0, 0, 0)
        main_window_layout.setSpacing(0)
        main_window_layout.addWidget(self.header_frame)
        main_window_layout.addWidget(self.main_widget)

        self.tampilkan_btn.clicked.connect(self.tampilkan_data)
        self.reset_btn.clicked.connect(self.reset_form)

        self.nama_input.textChanged.connect(lambda: self.update_field_color(self.nama_input))
        self.nim_input.textChanged.connect(lambda: self.update_field_color(self.nim_input))
        self.kelas_input.textChanged.connect(lambda: self.update_field_color(self.kelas_input))
        self.gender_combo.currentTextChanged.connect(lambda: self.update_field_color(self.gender_combo))

    def update_field_color(self, field):
        text = ""
        if isinstance(field, QLineEdit):
            text = field.text().strip()
        elif isinstance(field, QComboBox):
            text = field.currentText().strip()
            if text == "Pilih Jenis Kelamin":
                text = ""

        if text:
            field.setStyleSheet(f"background-color: {self.LIGHT_GREEN}; border: 1px solid #ccc;")
        else:
            field.setStyleSheet("background-color: white; border: 1px solid #ccc;")

    def tampilkan_data(self):
        default_style = "background-color: white; border: 1px solid #ccc;"
        self.nama_input.setStyleSheet(default_style)
        self.nim_input.setStyleSheet(default_style)
        self.kelas_input.setStyleSheet(default_style)
        self.gender_combo.setStyleSheet(default_style)
        
        self.hasil_frame.setStyleSheet("padding: 10px;")

        nama = self.nama_input.text().strip()
        nim = self.nim_input.text().strip()
        kelas = self.kelas_input.text().strip()
        gender = self.gender_combo.currentText().strip()
        
        empty_fields = []
        if not nama:
            empty_fields.append("Nama Lengkap")
            self.nama_input.setStyleSheet(f"background-color: white; border: 2px solid {self.LIGHT_RED_BORDER};")
        if not nim:
            empty_fields.append("NIM")
            self.nim_input.setStyleSheet(f"background-color: white; border: 2px solid {self.LIGHT_RED_BORDER};")
        if not kelas:
            empty_fields.append("Kelas")
            self.kelas_input.setStyleSheet(f"background-color: white; border: 2px solid {self.LIGHT_RED_BORDER};")
        if not gender or gender == "Pilih Jenis Kelamin":
            empty_fields.append("Jenis Kelamin")
            self.gender_combo.setStyleSheet(f"background-color: white; border: 2px solid {self.LIGHT_RED_BORDER};")
            
        if empty_fields:
            QMessageBox.warning(
                self, 
                "Validasi Gagal", 
                f"Field berikut belum terisi: \n{', '.join(empty_fields)}"
            )
            return
        filled_style = f"background-color: {self.LIGHT_GREEN}; border: 1px solid #ccc;"
        self.nama_input.setStyleSheet(filled_style)
        self.nim_input.setStyleSheet(filled_style)
        self.kelas_input.setStyleSheet(filled_style)
        self.gender_combo.setStyleSheet(filled_style)
        self.hasil_frame.setStyleSheet(f"padding: 10px; background-color: {self.LIGHT_GREEN};")

        self.hasil_label.setText(
            f"Nama        : {nama}\n"
            f"NIM          : {nim}\n"
            f"Kelas        : {kelas}\n"
            f"Jenis Kelamin: {gender}"
        )

    def reset_form(self):
        self.nama_input.clear()
        self.nim_input.clear()
        self.kelas_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.hasil_label.clear()

        default_style = "background-color: white; border: 1px solid #ccc;"
        self.nama_input.setStyleSheet(default_style)
        self.nim_input.setStyleSheet(default_style)
        self.kelas_input.setStyleSheet(default_style)
        self.gender_combo.setStyleSheet(default_style)
        self.hasil_frame.setStyleSheet("padding: 10px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BiodataForm()
    window.show()
    sys.exit(app.exec())