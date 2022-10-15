
arr = [5,9,2,4,5,7,4,19,3]        # create list/ array   
#i = arr[0]
lst1 = []                        # 3 empty list to store the number of trial zero 
lst2 = []
lst3 = []
for i in arr:                    # consider 1 hash function 
    hash1 = (5*i +3) % 32        # you can take random values or take input 
    #print(hash1)

    def dectobin(hash1):                    # conversion of the value we get after applying hash into its corresponding binary 
        return "{0:b}".format(int(hash1))

    if __name__ == '__main__':
        b = dectobin(hash1)
        print(b)

        def countlastzeros(b):            # here we are going to count tail zeros 
            b = b[::-1]                   # traverse from back using -1 
            zero = 0 

            for i in range(len(b)):       # calculate within range of tail zero 
                if (b[i] == '0'):
                    zero += 1

                else :
                     break 
            return zero

        count = countlastzeros(b)
        
        print(count)                  # print number of tail zeros 
        lst1.append(count)            # enter all the number of tail zeros we got from iteration into list 
print(lst1)

max1 = max(lst1)                     # finding maximum from that list 


for i in arr:                       # similarly for second hash 
    hash2 = (3*i +1) % 32
    #print(hash2)

    def dectobin(hash1):
        return "{0:b}".format(int(hash2))

    if __name__ == '__main__':
        b = dectobin(hash2)
        print(b)

        def countlastzeros(b):
            b = b[::-1]
            zero = 0 

            for i in range(len(b)):
                if (b[i] == '0'):
                    zero += 1

                else :
                     break 
            return zero

        count = countlastzeros(b)
        
        print(count)
        lst2.append(count)
print(lst2)

max2 = max(lst2)


for i in arr:                            # similarly for third hash 
    hash3 = (2*i +4) 
    #print(hash3)

    def dectobin(hash3):
        return "{0:b}".format(int(hash3))

    if __name__ == '__main__':
        b = dectobin(hash3)
        print(b)

        def countlastzeros(b):
            b = b[::-1]
            zero = 0 

            for i in range(len(b)):
                if (b[i] == '0'):
                    zero += 1

                else :
                     break 
            return zero

        count = countlastzeros(b)
        
        print(count)
        lst3.append(count)
print(lst3)

max3 = max(lst3)


print(max1)                # print max number from list 1 
print(max2)                # print max number from list 2 
print(max3)                # print max number from list 3 
                    #lets find the average of unique values 
r = pow(2,max1) + pow(2, max2) + pow(2, max3)    # find 2^R of each where R is the max count of zero 

x = r/3         # find its average (in our case its 3 )

print(x)        # and boom you have successfully implemented faljolet martin algorithm 
       
