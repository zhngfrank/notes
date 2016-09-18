#division normally operates in floating point, to truncate and get integer division use
#// e.g.

print ("3//5 = ", 3//5, "whereas\n3/5 =", 3/5)  

#when python is used as a calculator, e.g. through python3 command terminal, the last saved answer
#is stored in the variable "_" (underscore). same as 2nd ans on TI calculator
print('\n','_'*200,'\n')

##round(number, decimalplaces)
print ("round(75.0386, 2)= ", round(75.0386, 2))

#single and double quotes are interchangable, used them as needed to make text readable, e.g. 
#if you need quotes in a print statement. 

#you can also use \ as an escape sequence to the same effect, this means that the following 
#is a character and not something else, e.g. \" will be printed, and will not terminate a print 
#statement


print('\n', '_'*200,'\n')

print ("the dog said \"hello\"")

#use r before quotations to force the string to be raw characters. \will be ignored

print('\n', '_'*200,'\n')

print (r"the directory is \user\new, see, no newline")

#make multiline strings with triple quotes. no need to repeat print statements, or use new lines(\n) 
#most of the time. python automatically adds a newline, but you can circumvent this by putting a \
#at the end of the line to prevent the EOL"

print('\n', '_'*200,'\n')

print ("""my name is frank\
 nice to meet you
this is on the next line
and this is on the third line\
 but this isn't""")
 
 
#strings can be glued together using the "+" sign or repeated using "*"

print('\n', '_'*200,'\n')

print("my name is frank" + ", nice to meet you" *3)

#side by side string literals can glued together without a + sign, just put em together
#print("yo", " fam")

print('\n', '_'*200,'\n')

#strings are stored c style, e.g. an array of characters. can be accessed via indices
var = "word"
print("word[0] =", var[0],"\nand word[-3] =", var[-3], " (reads from the right)")

print('\n', '_'*200,'\n')

#can slice indices, basically a to statement within the array
print("word[:2] hi word[2:] = " , var[:2], " hi ", var[2:])
print("notice that the first is included and end excluded")

#despite being c string they are immutable, you can't set var[4] = 'j'

print('\n', '_'*200,'\n')

print("len(var)= ", len(var))

#lists in python are like typename vectors, can store any data type and can be added to the end
#format is same as array

print('\n', '_'*200,'\n')

squares = [1, 4, 9, 16]

print("squares[0] = ", squares[0])

#can add to the end using squares.append(literal)
#can be sliced as well. makes it a hell of a lot easier to iterate through them
#creates a shallow copy >> ram usage issues?

print('\n', '_'*200,'\n')

if 3<5 :
	print ("do, elif or else won't print")
elif 4>3:
	print("this is the same as else if")
else:
	print ('this is else')

test_boolean_logic1 = 0;
test_boolean_logic2 = 1;

if test_boolean_logic1:
	print("this is 0, should not have printed")
elif test_boolean_logic2:
	print("this should have printed, elif with 1 works!")


print('\n', '_'*200,'\n')

#for loop is significantly less explicit
for w in var:
	print(w, len(var))

print("so the control variable w, once printed, corresponds to var[i], where i is internal and not",
"explicit")

####

print('\n', '_'*200,'\n', sep='')







