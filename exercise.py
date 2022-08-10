# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

#---- Task 1 - Basic math operators ----#

# for n in range(0, 3):
#     user_number = int(input("Please choose a number: "))
#     print(user_number)
#     if user_number % 2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")

#---- Task 2 ----#

# start_num = end_num = step = 1

# user_range = int(input("Enter number of arguments to use (between 1 and 3): "))
# if user_range > 0:
#     start_num = int(input("Choose your starting number: "))
# if user_range > 1:
#     end_num = int(input("Choose your stopping number: "))
# if user_range > 2:
#     step = int(input("Choose your step number: "))

# for n in range(start_num, end_num+1, step):
#     print(n)


#---- Task 3 ----#

# user_num = int(input("Please choose a number: "))

# for n in range (1, user_num):
#     if user_num % n == 0:
#         print(n)
    
#--- Task 4 ---#

# user_num = int(input("Please choose a number: "))

# prime = True

# for n in range (2, user_num):
#     if user_num % n == 0:
#         prime = False

# if prime == True:
#     print(f"{user_num} is a prime number")
# else:
#     print(f"{user_num} is not a prime number")


#---- Task 5 ----#

# for n in range (0,100):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         (print(n))
    
#---- Task 6 ----#
for n in range (1000, 2001):
    if n % 7 == 0 and n % 5 != 0:
        print(n)


