def fibonacci(n):
    try:
        a = 0
        b = 1       
        while n > 0:
            temp = a+b
            a = b
            b = temp
            n -= 1
        return temp
    except:
        pass
        

exmpl = [1, 3, 0, 7, 10]
for num in exmpl:
    print(fibonacci(num))
