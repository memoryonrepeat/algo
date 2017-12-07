# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def get_single_area(k,l,m,n):
    return (m-k)*(n-l)

def solution(K, L, M, N, P, Q, R, S):
    
    first_rect_area = get_single_area(K,L,M,N)
    second_rect_area = get_single_area(P,Q,R,S)
    
    intersection_area = (min(M,R)-max(K,P))*(min(N,S)-max(L,Q))
    
    total_area = first_rect_area + second_rect_area - intersection_area
    
    if total_area<0:
        return -1
    if total_area>2147483647:
        return -1
    
    return total_area