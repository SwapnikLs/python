ini_str = "ababababa"
sub_str = 'ababa'
# Count count of substrings using count
def Countofoccurrences(ini_str,sub_str):
    
	count = 0
	start = 0
	while start < len(ini_str):
		pos = ini_str.find(sub_str, start)
        
        

		if pos != -1:
			# If a substring is present, move 'start' to
			# the next position from start of the substring
			start = pos + 1 

			# Increment the count
			count += 1
		else:
			# If no further substring is present
			break
	# return the value of count
	return count
# Printing result
print("Number of substrings", Countofoccurrences(ini_str,sub_str))
