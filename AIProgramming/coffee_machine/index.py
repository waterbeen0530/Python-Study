print("아메리카노 2500원")
print("카페라테 3000원")
print("카푸치노 3000원")

numA = int(input("아메리카노 개수 (잔) : "))
numL = int(input("카페라테 개수 (잔) : "))
numC = int(input("카푸치노 개수 (잔) : "))

result = ((numA*2500)+(numL*3000)+(numC*3000))
print("총금액 : ", result)

while True :
    money = int(input("금액 입력 : "))

    if money < result :
        print("금액이부족합니다. 다시 입력해주세요.")
        continue
    else :
        break

print("거스름 돈 : ", money-result)
    