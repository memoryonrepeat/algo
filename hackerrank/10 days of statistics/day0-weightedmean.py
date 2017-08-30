N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]
weighted_mean = sum(map(lambda x,y: x*y, X, W))/sum(W)
print(round(weighted_mean,1))