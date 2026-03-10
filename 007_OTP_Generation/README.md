##### Random is a built-in Python module.
It helps you generate:

- Random numbers

- Random choices

- Random strings

1. Simple OTP Generation:
' import random

otp = random.randint(1000, 9999)
print(otp) '


2. Better OTP (Using Digits)
' import random
import string

otp = ''.join(random.choices(string.digits, k=6))
print(otp) '

Important for REAL APPS:
----
random module is NOT secure for real OTP systems.

'
import secrets

otp = ''.join(secrets.choice("0123456789") for _ in range(6))
print(otp) '


### Generating OTP:
1. user giving input on the server through send.html page
2. using Generate_otp method inside the folder the random otp is generated and it will be printed on the console
3. Giving otp in the verify.html page 
4. checking the otp is valid or not [session['otp']== otp (user given otp)]
5. If condition is true then Valid and condition false then Invalid

note: Check the folder structure to test the cases
