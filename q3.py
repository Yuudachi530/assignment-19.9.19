TextFile = open("sequence qb.txt", 'r')
TextList = TextFile.readlines()
TextFile.close()

number = input("enter sequence number: ")

counter = 0

for line in TextList:
    if line[:4] == number:
        print(line)
        counter = True

if counter != True:
    print("not found")
    
    