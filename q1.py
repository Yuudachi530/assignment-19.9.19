TextFile = open("qb.txt", "r")
TextList = TextFile.readlines()
TextFile.close()

Character = input("enter a character: ")

OutFile = open("OutFile.txt", "w")

for line in TextList:
    PositionCounter = 0
    while PositionCounter != len(line):
        if line[PositionCounter] == ' ':
            line = line[:PositionCounter] + Character + line[PositionCounter + 1:]
        PositionCounter = PositionCounter + 1
    OutFile.write(line + '\n')
        

OutFile.close()
        
    

    
    
        
        
        
           
            
            
            
    
    
        
    