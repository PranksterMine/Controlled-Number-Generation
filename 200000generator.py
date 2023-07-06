#variable and initial value
seconds = 1

#loop to generate numbers
while seconds > 0:
	print(seconds)
	seconds = seconds + 1
	
	#once loop has reached 200,000, the loop will be stopped
	if seconds == 200000:
		break