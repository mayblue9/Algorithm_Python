"""
Sum
한국어 원문 문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	2777	1991	1746	74.647%
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.

예제 입력  복사
3
예제 출력  복사
6
"""

n = int(input())

sum = 0
for i in range(n+1):
    sum += i
print(sum)