# manejo de print un poco mas avanzado

edad = 23;  #poner valor explicitamente es llamado quemar valores, no es muy comun generalmente lo ingresa el usuario.
edadSister = 18;

print("la diferencia de edad es: ", edad - edadSister, "years"); # primera forma de contatener variables y mensajes
print("la diferencia es de: ", str(edad - edadSister), "years" ); # tambien puedo convertilo aca mismo de numero a texto


print(f"la direfencia entre las edades es de: {edad - edadSister}"); # coloco una f ante de todo y asi puedo meter variables dentro de llaver

result = f"hay una diferencia de edad de: {edad - edadSister} years";

print(result);


