import psutil
import ctypes
from ctypes import wintypes
import time
from PyQt6.QtCore import QObject, pyqtSignal

class RAMCleaner(QObject):
    ram_usage_updated = pyqtSignal(float, float)
    cleaning_completed = pyqtSignal(float, float)

    def __init__(self):
        super().__init__()
        self.whitelist = set()
        self.cleaning_intensity = 1.0
        self.auto_clean_threshold = 80.0

    def get_ram_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent, memory.available / (1024 * 1024)  # Return percentage and available RAM in MB

    def clean_ram(self):
        initial_usage = self.get_ram_usage()[0]

        # Clear file system cache
        ctypes.windll.kernel32.SetSystemFileCacheSize(-1, -1, 0)

        # Empty working sets of processes
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] not in self.whitelist:
                try:
                    handle = ctypes.windll.kernel32.OpenProcess(
                        wintypes.DWORD(0x001F0FFF),
                        wintypes.BOOL(False),
                        wintypes.DWORD(process.info['pid'])
                    )
                    ctypes.windll.psapi.EmptyWorkingSet(handle)
                    ctypes.windll.kernel32.CloseHandle(handle)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        # Release unused DLLs
        ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)

        time.sleep(1)  # Wait for changes to take effect
        final_usage = self.get_ram_usage()[0]
        self.cleaning_completed.emit(initial_usage, final_usage)

    def start_monitoring(self):
        while True:
            usage_percent, available_mb = self.get_ram_usage()
            self.ram_usage_updated.emit(usage_percent, available_mb)
            
            if usage_percent >= self.auto_clean_threshold:
                self.clean_ram()
            
            time.sleep(1)

    def set_whitelist(self, whitelist):
        self.whitelist = set(whitelist)

    def set_cleaning_intensity(self, intensity):
        self.cleaning_intensity = intensity

    def set_auto_clean_threshold(self, threshold):
        self.auto_clean_threshold = threshold