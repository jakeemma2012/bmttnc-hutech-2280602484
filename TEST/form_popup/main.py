import sys
import os
import argparse
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.main import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self, initial_tab=0):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set window to stay on top of other windows
        # self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        
        # Store navigation buttons
        self.nav_buttons = {
            0: self.ui.bt_Caesar,
            1: self.ui.bt_Vigenere,
            2: self.ui.bt_RailFence,
            3: self.ui.bt_PlayFair
        }
        
        # Set window properties
        self.setMinimumSize(800, 600)  # Set minimum size to prevent window from being too small
        self.setWindowTitle("CIPHER ENCRYPT")
        
        # Connect buttons with lambda to pass tab index
        for idx, button in self.nav_buttons.items():
            button.clicked.connect(lambda checked, x=idx: self.change_tab(x))
        
        # Set initial tab after connections are made
        self.change_tab(initial_tab)
        
        # Adjust size after everything is set up
        self.adjustSize()
        self.setFixedSize(self.size())  # Prevent resizing
        
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
            url = "http://localhost:5100/api/caesar/encrypt"
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
                    msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
            url = "http://localhost:5100/api/caesar/decrypt"
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
                    msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
            url = "http://localhost:5100/api/cipher/encrypt"
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
                    msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        url = "http://localhost:5100/api/cipher/decrypt"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        url = "http://localhost:5100/api/playfair/creatematrix"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        url = "http://localhost:5100/api/playfair/encrypt"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        url = "http://localhost:5100/api/playfair/decrypt"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        url = "http://localhost:5100/api/rail_fence/encrypt"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
            msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            msg.setText("Error: "+str(e))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    
    def call_api_railfence_decrypt(self):
        url = "http://localhost:5100/api/rail_fence/decrypt"
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
                msg.setWindowFlags(msg.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
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
        
        
    def change_tab(self, tab_index):
        """Change to the specified tab and update button states"""
        # Only allow changing tabs if no tab is currently active
        if not hasattr(self, 'current_tab'):
            # First time setting a tab
            self.current_tab = tab_index
            
            # Define cipher names for each tab
            cipher_names = {
                0: "CAESAR CIPHER",
                1: "VIGENÈRE CIPHER",
                2: "RAIL FENCE CIPHER",
                3: "PLAYFAIR CIPHER"
            }
            
            if hasattr(self.ui, 'label'):  
                self.ui.label.setText(cipher_names.get(tab_index, "CIPHER ENCRYPT"))
            
            for idx, button in self.nav_buttons.items():
                button.setVisible(idx == tab_index)
                
            self.ui.stackedWidget_Main.setCurrentIndex(tab_index)
            
            self.adjustSize()
            
        # If trying to change to a different tab, show a message
        elif tab_index != self.current_tab:
            QMessageBox.information(
                self, 
                'Thông báo', 
                'Vui lòng đóng form hiện tại trước khi chuyển sang mã hóa khác!'
            )
        
    def closeEvent(self, event):
        """Handle window close event"""
        try:
            # Reset the UI state when closing
            if hasattr(self, 'current_tab'):
                # Show all navigation buttons
                for button in self.nav_buttons.values():
                    button.setVisible(True)
                # Reset the title
                if hasattr(self.ui, 'label'):
                    self.ui.label.setText("CIPHER ENCRYPT")
                # Clear the current tab
                del self.current_tab
                # Resize window to fit the content
                self.adjustSize()
            print("Application is closing...")
        except Exception as e:
            print(f"Error during close: {e}")
        finally:
            # Make sure to call the parent's closeEvent
            super().closeEvent(event)

if __name__ == "__main__":
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser(description='Cipher Application')
        parser.add_argument('--tab', type=int, default=0, 
                         help='Initial tab index (0: Caesar, 1: Vigenere, 2: RailFence, 3: PlayFair)')
        args = parser.parse_args()
        
        # Ensure tab index is within valid range
        initial_tab = max(0, min(3, args.tab))  # Clamp between 0 and 3
        print(f"Starting application with initial tab: {initial_tab}")
        
        app = QApplication(sys.argv)
        window = MyApp(initial_tab=initial_tab)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error in main: {str(e)}", file=sys.stderr)
        raise