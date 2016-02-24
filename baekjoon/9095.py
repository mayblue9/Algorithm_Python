"""
1, 2, 3 더하기
한국어 원문 문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	1326	923	701	68.725%
문제
정수 4를 1, 2, 3의 조합으로 나타내는 방법은 총 7가지가 있다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫쨰 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1,2,3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력  복사
3
4
7
10
예제 출력  복사
7
44
274
"""

# D[N] = D[n-1] + D[n-2] + D[n-3]  DP 점화식

num_of_input = int(input())

for _ in range(num_of_input):
    n = int(input())
    d = [0] *(n+1)                 #중복되는 내용 메모

    def sum(n):
        if(n == 1 or n == 0):      #기저 포인트
            return 1
        elif(n < 0):
            return 0
        if(d[n] > 0):
            return d[n]

        d[n] = sum(n-1) + sum(n-2) + sum(n-3)
        return d[n]

    print(sum(n))



