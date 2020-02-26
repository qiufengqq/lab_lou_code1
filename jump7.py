#jump7
n = 1
#print('start while form 1 to 100 jump7')
#start while()
while n <= 100:
#jump x7
    if n%10 == 7:
        n=n+1
        continue
    elif n%7 == 0:
    #jump 7*x
        n=n+1
#        print('jump 7*x')
        continue
    elif n//10 == 7:
    #jump x7
        n=n+1
 #       print('jump 7x')
        continue
    else:
    #-----print the intiger
        print(n)
        n=n+1
