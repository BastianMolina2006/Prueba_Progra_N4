registro=[]
generos_validos=["F","M"]
def ing():
    nombre=input("Ingrese el nombre del usuario")
    if any(p["nombre"]==nombre for p in registro):
        print("nombre ya existente.")
        return
    genero=input("Ingrese genero: ")
    if genero not in generos_validos:
        print("generos validos son F & M.")
        return
    registro.append({
        "nombre":nombre,
        "contraseña"
        "genero":genero
        })
    print("El usuario se registró con éxito")
def buscarus():
    nombre=input("Ingrese nombre a buscar: ")
    for p in registro:
        if p["nombre"]==nombre:
            print(f"la persona es: {p['genero']} y su contraseña es: {p['contraseña']}")
            return
    print("La persona no se encuentra.")
def annn():
    nombre=input("Ingrese usuario a buscar: ")
    for i, p in enumerate(registro):
        if p["nombre"]==nombre:
            del registro[i]
            print("Usuario eliminado con éxito!")
            return
    print("No se pudo eliminar el usuario.")
def main():
    while True:
        print("###MENU PRINCIPAL###")
        print("1. Ingresar usuario: ")
        print("2. Buscar usuario: ")
        print("3. Eliminar usuario: ")
        print("4. Salir del programa.")
        opc=input("Ingrese opción: ")
        if opc==1:
            ing()
        elif opc==2:
            buscarus()
        elif opc==3:
            annn()
        elif opc==4:
            print("Saldrá del programa.")
            break
        else:
            print("Seleccione una opción válida.")
if __name__=="__main__":
    main()