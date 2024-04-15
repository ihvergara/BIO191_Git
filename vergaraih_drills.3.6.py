# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# # ================= Seatwork 3.6 =================
def print_square(size):
  # Print the filled square
  for i in range(size):
    for j in range(size):
      print("*", end="")
    print()

  # Print a space between the squares
  print()

  # Print the hollow square
  for i in range(size):
    # Print the top and bottom borders
    if i == 0 or i == size - 1:
      for j in range(size):
        print("*", end="")
    else:
      # Print the left and right borders
      print("*", end="")
      # Print spaces in the middle
      for j in range(size - 2):
        print(" ", end="")
      # Print the right border asterisk
      print("*", end="")
    print()

# Get the size of the squares from the user
size = int(input("\nEnter the size of the squares: "))

print_square(size)