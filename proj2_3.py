#CPSC 335 - Project 2 - Algorithm 3

def mergeLists(lst):
    if(len(lst)==0):
        print("Provided list was empty!")
        return
    
    targetarray = lst[0]
    
    result = []
    while (len(lst) != 0):
        for array in lst:
            if(len(array) > 0):
                if(array[0] < targetarray[0]):
                    targetarray = array
        
        result.append(targetarray[0])
        targetarray.pop(0)
        if(len(targetarray) == 0):
            lst.remove(targetarray)
        targetarray = [999999]


    print(result)

def main():
    Array_1  =[[2, 5, 9, 21],
	       [-1, 0, 2],
	       [-10, 81, 121],
	       [4, 6, 12, 20, 150]]
    Array_2  =[[10, 17, 18, 21, 29],
	       [-3, 0, 3, 7, 8, 11],
	       [81, 88, 121, 131],
	       [9, 11, 12, 19, 29]]
    Array_3  =[ [-4, -2, 0, 2, 7],
	       [4, 6, 12, 14],
	       [10, 15, 25],
	       [5, 6, 10, 20, 24] ]
    mergeLists(Array_1)
    mergeLists(Array_2)
    mergeLists(Array_3)
    

if __name__ == "__main__":
    main()    
