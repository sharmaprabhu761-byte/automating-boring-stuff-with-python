'''def a():
    print('a() starts')
    b()
    c()
    print("a() returns")

def b():
    print("b( starts)")
    
    c()
    print("b ends here")

def c():
    print("c starts")
    print("c finishes")

def d():
    print("d starts")
    print("d ends")

a()

def spam():
    egg = 'local'
    spam2()
    return print(egg)

egg = 'global'
def spam2():
    egg = 'spam2 local'
    print(egg)
spam()
print(egg)
'''

'''def spam(divide):
    a =42/divide
    print(a)

spam(2)
spam(0)
'''
'''def cam(divide):
    try:
        return 42/divide
    except ZeroDivisionError:
        print("divided by zero")
'''

import time , sys

indent = 0
indent_i = True

try:
    while True:
        print('' * indent, end = '')
        print('********')
        time.sleep(0.1)

        if indent_i:
            indent =  indent + 1

            if indent == 20:
                indent_i = False

        else:
            indent = indent - 1
            if indent == 0:
                indent_i = True

except KeyboardInterrupt:
    sys.exit()
