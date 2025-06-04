# hàm ktra số nhị phân có chia hết cho 5 hay không 
def chia_het_cho_5(so_nhi_phan):
    # chuyển số nhị phân sang thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    #ktra số thập phân có chia hết cho 5 không 
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
    
# Nhập chuỗi nhị phân 
chuoi_so_nhi_phan = input("Nhập chuổi số nhị phân (Phân tách bởi dấu phẩy): ")
# tách chuỗi thành số nhị phân và ktra so chia hết cho 5 
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [num for num in so_nhi_phan_list if chia_het_cho_5 (num)]

#in ra                                            
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5: ", ket_qua)
else:
    print("không có số nhị phân chia hết cho 5 trong chuỗi đã nhập.")