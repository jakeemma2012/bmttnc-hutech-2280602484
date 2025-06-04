from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railFence.raifence_cipher import RailFenceCipher
from cipher.playFair.playfair_cipher import PlayFairCipher
from cipher.tranposition.trans_cipher import TranspositionCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plain_text,key)
    return jsonify({'encrypted_text':encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt(encrypted_text,key)
    return jsonify({'decrypted_text':decrypted_text})

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

