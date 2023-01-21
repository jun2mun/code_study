if __name__ == '__main__':
    N = int(input()); num_list = []
    for _ in range(N):
        num_list.append(int(input()))

    num_list.sort(reverse=True)
    print(num_list)
