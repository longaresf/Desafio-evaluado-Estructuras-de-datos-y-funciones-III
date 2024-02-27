
def validate(opcion, eleccion):
    while eleccion in opcion:
        return eleccion

if __name__ == '__main__':

    letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    eleccion = input('Ingresa una Opción: ').lower()
    while eleccion not in letras :
        eleccion = input('Opcion no válida, ingrese una de las opciones válidas de a-d: ').lower()

# Si se ingresan valores no validos a eleccion debe seguir preguntando
    numeros = ['0','1']
    #validate(numeros, eleccion)

    
