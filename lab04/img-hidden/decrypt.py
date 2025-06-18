import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    end_marker = '1111111111111110' 
    
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
                
                if len(binary_message) >= 16 and binary_message[-16:] == end_marker:
                    binary_message = binary_message[:-16]  
                    
                    message = ""
                    for i in range(0, len(binary_message) - (len(binary_message) % 8), 8):
                        byte = binary_message[i:i+8]
                        if len(byte) == 8: 
                            message += chr(int(byte, 2))
                    return message
    
    return "No message found or message not properly terminated"

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        sys.exit(1)
    
    encoded_image_path = sys.argv[1]
    try:
        message = decode_image(encoded_image_path)
        print("Decoded message:", message)
    except Exception as e:
        print(f"Error decoding image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()