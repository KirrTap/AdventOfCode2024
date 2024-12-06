with open("list.txt", "r") as file:
    first_column = []
    second_column = []

    for line in file:
        numbers = line.split()
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1]))
       
first_column.sort()
second_column.sort()

result = 0
for number in first_column:
    counter = second_column.count(number)
    sum = number * counter
    result += sum
print("Result: ", result)    
