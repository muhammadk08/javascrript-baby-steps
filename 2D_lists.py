##########
##########from random import *
##########from pprint import *
#############1
############def connect4(grid):
############    # Check horizontal
############    for row in grid:
############        for col in range(len(row) - 3):
############            if row[col] !=0 and row[col]==row[col+1]==row[col+2]==row[col+3]:
############                print("horizontal")
############                return True
############    # Check vertical
############    for col in range(7):
############        for row in range(3):
############            if grid[row][col] !=0 and grid[row][col]==grid[row+1][col]==grid[row+2][col]==grid[row+3][col]:
############                print("vertical")
############                return True
############    # Check diagonal (down-right)
############    for row in range(3):
############        for col in range(4):
############            if grid[row][col] !=0 and grid[row][col]==grid[row+1][col+1]==grid[row+2][col+2]==grid[row+3][col+3]:
############                print("diagonal (down-right)")
############                return True
############    # Check diagonal (up-right)
############    for row in range(3, 6):
############        for col in range(4):
############            if grid[row][col] !=0 and grid[row][col]==grid[row-1][col+1]==grid[row-2][col+2]==grid[row-3][col+3]:
############                print("diagonal (up-right))
############                return True
############    return False
############grid = [
############    [1, 1, 1, 1, 0, 0, 0],
############    [0, 0, 0, 0, 0, 0, 0],
############    [0, 0, 0, 0, 0, 0, 0],
############    [0, 0, 0, 0, 0, 0, 0],
############    [0, 0, 0, 0, 0, 0, 0],
############    [0, 0, 0, 0, 0, 0, 0]
############]
############
############print(connect4(grid))
############2
############def checkerboard(row, col, myList=[], count=0):
############    for i in range(row):
############        myList.append([])  # Add a new row
############        for j in range(col):
############            if count % 2 == 0:  # Alternate between '.' and '*'
############                myList[i].append('.')
############            else:
############                myList[i].append('*')
############            count += 1  # add count after adding each element
############        count = (count + 1) % 2 #checks if count is 0 or 1 and then covert to back to the opposite
############    return myList
############pprint(checkerboard(6, 8))
##############3
#############input file for reading
##############output file for writing
############input_file=open('farfar.txt', 'r')
############input_file_lines=open('farfar.txt', 'r')
############output_file=open('scrambled.txt', 'w')
############# Get all individual words in a list
############words_list=input_file.read().split() 
############lines_list=input_file_lines.readlines()
############line_index=0
############for word in words_list:
############    # Split the word by commas
############    split_words=word.split(',')
############    # Loop through each split word and scramble the middle letters if eligible
############    for w in split_words:
############        if len(w) > 3:
############            # Scramble the middle part of the word 
############            middle=w[1:-1]
############            middle=list(middle)  # Convert middle part to a list for shuffling
############            shuffle(middle)
############            middle=''.join(middle)  # Rejoin the shuffled middle
############            scrambled_word=w.replace(w[1:-1], middle)  # Replace the middle part    
############            # Check if the word is at the end of the line
############            if w + '\n' in lines_list[line_index] or w + ' \n' in lines_list[line_index]:
############                output_file.write(scrambled_word + '\n')  # Add word with newline at the end
############                line_index+=1  # Move to the next line
############            else:
############                output_file.write(scrambled_word + ' ')  # Add word with space between words
############        else:
############            # If the word can't be scrambled (less than or equal to 3 letters), write it unchanged
############            output_file.write(w + ' ')
############# Close all files after processing
############output_file.close()
############input_file.close()
############input_file_lines.close()
