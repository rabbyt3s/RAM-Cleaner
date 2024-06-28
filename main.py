import sys
import traceback
import logging
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from system_tray import SystemTray
from ram_cleaner import RAMCleaner
from utils.system_utils import add_to_startup, run_as_admin

# Set up logging
logging.basicConfig(filename='pyramcleaner.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def exception_hook(exctype, value, tb):
    logging.error(''.join(traceback.format_exception(exctype, value, tb)))
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = exception_hook

def main():
    try:
        logging.info("Starting PyRAMCleaner")
        
        if not run_as_admin():
            logging.warning("Application not running with admin privileges")
            sys.exit()

        app = QApplication(sys.argv)
        
        logging.info("Initializing RAMCleaner")
        ram_cleaner = RAMCleaner()
        
        logging.info("Initializing MainWindow")
        main_window = MainWindow(ram_cleaner)
        
        logging.info("Initializing SystemTray")
        system_tray = SystemTray(main_window)
        
        # Add to startup if it's the first run
        if getattr(sys, 'frozen', False):
            add_to_startup(sys.executable)
        else:
            add_to_startup(sys.argv[0])

        logging.info("Showing main window")
        main_window.show()
        
        logging.info("Entering main event loop")
        sys.exit(app.exec())

    except Exception as e:
        logging.error(f"Unhandled exception: {str(e)}")
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    main()