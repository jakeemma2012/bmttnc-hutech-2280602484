import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.main import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        # setup __init__
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Setup Change Page StackWidget
        self.ui.bt_Caesar.clicked.connect(lambda: self.ui.stackedWidget_Main.setCurrentIndex(0))
        self.ui.bt_Vigenere.clicked.connect(lambda: self.ui.stackedWidget_Main.setCurrentIndex(1))
        self.ui.bt_RailFence.clicked.connect(lambda: self.ui.stackedWidget_Main.setCurrentIndex(2))
        self.ui.bt_PlayFair.clicked.connect(lambda: self.ui.stackedWidget_Main.setCurrentIndex(3))
        
        #Setup button for each page
        self.ui.bt_CeasarEncrypt.clicked.connect(self.call_api_caesar_encrypt)
        self.ui.bt_CeasarDecrypt.clicked.connect(self.call_api_caesar_decrypt)
        
        self.ui.bt_VigenereEncrypt.clicked.connect(self.call_api_vigenere_encrypt)
        self.ui.bt_VigenereDecrypt.clicked.connect(self.call_api_vigenere_decrypt)
        
        self.ui.bt_RailFenceEncrypt.clicked.connect(self.call_api_railfence_encrypt)
        self.ui.bt_RailFenceDecrypt.clicked.connect(self.call_api_railfence_decrypt)
        
        self.ui.bt_PlayFairEncrypt_2.clicked.connect(self.call_api_playfair_CreateMatrix)
        self.ui.bt_PlayFairEncrypt.clicked.connect(self.call_api_playfair_encrypt)
        self.ui.bt_PlayFairDecrypt.clicked.connect(self.call_api_playfair_decrypt)
        
        
        
        
    def call_api_caesar_encrypt(self):
            url = "http://localhost:5000/api/caesar/encrypt"
            payload = {
                "plain_text": self.ui.txt_CaesarPlainText.toPlainText(),
                "key": self.ui.txt_CaesarKey.toPlainText()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_CaesarCipherText.setPlainText(data['encrypted_text'])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Caesar Encrypt Success")
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

    def call_api_caesar_decrypt(self):
            url = "http://localhost:5000/api/caesar/decrypt"
            payload = {
                "encrypted_text": self.ui.txt_CaesarCipherText.toPlainText(),
                "key": self.ui.txt_CaesarKey.toPlainText()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_CaesarPlainText.setPlainText(data['decrypted_text'])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Caesar Decrypt Success")
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
    
    def call_api_vigenere_encrypt(self):
            url = "http://localhost:5000/api/cipher/encrypt"
            payload = {
                "plain_text": self.ui.txt_VigenerePlainText.toPlainText(),
                "key": self.ui.txt_VigenereKey.toPlainText()
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.ui.txt_VigenereCipherText.setPlainText(data['encrypted_text'])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Vigenere Encrypt Success")
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
    
    def call_api_vigenere_decrypt(self):
        url = "http://localhost:5000/api/cipher/decrypt"
        payload = {
            "encrypted_text": self.ui.txt_VigenereCipherText.toPlainText(),
            "key": self.ui.txt_VigenereKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_VigenerePlainText.setPlainText(data['decrypted_text'])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Vigenere Decrypt Success")
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
        
    def call_api_playfair_CreateMatrix(self):
        url = "http://localhost:5000/api/playfair/creatematrix"
        payload = {
            "key": self.ui.txt_RailFencePlainText_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Format the matrix into a readable string
                matrix = data['matrix']
                formatted_matrix = '\n'.join([' '.join(row) for row in matrix])
                self.ui.txt_RailFenceCipherText_3.setPlainText(formatted_matrix)
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Playfair Create Matrix Success")
                msg.setWindowTitle("Success")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                print("Failed to create matrix")
        except Exception as e:
            print("Error: ", e)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error: "+str(e))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()    
    
    def call_api_playfair_encrypt(self):
        url = "http://localhost:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_PlayFairPlainText.toPlainText(),
            "key": self.ui.txt_RailFencePlainText_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_PlayFairCipherText.setPlainText(data['encrypted_text'])
                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Playfair Encrypt Success")
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
    
    def call_api_playfair_decrypt(self):
        url = "http://localhost:5000/api/playfair/decrypt"
        payload = {
            "encrypted_text": self.ui.txt_PlayFairCipherText.toPlainText(),
            "key": self.ui.txt_RailFencePlainText_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_PlayFairPlainText.setPlainText(data['decrypted_text'])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Playfair Decrypt Success")
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
            
            
    def call_api_railfence_encrypt(self):
        url = "http://localhost:5000/api/rail_fence/encrypt"
        payload = {
            "plain_text": self.ui.txt_RailFencePlainText.toPlainText(),
            "key": self.ui.txt_RailFenceKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_RailFenceCipherText.setPlainText(data['encrypted_text'])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Railfence Encrypt Success")
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
    
    def call_api_railfence_decrypt(self):
        url = "http://localhost:5000/api/rail_fence/decrypt"
        payload = {
            "encrypted_text": self.ui.txt_RailFenceCipherText.toPlainText(),
            "key": self.ui.txt_RailFenceKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_RailFencePlainText.setPlainText(data['decrypted_text'])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Railfence Decrypt Success")
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