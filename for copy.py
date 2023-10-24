abc = ["a","b","c","d"]
ABC = ["A","B","C","D"]
num = [1,2,3,4,5]
ñandú = ["ñ","#","+","-","*"]
def contrasenia(palabra):
    m = False
    j = False
    k = False
    o = False
    for i in palabra:
        if i == abc:
            m = True
        elif i == ABC:
            j = True
        elif i == num:
            k = True
        elif i == ñandú:
            o = True
    if (m== True, j== True, k== True and o == True):
        return palabra
    else:
        respuesta = str(input("Por favor ingrese la contraseña nuevamente"))
        return contrasenia(respuesta)

perf = contrasenia(str(input("Ingrese la contraceña: ")))

print("Su contra es:", perf)