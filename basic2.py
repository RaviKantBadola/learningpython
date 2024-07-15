operand_1 = int(input("Enter operand1:"))
operand_2 = int(input("Enter operand1:"))
operator=input("Enter a operator(+,-,*,/)")

if operator=="+":
    print(operand_1 + operand_2)
elif operator=='-':
    print(operand_1-operand_2)
elif operator=="*":
    print(operand_1*operand_2)
elif operator=="/":
    print(operand_1/operand_2)
else:
    print("None")

print("Thank you")

