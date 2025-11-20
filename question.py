'''Name= Anshika Kumari
Enrollment=0157AL231033
Batch: 5 (MTF) 
Batch Time: 10:30 – 12:10'''

#Basic If–Else Problems:
'1.Write a program to check whether a number is positive, negative, or zero.'
num = int(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

'2. Write a program to check whether a number is even or odd.'
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

'3. Write a program to check if a given year is a leap year or not.'
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

'4. Write a program to find the greatest of two numbers.'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
   print("Both numbers are equal")

'5. Write a program to check whether a person is eligible to vote (age >= 18).'
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

'6. Write a program to check whether a given character is a vowel or consonant.'
ch = input("Enter a character: ").lower()
if ch in ('a', 'e', 'i', 'o', 'u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

'7. Write a program to check if a number is divisible by 5.'
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 5")

'8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.'
num = int(input("Enter a number: "))
if -9 <= num <= 9:
    print("Single-digit number")
elif -99 <= num <= 99:
    print("Two-digit number")
else:
    print("More than two-digit number")

'9. Write a program to check whether a student has passed or failed (passing marks = 40).'
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("You have Passed")
else:
    print("You have Failed")

'10. Write a program to find whether the entered number is a multiple of both 3 and 7.'
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print(num, "is a multiple of both 3 and 7")
else:
    print(num, "is NOT a multiple of both 3 and 7")

#Ladder If & Nested If:

'1. Write a program to find the greatest among three numbers.'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
  print(a, "is the greatest number")
elif b >= a and b >= c:
  print(b, "is the greatest number")
else:
   print(c, "is the greatest number")

'2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).'
age = int(input("Enter age: "))
if age >= 0 and age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior")
else:
    print("Invalid age! Age cannot be negative.")

'3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.'
marks = int(input("Enter marks (0-100): "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 75 <= marks < 90:
    print("Grade: B")
elif 50 <= marks < 75:
    print("Grade: C")
elif 35 <= marks < 50:
    print("Grade: D")
elif 0 <= marks < 35:
    print("Grade: Fail")
else:
    print("Invalid marks.")

'4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.'
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
'5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.'
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

'6. Write a program to calculate electricity bill based on units:Up to 100 units: ₹5 per unit, 101–200 units: ₹7 per unit, Above 200 units: ₹10 per unit.'

units = int(input("Enter electricity units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total Electricity Bill: ₹", bill)
'7. Write a program to determine the largest of four numbers using nested if.'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
if a > b:
    if a > c:
        if a > d:
            largest = a
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d
else:
    if b > c:
        if b > d:
            largest = b
        else:
            largest = d
    else:
        if c > d:
            largest = c
        else:
            largest = d
print("Largest number is:", largest)
'8. Write a program to check if a given year is a century year and also a leap year.'
year = int(input("Enter a year: "))
if year % 100 == 0:
    print(year, "is a Century Year")
else:
    print(year, "is NOT a Century Year")
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is also a Leap Year")
else:
    print(year, "is NOT a Leap Year")

'9. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).'
bmi = float(input("Enter BMI value: "))
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
'10. Write a program to display the smallest number among three using nested if.'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        print("The smallest number is:", a)
    else:
        print("The smallest number is:", c)
else:
    if b < c:
        print("The smallest number is:", b)
    else:
        print("The smallest number is:", c)

#For Loop Problems:

'1. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: sum of cubes of digits equals the number itself. Example: 153 => 13+53+33 = 153).'
print("Armstrong numbers between 100 and 999:")
for num in range(100, 1000):
    sum_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_cubes += digit ** 3
        temp //= 10
    if sum_cubes == num:
        print(num)
'2. Write a program to generate and display the first n prime numbers using a for loop.'
n = int(input("Enter how many prime numbers to generate: "))
count = 0
num = 2
while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
'3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.'
for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = sum(int(digit) for digit in str(num))  
        if digit_sum <= 10:
            print(num)
'''4. Write a program using a for loop to print a pyramid of stars (*) of height n. Example for n=4: 
* 
*** 
***** 
*******'''
n = int(input("Enter height of pyramid: "))
for i in range(1, n + 1):
    print("*" * (2 * i - 1))
'5. Write a program to accept a string and check whether it is a pangram (contains all 26 alphabets at least once) using a for loop.'
text = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for ch in alphabet:
    if ch not in text:
        print("Not a Pangram")
        break
else:
    print("It is a Pangram")
'6. Write a program using a for loop to print all twin primes between 1 and 100. (Twin primes: pairs of prime numbers with a difference of 2, e.g., (3,5), (11,13)). '
for num in range(2, 99):  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        # check if num+2 is prime
        for j in range(2, int((num + 2)**0.5) + 1):
            if (num + 2) % j == 0:
                break
        else:
            print(f"({num}, {num + 2})")
'7. Write a program that accepts a number from the user and prints whether it is a Harshad number (number divisible by the sum of its digits) using a for loop. '
num = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(num))
if num % digit_sum == 0:
    print(num, "is a Harshad Number")
else:
    print(num, "is NOT a Harshad Number")
'8. Write a program to generate Pascal’s Triangle up to n rows using a for loop.'
n = int(input("Enter number of rows: "))
for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)  
    print()
'9. Write a program using a for loop to display the sum of the series: 12 + 22 + 32 + ... + n2 .'
n = int(input("Enter the value of n: "))
total = 0

for i in range(1, n + 1):
    total += i ** 2  # add square of i to total

print("Sum of the series:", total)
'10. Write a program that accepts a number from the user and prints whether it is a Strong number (sum of factorials of digits = number itself) using a for loop. Example: 145 => 1! + 4! + 5! = 145. '

num = int(input("Enter a number: ")) 
s = 0 
for digit in str(num): 
   fact = 1 
for i in range(1, int(digit)+1): 
   fact *= i 
s += fact 
if s == num: 
        print("Strong Number") 
else: 
     print("Not a Strong Number")

#While Loop Problems:
'11.Write a program using a while loop to find the reverse of a number and check if the reversed number is prime. Example: Input = 73 → Reverse = 37 → Prime.'
num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reversed Number:", reverse)
if reverse > 1:
    for i in range(2, int(reverse ** 0.5) + 1):
        if reverse % i == 0:
            print(reverse, "is NOT a Prime Number")
    else:
        print(reverse, "is a Prime Number")
else:
    print(reverse, "is NOT a Prime Number")
'12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.'
total_sum = 0  
while total_sum <= 100:
    num = int(input("Enter a number: "))
    digit_sum = sum(int(digit) for digit in str(num))
    total_sum += digit_sum  # Add to total sum
    print("Sum of digits of this number:", digit_sum)
    print("Total sum so far:", total_sum)
print("Stopped! The total sum of digits is greater than 100.")
'13. Write a program using a while loop to check whether a number is a Duck number (a number containing zero but not starting with zero, e.g., 202, 1203). '
num = int(input("Enter a number: "))
temp = num
is_duck = False

while temp > 0:
    digit = temp % 10
    if digit == 0:
        is_duck = True
    temp //= 10

if is_duck and str(num)[0] != '0':
    print(num, "is a Duck Number")
else:
    print(num, "is NOT a Duck Number")                                                                      
'14. Write a program using a while loop to accept a number and check if it is a Happy number. (A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1). Example: 19 is a happy number.  '
num = int(input("Enter a number: "))
seen = set()
while num != 1 and num not in seen:
    seen.add(num)
    temp = num
    sum_sq = 0
    while temp > 0:
        digit = temp % 10
        sum_sq += digit ** 2
        temp //= 10
    num = sum_sq
if num == 1:
    print("It is a Happy Number")
else:
    print("It is NOT a Happy Number")                                                                                                                    
'15. Write a   program using a while loop to find the largest prime factor of a given number.'   
num = int(input("Enter a number: "))
i = 2
largest = 0
temp = num
while temp > 1:
    if temp % i == 0:
        largest = i
        temp //= i
    else:
        i += 1
print("Largest Prime Factor:", largest)     
'16.Write a program to repeatedly accept a string from the user until the string entered is a palindrome.     '
while True:
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome entered:", s)
        break
    else:
        print("Not a palindrome, try again.")
'17. Write a program using a while loop to compute the sum of digits of a number until the result becomes a  single-digit number (Digital root). Example: 9875 => 9+8+7+5=29 => 2+9=11 => 1+1=2. '  
num = int(input("Enter a number: "))
while num >= 10:
    sum_digits = 0
    temp = num
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    num = sum_digits
print("Digital Root:", num)             
'18. Write a program using a while loop to generate the Collatz sequence for a given number. (Rule: If n is even => n/2, if odd => 3n+1. Continue until n=1).   '
n = int(input("Enter a number: "))
print("Collatz sequence:", end=" ")
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(1)            
'''19. Write a program using a while loop to accept a number and check whether it is a Kaprekar number.
(Kaprekar number: if square of the number can be split into two parts whose sum equals the number.
Example: 452=2025 => 20+25=45).   '''    
num = int(input("Enter a number: "))
square = num ** 2
str_sq = str(square)
d = len(str(num))
right = int(str_sq[-d:])
left = int(str_sq[:-d]) if str_sq[:-d] != '' else 0
if left + right == num:
    print(num, "is a Kaprekar Number")
else:
    print(num, "is NOT a Kaprekar Number")  
''' 20. Write a program to simulate an ATM machine using a while loop where a user can:
• Check balance
• Deposit money
• Withdraw money (only if balance is sufficient)
• Exit'''
balance = 1000  
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Balance: ₹", balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited. New Balance: ₹", balance)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn. New Balance: ₹", balance)
        else:
            print("Insufficient balance!")
    elif choice == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

