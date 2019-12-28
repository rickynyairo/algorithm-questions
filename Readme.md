## Algorithm questions

### Solutions are written in python (3.6.6)

#### Question 4 Explanation

- The solution begins by selecting the shorter and the longer list of the two provided lists
- Iterate through the values in the shorter list while traversing the longer list
- Both the shorter list and the longer list are traversed only once
- We only move to the next value in the shorter list if it is greater than the value in the longer list
- The values that are similar in both lists are stored in a new list of duplicates
- This is returned as the final result

##### Alternative approach

- Create a set from both lists of male and female
- Get the intersection of the two sets
- This represents the similar values