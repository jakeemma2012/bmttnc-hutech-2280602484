import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '1111111111111110'  # 16-bit end marker
    data_index = 0
    
    for row in range(height):
        for col in range(width):
            if data_index >= len(binary_message):
                break
                
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Replace LSB of each color channel with message bit
                    pixel[color_channel] = (pixel[color_channel] & 0xFE) | int(binary_message[data_index])
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))
        
        if data_index >= len(binary_message):
            break
    
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print(f"Encoded image saved to {encoded_image_path}")
    return encoded_image_path

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()