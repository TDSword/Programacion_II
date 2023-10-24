abc = ["a", "b", "c", "d"]
ABC = ["A", "B", "C", "D"]
num = ["1", "2", "3", "4", "5"]
ñandú = ["ñ", "#", "+", "-", "*"]

def contrasenia(palabra):

    m = "\n- Una letra minúscula"
    j = "\n- Una letra mayúscula"
    k = "\n- Un número"
    o = "\n- Un caracter especial"

    for i in palabra:
        if i in abc:
            m = ""
        elif i in ABC:
            j = ""
        elif i in num:
            k = ""
        elif i in ñandú:
            o = ""

    if m== "" and j== "" and k== "" and o == "":
        return palabra
    else:
        print("Falta comlir con las siguientes condiciones: ", m, j, k, o)
        respuesta = input("Por favor ingrese la contraseña nuevamente: ")
        return contrasenia(respuesta)

perfil = contrasenia(input("Ingrese la contraseña: "))
print("Su contraseña es:", perfil)