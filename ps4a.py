# Problem Set 4A
# Name: <Aditya Adiga>


def get_permutations(sequence):
 
    if len(sequence)==0:
        return []
    if len(sequence)==1:
        return [sequence]
    
    permutation=[]
    for i in range(len(sequence)):
        ele=sequence[i]
        remlist=sequence[:i]+sequence[i+1:]
        for i in get_permutations(remlist):
            permutation.append(ele+i)
        
        
        
        
    return permutation
        



if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    

    

