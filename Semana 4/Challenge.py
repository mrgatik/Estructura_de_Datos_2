class Nodo:
  def __init__(self, nombre=None, apellido=None, telefono=None, direccion=None, izq=None, der=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.izq = izquierda
        self.der = derecha
        
  def __str__(self):
    return "%s %s" %(self.nombre, apellido, telefono, direccion)

class aBin:
  def __init__(self):
    self.raiz = None
  
  def agregar(self, elemento):
    if self.raiz == None:
    self.raiz = elemento
      else:
      aux = self.raiz
      padre = none
      while aux !=None:
        padre = aux
        if int(elemen.apellido) >= int(aux.apellido):
          aux =aux.der
          else:
          aux = aux.izq
          if int(elemento.apellido)>= int (padre.apellido):
          padre.der = elemento
            else:
            padre.izq = elemento
  
  def nombre(self, elemento):
    if elemento!= None:
    print(elemento)
      self.nombre(elemento.izq)
      self.nombre(elemento.der)

  def apellido(self, elemento):
    if elemento != None:
    print(elemento)
      self.apellido(elemento.izq)
      self.apellido(elemento.der)
        print(elemento)

  def telefono(self, elemento):
    print(elemento)
    self.telefono(elemento.izq)
      print(elemento)
        self.telefono(elemento.der)

  def direccion(self, elemento):
    print(elemento)
    self.direccion(elemento.izq)
      print(elemento)
      self.direccion(elemento.der)

  def getRaiz(self):
    return self.raiz

if __name__ == "__main__":
    ab = aBin()
    while(True):
        print(" Menu ")
        print("1. Agregar")
        print("2. Nombre")
        print("3. Apellido")
        print("4. Telefono")
        print("5. Direccion")
              num = input("ingrese la opcion")

        if num == "1":
          nombre = input("ingrese el nombre: ")
          cedula = input("ingrese el apellido: ")
          telefono = input("ingrese el telefono")
          direccion = input("ingrese la direccion:")
          nod = Nodo(nombre, apellido, telefono, direccion)
          ab.agregar(nod)

        elif num == "2":
          print("imprimiendo por nombre")
          ab.nombre(ab.getRaiz())

        elif num == "3":
          print("imprimiendo por apellido")
          ab.apellido(ab.getRaiz())

        elif num ==  "4":
          print("imprimiendo por telefono")
          ab.telefono(ab.getRaiz())

        elif num ==  "5":
          print("imprimiendo por direccion")
          ab.direccion(ab.getRaiz())
