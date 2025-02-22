### Functions Assignment
###1
##def subtract(a,b):
##    subtracted_list=[]
##    for item in a:
##        if item not in b:
##            subtracted_list.append(item)
##    return subtracted_list
##
##print(subtract([2,5,1,9,8],[9,8,7,6,3]))
###2a
##def isPrime(num):
##    if num<2:
##        return False
##    for i in range(2,int(num**0.5)+1):
##        if num%i==0:
##            return False
##    return True
##print(isPrime(5))
#####2b
##def primes(num):
##    primelist=[]
##    for i in range(2,num):
##        if isPrime(i):
##            primelist.append(i)
##    return primelist
##
##print(primes(15))
##3
##def nickel(num):
##    rounded=num*100
##    remainder=rounded%10
##    if remainder<5:
##        rounded-=remainder
##    elif remainder>5:
##        rounded+=(10-remainder)
##    return rounded/100
##print(nickel(3.82))
##4
##def bishopMoves(row,col):
##    moves=[]
##    for i in range(1,8):
##        if row+i<=8 and col+i<= 8:
##            moves.append((row+i,col+i))
##    for i in range(1,8):
##        if row+i<=8 and col-i>=1:
##            moves.append((row + i, col - i))
##    for i in range(1,8):
##        if row-i>=1 and col+i<=8:
##            moves.append((row-i,col+i))
##    for i in range(1,8):
##        if row-i>=1 and col-i>=1:
##            moves.append((row-i,col-i))
##
##    return moves
##print(bishopMoves(4, 4))

