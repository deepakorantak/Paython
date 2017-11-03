def generate_input():
    x = 1
    print("value of x :" ,str(x))
    for i in range(1,6):
        print("value of i:",str(i))
        x = x * i
        yield x 

my_generator = generate_input()
print("after my generator")
for i in my_generator:
    print(i)


