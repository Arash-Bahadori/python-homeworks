numbers = (input("enter 5 nums:")).split(",")
new_nums = list(map(int,numbers))
total_sum = sum(new_nums)
if total_sum % 2 == 0 :
    nn = int(input("enter new num:"))
    newt = new_nums.append(nn)
    newtotal = sum (new_nums)
    print(newtotal)
else :
    new_nums.pop(3)
    print(new_nums)