def solution(board, k):
    total_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                total_sum += board[i][j]
    return total_sum

#이차원 배열 대각선 순회하기