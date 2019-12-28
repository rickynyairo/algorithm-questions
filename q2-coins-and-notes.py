'''Solution to Q2'''
# Should be run in python 3.6.6

from typing import Generic, TypeVar


class Money:
    def __init__(self) -> None:
        self.value: int = 0

    def setValue(self, value: int) -> None:
        self.value: int = value

    def getValue(self) -> int:
        return self.value


class Coin (Money):
    pass

class Note (Money):
    pass

Cash = TypeVar('Money', bound=Money)

class Bag(Generic[Cash]):
    
    def __init__(self) -> None:
        self.items: List[Cash] = []
    
    def add(self, item: Cash) -> None:
        self.items.append(item)
        print('here>>>', self.items)

    def display(self) -> None:
        for item in self.items:
            print(item.getValue())

def main():
    # read N from stdin
    n: int = int(input())
    coin_bag = Bag[Coin]()
    note_bag = Bag[Note]()
    for i in range(n):
        # confirm whether it is a note or a coin
        [description, value] = input().split()

        if description == 'Coin':
            coin = Coin()
            coin.setValue(int(value))
            coin_bag.add(coin)
        elif description == 'Note':
            note = Note()
            note.setValue(int(value))
            note_bag.add(note)
    
    print("Coins :")
    coin_bag.display()
    print("Notes :")
    note_bag.display()

    
if __name__ == "__main__":
    main()
