import hashlib

def convertir_contra(password):
      
    if len(password) < 6 or len(password) > 12:
        raise ValueError('La contraseña debe tener entre 6 y 12 caracteres.')
    
    m = hashlib.md5() #El md5 genera un hash de 32 caracteres. siempre genera el mismo para la misma palabra
    m.update(password.encode('utf-8'))
    return m.hexdigest()

print(convertir_contra("contraseña"))