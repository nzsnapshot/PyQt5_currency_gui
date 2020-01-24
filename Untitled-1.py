#this program should accept integers between 1 and 12 (inclusive) a, turn all integers greater than 10 into 10
# and put them in a list

my_list =[]

while True:
    ven1 = int(input("Enter an integer between 1 and 12 or press q to quit."))
    if ven1 == "q":
        break

    if ven1 > 10:
        ven1 = 10
        my_list.append(ven1)
        break

print(ven1)