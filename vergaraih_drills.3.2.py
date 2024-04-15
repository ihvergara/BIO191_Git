# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 3.2 =================
row_count = int(input("Enter an integer (row): "))
column_count = int(input("Enter an integer (count): "))
for k in range(0,row_count): #for each row
    for l in range(0,column_count): #for each position in the row

        if l%2 == 0: #j is an even number
            print("*", end="")
        else: #j is an odd number
            print("-", end="")

    print()