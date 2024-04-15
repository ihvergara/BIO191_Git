# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# ================= Seatwork 2.3 =================
integer1= int(input("Please enter an integer: "))
integer2= int(input("Please enter another integer: "))
integer3= int(input("Please enter a third integer: "))
largest=0 #placeholder
# Check if any of the numbers are odd
if integer1 % 2 != 0:
  largest = integer1
elif integer2 % 2 != 0:
  largest = integer2
elif integer3 % 2 != 0:
  largest = integer3
else:
  print("None of the numbers are odd")
  exit()  # Exit the program if no odd numbers are found

# Find the largest among the odd numbers
if integer1 % 2 != 0 and integer1 > largest:
  largest = integer1
if integer2 % 2 != 0 and integer2 > largest:
  largest = integer2
if integer3 % 2 != 0 and integer3 > largest:
  largest = integer3

# Print the result
print(f"{largest} is the greatest")
