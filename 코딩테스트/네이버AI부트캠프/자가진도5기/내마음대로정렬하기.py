def solution(strings, n):
    strings.sort()
    return sorted(strings,key=lambda x:x[n])

if __name__ == '__main__':
    strings =["sun", "bed", "car"]
    n = 1
    print(solution(strings,n))
    strings = ["abce", "abcd", "cdx"]
    n =2
    print(solution(strings,n))
