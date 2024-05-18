import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

numbers_req = int(input("Enter the number of digits you want to choose for your OTP: "))

otp_list = []

for number in range(1, numbers_req + 1):
    otp_list.append(random.choice(numbers))
       
otp_1 = map(str, otp_list)   
print(list(otp_1))

otp_final = ""

for number in otp_1:
    otp_final += number
    
print(otp_final)

    