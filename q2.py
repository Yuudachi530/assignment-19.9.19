TextFile = open("qb.txt", "r")
TextList = TextFile.readlines()
TextFile.close()

OutFile = open('OutFile.txt', 'w')

Name =  input("enter a name: ")

SpaceCounter = 0
PositionCounter = 0
SequenceCounter = 1

for line in TextList:
    while SpaceCounter != 2:
        if line[PositionCounter] == " ":
            SpaceCounter = SpaceCounter + 1
        PositionCounter = PositionCounter + 1
    if line[:PositionCounter - 1] != Name:
        line = '0' * (4 - len(str(SequenceCounter))) + str(SequenceCounter) + ' ' + line
        OutFile.write(line + '\n')
        SequenceCounter = SequenceCounter + 1
    PositionCounter = 0
    SpaceCounter = 0
        
OutFile.close()
        














