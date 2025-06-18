from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from flask import jsonify
from cipher.railFence import RailFenceCipher
from cipher.playFair import PlayFairCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    plainText = request.form.get("inputPlainText")
    key = int(request.form.get("inputKey"))
    caesarCipher = CaesarCipher()
    encryptedText = caesarCipher.encrypt_text(plainText, key)
    return render_template("caesar.html", encryptedText=encryptedText)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    encryptedText = request.form.get("inputEncryptedText")
    key = int(request.form.get("inputKey"))
    caesarCipher = CaesarCipher()
    decryptedText = caesarCipher.decrypt_text(encryptedText, key)
    return render_template("caesar.html", decryptedText=decryptedText)

@app.route("/rail_fence")
def rail_fence():
    return render_template("railFence.html")

@app.route("/encrypt_rail_fence", methods=["POST"])
def encrypt_rail_fence():
    plainText = request.form.get("inputPlainText")
    key = int(request.form.get("inputKey"))
    rail_fence_cipher = RailFenceCipher()
    encryptedText = rail_fence_cipher.rai_fence_encrypt(plainText, key)
    return render_template("railFence.html", encryptedText=encryptedText)

@app.route("/decrypt_rail_fence", methods=["POST"])
def decrypt_rail_fence():
    encryptedText = request.form.get("inputEncryptedText")
    key = int(request.form.get("inputKey"))
    rail_fence_cipher = RailFenceCipher()
    decryptedText = rail_fence_cipher.rai_fence_decrypt(encryptedText, key)
    return render_template("railFence.html", decryptedText=decryptedText)

@app.route("/playfair")
def playfair():
    return render_template("playFair.html")

@app.route("/playfair_key", methods=["POST"])
def playfair_key():
    key = request.form.get("inputMatrix")
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return render_template("playFair.html", playfair_matrix=playfair_matrix)

@app.route("/encrypt_playfair", methods=["POST"])
def encrypt_playfair():
    plainText = request.form.get("inputPlainText")
    key = request.form.get("inputKey")
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encryptedText = playfair_cipher.playfair_encrypt(plainText, playfair_matrix)
    return render_template("playFair.html", encryptedText=encryptedText)

@app.route("/decrypt_playfair", methods=["POST"])
def decrypt_playfair():
    encryptedText = request.form.get("inputEncryptedText")
    key = request.form.get("inputKey")
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decryptedText = playfair_cipher.playfair_decrypt(encryptedText, playfair_matrix)
    return render_template("playFair.html", decryptedText=decryptedText)


@app.route("/transposition")
def transposition():
    return render_template("tranposition.html")

@app.route("/encrypt_transposition", methods=["POST"])
def encrypt_transposition():
    plainText = request.form.get("inputPlainText")
    key = int(request.form.get("inputKey"))
    transposition_cipher = TranspositionCipher()
    encryptedText = transposition_cipher.encrypt(plainText, key)
    return render_template("tranposition.html", encryptedText=encryptedText)

@app.route("/decrypt_transposition", methods=["POST"])
def decrypt_transposition():
    encryptedText = request.form.get("inputEncryptedText")
    key = int(request.form.get("inputKey"))
    transposition_cipher = TranspositionCipher()
    decryptedText = transposition_cipher.decrypt(encryptedText, key)
    return render_template("tranposition.html", decryptedText=decryptedText)

@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/encrypt_vigenere", methods=["POST"])
def encrypt_vigenere():
    plainText = request.form.get("inputPlainText")
    key = request.form.get("inputKey")
    vigenere_cipher = VigenereCipher()
    encryptedText = vigenere_cipher.encrypt_text(plainText, key)
    return render_template("vigenere.html", encryptedText=encryptedText)

@app.route("/decrypt_vigenere", methods=["POST"])
def decrypt_vigenere():
    encryptedText = request.form.get("inputEncryptedText")
    key = request.form.get("inputKey")
    vigenere_cipher = VigenereCipher()
    decryptedText = vigenere_cipher.decrypt_text(encryptedText, key)
    return render_template("vigenere.html", decryptedText=decryptedText)

if __name__ == "__main__":
    app.run(debug=True)
