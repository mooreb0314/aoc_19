count = 0
options = []
for i in range(109165, 576723):

    digit_array = [int(d) for d in str(i)]

    double = False
    increasing = False
    double_count = False

    # Find if duplicates exists
    if sorted(list(set(digit_array))) != sorted(digit_array):
        double = True

    # Ensure increasing
    if digit_array == sorted(digit_array):
        increasing = True

    # Ensure at least a group of exactly two matching digits
    for d in str(i):
        digit_count = 0
        for j in str(i): 
            if j == d: 
                digit_count += 1
        if digit_count == 2:
            double_count =  True

    if double and increasing and double_count:
        count+=1

print(count)



