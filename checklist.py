checklist = list()
#CREATE
def create(item):
    checklist.append(item)

# READ 
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item


# DESTROY
def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1


def mark_completed(index):
     checklist[index] = "√ " + checklist[index]
    


     

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item:")
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)
    elif function_code == "P":
        list_all_items()
    elif function_code =="Q":
        return False
    else:
        print("Unkown Option")        

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

    user_value = user_input("Please Enter a value:")
    print(user_value)

test()
running = True
while running:
    selection = user_input("Press C to add to list, T to Read from list, P to display list, and Q to quit")
    select(selection)
