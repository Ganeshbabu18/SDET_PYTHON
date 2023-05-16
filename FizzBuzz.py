# Write a program that, given a number from STDIN, prints out all numbers from 1 to number (inclusive) to STDOUT, each on their own line. But there's a catch:
# For numbers divisible by 3, instead of number, print Fizz
# For numbers divisible by 5, instead of number, print Buzz
# For numbers divisible by 3 and 5, just print FizzBuzz

number = 15

for i in range(1, number+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)