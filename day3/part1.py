"""
initial idea: 
search for substring "mul("
analyse following letters 
regexs probably but probs dont want to do it all with regexs


valid forms of mul:
mul(a,x)
mul(ab,xy)
mul(abc,xyz)

"""

testinput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# mul(2x4)

def isDigit(char):
    try:
        int(char)
        return True      
    except:
        return False


# print(isDigit("d"))



# while True:
try:
    startIndex = testinput.index("mul(", )
    firstInputIndexStart = startIndex + 4 
    if isDigit(testinput[firstInputIndexStart+1]): # check if character after mul( is an int


    elif testinput[firstInputIndexStart+1] == ",": # if its not, check if its a ","
        pass
    else: # else, chop input string here, as its not a valid instruction
        testinput = testinput[firstInputIndexStart:]

except:
    # break
    print("end")