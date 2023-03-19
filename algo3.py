

def merge_lists(input_list):
    #If the size of the input is zero then return 
    if(len(input_list) == 0):
        print("Provided list was empty!")
        return
    #intialize result list
    result = []
    
    #while input_list is not empty keep on iterating 
    while len(input_list) != 0:
        index = 0
        array = 0
        
        #assign the first element of the first inner list to smallest_element
        smallest_element = input_list[0][0]
        
        #loop through the first element of all the inner list and find the smallest_element
        for inner_list in input_list:
            if smallest_element > inner_list[0]:
               #store array index that has the smallest element
               array = index
               #store smallest element
               smallest_element = inner_list[0]
            index += 1 
        
        #append the smallest element to result 
        result.append(smallest_element)

        #delete the element from the orginal list (input_list)
        del input_list[array][0]
    
        #if [] is found in input list, delete it. This means that all elements from inner list were deleted
        if [] in input_list: 
            input_list.remove([])
    return result 

def main():
    
    with open("in2C.txt", "r") as file:

        next(file)

        lines = file.readlines()

        lines = [line.strip() for line in lines]

        Array_1str = lines[0]
        Array_1list = eval(Array_1str.replace("Array_1 =", ""))

        Array_2str = lines[1]
        Array_2list = eval(Array_2str.replace("Array_2 =", ""))
        
        Array_3str = lines[2]
        Array_3list = eval(Array_3str.replace("Array_3 =", ""))

    print(merge_lists(Array_1list))
    print(merge_lists(Array_2list))
    print(merge_lists(Array_3list))
    

if __name__ == "__main__":
    main()    
