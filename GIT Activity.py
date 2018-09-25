def make_sqaure(size):
    for x in range(size):
        for y in range(size):
            print ('*', end='')
        print("")
    return

def make_rectangle(length, width):
    for x in range(length):
        for y in range(width):
            print ('*', end='')
        print("")
    return

def make_triangle(size):
    ast = '*'
    dot = '.'
    for i in range(size):
        print(dot*(size-(i+1))+(ast*((2*(i+1))-1))+(dot*(size-(i+1))))
        
    return

def main():
    while(True):
        print('Hello, please enter what to print')
        print('1\tsquare')
        print('2\trectangle')
        print('3\ttriangle')
        shape = (int)(input('Input: '))
        if(shape == 1):
            size = (int)(input('Input size:'))
            make_sqaure(size)
        elif(shape == 2):
            length = (int)(input('Input length: '))
            width = (int)(input('Input width: '))
            make_rectangle(length, width)
        elif(shape == 3):
            size = (int)(input('Input size: '))
            make_triangle(size)

main()
