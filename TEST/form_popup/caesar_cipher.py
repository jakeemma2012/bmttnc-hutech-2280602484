import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.bt_Decrypt.clicked.connect(self.call_api_decrypt)
    
        
    def call_api_encrypt(self):
            url = "http://localhost:5000/api/caesar/encrypt"
            payload = {
                "plain_text": self.ui.txt_PlaintText.toPlainText(),
                "key": self.ui.txt_Key.toPlainText()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_CipherText.setPlainText(data['encrypted_text'])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Encrypt Success")
                    msg.setWindowTitle("Success")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    print("Failed to encrypt text")
            except Exception as e:
                print("Error: ", e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error: "+str(e))
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    def call_api_decrypt(self):
            url = "http://localhost:5000/api/caesar/decrypt"
            payload = {
                "encrypted_text": self.ui.txt_CipherText.toPlainText(),
                "key": self.ui.txt_Key.toPlainText()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_PlaintText.setPlainText(data['decrypted_text'])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypt Success")
                    msg.setWindowTitle("Success")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    print("Failed to decrypt text")
            except Exception as e:
                print("Error: ", e)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error: "+str(e))
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())