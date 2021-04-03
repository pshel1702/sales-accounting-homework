"""Generate sales report showing total melons each salesperson sold."""

# #Initiate two empty lists
# salespeople = []
# melons_sold = []

# f = open('sales-report.txt') #open the file sales-report.txt
# for line in f:
# """Print the sales report showing total melons each salesperson sold.""" #Good to write a docstring to show what a function does
#     line = line.rstrip() #Strips the blank space at the end of the line
#     entries = line.split('|') #Splits each line of the file on the '|' character

#     salesperson = entries[0] #Saves the first element, or the element at index[0] in entries as the salesperson
#     melons = int(entries[2]) #Converts the element at index[2] in entries to int type, and then saves it to melon

#     if salesperson in salespeople: #Checks if the current salesperson has already been added to the salespeople list
#         position = salespeople.index(salesperson) #If yes, then saves the index of the current salesperson from the salespeople list to position

#         melons_sold[position] += melons #Adds one to the number of melons sold at that position indicating one more sale counted
#     else:
#         salespeople.append(salesperson) #If salesperson is not found, append the salesperson to the salespeople list
#         melons_sold.append(melons) #Append the number of melons sold to the melons_sold list


# for i in range(len(salespeople)): #Print the melons sold by looping through both lists
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#instead of using two lists and keeping track of positions, a dictionary can be used
#Every person can be a key, and the number of melons sold can be the value

#Initiate an empty dictionary

melons_report = {}
f = open('sales-report.txt')

for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in melons_report:
        melons_report[salesperson] += melons
    else:
        melons_report[salesperson] = melons

for key,value in melons_report.items():
    print(f'{key} sold {value} melons')

