print("welcome")

with open("data.txt", "r") as file:
    data = file.read().splitlines()

print("Good count:", data.count("GOOD"))
print("Bad count:", data.count("BAD"))
print("Defect count:", data.count("DEFECT"))