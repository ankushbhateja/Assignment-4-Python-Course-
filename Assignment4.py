# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


def openFile():
    try:
        with open('sample.txt', 'w') as sampleTextFile:
            sampleTextFile.write('This is the sample text file\nIt contains multiple lines')
    
        with open('sample.txt', 'r+') as sampleTextFile:
            print(sampleTextFile.read())    
            
    except FileNotFoundError:
        print("The file 'sample.txt' was not found")


openFile()


# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


enteredData = input("Enter text to write to the file : ")

def writeData():
    try:
        with open("sample.txt",'w') as outputTextFile:
            outputTextFile.write(enteredData + '\n')
            print("Data successfully written to sample.txt")
        appendData= input("Enter additional to add in sample.txt : ")
        with open("sample.txt",'a') as outputTextFile:
            outputTextFile.write(appendData)
        print("Data successfully appended")
        
        print("Final content of sample.txt")
        with open("sample.txt",'r') as outputTextFile:
           print(outputTextFile.read())
    except FileNotFoundError:
        print("sample.txt not found")


writeData()
