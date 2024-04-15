# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 2.1 =================
age= int(input("What is your age? "))
fish_license=input("Do you have a fishing license in MN (yes/no)? ")
parent_fish_license=input("Does your parent have a fishing license (yes/no)? ")

if age <= 15 and parent_fish_license=='no':
    print("You are illegal to fish in MN. Your parent does not have license")
elif age >= 16 and fish_license=='no':
    print("You are illegal to fish in MN. You do not have license")
elif age >= 16 and fish_license=='yes':
    print("You are legal to fish in MN.")
if age <= 15 and parent_fish_license=='yes':
    print("You are legal to fish in MN. Your parent has a license\n")