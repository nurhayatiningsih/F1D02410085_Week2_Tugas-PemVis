# Nama: Nurhayati Ningsih
# NIM : F1D02410085
# Kelas: 6C
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QCheckBox,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtCore import Qt, QPoint

class FormMasuk(QWidget):
    def __init__(self):
        super().__init__()

        self.PURPLE = "#a29bfe"
        self.GREEN = "#28a745"
        self.GRAY = "#6c757d"
     
        self.BG_SUCCESS = "#d4edda"
        self.BORDER_SUCCESS = "#c3e6cb"
        self.TEXT_SUCCESS = "#155724"
        
        self.BG_DANGER = "#f8d7da"
        self.TEXT_DANGER = "#721c24"
        
        self.BORDER_GREEN = "#27c93f"
        self.BORDER_RED = "#dc3545"
        self.BORDER_GRAY = "#ccc"

        self.default_input_style = (
            "padding: 8px; "
            "border-radius: 5px; "
            "font-size: 14px; "
            "border: 2px solid #ccc; "
            "background-color: white;"
        )
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("Login")
        self.setFixedSize(400, 530) 
        self._drag_pos = QPoint()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0) 
        main_layout.setSpacing(0)

        self.title_bar = QFrame()
        self.title_bar.setFixedHeight(40)
        self.title_bar.setStyleSheet("background-color: #f0f0f0;") # Warna latar title bar

        self.close_button = QPushButton()
        self.close_button.setFixedSize(12, 12)
        self.close_button.setStyleSheet("background-color: #ff5f56; border-radius: 6px; border: none;")
        self.close_button.clicked.connect(self.close)

        self.minimize_button = QPushButton()
        self.minimize_button.setFixedSize(12, 12)
        self.minimize_button.setStyleSheet("background-color: #ffbd2e; border-radius: 6px; border: none;")
        self.minimize_button.clicked.connect(self.showMinimized)

        self.maximize_button = QPushButton()
        self.maximize_button.setFixedSize(12, 12)
        self.maximize_button.setStyleSheet("background-color: #27c93f; border-radius: 6px; border: none;")
        self.maximize_button.clicked.connect(self.toggle_maximize)

        self.title_label = QLabel("Login")
        self.title_label.setAlignment(Qt.AlignJustify)
        self.title_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")

        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(10, 0, 10, 0)
        title_layout.addWidget(self.close_button)
        title_layout.addWidget(self.minimize_button)
        title_layout.addWidget(self.maximize_button)
        title_layout.addStretch() 
        title_layout.addWidget(self.title_label)
        title_layout.addStretch() 

        self.header_frame = QFrame()
        self.header_frame.setFixedHeight(60)
        self.header_frame.setStyleSheet(
            f"background-color: {self.PURPLE}; "
            "border-radius: 10px;"
        )
        
        self.header_label = QLabel("LOGIN")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet(
            "color: white; font-size: 20px; font-weight: bold;"
        )
        
        header_layout = QHBoxLayout(self.header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.addWidget(self.header_label)

        self.widget_utama = QFrame()
        self.widget_utama.setStyleSheet("background-color: white; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;")
        
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Enter Username")
        self.input_username.setStyleSheet(self.default_input_style)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Enter Password")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet(self.default_input_style)

        self.input_username.textChanged.connect(self.validate_input_realtime)
        self.input_password.textChanged.connect(self.validate_input_realtime)

        self.cb_show_password = QCheckBox("Tampilkan Password")
        self.cb_show_password.toggled.connect(self.toggle_password_visibility)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(
            f"QPushButton {{ background-color: {self.GREEN}; color: white; font-weight: bold; "
            "border-radius: 5px; padding: 10px; }}"
            "QPushButton:hover { background-color: #218838; }"
        )

        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet(
            f"QPushButton {{ background-color: {self.GRAY}; color: white; font-weight: bold; "
            "border-radius: 5px; padding: 10px; }}"
            "QPushButton:hover { background-color: #5a6268; }"
        )

        self.notification_frame = QFrame()
        self.notification_frame.setVisible(False)
        self.notification_frame.setStyleSheet("border-radius: 5px;")
        self.notification_label = QLabel("")
        self.notification_label.setAlignment(Qt.AlignCenter)
        self.notification_label.setWordWrap(True)
        notification_layout = QVBoxLayout(self.notification_frame)
        notification_layout.setContentsMargins(15, 10, 15, 10)
        notification_layout.addWidget(self.notification_label)

        content_layout = QVBoxLayout(self.widget_utama)
        content_layout.setContentsMargins(30, 20, 30, 20)
        content_layout.setSpacing(15)

        row_username_layout = QVBoxLayout()
        label_username = QLabel("Username")
        label_username.setStyleSheet("font-size: 13px; margin-bottom: 5px;")
        row_username_layout.addWidget(label_username)
        row_username_layout.addWidget(self.input_username)
        content_layout.addLayout(row_username_layout)

        row_password_layout = QVBoxLayout()
        label_password = QLabel("Password")
        label_password.setStyleSheet("font-size: 13px; margin-bottom: 5px;")
        row_password_layout.addWidget(label_password)
        row_password_layout.addWidget(self.input_password)
        content_layout.addLayout(row_password_layout)

        content_layout.addWidget(self.cb_show_password)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.reset_button)
        content_layout.addLayout(button_layout)
        content_layout.addWidget(self.notification_frame)
        content_layout.addStretch()

        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.header_frame)
        main_layout.addWidget(self.widget_utama)

        self.login_button.clicked.connect(self.validate_login)
        self.reset_button.clicked.connect(self.reset_form)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and not self.isMaximized():
            self.move(event.globalPosition().toPoint() - self._drag_pos)
            event.accept()
            
    def mouseReleaseEvent(self, event):
        self._drag_pos = QPoint()
        event.accept()

    def toggle_password_visibility(self, checked):
        if checked:
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    def validate_input_realtime(self):
        username = self.input_username.text()
        password = self.input_password.text()
        if len(username) > 0:
            self.input_username.setStyleSheet(f"{self.default_input_style} background-color: {self.BG_SUCCESS}; border-color: {self.BORDER_GRAY};")
        else:
            self.input_username.setStyleSheet(self.default_input_style)
        if len(password) > 0:
            self.input_password.setStyleSheet(f"{self.default_input_style} background-color: {self.BG_SUCCESS}; border-color: {self.BORDER_GRAY};")
        else:
            self.input_password.setStyleSheet(self.default_input_style)

    def show_notification(self, message, is_success):
        """Fungsi untuk menampilkan notifikasi, tanpa mengubah style input."""
        self.notification_label.setText(message)
        self.notification_frame.setVisible(True)
        
        if is_success:
            self.notification_frame.setStyleSheet(
                f"background-color: {self.BG_SUCCESS}; border: 1px solid {self.BORDER_SUCCESS}; border-radius: 5px;"
            )
            self.notification_label.setStyleSheet(f"color: {self.TEXT_SUCCESS}; font-weight: bold; font-size: 14px;")
        else:
            self.notification_frame.setStyleSheet(
                f"background-color: {self.BG_DANGER}; border: 1px solid #f5c6cb; border-radius: 5px;"
            )
            self.notification_label.setStyleSheet(f"color: {self.TEXT_DANGER}; font-weight: bold; font-size: 14px;")

    def validate_login(self):
        """Validasi login dengan feedback visual spesifik tapi pesan error umum."""
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        self.notification_frame.setVisible(False)
        self.input_username.setStyleSheet(self.default_input_style)
        self.input_password.setStyleSheet(self.default_input_style)
        if not username or not password:
            self.show_notification("Username dan password harus diisi!", is_success=False)
            if not username:
                self.input_username.setStyleSheet(f"{self.default_input_style} border: 2px solid {self.BORDER_RED};")
            if not password:
                self.input_password.setStyleSheet(f"{self.default_input_style} border: 2px solid {self.BORDER_RED};")
            return

        if username != "admin":
            self.input_username.setStyleSheet(f"{self.default_input_style} border: 2px solid {self.BORDER_RED};")
            self.show_notification("Login gagal! Username atau password salah.", is_success=False)
            return 
        if password != "12345":
            self.input_password.setStyleSheet(f"{self.default_input_style} border: 2px solid {self.BORDER_RED};")
            self.show_notification("Login gagal! Username atau password salah.", is_success=False)
            self.input_password.clear()
            self.input_password.setStyleSheet(f"{self.default_input_style} border: 2px solid {self.BORDER_RED};")
            return 
        self.show_notification(f"Login berhasil! Selamat datang, {username}.", is_success=True)
        self.validate_input_realtime()

    def reset_form(self):
        self.input_username.clear()
        self.input_password.clear()
        self.notification_frame.setVisible(False)
        self.input_username.setStyleSheet(self.default_input_style)
        self.input_password.setStyleSheet(self.default_input_style)
        self.cb_show_password.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormMasuk()
    window.show()
    sys.exit(app.exec())