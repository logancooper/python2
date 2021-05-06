#VARIABLES
num_list = []
numberCapture = 0

#FUNCTIONS
#Sum of numbers
def sumList(mylist):
    printDivider()
    total = 0
    for number in mylist:
        total += number
    print("The total of your list is: " + str(total))

#Largest Number
def largestInList(mylist):
    printDivider()
    largest = mylist[0]
    for number in mylist:
        if(number > largest):
            largest = number
    print("The largest number of your list is: " + str(largest))

#Smallest Number
def smallestInList(mylist):
    printDivider()
    smallest = 0
    for number in mylist:
        if(number < smallest):
            smallest = number
    print("The smallest number of your list is: " + str(smallest))

#Even Numbers
def evenNumbersInList(mylist):
    printDivider()
    evenList = []
    for number in mylist:
        if(number % 2 == 0):
            evenList.append(number)
    print("The even numbers of your list are: ")
    print(*evenList)

#Positive Numbers
def posNumbersInList(mylist):
    printDivider()
    posNums = []
    for number in mylist:
        if(number > 0):
            posNums.append(number)
    print("The positive numbers of your list are: ")
    print(*posNums)


#Positive Numbers II
def positiveNumbersAlt(mylist):
    printDivider()
    newList = []
    for number in mylist:
        if(number > 0):
            newList.append(number)
    print("The positive numbers of your list (in a new list) are: ")
    print(*newList)


def captureNumbers():
    numberCapture = input("Please enter a number: ")
    if numberCapture:
        num_list.append(int(numberCapture))
        captureNumbers()

def functionChoice():
    printDivider()
    myInput = input("Please choose a function: \nEnter 1 to sum the list\nEnter 2 to find the largest number in the list\nEnter 3 to find the smallest number in the list\nEnter 4 to find the even numbers in the list\nEnter 5 to find the postitive numbers in the list\nEnter 6 to create a new list of the positive numbers in the list\n")
    
    if myInput:
        myInput = int(myInput)
        if(myInput == 1):
            sumList(num_list)
            functionChoice()
        elif(myInput == 2):
            largestInList(num_list)
            functionChoice()
        elif(myInput == 3):
            smallestInList(num_list)
            functionChoice()
        elif(myInput == 4):
            evenNumbersInList(num_list)
            functionChoice()
        elif(myInput == 5):
            posNumbersInList(num_list)
            functionChoice()
        elif(myInput == 6):
            positiveNumbersAlt(num_list)
            functionChoice()
        else:
            print("Your input was invalid!")
            functionChoice()

def printDivider():
    print("-----------------------------------------------")
        

#USER INPUT
print("Please enter a series of numbers to add to the list. When you are finished, press enter to continue.")
captureNumbers()
functionChoice()



