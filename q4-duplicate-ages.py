'''Solution to question 4'''

def find_duplicate_ages(males, females):
    longer = males if len(males) > len(females) else females
    shorter = males if len(males) <= len(females) else females
    index_in_longer = 0
    duplicate_ages = []
    for age in shorter:
        # traverse the longer array
        # stop when the age is equal to the 
        # current age in shorter array
        # or at the end of the longer array
        while len(longer) > index_in_longer + 1 and age > longer[index_in_longer]:
            index_in_longer += 1
        if age == longer[index_in_longer]:
            duplicate_ages.append(age)
    return duplicate_ages


def main():
    male = [17,19,20,22,27,45,56,59,69]
    female = [17,22,25,29,32,34,35,45,59]
    print(find_duplicate_ages(male, female))
    print(find_duplicate_ages([22,23,36,39],  [22,24,29,39,43]))

if __name__ == "__main__":
    main()

