
if __name__ == '__main__':

    N = int(input())
    students = []
    for _ in range(N):
        student = input().split(); 
        student[1] = int(student[1])
        students.append(student)
    
    students.sort(key=lambda x: x[1])
    print(students)