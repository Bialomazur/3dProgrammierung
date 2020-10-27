def grid_index(grid, indexes):
    letters = []
    result = ""
    for array in grid:
        for letter in array:
            letters.append(letter)
    for index in indexes:
        result += letters[index-1]
    return result


    # print(len(grid))
    # for j,array in enumerate(grid):
    #     for index in indexes:
    #         if len(array) * j < index:
    #             continue
    #         else:
    #             letters.append(array[index-1-((j-1)*len(array))])
                
    
    print(letters)



grid_index([['m', 'y', 'e'], 
 ['x', 'a', 'm'], 
 ['p', 'l', 'e']], [1,3,5,8])
"""
[['m', 'y', 'e'], 
 ['x', 'a', 'm'], 
 ['p', 'l', 'e']]

 [1, 3, 5, 8]

 -->  meal
"""