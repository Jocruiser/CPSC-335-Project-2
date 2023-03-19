def target_cities(source_arrayofcities, target_arrayofcities):
    #store the string containing all the cities  
    source = source_arrayofcities[0]
    output_order = []
    output_array = []
    index = 0
    #loop through each character of the source string
    for start in source:
        #loop through the list that contains the cities we're looking for
        for target in target_arrayofcities:
            #if the remaining characters is the source is less than the length of the target city skip to the next iteration
            if(len(source) - index < len(target)):
                continue
            
            #create a substring from the source string
            substring = source[index:index+len(target)]
            
            #if target city is equal to the substring that means we found the city we're looking for 
            if target == substring:
                output_order.append(index)
                output_array.append(target)
        
        index = index + 1

    return output_order, output_array

                
def main():

    f = open("in2a.txt", "r")
    next(f) 
    line = f.readline()
    
    while(line):

        source_str = line.split('"')[1::2]
    
        line = f.readline()
        target_str = line.split('"')[1::2]
        
        print(target_cities(source_str, target_str))
        
        line = f.readline()

    f.close()

if __name__ == "__main__":
    main()
