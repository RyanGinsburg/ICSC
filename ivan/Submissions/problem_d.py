import sys
import random

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE

    import string

    def printGrid(grid):
        for arr in grid:
            printString = ""
            for elem in arr:
                printString += (elem + " ")
            print(printString)

    def randomBackwards(wordlist):
        for j in range(len(wordlist)):
            choice = random.randint(2, 3)
            if (choice == 2):
                reverse = ""
                for i in range(len(wordlist[j])-1, -1, -1):
                    reverse += wordlist[j][i]
                wordlist[j] = reverse
        return wordlist
    for i in range(len(words)):
        words[i] = words[i].lower()
    words = randomBackwards(words)

    grid =  [["|" for i in range(10)] for j in range(10)]

    def horizontal(grid, startPoint, word):
        i = startPoint[1]
        for w, char in enumerate(word):
            if grid[startPoint[0]][i] != "|" and grid[startPoint[0]][i] != word[w]: #THROW SAME KEY LOGIC HERE
                return False
            i += 1
        i = startPoint[1]
        for j, char in enumerate(word):
            grid[startPoint[0]][i] = word[j]
            i+=1 
        return True

    def vertical(grid, startPoint, word):
        i = startPoint[0]
        for w, char in enumerate(word):
            if grid[i][startPoint[1]] != "|" and grid[startPoint[0]][i] != word[w]: #THROW SAME KEY LOGIC HERE
                return False
            if i != 9:
                i += 1
        i = startPoint[0]
        for j, char in enumerate(word):
            grid[i][startPoint[1]] = word[j]
            i+=1 
        return True
    
    def diagonalDown(grid, startPoint, word):
        i = startPoint[0]
        l = startPoint[1]
        for w, char in enumerate(word):
            if grid[i][l] != "|" and grid[startPoint[0]][i] != word[w]: #THROW SAME KEY LOGIC HERE
                return False
            if i != 9:
                i += 1
            if l != 9:
                l += 1
        i = startPoint[0]
        l = startPoint[1]
        for j, char in enumerate(word):
            grid[i][l] = word[j]
            i+=1
            l+=1 
        return True
    
    def diagonalUp(grid, startPoint, word):
        i = startPoint[0]
        l = startPoint[1]
        for w, char in enumerate(word):
            if grid[i][l] != "|" and grid[startPoint[0]][i] != word[w]: #THROW SAME KEY LOGIC HERE
                return False
            if i > 0:
                i -= 1
            if l < 9:
                l += 1
        i = startPoint[0]
        l = startPoint[1]
        for j, char in enumerate(word):
            grid[i][l] = word[j]
            if i > 0:
                i -= 1
            l+=1 
        return True
    
    for word in words:
        num = random.randint(1, 4)
        match num:
            case 1:
                #print("Horizontal") 
                for i in range(100):
                    x = random.randint(0, 9)
                    y = random.randint(0, 10-len(word))
                    #print(f"{x}, {y}")
                    if(horizontal(grid, [x, y], word)):
                        found = True
                        break
                if found == False:
                    words.append(word)
                    continue
                #printGrid(grid)
            case 2:
                #print("Vertical")
                for i in range(100):
                    x = random.randint(0, 10-len(word))
                    y = random.randint(0, 9)
                    #print(f"{x}, {y}")
                    if(vertical(grid, [x, y], word)):
                        found = True
                        break
                if found == False:
                    words.append(word)
                    continue
                #printGrid(grid)
            case 3:
                #print("Diagonal Down")
                for i in range(100):
                    x = random.randint(0, 10-len(word))
                    y = random.randint(0, 10-len(word)) 
                    #print(f"{x}, {y}")
                    if(diagonalDown(grid, [x, y], word)):
                        found = True
                        break 
                if found == False:
                    words.append(word)
                    continue
            case 4:
                #print("Diagonal Up")
                for i in range(100):
                    x = random.randint(len(word)-1, 9)
                    y = random.randint(0, 10-len(word))
                    #print(f"{x}, {y}")
                    if(diagonalUp(grid, [x, y], word)):
                        found = True
                        break  
                if found == False:
                    words.append(word)
                    continue
                #printGrid(grid)
    def fillGaps(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(elem)
                if grid[i][j] == "|":
                    grid[i][j] = random.choice(string.ascii_letters).lower()
                    #print(grid[i][j])
    #printGrid(grid)
    #print()

    fillGaps(grid)
    #somehprintGrid(grid)
    return grid


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)