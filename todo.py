to_do_list = []


def add_to_list():
    print("Add an element to your to do list: ")
    element = input()
    to_do_list.append(element)
    print(to_do_list)

add_to_list()

'''def mark():
mark()'''

def archive():
    print(to_do_list)
    print("Delete an elemet from the list:")
    element = input()
    if element in to_do_list:
        to_do_list.remove(element)
        print(to_do_list)
    elif element not in to_do_list:
        print("The element is not in the list. Try again!")

archive()
    

