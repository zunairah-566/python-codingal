def add(bill,tip): 
    total= bill*(1 + 0.01*tip)
    
    return total

bill= input("enter the bill")

tip= input("enter the tip percentage")

print(f"the answer is {add(bill,tip)}, its the correct answer")



