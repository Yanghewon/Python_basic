# Chapter10-1
# Hangman(행맨) 미니 게임 제작(1)
# 기본 프로그램 제작 및 테스트

import time

# 처음 인사
name = input("What is your name? ")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 단언
word = "secret"

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 획수
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print("_", end=' ')
            failed += 1
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        print('Congrateulations! The Guesses is correct.')
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input("guess a charater.")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, 'more guesses!')

        if turns == 0:
            # 실패 메시지
            print("You hangman gane failed")


























