print("bienvenue dans la calculatrice de x2lx.dev")

premier = float(input("premier nombre : "))
methode = input("quelle methode voulez vous utiliser , (*, /, +, -) : ")
deuxieme = float(input("deuxième nombre : "))

if methode == "*":
    print(premier * deuxieme)
    
elif methode == "/":
      print(premier / deuxieme)
      
elif methode == "+":
      print(premier + deuxieme)
      
elif methode == "-":
      print(premier - deuxieme)
      
      
else:
    print("methode non reconnue")
