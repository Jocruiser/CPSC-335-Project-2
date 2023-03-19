def encode(myStr:str):
    # edge cases in case user enters an empty or 1 letter string
    if(len(myStr) == 0):
        print("No string entered")
        return
    elif (len(myStr) == 1):
        print(myStr)
        return

    #Variables used for the algorithm
    count          = 0        # The count for how many times a letter appears
    currentLetter  = None     # letter of current index and runs through array
    previousLetter = myStr[0] # letter of the previous index. Intialized to first letter for comparison
    result         = str()    # the results of algorithm. Starts empty but more is appended on


    for letter in myStr: # runs through ever letter within the string
        currentLetter = letter # refresh what the current letter is

        if (currentLetter != previousLetter): # compares current to previous if the same continues the chain until discrepency is found
            if (count != 1): # we only want to add the count if count > 1 otherwise if it is 1 it is ignored
                result = result + str(count) #append on the count to result
            
            result = result + previousLetter # append the letter to result
            count = 0 # reset count for next series of 

        previousLetter = currentLetter # Move previous letter up
        count += 1 # increment
    # end of for letter in myStr
   
    # does the comparison one more time otherwise the last letter/chain gets cut off
    if(count != 1):
        result = result + str(count)
    result = result + previousLetter
    
    print(result)
        



def main():
    encode("heloooooooo there")
    encode("choosemeeky and tuition-free")
    encode("ddd")
    encode("")
    encode("e")
    

if __name__ == "__main__":
    main()    
