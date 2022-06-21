from random import *
import time

wordList = ["apple", "banana", "orange", "grape", "peak"]

computerThink = ""
personThink = ""

correctCount = 0
chance = 7
checkList = {}

def initCheckList():
    global checkList

    for i in range(0, len(computerThink)):
        checkList[i] = False

def createQuiz():
    global personThink
    global computerThink
    computerThink = wordList[randint(0, len(wordList) -1)]
    personThink = "?" * len(computerThink)

def wordCheck(answer):
    global correctCount
    global personThink
    global checkList
    conversion = False

    for i in range(0, len(computerThink)):
        if answer == computerThink[i] and checkList[i] == False:
            checkList[i] = True
            temp = list(personThink)
            temp[i] = answer
            personThink = "".join(temp)
            conversion = True

    print(checkList)
    if conversion:
        correctCount += 1

def hangmanShow(chance):
    if chance == 1:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│      └│┐")
        print("│      ┌ ┐")
        print("│")
        print("┴")
    elif chance == 2:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│      └│┐")
        print("│        ┐")
        print("│")
        print("┴")
    elif chance == 3:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│      └│┐")
        print("│")
        print("│")
        print("┴")
    elif chance == 4:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│      └│")
        print("│")
        print("│")
        print("┴")
    elif chance == 5:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│       │")
        print("│")
        print("│")
        print("┴")
    elif chance == 6:
        print(" ─────── ")
        print("│       │")
        print("│       Ο")
        print("│")
        print("│")
        print("│")
        print("┴")
    elif chance == 7:
        print(" ─────── ")
        print("│       │")
        print("│")
        print("│")
        print("│")
        print("│")
        print("┴")

def introMessage():
    print("########## Hang Man Game ########## ")
    print("행맨 게임을 시작합니다.영어 단어를 맞춰보세요. ")
    print("주제는 과일 입니다.")
    print("틀릴 때 마다 행맨은 죽어갑니다. ")

introMessage()
hangmanShow(chance)
createQuiz()
initCheckList()

while True:
    print("기회는 {}번 남았습니다.".format(chance))
    print(personThink)
    print("")

    answer = input("알파벳을 입력하세요: ")
    wordCheck(answer)
    hangmanShow(chance)

    chance -= 1

    if "?" not in personThink:
        print("행맨은 살았습니다.")
        time.sleep(5)
        break
    elif chance == 0:
        print("행맨은 죽었습니다.")
        time.sleep(5)
        break

