# VERGARA, IVYANN ROMIJN H. 
# 2020-00761

# # ================= Seatwork 3.7 =================
# Get the size of the diamond from the user
diamond_size = int(input("\nEnter the size of the diamond: "))
def print_diamond(dsize):
  # Iterate through half the size (up)
  for i in range(size):
      print(" " * (size - i), "*" * (2*i + 1))
      # Iterate through half (down)
  for i in range(size - 2, -1, -1):
      print(" " * (size - i), "*" * (2*i + 1))



print_diamond(diamond_size)