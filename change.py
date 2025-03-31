def change():
    expense = 23.75
    money = 100
    vuelto= money-expense
    pesos= int(vuelto)
    centavos= int((vuelto-pesos)*100)
    print (f' Ingresar gasto:\n{expense}nDniero recibido\n{money}\n\nVuelto\n\nPesos:\n {pesos}\nCentavos:\n{centavos}')
    
    
