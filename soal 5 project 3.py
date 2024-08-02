x = input("enter your nums with operation:").split()
xnum1 = int(x[0])
xop = x[1]
xnum2 = int(x[2])

match xop :
    case "+" :
        print(xnum1 + xnum2)
    case "*" :
        print(xnum1 * xnum2)
    case "/" :
        print(xnum1 / xnum2)
    case "-" :
        print(xnum1 - xnum2)
