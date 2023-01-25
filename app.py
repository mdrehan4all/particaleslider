import re
# Initialising string
s = 'ababababa'
 
 
# Count count of substrings using re.findall
res= len(re.findall('(?=(a))', s))
 
print("Number of substrings", res)