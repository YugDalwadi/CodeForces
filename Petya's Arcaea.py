testCases = int(input())

for i in range(testCases):

    squares = int(input())
    string = input()
    splitString = list(string)

    if(squares==1):
        string = "B"
        print(string)

    if(squares==splitString.count("?")):
        splitString[0]= "B"
        string= "".join(splitString)

    while "?" in string:
        string= string.replace("?R", "BR")
        string= string.replace("R?", "RB")
        string= string.replace("B?", "BR")
        string= string.replace("?B", "RB")

        if("?" not in string):
            print(string)      
        
  


