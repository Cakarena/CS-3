##Given a string, return the string made of its first two chars, 
##so the String "Hello" yields "He". If the string is shorter than length 2, 
##return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


def first_two(str):
	print (str[0:2])


first_two('Hello')
first_two('abcdefg')
first_two('ab')
first_two('a') 
first_two('')
first_two('kitten')
first_two('hi')
first_two('hiya')
