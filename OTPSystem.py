import math
import random

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lent = len(string)
otp = ""

#range will decide the length of the OTP
for i in range(7):
    otp += string[math.floor(random.random() * lent)]

print("The 6-digit OTP is:", otp)
