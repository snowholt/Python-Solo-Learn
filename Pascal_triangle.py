def C(n,m):
    """Calculate m'th number of n'th row in the triangle
       using arrays 'seen[][]' and 'value[][]'
    -------------------------------------------------
    """
    if seen[n][m] == 1:
        return value[n][m]
    seen[n][m] = 1
    if m == 0 or n == m:
        value[n][m] = 1
    else:
        value[n][m] = C(n-1 , m) + C(n-1 , m-1)
    return value[n][m]
 
# initial variables
n = int(input())
seen  = [[0 for i in range(n)] for i in range(n)]
value = [[0 for i in range(n)] for i in range(n)]


#Output pascals triangle to the n'th row
#---------------------------------------

for i in range(n):
    for j in range(i + 1):
        x = C(i , j)
        print(x, end = ' ')
    print()
