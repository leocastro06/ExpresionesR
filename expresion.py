import re 

expresion ='A123bar$&%'
patron = re.compile("[A-Z]{1}[0-9]{3}[a-z]+\W{3}")

if (patron.search(expresion)):
     resul = patron.search(expresion).group(0)
else: 
     print("No pertenece!!...")
     exit()  

if (resul == expresion):   
      print("Pertenece a esta expresión regular...")
