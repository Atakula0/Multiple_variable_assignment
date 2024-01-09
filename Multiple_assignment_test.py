
#assigning multiple variables using one line, compared to using several lines

var_a = "variable a"
var_b = 50
var_c = True

var_a, var_b, var_c = "variable a", 50, True

print(var_a)
print(var_c)
print(var_b)

Spongebob = 30
Patrick = 30
Sandy = 30
Squidward = True

print(Spongebob)
print(Patrick)
print(Sandy)
print("Is Squidward insufferable: "+str(Squidward))

#now, using one single line

Spongebob, Sandy, Patrick, Squidward = 30, 30, 30, True
