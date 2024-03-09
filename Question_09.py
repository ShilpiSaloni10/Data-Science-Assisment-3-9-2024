str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if both strings are anagrams
if sorted(str1) == sorted(str2):
    print("Yes")
else:
    print("No")