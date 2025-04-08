try:
    num1,num2 = eval(input("Enter two numbers separated by comma"))
    result = num1 /num2
    print('Result',result)
except ZeroDivisionError:
    print("Division error")   
except SyntaxError:
     print("Syntax error")   
except: 
    print("Wrong input")   
else:
    print("no error")    
finally:
    print("All good")   
       
       