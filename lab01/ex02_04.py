j=[]
# duyệt các số từ 2000 - 3200, ktra xem i có chia hết cho 7 và không là bội số của 5 không 
for i in range(2000, 3201):
    if((i % 7 == 0) and (i % 5 != 0)):
        j.append(str(i))
print(','.join(j))