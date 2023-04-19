paciente = {

}
def generarId():
    nuevaId = ((len(paciente.keys()) - 1) + 1) - 1 if len(paciente.keys()) > 0 else 0
    return nuevaId
def guardar(param):
    paciente[generarId()] = {
        "nombre":param['nombre'],
        "edad":param['edad'],
        "peso":param['peso'],
        "sexo":param['sexo']
    }
def mostrar():
    print("Nombre | Edad | peso | Sexo")
    print(" ".join([paciente[x]["nombre"] + " " +str(paciente[x]["edad"]) + " " + str(paciente[x]["peso"])+ " " +paciente[x]["sexo"] for x in paciente]) )
def menu():
    print("1.Nuevo Paciente\n2.Editar datos de un paciente\n3.Borrar datos de un paciente\4Listar todos los pacientes")
opc = ""
while opc != "S":
    menu()
    opc1 = input()
    if opc1 == "1":
        print('ingrese su nombre')
        nombre = input()
        print('ingrese su edad')
        edad = int(input())
        print('ingrese su peso')
        peso = float(input())
        print("Cual es su sexo F/M?")
        sexo = input()
        if sexo == "M" or sexo == "F":
            guardar({
                "nombre":nombre,
                "edad":edad,
                "peso":peso,
                "sexo":sexo
                })
            continue
        else:
            print("error")
    if opc1 == "2":
        mostrar()

