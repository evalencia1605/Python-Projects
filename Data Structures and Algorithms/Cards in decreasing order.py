#Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

#We need to find the card that alice has selected with the fewer loops

cards = [2, 7]
query = 7


def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return 0
        else:
            position = position + 1
    return -1
      
print(locate_card(cards, query))


