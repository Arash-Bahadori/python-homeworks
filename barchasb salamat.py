# تشخیص خوراکی مناسب برای رژیم
a = input("G or Y or R:")
ac = (a.upper ())
alen = (len(ac))
if alen == 5 :
    rc = ac.count ("R")
    yc = ac.count ("Y")
    if rc >= 3 :
        print("nakhor lite")
    elif rc >= 2 and yc >= 2 :
        print("nakhor lite")
    elif rc == 5 or yc == 5 :
        print("nakhor lite")
    else :
        print("rahat bash lite")
else :
    print("just 5 words")