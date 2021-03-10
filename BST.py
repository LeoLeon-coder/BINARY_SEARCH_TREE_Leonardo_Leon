# BINARY_SEARCH_TREE_Leonardo_Leon
 '''
 The goal is to add many methods to the class with an efficient work. 
 I want to optimize the program to the maximum without losing its functionality.
 '''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
'''
When you add a new element to the tree, you are not expecting for these element to
have children that is why left and right are None. Initially the data is set to
None because the tree is empty.
'''

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_data(self, data):
        '''data = input('Insert the new element: ')'''
        if self.root is None:
            self.root = Node(data)
        else:
            self.arrange(data, self.root)
    
    def arrange(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.arrange(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.arrange(data, cur_node.right)

        else:
            print(data, 'is a repeated value.')

    def seek_data(self):
        dato = input('Search: ')
        if self.root:
            found = self.seek(data, self.root)
            if found:
                print(data, 'is in the tree at', found)
            else:
                print(data, 'is not in the tree.')
        else:
            print('The tree does not exist.')
        
    def seek(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self.seek(data, cur_node.right)
        elif data < cur_note.data and cur_node.left:
            return self.seek(data, cur_node.left)
        elif data == cur_node.data:
            return cur_node

    def walk_tree(self):
        print('Orderly.')
        if self.root:
            self.sort(self.root)
        print()
    
    def sort(self, cur_node):
        if cur_node:
            self.sort(cur_node.left)
            print(cur_node.data, end=' ')
            self.sort(cur_node.right)
            
    #---------------------------------------------
    #create a function to delete data in the tree
    #---------------------------------------------
    

  
tree = BinarySearchTree()

tree.add_data(4)
tree.add_data(7)
tree.add_data(9)
tree.add_data(3)
tree.add_data(8)
tree.add_data(5)
tree.add_data(1)

tree.walk_tree()

#tree.delete_data(7)

tree.walk_tree()


#the next line of code will be like a menu for the user (the options are in spanish)
""" 
while True:
    print('Árbol Binario')
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
"""
