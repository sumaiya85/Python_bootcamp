#string methods are
#isalpha
#isdigit
#isalam(alpha numeric)
#isupper 
#islower
#check with converting in lower & upper case
#title case
#swap case

inp="haaallo worRldz"
print(inp.upper()) #prints in upper case

print(inp.lower()) #prints in lower case

print(inp.capitalize()) #prints first word capitalize

print(inp.title()) #prints capital in starting words(Hello World)

print(inp.swapcase()) #swaps upper and lower case

print(inp.strip()) #inp:"        hello    world   "(trims the spaces )

print(inp.replace('a','z')) # replace the values

print(inp.split()) #shows each separate

print(inp.split('a'))# aplits after particular value

#these checks true or false
inp="12"
print(inp.isalpha()) # without spaces then only it gives true

print(inp.isnumeric()) #only numbers

print(inp.isalnum()) # without spaces it gives true orelse false

print(inp.isascii())

print(inp.islower())#everything is in lower case

print(inp.isupper())# everything should in upper case

print(inp.isnumeric()) #numbers

print(inp.isdigit()) #only digits 0-9