#CPSC 335 - Project 2 - Algorithm 1

def target_cities(source_arrayofcities, target_arrayofcities):
    source = source_arrayofcities[0]
    output_order = []
    output_array = []
    index = 0

    for start in source:
        for target in target_arrayofcities:
            if(len(source) - index < len(target)):
                continue

            substring = source[index:index+len(target)]
            
            if target == substring:
                output_order.append(index)
                output_array.append(target)
        
        index = index + 1

    return output_order, output_array

                
def main():

    f = open("in2a.txt", "r")
   
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
