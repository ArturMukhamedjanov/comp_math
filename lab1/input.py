import os.path

def load_file():
    while(True):
        print("Enter file name:")
        file_name = input()
        if(os.path.isfile("./" + file_name)):
            file = open( "./" + file_name)
            return file
        else:
            continue


def enter_demension():
    while(True):
        print("type 1 for using file, type 2 for using console input for demension")
        selection = int(input())
        if(selection == 2):
            while(True):
                print("Enter demension:")
                demension = int(input())
                if(demension < 1 or demension > 20):
                    print("Demension should be lower than 20 and higher than 0")
                    continue
                else:
                    return demension
        if(selection == 1):
            while(True):
                file = load_file()
                line = file.readline()
                demension = int(line.strip())
                if(demension < 1 or demension > 20):
                    print("Demension should be lower than 20 and higher than 0")
                    continue
                else:
                    return demension
                
            
def enter_accuracy():
    while(True):
        print("type 1 for using file, type 2 for using console input for accuracy")
        selection = int(input())
        if(selection == 2):
            while(True):
                print("Enter accuracy:")
                accuracy = float(input())
                if(accuracy < 0):
                    print("Accuracy higher than 0")
                    continue
                else:
                    return accuracy
        if(selection == 1):
            while(True):
                file = load_file()
                line = file.readline()
                accuracy = float(line.strip())
                if(accuracy < 0):
                    print("Accuracy higher than 0")
                    continue
                else:
                    return accuracy
                

def enter_matrix(n):
     while(True):
        print("type 1 for using file, type 2 for using console input for matrix")
        selection = int(input())
        if(selection == 2):
            while(True):
                print("Enter matrix:")
                A = [[0 for _ in range(n)] for _ in range(n)]
                B = [0 for _ in range(n)]
                for i in range(n):
                    numbers = list(map(float, input().split()))
                    if(len(numbers) != n + 1):
                        print("Lines lenght must be n + 1")
                        exit()
                    A[i] = numbers[:n]
                    B[i] = numbers[n]
                return A, B
        if(selection == 1):
            while(True):
                A = [[0 for _ in range(n)] for _ in range(n)]
                B = [0 for _ in range(n)]
                file = load_file()
                lines = file.readlines()
                if(len(lines) != n):
                    print("Demension of matrix must be n*n+1 ")
                    continue
                for i in range(n):
                    numbers = lines[i].strip().split(" ")
                    if(len(numbers) != n+1):
                        print("Demension of matrix must be n*n+1 " + str(numbers))
                        exit()
                    for j in range(n+1):
                        dummy = float(numbers[j])
                        if(j == n):
                            B[i] = dummy
                        else:
                            A[i][j] = dummy
                return A,B