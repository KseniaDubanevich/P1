#Data types: 
#-String 
#-Integer 
#-Float (734_529.678) 
#-List [value1,valu2]
#-Dictionary {Key1: "Value1",Key2:"Value2}
#-Boolean (True, False)
#
#Even though the underscore is there to make the large number more readable, because there is a decimal point it is still a Float. If you printed the number in your code, it would be stripped down to 734529.678 
#Booleans are either True or False, they don't have quotation marks around them, otherwise it would turn them into a String. So it should be bool = False 



#Program for print length of your name 
num_char = len(input("What is your name?")) 

#Converting num_char variable into string data type 
new_num_char = str(num_char) 
print("Your name has " + new_num_char + " characters.") 