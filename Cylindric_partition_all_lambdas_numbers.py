import itertools

def print_matrix(all_cylindric_partitions):
    print("\n")
    for cylindric_partition in all_cylindric_partitions:
        print("->", end=" ")
        for part in cylindric_partition:
            
            if part != 0:
                print(part, end="")
            else:
                print(0, end="")
        
        print(end=None)
    print("~~~~~~~~~~~~~~~~~~")

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
   
  
    for i in range(len(partition_permutations)):
        matrix=generate_zero_matrix(λ,len(λ),d)
        count=0

        for row in range(1, len(matrix)):
            for column in range(μ[row-1], λ[row-1]):
                matrix[row][column]=partition_permutations[i][count]
                count+=1
        
        for i in range(μ[len(λ)-1], λ[len(λ)-1]):
            matrix[0][i+d]=matrix[len(λ)][i]

        check=True
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] != 0:
                    if (i+1<len(matrix) and matrix[i][j] < matrix[i+1][j]) or (j+1<len(matrix[1]) and matrix[i][j] < matrix[i][j+1]):
                        check=False
                for count in range(1, len(matrix)-i):
                    if matrix[i][j]!=0 and matrix[i+count][j]!=0 and matrix[i][j]<matrix[i+count][j]:
                        check=False
        
            
        if check==True:
            all_cylindric_partitions.append(matrix)

    if part_count == 0 and num!=0:
        matrix=generate_zero_matrix(λ,len(λ),d)
        all_cylindric_partitions.insert(0, matrix)
   
    for matrix in all_cylindric_partitions:
        print("λ =", λ)
        print("μ =", μ)
        print("d =", d)
        print_matrix(matrix)
      
    

def for_every_λ(num, μ, λ_permutations):
    for number in range(num+1):
        
        for i in range(0, len(μ)+1):
            a=dP([], number, number, i, [])
          
            
            if i != len(μ):
               
                for each in range(len(a)):
         
                    for j in range(len(μ)-i):
                        
                        a[each].append(0)
                    possible_λ.append(a[each])
           

            else:

                for each in range(len(a)):
                    possible_λ.append(a[each])
  

    for partition in possible_λ:
        λ_permutations+=set(itertools.permutations(partition))

    
    for i in range(len(λ_permutations)):
        λ_permutations[i]=list(λ_permutations[i])
   

    for λ in λ_permutations:
        for a in range(len(λ)):
            λ[a]= λ[a] + μ[a]
    
def alternative_for_every_λ(num, μ, λ_permutations):
    minimum=sum(μ)
    maximum=minimum+num
    my_λ=[]
    for i in range(len(μ)):
        my_λ.append(0)
    for i in range(minimum,maximum+1):
        for j in range(1, len(μ)+1):
            a=dP([], i, i, j, [])
            print(a)
            if len(a)!=0:
                for count in range(len(a[0])):
                    for each in range(len(a)):
                        my_λ[count]=my_λ[count]+a[each][count]
                        possible_λ.append(my_λ)
                my_λ=[]
                for i in range(len(μ)):
                    my_λ.append(0)

    for partition in possible_λ:
        
        λ_permutations+=set(itertools.permutations(partition))
    for i in range(len(λ_permutations)):
        λ_permutations[i]=list(λ_permutations[i])
    print("Not selected form: ", λ_permutations)

    to_be_removed=[]
    for i in range(len(λ_permutations)):
        print("Now the perm is: ", λ_permutations[i])
        second_check=False
        for k in range(len(my_λ)):
            if λ_permutations[i][k]<μ[k]:
                second_check=True
        if second_check:
            print(λ_permutations[i], " is not allowed.")
            to_be_removed.insert(0,λ_permutations[i])
        else: 
            print(λ_permutations[i], " is allowed.")
    
    for i in range(len(to_be_removed)):
        print( "Now the lambdas are: ", λ_permutations)
        print("To be removed is: ",to_be_removed[i])
        λ_permutations.remove(to_be_removed[i])
    
    print("These are all possible lambdas: ", λ_permutations)



print("~ INITIALIZATION~\n")
num = 5
λ=[]
d=3
μ=[1,0]
all_cylindric_partitions = []

print("1) μ is given as constant. In this case it is μ =", μ)
print("2) Up to some d, in this case", d)
print("3) Up to some number, in this case", num, "will be shown for all possible λ's. \n\n")

for dd in range(1,d+1):
    print("** d is now", dd,":")
    for all_numbers in range(num+1):
        print("")
        possible_λ=[]
        λ_permutations = []
        for_every_λ(all_numbers, μ, λ_permutations)
        print("All cylindric partitions of", all_numbers, ":")
        print("All possible λ's are: ", λ_permutations, "\n")
       
        for λ in λ_permutations: 
            count=0
            cylindric_partitions(λ, dd, all_numbers, μ)
            print("While μ =", μ, "and d =", d, "there are", count, "partitions for", num)
