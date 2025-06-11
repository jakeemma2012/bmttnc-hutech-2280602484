from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Hàm tạo cặp khóa client từ thông số DH
def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

# Hàm tính khóa chia sẻ từ private key của client và public key của server
def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    # Load server's public key từ file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

    # Lấy thông số DH từ public key của server
    parameters = server_public_key.parameters()

    # Tạo khóa client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính khóa chia sẻ
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret (raw):", shared_secret.hex())

    # Nếu muốn: Dùng PBKDF2 để biến shared secret thành AES key
    salt = b'static_salt_value'  # Trong thực tế nên random + gửi kèm!
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256-bit AES key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    aes_key = kdf.derive(shared_secret)
    print("Derived AES Key:", aes_key.hex())

if __name__ == "__main__":
    main()
