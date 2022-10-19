def snake(board_size, a_number, apple_info_list, moving_info_list):

    board = [[0]*board_size for i in range(board_size)]

    row_dir = [1,-1,0,0]
    col_dir =[0,0 ,1, -1]

    print(board_size)
    print(a_number)
    print(apple_info_list)
    print(moving_info_list)

    for i in apple_info_list:
        col_info = int(i[0])
        row_info = int(i[1])

        board[col_info][row_info] = 1

    for i in board:
        for j in i:
            print(j, end=" ")
        print()

    return 0;


board_size = int(input())
a_number = int(input())
apple_info_list = []

for _ in range(a_number):
    apple_info = list(map(int, input().split()))
    apple_info_list.append(apple_info)


d_change_number = int(input())
moving_info_list = []

for _ in range(d_change_number) :
    change_info = input().split()
    moving_info_list.append(change_info)

snake(board_size, a_number, apple_info_list, moving_info_list)

