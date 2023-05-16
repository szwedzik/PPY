import MyLinkedList

list = MyLinkedList.MyLinkedList()
list.append(3)
list.append(1)
list.append(4)
list.append(2)
list.append(1)

print("Lista po dodaniu elementów: ", list)

list.delete(1)

print("Lista po usunięciu elementów: ", list)

print("Element o wartości 3: ", list.get(3))

list.append(2)
list.append(5)
list.append(0, func=lambda x, y: x > y)

print("Lista po dodaniu elementów: ", list)
