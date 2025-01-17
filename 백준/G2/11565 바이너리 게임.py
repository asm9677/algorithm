'''
문제
준민이는 세계적인 프로그래머 백준이, 선영이와 함께 낚시를 즐기고 있었다. 3시간 동안 고기가 낚이지 않자, 지루함을 느낀 그들은 준민이를 놀리기 위해 바이너리 게임을 시작했다! 게임의 룰은 다음과 같다.

먼저 백준이와 선영이는 0과 1로만 이루어진 문자열 a, b를 만들어 준민이에게 준다. 준민이는 받은 문자열 a를 b로 변형시켜야 승리하는데, 변형은 다음의 2개의 연산을 여러 번 반복하여 사용하는 식으로 이루어진다.

문자열 a의 맨 앞에 있는 문자를 뺄 수 있다. 예를 들어, (1001 → 001)이 가능하다. a가 빈 문자열이면 더 이상 뺄 수 없다.
문자열 a의 맨 끝에 parity(a)를 추가할 수 있다. 예를 들어, (1000 → 10001)이 가능하다. parity(a)는 문자열 a에 들어있는 1의 개수가 홀수개이면 1이고, 나머지 경우에는 0이다.
게임을 잘 못하는 준민이는 당신에게 게임의 승리 가능 여부를 물어봤다. 프로그래밍을 잘하는 당신은 불쌍한 준민이를 위해, binary string (0과 1로 이루어진 문자열) a, b를 보고 준민이의 승리 가능성을 알려주는 프로그램을 작성하려 한다.

입력
첫 번째 줄에는 문자열 a, 두 번째 줄에는 문자열 b가 주어진다. 두 문자열은 0과 1로만 이루어져 있으며, 문자열 a와 문자열 b의 길이는 1 이상 1,000 이하이다.

출력
준민이가 승리할 수 있으면 VICTORY, 아니면 DEFEAT를 출력한다.

예제 입력 1 
01011
0110
예제 출력 1 
VICTORY
예제 입력 2 
0011
1110
예제 출력 2 
DEFEAT
'''
'''
시간 복잡도: O(N)
1의 개수를 늘리기 위해선 1의 개수가 홀수개여야만하고 1개를 늘리는 순간 짝수개가 되므로 더이상 늘릴 수가 없다.
문자열 b의 1의 개수가 a보다 적다면 0의 개수는 무한히 늘릴 수 있으므로 문자열의 길이가 아닌 1의 개수만 체크해주면 된다.
'''

src,des = input(),input()

srcCount,desCount = src.count("1"), des.count("1")
srcCount += srcCount % 2

print("VICTORY" if srcCount >= desCount else "DEFEAT")