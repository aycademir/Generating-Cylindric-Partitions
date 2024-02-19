import itertools

# cylindric partition all parameters given

num = 6
λ=[1, 1, 6]
d=2
μ=[1,1,0]
r=len(λ)
partitions = []
all_cylindric_partitions = []



def print_matrix(all_cylindric_partitions):
    for cylindric_partition in all_cylindric_partitions:
        for part in cylindric_partition:
            if part != 0:
                print(part, end=" ")
            else:
                print(" ", end=" ")
        print("\n")
    print("\n")



def dP(arr, bound, n, part_count):
    if n == 0 and part_count==len(arr.copy()):
        partitions.append(arr.copy())

    for k in range(1, bound+1):
        arr.append(k)
        dP(arr, min(k, n - k), n - k, part_count)
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
    

    part_count=0
    for i in range(r):
        part_count += λ[i] - μ[i]

       
    dP([], num, num, part_count)
    
   

    partition_permutations = []
    for partition in partitions:
        partition_permutations+=set(itertools.permutations(partition))

    for i in range(len(partition_permutations)):
        partition_permutations[i]=list(partition_permutations[i])

    for i in range(len(partition_permutations)):
        matrix=generate_zero_matrix(λ,r,d)
        count=0

        for row in range(1, len(matrix)):
            for column in range(μ[row-1], λ[row-1]):
                matrix[row][column]=partition_permutations[i][count]
                count+=1
        
        for i in range(λ[r-1] - μ[r-1]):
            matrix[0][i+d]=matrix[r][i]

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


cylindric_partitions(λ, d, num, μ)