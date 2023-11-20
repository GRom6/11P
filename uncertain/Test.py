N = abs(int(input()))
def fact(N):
    if N == 1:
        return 1
    return (N * fact(N-1))

print(fact(N))

# N = int(input())
# result = ""
# for i in range(10**N, 10**(N-1)-1, -1):
#     if  i % 2 != 0:
#         result += str(i) + ' '
# print(result)
