# VERGARA, IVYANN ROMIJN H. 
# 2020-00761


# ================= Seatwork 3.5 =================

# # Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Outer loop to iterate over the numbers
for i in numbers:
  # Inner loop to iterate over the numbers again
  for j in numbers:
    # Print the multiplication of i and j with a space after each number
    print(i * j, end=" ")
  # Print a new line after each row
  print()