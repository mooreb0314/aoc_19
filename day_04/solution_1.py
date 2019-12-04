count = 0
for i in range(109165, 576723):

    double = False
    increasing = False
    double_count = False

    if sorted(list(set([int(d) for d in str(i)]))) != sorted([int(d) for d in str(i)]):
        double = True

    if [int(d) for d in str(i)] == sorted([int(d) for d in str(i)]):
        increasing = True

    if double and increasing:
        count+=1


print(count)


