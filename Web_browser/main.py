# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWebEngine import QtWebEngine

if __name__ == "__main__":
    
    QGuiApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    
    app = QGuiApplication(sys.argv)
    

    QtWebEngine.initialize()
    
    engine = QQmlApplicationEngine()

    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load("main.qml")
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
