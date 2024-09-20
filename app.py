from cal_fun import do_add,do_subtract
from multiply import multiply
def main():
    print('welcome to calculator')
    print('''1.addition
             2.substraction
             3.multiplication''')
             
    
    choice = input('enter your choice:')
    num1 = int(input('enter first number:'))
    num2 = int(input('enter second number:'))
    if choice=='1':
        result=do_add(num1,num2)
    elif choice=='2':
        result=do_subtract(num1,num2)
    elif choice=='3':
        result=multiply(num1,num2)

    print("Result:",result)

if __name__=="__main__":
    main()
        