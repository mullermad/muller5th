print("WELLCOME TO MULLER CALCULATOR\n")


def addition(n1, n2):
    sum = n1 + n2
    return sum


def subtraction(n1, n2):
    sub = n1 - n2
    return sub


def multiplication(n1, n2):
    mul = n1 * n2
    return mul


def division(n1, n2):
    div = n1 / n2
    return div
operation={"+":addition,
               "-":subtraction,
               "*":multiplication,
               "/":division,
    }
def calculator():
    num1=float(input("what is the first number?:"))

    for i in operation:
        print(i)


    continuee=True
    while continuee:

        choice=input("choose the operation ?\n")
       

        num2=float(input("what is the second number?:"))

        calculation_function=operation[choice]

        answer=calculation_function(num1,num2)

        print(f"{num1} {choice} {num2} = {answer}")
        imput = input("type 'y' to continue or 'n' to renew or 'f; to exit \n")
        if imput=="y":
            num1=answer

        elif imput=="n":
            continuee=False
            calculator()
        elif imput=="f":
            continuee = False
            print("GOODBYE")
calculator()