##Given two strings, a and b, return the result of putting them together in the order abba,
## e.g. "Hi" and "Bye" returns "HiByeByeHi". Make sure all test cases below will pass. 

def make_abba(a,b):
	print (a + b + b + a) 

make_abba('Hi', 'Bye')
make_abba('Yo','Alice')
make_abba('What','Up')
make_abba('aaa','bbb')
make_abba('x','y')
make_abba('x','')
make_abba('','y')
make_abba('Bo','Ya')
make_abba('Ya','Ya')