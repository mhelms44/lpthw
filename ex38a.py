def get_cards():
    """
    Allows user to add their cards to a list
    """
    collection = []
    while True:
        card_name = input("Enter a card name: ")
        collection.append(card_name)
        if not card_name:
            collection.pop(-1)
            break
    print (collection)   
    display_cards(collection)

def display_cards(collection):
    pass

def main():
    get_cards()

main()