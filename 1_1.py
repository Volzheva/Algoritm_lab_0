f = open("1_1_input.txt")
m = open("1_1_output.txt", "w")
num = f.read()
a, b = num.split()
m.write(str(int(a)+int(b)))

f.close()
m.close()
