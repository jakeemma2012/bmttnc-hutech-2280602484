class RailFenceCipher:
    def __init__(self):
        pass
    def rai_fence_encrypt(self,plain_text,num_rails)->str:
        rail = [[]for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rail[rail_index].append(char)
            if rail_index ==0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        encrypted_text = "".join(["".join(row) for row in rail])
        return encrypted_text
    
    def rai_fence_decrypt(self,encrypted_text,num_rails)->str:
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(encrypted_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        rails_content = []
        start = 0
        for length in rail_lengths:
            rails_content.append(list(encrypted_text[start : start + length]))
            start += length
        plaint_text_chars = [] 
        rail_index = 0 
        direction = 1 
        
        for _ in range(len(encrypted_text)):
            plaint_text_chars.append(rails_content[rail_index].pop(0))
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return "".join(plaint_text_chars)