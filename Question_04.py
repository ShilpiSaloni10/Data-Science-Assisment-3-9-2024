# Input
n = int(input("Total number of monkey="))
k = int(input(" Number of eatable Bananas by Single Monkey="))
j = int(input(" Number of eatable Peanuts by single Monkey="))
m = int(input(" Total number of Bananas="))
p = int(input(" Total="))

# Calculation
total_bananas_eaten = (m + k - 1) // k
total_peanuts_eaten = (p + j - 1) // j
monkeys_eaten = min(total_bananas_eaten, total_peanuts_eaten)

# Output
if n >= monkeys_eaten:
    print("Number of Monkeys left on the tree:", n - monkeys_eaten)
else:
    print("INVALID")