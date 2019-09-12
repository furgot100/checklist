checklist = list()
#CREATE
def create(item):
    checklist.append(item)

# READ 
def read(index):
    return checklist[int(index)]

# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(int(index))


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(int(index), list_item))
        index += 1


def mark_completed(index):
     checklist[int(index)] = "√ " + checklist[int(index)]


def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)
    elif function_code == "U":
        index = user_input("Enter in an Index: ")
        item = user_input("Enter in an item: ")
        update(int(index), item)
    elif function_code == "D":
        index = user_input("What index to destory")
        destroy(int(index))
    elif function_code == "P":
        list_all_items()

    elif function_code =="Q":
        return False
    else:
        print("Unkown Option")
    return True        


def user_input(prompt):
    user_input = input(prompt)
    return user_input



def test():
    create("purple sox")
    create("red cloak")
    
    print(read(0))
    print(read(1))
    
    update(0, "purple socks")
    
    destroy(1)
    
    print(read(0))
    
    list_all_items()
    
    mark_completed(0)
    
    print(read(0))
   
    select("C")
    list_all_items()
    select("R")
    list_all_items()
    select("P")
    list_all_items()
    select("Q")
    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

#test()


running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
