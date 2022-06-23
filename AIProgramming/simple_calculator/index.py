value = 0

while(True) :
  print("현재 값 : ",  value)
  work = input("작업 명령 입력 : ") 
  oper = work.split()

  if (len(oper) == 2) and (oper[0] ==  "+" or "*" or "/" or "%" or "=") :
    check_value = float(oper[1])
    if oper[0] == "=" :
      value = check_value

    elif oper[0] == "%" :
      value %= check_value

    elif oper[0] == "/" :
      if check_value == 0 :
        print("잘못된 명령 입력!!(0으로 나누기)")
        continue
      else :
        value /= check_value

    elif oper[0] == "*" :
      value *= check_value

    elif oper[0] == "+" :
      value += check_value

  elif oper[0] == "X" and len(oper) == 1:
    break

  else : 
    print("잘못된 작업 입력!!")
    continue
    








