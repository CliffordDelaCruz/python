#blocks.py
blocks = int(input("Enter the number of blocks: "))

height = 0
total_blocks = 0
for block in range(blocks):
    total_blocks += block + 1
    if total_blocks <= blocks:
        height += 1
    else:
        break

print("The height of the pyramid:", height)