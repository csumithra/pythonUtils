# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class MyGenerator():
    def func_generate(self, num):
        for i in range(num):
            if i % 7 == 0 :
                yield i


gObj = MyGenerator()
do_generator = gObj.func_generate(30)
for n in do_generator:
    print(n)
