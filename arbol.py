class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data == root.data:
            print("Ese elemento ya está en el árbol.")
            return root
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)
def search(root, data):
    if root is None:
        return False
    else:
        if root.data == data:
            return True
        elif data < root.data:
            return search(root.left, data)
        else:
            return search(root.right, data)

def min_value(root):
    minimo = None
    if root:
        minimo = root.data
        while root.left is not None:
            minimo = root.left
            min_value(root.left)
    return minimo

def erase(root, data):
    if root is None:
        print("El nodo no tiene elementos.")
        return root
    else:
        if search(root, data) is True:
            if data < root.data:
                erase(root.left, data)
            elif data > root.data:
                erase(root.right, data)
            else:
                #Caso donde borramos una hoja. 
                if root.left is None and root.right is None:
                    root = None
                #Caso donde borramos una rama con  un solo hijo.
                elif root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                #Caso donde borramos una rama con dos hijos.
                else:
                    minimo = min_value(root.right)
                    root = minimo
                    self.erase(root, minimo)
        return root

Om = True
arbol = None
print("¡Bienvenido al menú para la creación y manejo de árboles binarios en python!")
while Om:

    w = True 
    print("Decide qué quieres hacer:")
    print("1.-Insertar un elemento al árbol.")
    print("2.-Buscar un elemento del árbol.")
    print("3.-Eliminar un elemento del árbol.")
    print("4.-Recorrido previo del árbol.")
    print("5.-Recorrido simétrico del árbol.")
    print("6.-Recorrido posterior del árbol.")
    print("7.-Salir del programa")
    while w:
        try:
            decision = input("Por favor, introduce un número de las 7 opciones: ")
            numint = int(decision)
            esentero = isinstance(numint, int)
            if esentero:
                w = False
        except ValueError:
            print("Ingresa una opción válida (Número entero del 1 al 7.")

        if numint == 1:

            r = True
            elemento = None
            dec2 = None
            while r:
                try:
                    elemento = input("¿Qué elemento quieres Ingresar al árbol?: ")
                    dec2 = int(elemento)
                    v2 = isinstance(dec2, int)
                    if v2:
                        r = False
                except ValueError:
                    print("Ingresa un valor válido para insertarlo en el nodo (Un número entero).")
            arbol = insert(arbol,dec2)
            break
        elif numint == 2:
            if arbol is None:
                print("El arbol aún no tiene elementos")
                break
            else: 
                s = True
                dec3 = None
                while s:
                    try:
                        buscado = input("¿Qué elemento quieres buscar en el árbol?: ")
                        dec3 = int(buscado)
                        v3 = isinstance(dec3, int)
                        if v3:
                            s = True
                    except ValueError:
                        print("Ingresa una opción válida")
            s = search(dec3)
            if s:
                print("!El elemnto que buscas está en el árbol¡")
            else:
                print("El elemento que buscas no está en el árbol")
            break
        elif numint == 3:
            if arbol is None:
                print("El arbol aún no tiene elementos")
                break
            else:
                t = True
                eliminado = None
                while t:
                    try:
                        elementoB = input("¿Qué elemento desea eliminar del árbol?: ")
                        dec4 = int(elementoB)
                        eliminado = int(elementoB)
                        v4 = isinstance(dec4, int)
                        if v4:
                            t = False
                            break
                    except ValueError:
                        print("Ingresa una opción válida")
            arbol = erase(arbol, eliminado)
            break
        elif numint == 4:
            if arbol is None:
                print("El arbol aún no tiene elementos")
            else:
                print("El recorrido previo del árbol es: ")
                pre_order(arbol)
            break
        elif numint == 5:
            if arbol is None:
                print("El arbol aún no tiene elementos")
            else:
                print("El recorrido simétrico del árbol es: ")
                in_order(arbol)
            break
        elif numint == 6:
            if arbol is None:
                print("El arbol aún no tiene elementos")
            else:
                print("El recorrido posterior del árbol es: ")
                post_order(arbol)
            break
        elif numint == 7:
            print("¡Hasta pronto!")
            Om = False
            break
        else: 
            print("Ingresa una opción válida")
            break





