# Nisdalie doncell 10/1/25
# import random
#
# Num = [random.randint(1, 100) for a in range(10)]
# print(Num)
#
# for a in range(len(Num)):
#     for i in range(len(Num) - 1):
#         j = i + 1
#         if Num[i] > Num[j]:
#             Num[j], Num[i] = Num[i], Num[j]
#
# print(Num)

import random

Num = [random.randint(1, 100) for a in range(10)]
print(Num)
outer_pass = 0
inner_pass = 0
Z = len(Num)
# kinda going thru zero thru 100 yeah, subtractin the last value to check each time
# ohhh, thats how it's apart of the loop and removing each loop section I FORGOT
# OKAY KEWL
for i in range(Z-1):
    outer_pass += 1
    for j in range(Z-i-1):
        inner_pass += 1
        if Num[j] > Num[j+1]:
            #SO IF IT IS ACTUALLY GREATER,
            # and the assumption made, we kinda suffle about okayyy
            #the guy of the computer that sort short it yay.
            # temp variable i do not get 2 much scary
            #I do need to get the logic paired with the code, like how to
            #associate the code with the logic, why does it do it hm.
            #wait hello bro,,,,, :eyes:
            Num[j], Num[j+1] = Num[j+1], Num[j]
print("SEPERATEEE")

print("OUTER:", outer_pass)
print("INNER", inner_pass)
print("j", j)
print("i", i)
print(Num)
# I do and dont get the logic :-(
#looks like its being mutiplied almost, the number okay i see, inner twice, or atleast, more but outer search = less than the
#innerouter less bc thats the part subtracting
#inner more, bc it is the range self i think