def fibonacciSeries(i):
 if i<=1:
    return i
 else:
  return fibonacciSeries(i - 1)+ fibonacciSeries(i - 2)
 num=10
 if num<=0:
     print("please enter a positive number")
 else:
     print("Fibonacci Series:",end="")
     for i in range(num):
         print(fibonacciSeries(i),end="")


