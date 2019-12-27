def distribute_cash(amount, starting_point, number=0):
    if amount <= starting_point:
        return number, amount
    # 12% is specified in the question
    # however, the solution provided suggests an increase of 20 %
    # e.g 10, 12... 
    # 2 is 20% of 10
    # For the sake of correctness, I shall use 20%
    return distribute_cash(amount - starting_point, starting_point * 1.2, number + 1)

def main():
    number, balance = distribute_cash(4000, 10)
    print('4000 was distributed to ', number, ' people, balance: ', balance)

if __name__ == "__main__":
    main()