import sys
sys.setrecursionlimit(100000)

def solution(tree):
    length = len(tree)

    if length <= 1:
        return tree
    
    for i in range(1,length):
        if tree[i] > tree[0]: # 전위순회에서 tree[0]은 root
            # 후위 순회에서 root는 맨 마지막 이기에 root 보다 더 큰 숫자가 나오면
            # 오른쪽 자식 트리라는 것을 알 수 있다.
            # 따라서 왼쪽 자식트리 부터 출력 + 오른족 자식트리 출력 + 루트 트리 출력
            return solution(tree[1:i]) + solution(tree[i:]) + [tree[0]]
    
    # 오른쪽 자식 트리가 없을 경우 (root 보다 큰 오른쪽 자식 노드가 없으면)
    return solution(tree[1:]+ [tree[0]]) # 왼쪽자식트리 + root 순서로 출력

if __name__ == '__main__':
    count= 0; tree =[]
    while count <= 10000:

        try:
            temp = int(input())
        except:
            break
        tree.append(temp)
        count += 1
    print(tree)
    trees = solution(tree)

    for n in trees:
        print(n)
