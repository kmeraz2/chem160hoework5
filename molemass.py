names=["H","C","N","O","P","S"]
masses=[1.00794,12.0107,14.00674,15.9994,30.973761,32.066]
Dict1={}
for i in range(len(names)):
    Dict1[names[i]]=masses[i]
print(Dict1)
def molemass(formula):
    mass=0
    for a in formula:
        mass+=Dict1[a]
    print(mass)
molemass("CHHHH")