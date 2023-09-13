def check_pattern(List,pattern)->bool:
    '''This function checks if the sub-lists in a list adhere to the specified pattern.'''
    if len(pattern) == len(List) :
        for i in range(len(List)) :
            if i == len(List)-1 :
                continue
            else :
                if List[i] == List[i+1] and pattern[i] == pattern[i+1] :
                    continue
                elif List[i] != List[i+1] and pattern[i] != pattern[i+1] :
                    continue
                else :
                    return False
        return True 
    else :
        return 'List and pattern must have same length.'

print(check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB"))
print(check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA"))
print(check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB"))
print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD"))
print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA"))
print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [7, 7, 7, 7], [5, 5, 5, 5]], "DCBA"))
print(check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCOBA"))
exit = input('Enter any key to exit:')
