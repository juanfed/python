# contraseñas iguales

password = "0707MT60FZxSp35";
passwordIgual = False;
contador = 0;

while passwordIgual == False and contador < 3:
    password2 = input("Ingrese la contraseña :");
    if password == password2 :
        passwordIgual = True
    else:
        passwordIgual = False
        contador = contador + 1;
    # if contador >= 3:
    #     passwordIgual = True


if contador >= 3 :
    print("Ha agotado las oportunidades para ingresar por medio de la contraseña, te hemos bloqueado");
else:
    print("Las contraseña ingresada conincide con la registrada, puede ingresar")