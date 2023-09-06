import PyInstaller.__main__
import sys

if sys.platform == 'win32' or sys.platform == 'cygwin':
    PyInstaller.__main__.run([
        'C:\Dev\TP1-TC-Grupo3\TP1-TC-Grupo3\main.py',
        '--onefile',
        '--windowed',
        '--add-data=C:\Dev\TP1-TC-Grupo3\TP1-TC-Grupo3\info.png;.'
    ])
else:
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--add-data=info.png:.'
    ])