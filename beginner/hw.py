import sys
# message = """Edd Ed n Eddy 
# was a good cartoon
# in the 90's"""
# print(len(message))
# print(message[len(message) - 1])
# print(message[0:len(message) - 1])
# print(message[0:5])
# print(message[:3])
# print(message.lower())
# print(message.count('z'))
# print(message.find('Eddy'))

# start = "hello"
# end = "world"

# message = start + ' ' + end + '.'
# message = '{}, {}. Welcome'.format(start, end)
# message = f'{start}, {end.upper()}. Welcome'
# print(help(str))

# if __name__ == '__main__':

# print ("This is the name of the script: ", sys.argv[0])
# print ("Number of arguments: ", len(sys.argv))
# print ("The arguments are: " , str(sys.argv))

#bubblesort 
if __name__ == '__main__':
    
    n = len(sys.argv)
    cout = 0
    print(n)
    for i in range(n):
        cout += 1
        for j in range(0, n-i-1):
            if sys.argv[j] > sys.argv[j + 1]:
                sys.argv[j], sys.argv[j + 1] = sys.argv[j + 1], sys.argv[j]
                j = 0
                i = 0
    # i = 0
    # while i < n:
              
    #     if sys.argv[i] > sys.argv[i + 1]:
    #         sys.argv[i], sys.argv[i + 1] = sys.argv[i + 1], sys.argv[i]
    #         i = 0
    #     else:
    #         i += 1
    #         if i + 1 == n:
    #             break
    print(cout)        
    print(sys.argv)
    