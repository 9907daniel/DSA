# https://www.acmicpc.net/problem/2609

n, m = map(int, input().split())

greatest = abs(n*m)

while m !=0:
    r = n%m
    n,m = m,r

print(n)
print(greatest // m)