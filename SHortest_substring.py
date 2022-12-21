import itertools

## the greedy strategy is quicker, but it presupposes an approximation.
#The greedy method below combines the areas of maximum overlap between two substings.
#This process is repeated till we have a single string in the end.
#It won't even verify whether the final string will be the smaller one
#As a result, it won't calculate the best answer.
#For the following instance:
#[ABCD], "CDBC," and "BCDA"] This CDBCABCDA will be calculated using a greedy approach, 
#which is not the best answer. Instead, ABCDBCDA is the best response.

#greedy approach:
def shortest_superstring(A):
    
    
    def find_string_overlap(i,j):
        #this function returns the longest overlap length between i and j such as suffix of i should match prefix of j.
        #if no overlap return zero.
        start = 0
        while True:
            start = i.find(j[:1],start) #looking for j suffix in b 
            if start == -1:
                return 0
            #checking for complete suffix if found
            if j.startswith(i[start:]):
                return len(i)-start
            start = start + 1
        
    def overlap(A): 
        index_1,index_2 = None,None
        max_len = 0
        #for every pair in the array calculating the overlap between them 
        for i,j in itertools.permutations(A,2):
            len_overlap=find_string_overlap(i,j)
            #if len larger than best we seen so far we swap them.
            if len_overlap > max_len:
                index_1,index_2 = i,j
                max_len=len_overlap
        #returning the best overlap found
        return index_1,index_2,max_len
    
    #finding the max overlap
    index1,index2,max_len = overlap(A) 
    
    while max_len > 0:
        A.remove(index1) 
        A.remove(index2) 
        A.append(index1+index2[max_len:]) 
        index1,index2,max_len = overlap(A)
    return ''.join(A)

print("---Output---")
print()
print("The shortest superstring for ['CATGC', 'CTAAGT', 'GCTA', 'TTCA', 'ATGCATC'] is:")
output=shortest_superstring(['CATGC', 'CTAAGT', 'GCTA', 'TTCA', 'ATGCATC'])
print(output)
print()

print("The shortest superstring for ['ABCD', 'CDBC', 'BCDA'] is:")
output=shortest_superstring(['ABCD', 'CDBC', 'BCDA'])
print(output)
print()

print("The shortest superstring for ['X','X','X'] is:")
output=shortest_superstring(['X', 'X', 'X'])
print(output)