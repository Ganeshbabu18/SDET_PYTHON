# Python program to check if the number is an Armstrong number or not
class ArmStrong():
 def arm_strong(self):
    num = 371
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
armstrong_number = ArmStrong()
armstrong_number.arm_strong()
