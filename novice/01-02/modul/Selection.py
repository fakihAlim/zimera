def sort(numbers):
    for i in range(4):
        min_pos = i
        for j in range(i, 5):
            if numbers[j] < numbers[min_pos]:
                min_pos = j
        temp = numbers[i]
        numbers[i] = numbers[min_pos]
        numbers[min_pos] = temp
