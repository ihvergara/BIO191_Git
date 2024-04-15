# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 2.2 =================

eligible = True
age2= int(input("Please enter your age: "))
if age2 < 35:
    eligible=False

natural_born=input("Are you a natural born citizen of the U.S. (yes/no)?")
if natural_born == "no":
    eligible=False

years_residing=int(input("How many years have you resided in the U.S.?"))
if years_residing <14:
    eligible =False

if eligible:
    print("You can run for president of \n")
else:
    print("You can't run for president\n")