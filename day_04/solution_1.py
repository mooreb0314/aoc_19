count = 0
for i in range(109165, 576723):

    digit_array = [int(d) for d in str(i)]
    double = False
    increasing = False

    # Find if duplicates exists
    if len(list(set(digit_array))) != len(digit_array):
        double = True

    # Ensure increasing
    if digit_array == sorted(digit_array):
        increasing = True

    if double and increasing:
        count+=1


print(count)


