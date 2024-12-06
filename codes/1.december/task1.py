with open("list.txt", "r") as file:
    first_column = []
    second_column = []

    for line in file:
        numbers = line.split()
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1]))
       
first_column.sort()
second_column.sort()

index = 0
result = 0
while index < len(second_column):
    number = abs(first_column[index] - second_column[index])
    result = result + number
    index = index + 1

print("Result: ", result)
