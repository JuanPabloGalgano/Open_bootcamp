import pandas as pd
import csv

accion = input('Indique que quiere hacer: Buscar por nombre(N), Agregar persona(A)').lower()

if accion == 'a':
      
      persona  = {
            "nombre": input("Ingrese su nombre: "),
            "telefono": int(input("Ingrese su telefono: ")),    
      }

      with open("Open_bootcamp\\datos.csv", mode="a", newline='') as datos:      
      
            nombres_campos = ["nombre", "telefono"]      
            writer = csv.DictWriter(datos, fieldnames=nombres_campos)                
            writer.writerow(persona)
 
     
if accion == 'n':
      nombre_buscado = input("Ingrese el nombre de la persona buscada: ")
      with open('Open_bootcamp\\datos.csv') as datos:
            leedor = csv.reader(datos)
            for fila in leedor:
                  if fila[0] == nombre_buscado:
                        telefono = fila[1]
                        print(f'El telefono de {nombre_buscado} es {telefono}')
                        break
            else:
                  print(f"No se encontro ningun telefono relacionado con el nombre {nombre_buscado}")
                  
if accion != 'n' and accion != 'a':
      print('No papa, no estaba esa opcion, chau')                  
