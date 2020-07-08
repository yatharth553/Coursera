
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        n = int(num)
        if largest is None:
            largest = n
        if smallest is None:
            smallest = n
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
