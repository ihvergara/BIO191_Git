# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 3.1 =================
asterisk_count = int(input("Enter an integer: "))
cnt=1
while cnt<=asterisk_count:
    for j in range(0,cnt):
        print("*", end="")
        
    if (j != cnt):
        print(" ", end="\n")
    cnt = cnt + 1
print() 