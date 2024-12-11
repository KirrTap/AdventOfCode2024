def count_increase(filename):
    with open(filename, "r") as file:
        final = 0
        for line in file:
            column = line.split() 
            column = [int(x) for x in column] 
            counter = len(column) 
            pocitadlo = 0
            

            while pocitadlo < counter :
                i = column.pop(pocitadlo)
                while_pocitadlo = 0
                while while_pocitadlo < counter -2:
                    result = abs(column[while_pocitadlo] - column[while_pocitadlo + 1]) 
                    if (result >= 1 and result <=3) and (column[while_pocitadlo] < column[while_pocitadlo + 1]):
                        while_pocitadlo+=1
                    else:
                        break 
                if while_pocitadlo == counter - 2:
                    final += 1
                    break
                else:      
                    column.insert(pocitadlo,i)
                    pocitadlo +=1                    
    return final            

def count_decrease(filename):
    with open(filename, "r") as file:
        final = 0
        for line in file:
            column = line.split() 
            column = [int(x) for x in column] 
            counter = len(column) 
            pocitadlo = 0
            

            while pocitadlo < counter :
                i = column.pop(pocitadlo)
                while_pocitadlo = 0
                while while_pocitadlo < counter -2:
                    result = abs(column[while_pocitadlo] - column[while_pocitadlo + 1]) 
                    if (result >= 1 and result <=3) and (column[while_pocitadlo] > column[while_pocitadlo + 1]):
                        while_pocitadlo+=1
                    else:
                        break 
                if while_pocitadlo == counter - 2:
                    final += 1
                    break
                else:      
                    column.insert(pocitadlo,i)
                    pocitadlo +=1                    
    return final
filename = "list.txt"       
increase = count_increase(filename)
decrease = count_decrease(filename)
result = increase + decrease
print(result)  