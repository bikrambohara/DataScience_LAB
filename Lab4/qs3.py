# Create a generator function using the yield keyword that produces numbers from 1 to
# 5 one by one to illustrate how lazy evaluation can save memory when dealing with large
# datasets.
def number_generator():
    for i in range(1, 6):
        yield i #yield returns one number at a time.
print("The numbers from 1 to 5 are:")
for number in number_generator():
    print(number)


