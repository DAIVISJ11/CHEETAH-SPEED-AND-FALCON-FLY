print("Welcome to odd Hunt")
print("Find the hidden numbers using XOR")

#Part 1
A = 7
B = 7

print("\n Identity and equality")
print("Same numbers disappear")
print("7 ^ 7 = ",A ^ A)

print(" Zero does nothing")
print("7 ^ 0 = ",A ^ 0)

print("If the numbers are the same")
print("7 ^ 7 = ",(A ^ B) == 0)

print("\n -------------------------------\n")

# Pair destroyer
print("Pair destroyer")
print("XOR cancellation")

ARR = [ 1 , 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 3, 1]

print(" Numbers: ", ARR)
print("Matching pairs will disappear...")

result = 0

for n in ARR:
    result ^= n
print("THE survivor is:", result)
print("\n -------------------------------\n")