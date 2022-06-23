import random

print("나랑 숫자 추측 게임을 해 보자")
print("네 이름은 뭐니?")
name = input()
print("반가워.", name, "내가 1부터 30 사이의 수를 가지고 있어. 맞혀봐.")
print("5번만에 맞혀야 돼.")

while True:
  number = random.randint(1,30)
  sum = 5
  for _ in range(5) :
      print("추측한 숫자를 입력하세요 -> ")
      guess = int(input())
      sum -= 1
      if guess == number :
          print(sum, "번만에 맞혔어요!! 축하해요.")
          break
      
      elif sum == 0 :
          print("5번 지남 ㅅㄱ") 
          print(f"정답은 {number} 입니다~")
          break
      
      else :
          print("틀림 ㅅㄱ")
          if number < guess :
            print("down")
          elif number > guess :
            print("up")
          print(sum,"번 기회 있음")

  good_choice=False
  while True:
    print("게임을 다시 할까요?(YES or NO)")
    re = input()
    if re.upper() == "YES" :
        good_choice=True
        break
    elif re.upper() == "NO" :
      good_choice=False
      break
    else :
      print("YES 또는 NO로 입력 좀 해주세요.")
      continue
  if good_choice==False:
    break


