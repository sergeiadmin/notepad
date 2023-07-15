import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, QtCore

class Notepad(QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_file = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Блокнот')
        self.setGeometry(100, 100, 800, 600)

        # Создание меню
        new_action = QAction(QIcon.fromTheme('document-new'), 'Новый', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)

        open_action = QAction(QIcon.fromTheme('document-open'), 'Открыть', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        save_action = QAction(QIcon.fromTheme('document-save'), 'Сохранить', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction(QIcon.fromTheme('document-save-as'), 'Сохранить как', self)
        save_as_action.triggered.connect(self.save_file_as)

        exit_action = QAction(QIcon.fromTheme('application-exit'), 'Выход', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        edit_toolbar = self.addToolBar('Редактирование')
        edit_toolbar.addAction(new_action)
        edit_toolbar.addAction(open_action)
        edit_toolbar.addAction(save_action)
        edit_toolbar.addAction(save_as_action)
        edit_toolbar.addSeparator()
        edit_toolbar.addAction(exit_action)

        # Создание текстового поля
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Создание статус бара
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Создание меню тем
        self.theme_menu = QMenu('Темы', self)
        self.theme_menu.addAction('Светлая', self.light_theme)
        self.theme_menu.addAction('Темная', self.dark_theme)
        self.theme_menu.addAction('Синяя', self.blue_theme)

        # Добавление меню тем в главное меню
        self.view_menu = self.menuBar().addMenu('Вид')
        self.view_menu.addMenu(self.theme_menu)

        # Настройка окна приложения
        self.setWindowIcon(QIcon.fromTheme('applications-office'))
        self.show()

    def new_file(self):
        self.text_edit.clear()
        self.current_file = None
        self.status_bar.showMessage('Новый файл')

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                    'Текстовые файлы (*.txt);;Все файлы (*)', options=options)
        if file_name:
            with open(file_name, 'r') as f:
                file_content = f.read()
                self.text_edit.setText(file_content)
            self.current_file = file_name
            self.status_bar.showMessage('Файл открыт')

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as f:
                f.write(self.text_edit.toPlainText())
            self.status_bar.showMessage('Файл сохранен')
        else:
            self.save_file_as()

    def save_file_as(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
                                                    'Текстовые файлы (*.txt);;Все файлы (*)', options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.text_edit.toPlainText())
            self.current_file = file_name
            self.status_bar.showMessage('Файл сохранен')

    def light_theme(self):
        qApp.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        qApp.setPalette(palette)

    def dark_theme(self):
        qApp.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        qApp.setPalette(palette)

    def blue_theme(self):
        qApp.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(180, 210, 255))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(180, 210, 255))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        qApp.setPalette(palette)

    def wheelEvent(self, event):
        if event.modifiers() & QtCore.Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                # увеличение размера текста
                font = self.text_edit.font()
                font.setPointSize(font.pointSize() + 1)
                self.text_edit.setFont(font)
            else:
                # уменьшение размера текста
                font = self.text_edit.font()
                font.setPointSize(font.pointSize() - 1)
                self.text_edit.setFont(font)
        else:
            super().wheelEvent(event)

    def create_new_text_area(self):
        new_text_area = QTextEdit(self)
        self.setCentralWidget(new_text_area)

    def search_keyword(self, keyword):
        text = self.text_edit.toPlainText()
        if keyword in text:
            QMessageBox.information(self, 'Результат поиска', 'Ключевое слово найдено')
        else:
            QMessageBox.information(self, 'Результат поиска', 'Ключевое слово не найдено')

    def show_search_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Поиск')
        dialog.setModal(True)

        layout = QVBoxLayout(dialog)

        keyword_label = QLabel('Ключевое слово:')
        keyword_input = QLineEdit()
        search_button = QPushButton('Найти')

        layout.addWidget(keyword_label)
        layout.addWidget(keyword_input)
        layout.addWidget(search_button)

        search_button.clicked.connect(lambda: self.search_keyword(keyword_input.text()))
        dialog.exec_()

app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())
