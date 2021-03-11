# ARBOL_BINARIO_DE_BUSQUEDA_Leonardo_Leon
 '''
 Se desea añadir varios métodos a la clase del Árbol Binario de Búsqueda de forma eficiente.
 Quiero optimizar el programa al máximo sin que este pierda su funcionalidad.
 '''
class Hoja:

    '''
    Esta clase asigna el dato a la variable que se le indique.
    A su vez, esta clase no pertenece al árbol, sino que se
    encarga de distribuir la información al área correspondiente.
    '''
    def __init__(self, dato=None):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        
'''
Cuando añades un nuevo elemento al árbol, no esperas que este tenga descendientes, por ello
sus hijos (derecho e izquierdo) = None. El dato inicial también es cero debido a que no hay
datos en el árbol.
'''

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def agregar_dato(self):
        dato = int(input('Ingrese el elemento: '))
        if self.raiz is None:
            self.raiz = Hoja(dato)
        else:
            self.acomodar(dato, self.raiz)

    def acomodar(self, dato, hoja_act):
        if dato < hoja_act.dato:
            if hoja_act.izquierda is None:
                hoja_act.izquierda = Hoja(dato)
            else:
                self.acomodar(dato, hoja_act.izquierda)
        elif dato > hoja_act.dato:
            if hoja_act.derecha is None:
                hoja_act.derecha = Hoja(dato)
            else:
                self.acomodar(dato, hoja_act.derecha)
        else:
            print('El valor ya está en el árbol.')

    def buscar_dato(self):
        dato = int(input('Busqueda: '))
        if self.raiz:
            akita = self.buscar(dato, self.raiz)
            if akita:
                print(dato, 'pertenece al árbol y se encuentra en:', akita)
            else:
                print(dato, 'no pertenece al árbol.')
        else:
            print('No se ha creado el árbol.')
        
    def buscar(self, dato, hoja_act):
        if dato > hoja_act.dato and hoja_act.derecha:
            return self.buscar(dato, hoja_act.derecha)
        elif dato < hoja_act.dato and hoja_act.izquierda:
            return self.buscar(dato, hoja_act.izquierda)
        elif dato == hoja_act.dato:
            return hoja_act

    def recorrer_arbol(self):
        print('Recorrido.')
        if self.raiz:
            self.orden(self.raiz)
        print()
    
    def orden(self, hoja_act):
        if hoja_act:
            self.orden(hoja_act.izquierda)
            print(hoja_act.dato, end=' ')
            self.orden(hoja_act.derecha)

    def eliminar_dato(self):
        dato = int(input('Eliminar: '))
        if self.buscar(dato, self.raiz):
            print(dato, 'fue eliminado del árbol.')
        else:
            print(dato, 'no pertenecía al árbol registrado.')
        self.borrar(self.raiz, dato)
    
    def borrar(self, hoja_act, dato):
        if hoja_act is None:
            return hoja_act
        elif dato < hoja_act.dato:
            hoja_act.izquierda = self.borrar(hoja_act.izquierda,dato)
        elif dato > hoja_act.dato: 
            hoja_act.derecha = self.borrar(hoja_act.derecha,dato)
        else:
            if hoja_act.izquierda is None and hoja_act.derecha is None:
                hoja_act = None
            elif hoja_act.izquierda is None:
                return hoja_act.derecha
            elif hoja_act.derecha is None:
                return hoja_act.izquierda
            else:
                temp = self.min(hoja_act.derecha)
                hoja_act.derecha = self.borrar(hoja_act.derecha, temp)
                hoja_act.dato = temp
                self.borrar(hoja_act.derecha,temp)
        return hoja_act

    def min(self, hoja_act): 
        if hoja_act != None:
            return self._min(hoja_act)
        else:
            return None

    def _min(self,hoja_act):
        if hoja_act.izquierda != None:
            return self._min(hoja_act.izquierda)
        else:
            return hoja_act.dato

ab = ArbolBinarioBusqueda()

while True:
    print()
    print('     ', 'Árbol Binario', '     ')
    print()
    print('(1) Agregar elemento.')
    print('(2) Buscar elemento.')
    print('(3) Recorrer árbol.')
    print('(4) Eliminar elemento.')
    print('(5) Salir.')
    opcion = int(input('Opción: '))
    if opcion == 1:
        ab.agregar_dato()
    elif opcion == 2:
        ab.buscar_dato()
    elif opcion == 3:
        ab.recorrer_arbol()
    elif opcion == 4:
        ab.eliminar_dato()
    elif opcion == 5:
        print('¡Hasta pronto!')
        break
