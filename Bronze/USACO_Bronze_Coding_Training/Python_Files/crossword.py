def split(word):
    return list(word)
coordinates = []
clueCount = 0
x, y = input().split()
rows = int(x)
columns = int(y)
getHashtagLine = []
for i in range (0,columns+1):
    getHashtagLine.append("#")
crossword = []
crossword.append(getHashtagLine)
for i in range (1,rows+1):
    a = "#" + input()

    crossword.append(split(a))
#print (rows)
#print (columns)
for i in range (rows+1):
    for j in range (columns+1):
        #print (crossword[i][j])
        if crossword[i][j] == ".":
            if i + 2 <= rows and j + 2 <=  columns :
                if crossword[i][j-1] == "#" and crossword[i][j+1] == "." and crossword[i][j+2] == "." and crossword[i-1][j] == "#" and crossword[i+1][j] == "." and crossword[i+2][j] == "." :
                    crossword[i][j] = "!"
                    clueCount += 1
                    coordinates.append([i,j])
                    #print ([i,j,1])
                elif crossword[i][j-1] == "#" and crossword[i][j+1] == "." and crossword[i][j+2] == ".":
                    crossword[i][j] = "!"
                    clueCount += 1
                    coordinates.append([i,j])
                    #print ([i,j,2])
                elif crossword[i-1][j] == "#" and crossword[i+1][j] == "." and crossword[i+2][j] == "." :
                    crossword[i][j] = "!"
                    clueCount += 1
                    coordinates.append([i,j])
                    #print ([i,j,3])
            elif j+2 <= columns :
                if crossword[i][j-1] == "#" and crossword[i][j+1] == "." and crossword[i][j+2] == ".":
                    crossword[i][j] = "!"
                    clueCount += 1
                    coordinates.append([i,j])
                    #print ([i,j,4])
            elif i + 2 <= rows :
                if crossword[i-1][j] == "#" and crossword[i+1][j] == "." and crossword[i+2][j] == "." :
                    crossword[i][j] = "!"
                    clueCount += 1
                    coordinates.append([i,j])
                    #print ([i,j,5])
print (clueCount)
coordinates.sort()
for i in range (len(coordinates)):
    print (coordinates[i][0],end=' ')
    print (coordinates[i][1])
#print (crossword)
