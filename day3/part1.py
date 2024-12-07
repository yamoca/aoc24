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

def isDigit(char):
    try:
        int(char)
        return True      
    except:
        return False


print(isDigit("d"))