def count_increase(filename):
    with open(filename, "r") as file:
        final = 0
        for line in file:
            column = line.split() 
            column = [int(x) for x in column] 
            counter = len(column) 
            pocitadlo = 0
            
            while pocitadlo < counter -1: 
                if column[pocitadlo] < column[pocitadlo + 1]:
                    result = abs(column[pocitadlo] - column[pocitadlo + 1])
                    if result >= 1 and result <=3:
                        pocitadlo +=1
                    else:
                        break    
                else:
                    break
            if pocitadlo == counter -1:
                final +=1
    return final            

def count_decrease(filename):
    with open(filename, "r") as file:
        final = 0
        for line in file:
            column = line.split()
            column = [int(x) for x in column]  
            counter = len(column) 
            pocitadlo = 0
            
            while pocitadlo < counter -1: 
                if column[pocitadlo] > column[pocitadlo + 1]:
                    result = abs(column[pocitadlo] - column[pocitadlo + 1])
                    if result >= 1 and result <=3:
                        pocitadlo +=1
                    else:
                        break
                else:
                    break
            if pocitadlo == counter -1:
                final +=1
    return final

filename = "list.txt"       
increase = count_increase(filename)
decrease = count_decrease(filename)
result = increase + decrease
print(result)   