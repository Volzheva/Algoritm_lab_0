f = open("1_2_input.txt")
m = open("1_2_output.txt", "w")
num = f.read()
a, b = num.split()
m.write(str(int(a)+int(b)**2))

f.close()
m.close()
