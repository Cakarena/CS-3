##http://data.gov.au/dataset/international-trade-import-price-index/resource/8a1a8406-a7bc-42f7-86b4-7a9c9c95b174
##Go to www.data.gov.au or https://data.nsw.gov.au/, get any small dataset,
## convert it to text file and write a program to just do a very simple read of each record
## in the file, some level of processing of your choice(does not need to be complicated) 
##and output a new file.
## Do not forget to put descriptive comments in the code. 
##Let the trainer know about the name of the program in GitHub. 


## Downloaded Excel file: ##http://data.gov.au/dataset/international-trade-import-price-index/resource/8a1a8406-a7bc-42f7-86b4-7a9c9c95b174
## converted to text-deliminated txt file

fhand = open ('dataset.txt', 'w')
## For the first part I did the following that I've now ##:

##for line in fhand:
	##if line.startswith ('2'):
		##print(line) ## output herehttps://www.screencast.com/t/0wtH1hEq

## For the second part, output a new file, I did the following:
line1 = "This is a Checkpoint 3, exercise 6 thingo"
fhand.write(line1)
fhand.close()

## Change of dataset.txt became this https://www.screencast.com/t/5JIZ9957rbw see dataset.cvs.txt in this respository for original appearance.
