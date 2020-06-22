def fib(n, maxNum):
  if n == 1:
    return [1]
  elif n == 2:
    return [1,2]
  else:
    x = fib(n-1, maxNum)
    if sum(x[:-3:-1]) > maxNum:
     return x
    x.append(sum(x[:-3:-1]))
    return x

def getSum(n, maxNum):
  fibSeq = fib(n, maxNum)
  sum = 0
  for i in range(0, len(fibSeq)):
    if fibSeq[i] % 2 == 0:
      sum += fibSeq[i]
  return sum

print(getSum(100, 4000000))
