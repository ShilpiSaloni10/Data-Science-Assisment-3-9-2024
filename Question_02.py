
total_stairs = int(input("Enter the number of stairs: "))
steps_per_move = int(input("Enter the number of steps: "))

#Calculate total steps taken

total_steps = (total_stairs + steps_per_move - 1) // steps_per_move

print("Total steps taken:", total_steps)