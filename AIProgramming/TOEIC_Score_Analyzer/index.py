toeic_scores =[510, 630, 750, 780, 620, 805, 930, 650, 840, 670]

def frequency(toeic_scores) :
  counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in toeic_scores :
    counters [i // 100]+=1
  return counters

def max_frequency(counters) :
  max = 0
  max_value = 0
  length = len(counters)
  for i in range(length) :
    if max < counters[i] :
      max = counters[i]
      max_value = i * 100
  return max_value, max


def min_frequency(counters):
  min = 100
  min_value = 0
  length = len(counters)
  for i in range(length) :
    if counters[i] == 0:
      continue
    elif min > counters[i]:
      min = counters[i]
      min_value = i * 100
  return min_value, min

counters = frequency(toeic_scores)

max_count, count= max_frequency(counters)
print("가장 많은 점수대 = ", max_count, ", 빈도수 = ",count)

min_count,count = min_frequency(counters)
print("가장 적은 점수대 = ", min_count, ", 빈도수 = ",count)
