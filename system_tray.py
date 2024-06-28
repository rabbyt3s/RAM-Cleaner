from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class SystemTray(QSystemTrayIcon):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setIcon(QIcon("resources/icon.png"))
        self.setVisible(True)
        
        self.menu = QMenu()
        self.create_menu()
        self.setContextMenu(self.menu)
        
        self.activated.connect(self.on_tray_activated)

    def create_menu(self):
        show_action = self.menu.addAction("Show")
        show_action.triggered.connect(self.main_window.show)
        
        hide_action = self.menu.addAction("Hide")
        hide_action.triggered.connect(self.main_window.hide)
        
        clean_action = self.menu.addAction("Clean RAM")
        clean_action.triggered.connect(self.main_window.ram_cleaner.clean_ram)
        
        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(self.main_window.close)

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if self.main_window.isVisible():
                self.main_window.hide()
            else:
                self.main_window.show()