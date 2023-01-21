

if __name__ == '__main__':
    S = list(input())
    words = []; nums = []
    for i in S:
        try:
            nums.append(int(i))
        except:
            words.append(i)

    words.sort(); nums.sort()
    print(words + nums)
