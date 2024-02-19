import itertools

num = 13
λ=[]
d=2
μ=[1,1,0]


all_cylindric_partitions = []



def print_matrix(all_cylindric_partitions):
    for cylindric_partition in all_cylindric_partitions:
        for part in cylindric_partition:
            if part != 0:
                print(part, end=" ")
            else:
                print(" ", end=" ")
        print("\n")
    print("***")



def dP(arr, bound, n, part_count, partitions):
    if n == 0 and part_count==len(arr.copy()):
        partitions.append(arr.copy())

    for k in range(1, bound+1):
        arr.append(k)
        dP(arr, min(k, n - k), n - k, part_count, partitions)
        arr.pop()
    return partitions


def generate_zero_matrix(λ, r, d):
    matrix=[]
    for i in range(r+1):
        matrix.append([])
        for j in range(max(max(λ), λ[r-1]+d)):
            matrix[i].append(0) 
    return matrix


def cylindric_partitions(λ, d, num, μ):
    print("Now, we will calculate all cylindric partitions with λ: ", λ)
    all_cylindric_partitions=[]
    part_count=0
    for i in range(len(λ)):
        part_count += λ[i] - μ[i]

       
    partitions=dP([], num, num, part_count, [])
    
   

    partition_permutations = []
    for partition in partitions:
        partition_permutations+=set(itertools.permutations(partition))

    for i in range(len(partition_permutations)):
        partition_permutations[i]=list(partition_permutations[i])

    print("Partition permutations are: ", partition_permutations)
    for i in range(len(partition_permutations)):
        matrix=generate_zero_matrix(λ,len(λ),d)
        count=0

        for row in range(1, len(matrix)):
            for column in range(μ[row-1], λ[row-1]):
                matrix[row][column]=partition_permutations[i][count]
                count+=1
        
        for i in range(λ[len(λ)-1] - μ[len(λ)-1]):
            matrix[0][i+d]=matrix[len(λ)][i]

        check=True
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                if matrix[i][j] != 0:
                    if (i+1<len(matrix) and matrix[i][j] < matrix[i+1][j]) or (j+1<len(matrix[1]) and matrix[i][j] < matrix[i][j+1]):
                        check=False
        if check==True:
            all_cylindric_partitions.append(matrix)

    for matrix in all_cylindric_partitions:
        print_matrix(matrix)


possible_λ=[]
λ_permutations = []
def for_every_λ(num, μ, λ_permutations):
    for number in range(num):
        
        #print("The number is: " , number)
        #print("The mu is: " , μ)
        
        for i in range(1, len(μ)+1):
            a=dP([], number, number, i, [])
            #print("The partitions of ", number, " with ", i, " parts: ", a)
            
            if i != len(μ):
                #print(i, " is not equal to ", len(μ))
                #print("Add 0 ", len(μ)-i, " times")
                for each in range(len(a)):
                    for j in range(len(μ)-i):
                        
                        a[each].append(0)
                    possible_λ.append(a[each])
                #print("A possible λ is: ", a)
            else:
                #print(i, "is equal to ", len(μ))
                for each in range(len(a)):
                    possible_λ.append(a[each])
            #print("Newly formed possible_λ list is: ", possible_λ)

        #print("Permutations of lambda: ", λ_permutations)
        for partition in possible_λ:
            λ_permutations+=set(itertools.permutations(partition))
        #print("Permutations of lambda as set: ", λ_permutations)
        for i in range(len(λ_permutations)):
            λ_permutations[i]=list(λ_permutations[i])
        
        #print("Permutations of lambdas without mus: ", λ_permutations)
    for λ in λ_permutations:
        for a in range(len(λ)):
            λ[a]= λ[a] + μ[a]

    print("At last, all possible lambdas are: ", λ_permutations)

    
    


for_every_λ(num, μ, λ_permutations)

for λ in λ_permutations: 
    cylindric_partitions(λ, d, num, μ)

    