##Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
	result =""
	for char in (str):
		result += char + char
	print(result)

double_char("The")
double_char("AAbb")
double_char("Hi-There")
double_char("Word")
double_char("!!")
double_char('')
double_char('a')
double_char('.')
double_char('as')
