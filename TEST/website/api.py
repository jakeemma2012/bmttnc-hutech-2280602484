from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import sys
import platform
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railFence.raifence_cipher import RailFenceCipher
from cipher.playFair.playfair_cipher import PlayFairCipher

app = Flask(__name__)
CORS(app) 
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORM_POPUP_DIR = os.path.join(BASE_DIR, 'form_popup')

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_create_matrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'matrix':playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text,playfair_matrix)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(encrypted_text,playfair_matrix)
    return jsonify({'decrypted_text':decrypted_text})

@app.route('/api/rail_fence/encrypt', methods=['POST'])
def rail_fence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    num_rails = int(data['key'])
    encrypted_text = rail_fence_cipher.rai_fence_encrypt(plain_text,num_rails)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/rail_fence/decrypt', methods=['POST'])
def rail_fence_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    num_rails = int(data['key'])
    decrypted_text = rail_fence_cipher.rai_fence_decrypt(encrypted_text,num_rails)
    return jsonify({'decrypted_text':decrypted_text})



@app.route('/api/cipher/encrypt', methods=['POST'])
def cipher_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt_text(plain_text,key)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/cipher/decrypt', methods=['POST'])
def cipher_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt_text(encrypted_text,key)
    return jsonify({'decrypted_text':decrypted_text})


@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    print(data)
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text,key)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(encrypted_text,key)
    return jsonify({'decrypted_text':decrypted_text})

@app.route('/run_command', methods=['POST'])
def run_command():
    data = request.json
    command = data.get('command')
    
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    
    try:
        # Thay đổi thư mục làm việc đến thư mục form_popup
        os.chdir(FORM_POPUP_DIR)
        
        # In thông tin debug
        print(f"Executing command: {command}")
        print(f"Current directory: {os.getcwd()}")
        
        # Tạo đối tượng Popen với các tham số phù hợp cho từng hệ điều hành
        if platform.system() == 'Windows':
            process = subprocess.Popen(
                command,
                shell=True,
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.getcwd()  # Đảm bảo chạy trong đúng thư mục
            )
        else:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.getcwd()  # Đảm bảo chạy trong đúng thư mục
            )
        
        # Đọc lỗi nếu có
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            return jsonify({
                'error': f'Command failed with return code {process.returncode}',
                'stderr': stderr,
                'stdout': stdout,
                'command': command,
                'cwd': os.getcwd()
            }), 500
        
        # Không cần đợi process kết thúc
        return jsonify({
            'success': True, 
            'pid': process.pid,
            'command': command,
            'cwd': os.getcwd()
        })
        
    except Exception as e:
        error_msg = str(e)
        print(f"Error in run_command: {error_msg}")
        return jsonify({
            'error': error_msg,
            'cwd': os.getcwd(),
            'command': command,
            'type': type(e).__name__
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)

