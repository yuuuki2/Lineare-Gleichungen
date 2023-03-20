import matplotlib.pyplot as plt

funktion = input("Geben Sie eine Funktion (y = a * x + b) ein: ")

# Split the input string into separate variables
y, rest = funktion.split(" = ")
a, rest = rest.split(" * ")
x, b = rest.split(" + ")

def definitionsmenge():
    d_menge = [-10,-9,-8,-7,-6,-5,-4,-3,-2,1,0,1,2,3,4,5,6,7,8,9,10]

    return d_menge

def wertemenge(a,b,d_menge):
    #new_y = a * x + b
    w_menge = []
    for x in d_menge:
       new_y = int(a) * x + int(b)
       w_menge.append(new_y) 


    return w_menge





def main():
    d_menge = definitionsmenge()
    w_menge = wertemenge(a,b,d_menge)

    print(w_menge)
    
    plt.plot(d_menge,w_menge)
    plt.xlabel("Definitionsmenge")
    plt.ylabel("Wertemenge")
    plt.show()
    
main()
