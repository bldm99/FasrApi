import threading
from fastapi import FastAPI
from tomlkit import string
import requests
import json
app = FastAPI()

@app.get("/top")

def producto():
    def laravelmensaje():

        res = requests.get("http://localhost:3000/api/users/all")
        return res.text

    import json

    res = requests.get("http://localhost:3000/api/users/all")
    datos = res.text

    # print(datos)
    print('---------------------------------------------------------------------')

    # ------------------------iNICIO----------------------------#
    # ------------------------Llamada al API----------------------------#
    from urllib.request import urlopen
    import json

    # url = 'http://localhost:3000/api/users/ver'
    url = 'http://localhost:3000/api/users/ver'
    response = urlopen(url)
    # ------------------------Convirtiendo reesponse a un json----------------------------#
    dat = json.loads(response.read())
    # print(dat)

    # ------------------------Reorer json dat y agregando----------------------------#
    # ------------------------valores en un diccionario----------------------------#
    diccionario = {}
    for z in dat:
        clave = z['_id']['producto']  # reprenta una clave ejm Chompa de lana
        print(clave)
        valor = z['count']  # reprenta una valor ejm 78
        print(valor)
        diccionario[clave] = valor  # 1mer recorrido  diccionario = {'Chompa de lana': 1}

    print(diccionario)

    # ------------------------guardando en un lista todos los count del json dat----------------------------#
    guardar = []
    for i in dat:
        guardar.append(i['count'])

    print(guardar)

    # ------------------------ordenandode mayor a menor la lista guardar----------------------------#
    ordermax = sorted(guardar, reverse=True)

    # print(ordermax)

    # ------------------------ordenar con maxHeap----------------------------#
    # ------------------------ordenar con maxHeap----------------------------#

    class Heap:
        '''
        Heap class
        '''

        def __init__(self):
            self.heapList = []
            self.size = 0

        def parentIndex(self, index):
            return (index - 1) // 2

        def leftChildIndex(self, index):
            return 2 * index + 1

        def leftChild(self, index):  # [1,3,5,7] 1
            '''
            Get value of left child
            :param index:
            :return:
            '''
            leftIndex = self.leftChildIndex(index)
            if leftIndex < self.size:
                return self.heapList[leftIndex]
            return -1

        def rightChildIndex(self, index):
            return 2 * index + 2

        def rightChild(self, index):
            '''
            Get value of right child
            :param index:
            :return:
            '''
            rightIndex = self.rightChildIndex(index)
            if rightIndex < self.size:
                return self.heapList[rightIndex]
            return -1

        def searchElement(self, itm):
            i = 0
            while (i <= self.size):
                if itm == self.heapList[i]:
                    return i
                i += 1

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def max(self, idx):
            valueRightChild = self.rigthChild(idx)
            valueLefttChild = self.leftChild(idx)

            if valueRightChild < valueLefttChild:  #
                return self.rigthChild(idx)

            elif valueRightChild > valueLefttChild:  #
                return self.leftChild(idx)
            else:
                # return any child index
                return self.rigthChild(idx)

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def minimumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            # print("valueLeftChild = %d" % valueLeftChild)
            # print("valueRightChild = %d" % valueRightChild)
            if valueRightChild == -1:
                return self.leftChildIndex(idx)
            if valueLeftChild > valueRightChild:
                return self.rightChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.leftChildIndex(idx)
            else:
                # return any child index
                return self.rightChildIndex(idx)

        def getTop(self):
            '''
            Get root value for Heap
            :return:
            '''
            if self.size == 0:
                return -1
            return self.heapList[0]

        def percolateDown(self, i):
            pass

        def buildHeap(self, list):
            '''
            Built heap from array
            :param list:
            :return:
            '''
            i = len(list) // 2
            self.size = len(list)
            self.heapList = list
            print("")
            while i >= 0:
                tmp = self.heapList[i]
                print("percolate-down ", tmp, " <<", self.heapList)
                self.percolateDown(i)
                print("percolate-down ", tmp, " >>", self.heapList)
                print("")
                i = i - 1

        def delete(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]  # 1
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def delete2(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def percolateUp(self, i):
            pass

        def insert(self, k):
            '''
            Insert an element at the end
            of heap and apply percolate up
            :param k:
            :return:
            '''
            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def insert2(self, k):

            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def interchangeTopWithBottom(self):
            '''
            interchange first and last element
            of heap
            :return:
            '''
            tmp = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.heapList[self.size - 1] = tmp
            self.size = self.size - 1
            self.percolateDown(0)

    class MaxHeap(Heap):
        def __init__(self):
            Heap.__init__(self)
            # i = 10 que esta en la pos  0

        def percolateDown(self, i):  # [10, 9, 8, 5, 7, 2, 3, 1]
            # 'i' es el indice  0
            # la pos 1 hace refere.. al valor 9 que es el hijo izq del indice 0
            while self.leftChildIndex(i) < self.size:  # 1< 8 SI  -otra iteracion 3<8 SI  -ultima iteracion 9<8 NO
                max = self.maximumChildIndex(i)  # maximo hijo de indi 0 es el indice 1
                if self.heapList[i] < self.heapList[max]:
                    tmp = self.heapList[i]
                    self.heapList[i] = self.heapList[max]
                    self.heapList[max] = tmp
                i = max  # i =1  i = 4

        def percolateUp(self, i):

            iParent = self.parentIndex(i)  # 1
            while (iParent >= 0):  # si

                if self.heapList[iParent] < self.heapList[i]:
                    tmp = self.heapList[iParent]
                    self.heapList[iParent] = self.heapList[i]
                    self.heapList[i] = tmp
                i = iParent
                iParent = self.parentIndex(i)

    ##
    ####

    heap = MaxHeap()
    for i in range(len(guardar)):
        # print("c[%d] = %d" % (i,list[i]))
        heap.insert2(guardar[i])
        # print("--------------------------")
        # print(heap.heapList)
    print("--------------------------")

    print("Ordenacion MaxHeap", heap.heapList)

    mayorHeap = heap.heapList

    # ------------------------End maxHeap------------------------------------#

    # ------------------------El top de mayor venta de la api----------------------------#
    ##########################################################

    ##########################################################
    mayor = ordermax[0]

    Segundo = ordermax[1]

    print('Mayor cantidad metodo sorted', mayor)

    print('Mayor cantidad metodo sorted', Segundo)

    # productolaravel= get_key(mayor)

    # segundo mas vendido

    def get_key(val):
        for key, value in diccionario.items():
            if val == value:
                return key
    mayorHeap = heap.heapList[0]
    productolaravel = get_key(mayorHeap)
    print('Mayor cantidad metodo maxHeap', mayorHeap)
    print('Mas vendido 1:  ', productolaravel)
    return productolaravel


@app.get("/Add")

def producto():
    def laravelmensaje():

        res = requests.get("http://localhost:3000/api/users/all")
        return res.text

    import json

    res = requests.get("http://localhost:3000/api/users/all")
    datos = res.text

    # print(datos)
    print('---------------------------------------------------------------------')

    # ------------------------iNICIO----------------------------#
    # ------------------------Llamada al API----------------------------#
    from urllib.request import urlopen
    import json

    # url = 'http://localhost:3000/api/users/ver'
    url = 'http://localhost:3000/api/users/ver'
    response = urlopen(url)
    # ------------------------Convirtiendo reesponse a un json----------------------------#
    dat = json.loads(response.read())
    # print(dat)

    # ------------------------Reorer json dat y agregando----------------------------#
    # ------------------------valores en un diccionario----------------------------#
    diccionario = {}
    for z in dat:
        clave = z['_id']['producto']  # reprenta una clave ejm Chompa de lana
        print(clave)
        valor = z['count']  # reprenta una valor ejm 78
        print(valor)
        diccionario[clave] = valor  # 1mer recorrido  diccionario = {'Chompa de lana': 1}

    print(diccionario)

    # ------------------------guardando en un lista todos los count del json dat----------------------------#
    guardar = []
    for i in dat:
        guardar.append(i['count'])

    print(guardar)

    # ------------------------ordenandode mayor a menor la lista guardar----------------------------#
    ordermax = sorted(guardar, reverse=True)

    # print(ordermax)

    # ------------------------ordenar con maxHeap----------------------------#
    # ------------------------ordenar con maxHeap----------------------------#

    class Heap:
        '''
        Heap class
        '''

        def __init__(self):
            self.heapList = []
            self.size = 0

        def parentIndex(self, index):
            return (index - 1) // 2

        def leftChildIndex(self, index):
            return 2 * index + 1

        def leftChild(self, index):  # [1,3,5,7] 1
            '''
            Get value of left child
            :param index:
            :return:
            '''
            leftIndex = self.leftChildIndex(index)
            if leftIndex < self.size:
                return self.heapList[leftIndex]
            return -1

        def rightChildIndex(self, index):
            return 2 * index + 2

        def rightChild(self, index):
            '''
            Get value of right child
            :param index:
            :return:
            '''
            rightIndex = self.rightChildIndex(index)
            if rightIndex < self.size:
                return self.heapList[rightIndex]
            return -1

        def searchElement(self, itm):
            i = 0
            while (i <= self.size):
                if itm == self.heapList[i]:
                    return i
                i += 1

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def max(self, idx):
            valueRightChild = self.rigthChild(idx)
            valueLefttChild = self.leftChild(idx)

            if valueRightChild < valueLefttChild:  #
                return self.rigthChild(idx)

            elif valueRightChild > valueLefttChild:  #
                return self.leftChild(idx)
            else:
                # return any child index
                return self.rigthChild(idx)

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def minimumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            # print("valueLeftChild = %d" % valueLeftChild)
            # print("valueRightChild = %d" % valueRightChild)
            if valueRightChild == -1:
                return self.leftChildIndex(idx)
            if valueLeftChild > valueRightChild:
                return self.rightChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.leftChildIndex(idx)
            else:
                # return any child index
                return self.rightChildIndex(idx)

        def getTop(self):
            '''
            Get root value for Heap
            :return:
            '''
            if self.size == 0:
                return -1
            return self.heapList[0]

        def percolateDown(self, i):
            pass

        def buildHeap(self, list):
            '''
            Built heap from array
            :param list:
            :return:
            '''
            i = len(list) // 2
            self.size = len(list)
            self.heapList = list
            print("")
            while i >= 0:
                tmp = self.heapList[i]
                print("percolate-down ", tmp, " <<", self.heapList)
                self.percolateDown(i)
                print("percolate-down ", tmp, " >>", self.heapList)
                print("")
                i = i - 1

        def delete(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]  # 1
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def delete2(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def percolateUp(self, i):
            pass

        def insert(self, k):
            '''
            Insert an element at the end
            of heap and apply percolate up
            :param k:
            :return:
            '''
            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def insert2(self, k):

            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def interchangeTopWithBottom(self):
            '''
            interchange first and last element
            of heap
            :return:
            '''
            tmp = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.heapList[self.size - 1] = tmp
            self.size = self.size - 1
            self.percolateDown(0)

    class MaxHeap(Heap):
        def __init__(self):
            Heap.__init__(self)
            # i = 10 que esta en la pos  0

        def percolateDown(self, i):  # [10, 9, 8, 5, 7, 2, 3, 1]
            # 'i' es el indice  0
            # la pos 1 hace refere.. al valor 9 que es el hijo izq del indice 0
            while self.leftChildIndex(i) < self.size:  # 1< 8 SI  -otra iteracion 3<8 SI  -ultima iteracion 9<8 NO
                max = self.maximumChildIndex(i)  # maximo hijo de indi 0 es el indice 1
                if self.heapList[i] < self.heapList[max]:
                    tmp = self.heapList[i]
                    self.heapList[i] = self.heapList[max]
                    self.heapList[max] = tmp
                i = max  # i =1  i = 4

        def percolateUp(self, i):

            iParent = self.parentIndex(i)  # 1
            while (iParent >= 0):  # si

                if self.heapList[iParent] < self.heapList[i]:
                    tmp = self.heapList[iParent]
                    self.heapList[iParent] = self.heapList[i]
                    self.heapList[i] = tmp
                i = iParent
                iParent = self.parentIndex(i)

    ##
    ####

    heap = MaxHeap()
    for i in range(len(guardar)):
        # print("c[%d] = %d" % (i,list[i]))
        heap.insert2(guardar[i])
        # print("--------------------------")
        # print(heap.heapList)
    print("--------------------------")

    print("Ordenacion MaxHeap", heap.heapList)

    mayorHeap = heap.heapList

    # ------------------------End maxHeap------------------------------------#

    # ------------------------El top de mayor venta de la api----------------------------#
    ##########################################################

    ##########################################################
    mayor = ordermax[0]

    Segundo = ordermax[1]

    print('Mayor cantidad metodo sorted', mayor)

    print('Mayor cantidad metodo sorted', Segundo)

    # productolaravel= get_key(mayor)

    # segundo mas vendido

    def get_key(val):
        for key, value in diccionario.items():
            if val == value:
                return key
    mayorHeap1 = heap.heapList[1]
    productolaravelsegundo = get_key(mayorHeap1)
    print('Mayor cantidad metodo maxHeap', mayorHeap1)
    print('Mas vendido 2:  ', productolaravelsegundo)


    return productolaravelsegundo


@app.get("/See")

def producto():
    def laravelmensaje():

        res = requests.get("http://localhost:3000/api/users/all")
        return res.text

    import json

    res = requests.get("http://localhost:3000/api/users/all")
    datos = res.text

    # print(datos)
    print('---------------------------------------------------------------------')

    # ------------------------iNICIO----------------------------#
    # ------------------------Llamada al API----------------------------#
    from urllib.request import urlopen
    import json

    # url = 'http://localhost:3000/api/users/ver'
    url = 'http://localhost:3000/api/users/ver'
    response = urlopen(url)
    # ------------------------Convirtiendo reesponse a un json----------------------------#
    dat = json.loads(response.read())
    # print(dat)

    # ------------------------Reorer json dat y agregando----------------------------#
    # ------------------------valores en un diccionario----------------------------#
    diccionario = {}
    for z in dat:
        clave = z['_id']['producto']  # reprenta una clave ejm Chompa de lana
        print(clave)
        valor = z['count']  # reprenta una valor ejm 78
        print(valor)
        diccionario[clave] = valor  # 1mer recorrido  diccionario = {'Chompa de lana': 1}

    print(diccionario)

    # ------------------------guardando en un lista todos los count del json dat----------------------------#
    guardar = []
    for i in dat:
        guardar.append(i['count'])

    print(guardar)

    # ------------------------ordenandode mayor a menor la lista guardar----------------------------#
    ordermax = sorted(guardar, reverse=True)

    # print(ordermax)

    # ------------------------ordenar con maxHeap----------------------------#
    # ------------------------ordenar con maxHeap----------------------------#

    class Heap:
        '''
        Heap class
        '''

        def __init__(self):
            self.heapList = []
            self.size = 0

        def parentIndex(self, index):
            return (index - 1) // 2

        def leftChildIndex(self, index):
            return 2 * index + 1

        def leftChild(self, index):  # [1,3,5,7] 1
            '''
            Get value of left child
            :param index:
            :return:
            '''
            leftIndex = self.leftChildIndex(index)
            if leftIndex < self.size:
                return self.heapList[leftIndex]
            return -1

        def rightChildIndex(self, index):
            return 2 * index + 2

        def rightChild(self, index):
            '''
            Get value of right child
            :param index:
            :return:
            '''
            rightIndex = self.rightChildIndex(index)
            if rightIndex < self.size:
                return self.heapList[rightIndex]
            return -1

        def searchElement(self, itm):
            i = 0
            while (i <= self.size):
                if itm == self.heapList[i]:
                    return i
                i += 1

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def max(self, idx):
            valueRightChild = self.rigthChild(idx)
            valueLefttChild = self.leftChild(idx)

            if valueRightChild < valueLefttChild:  #
                return self.rigthChild(idx)

            elif valueRightChild > valueLefttChild:  #
                return self.leftChild(idx)
            else:
                # return any child index
                return self.rigthChild(idx)

        def maximumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            if valueLeftChild > valueRightChild:
                return self.leftChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.rightChildIndex(idx)
            else:
                # return any child index
                return self.leftChildIndex(idx)

        def minimumChildIndex(self, idx):
            valueLeftChild = self.leftChild(idx)
            valueRightChild = self.rightChild(idx)
            # print("valueLeftChild = %d" % valueLeftChild)
            # print("valueRightChild = %d" % valueRightChild)
            if valueRightChild == -1:
                return self.leftChildIndex(idx)
            if valueLeftChild > valueRightChild:
                return self.rightChildIndex(idx)
            elif valueLeftChild < valueRightChild:
                return self.leftChildIndex(idx)
            else:
                # return any child index
                return self.rightChildIndex(idx)

        def getTop(self):
            '''
            Get root value for Heap
            :return:
            '''
            if self.size == 0:
                return -1
            return self.heapList[0]

        def percolateDown(self, i):
            pass

        def buildHeap(self, list):
            '''
            Built heap from array
            :param list:
            :return:
            '''
            i = len(list) // 2
            self.size = len(list)
            self.heapList = list
            print("")
            while i >= 0:
                tmp = self.heapList[i]
                print("percolate-down ", tmp, " <<", self.heapList)
                self.percolateDown(i)
                print("percolate-down ", tmp, " >>", self.heapList)
                print("")
                i = i - 1

        def delete(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]  # 1
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def delete2(self):
            '''
            Delete an element from top
            of heap and apply percolate doown
            :return:
            '''
            ret = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.size = self.size - 1
            self.heapList.pop()
            self.percolateDown(0)
            return ret

        def percolateUp(self, i):
            pass

        def insert(self, k):
            '''
            Insert an element at the end
            of heap and apply percolate up
            :param k:
            :return:
            '''
            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def insert2(self, k):

            self.heapList.append(k)
            self.size = self.size + 1
            self.percolateUp(self.size - 1)

        def interchangeTopWithBottom(self):
            '''
            interchange first and last element
            of heap
            :return:
            '''
            tmp = self.heapList[0]
            self.heapList[0] = self.heapList[self.size - 1]
            self.heapList[self.size - 1] = tmp
            self.size = self.size - 1
            self.percolateDown(0)

    class MaxHeap(Heap):
        def __init__(self):
            Heap.__init__(self)
            # i = 10 que esta en la pos  0

        def percolateDown(self, i):  # [10, 9, 8, 5, 7, 2, 3, 1]
            # 'i' es el indice  0
            # la pos 1 hace refere.. al valor 9 que es el hijo izq del indice 0
            while self.leftChildIndex(i) < self.size:  # 1< 8 SI  -otra iteracion 3<8 SI  -ultima iteracion 9<8 NO
                max = self.maximumChildIndex(i)  # maximo hijo de indi 0 es el indice 1
                if self.heapList[i] < self.heapList[max]:
                    tmp = self.heapList[i]
                    self.heapList[i] = self.heapList[max]
                    self.heapList[max] = tmp
                i = max  # i =1  i = 4

        def percolateUp(self, i):

            iParent = self.parentIndex(i)  # 1
            while (iParent >= 0):  # si

                if self.heapList[iParent] < self.heapList[i]:
                    tmp = self.heapList[iParent]
                    self.heapList[iParent] = self.heapList[i]
                    self.heapList[i] = tmp
                i = iParent
                iParent = self.parentIndex(i)

    ##
    ####

    heap = MaxHeap()
    for i in range(len(guardar)):
        # print("c[%d] = %d" % (i,list[i]))
        heap.insert2(guardar[i])
        # print("--------------------------")
        # print(heap.heapList)
    print("--------------------------")

    print("Ordenacion MaxHeap", heap.heapList)

    mayorHeap = heap.heapList

    # ------------------------End maxHeap------------------------------------#

    # ------------------------El top de mayor venta de la api----------------------------#
    ##########################################################

    ##########################################################
    mayor = ordermax[0]

    Segundo = ordermax[1]

    tercer = ordermax[2]

    print('Mayor cantidad metodo sorted', mayor)

    print('Mayor cantidad metodo sorted', Segundo)
    print('Mayor cantidad metodo sorted', tercer)

    # productolaravel= get_key(mayor)

    # segundo mas vendido

    def get_key(val):
        for key, value in diccionario.items():
            if val == value:
                return key
    mayorHeap2 = heap.heapList[2]
    productolaraveltercero = get_key(mayorHeap2)
    print('Mayor cantidad metodo maxHeap', mayorHeap2)
    print('Mas vendido 3:  ', productolaraveltercero)


    return productolaraveltercero

###


