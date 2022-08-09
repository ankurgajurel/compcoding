#not done for all test cases beacuse not all test cases have passed

a = [1, 2, 3, 4, 5]

def hmm(a):
    max = 0
    min = 0

    for i in a:
        min += i

    for i in range(5):
        x = i
        sum = 0
        for j in range(4):
            sum += a[x]
            x += 1
            if x > len(a) - 1:
                x = 0
        
        if sum > max:
            max = sum
        elif sum < min:
            min = sum
        
    print(min-(a[1] - a[0]), max)

print(hmm(a))