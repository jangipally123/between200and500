a=5

for i in range(1,a+1):
    if i==1 or i==a:
        spaces = " " * (a-i)
        print(spaces + ("* " * i) + spaces)
    else:
        spaces = " " * (a-i)
        hollow_spaces = "  " * (i-2) 
        print(spaces + "* " + hollow_spaces + "* " + spaces)