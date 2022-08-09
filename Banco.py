
banco_datos= {"matias2":"df123","luca9":"plp766","martina":"mil453"}

accion = str(input("desea tomar alguna accion con su cuenta? S/N"))

ingreso1 = str(input("(a) para Ingresar, (b) para Registrarse, (d) para Salir, (e) para Cambiar contraseña "))

while accion == "S":
  if ingreso1 == "a":
    usuario1 = input("ingrese su usuario ")
    contraseña1 = input("ingrese su contraseña")
    for x in banco_datos:
      if x == usuario1 and banco_datos[x] == contraseña1:
        print("ingreso exitoso")
        ingreso2 = input("(c) para Cerrar sesion, (d) para Salir, (e) para Cambiar contraseña")
        if ingreso2 == "c":
          print("Sesion cerrada con exito")
          break
        if ingreso2 == "d":
          print("usted ha salido con exito")
          break
        if ingreso2 == "e":
          ingreso3 = input("contraseña nueva: ")
          banco_datos[x] = ingreso3
  if ingreso1 == "b":
    usuario2 = input("ingrese su nuevo usuario ")
    contraseña2 =input("ingrese su nueva contraseña")
    banco_datos[usuario2] = contraseña2
    ingreso2 = input("(c) para Cerrar sesion, (d) para Salir, (e) para Cambiar contraseña")
    if ingreso2 == "c":
      print("Sesion cerrada con exito")
      break
    if ingreso2 == "d":
      print("usted ha salido con exito")
      break
    if ingreso2 == "e":
      ingreso3 = input("contraseña nueva: ")
      banco_datos[x] = ingreso3
  if ingreso1 == "d":
    break
  if ingreso1 == "e":
    ingreso3 = input("contraseña nueva: ")
    banco_datos[x] = ingreso3
  ingreso1 = input("(a) para Ingresar, (b) para Registrarse, (d) para Salir, (e) para Cambiar contraseña ")



#ingreso1 = str(input("(a) para Ingresar, (b) para Registrarse, (c) para Cerrar sesion, (d) para Salir, (e) para Cambiar contraseña"))