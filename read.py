#Open the file to process
file = open("./a_example.in", "r")

#Read all the lines in the file
lines = file.readlines()

#Get all the information from the first line and split it
#into its different components, converting them to integers
numbers_string = lines[0].split()
numbers_int = [int(x) for x in numbers_string]

#Close the file and print the numbers
file.close()
print(numbers_int)