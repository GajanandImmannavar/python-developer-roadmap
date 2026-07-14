#  How to convert Minutes to Hours  (Using "//" and "%")
Time  = 135
min = 60
Hour = Time // min
Min_1 = Time % min
print(f"{Hour} Hours {Min_1} Minutes\n")

# You have: seconds = 367  Convert into: minutes and remaining seconds 

Sec = 367
m = 367 // 60 
SEC = 367 % 60
print(f"{m} minutes {SEC} sec")

#  Convert Seconds to Hours, Minutes, Seconds You are given: seconds = 7384

Total_Minutes = 7384

hours = Total_Minutes // 3600
Remaining_Minutes = Total_Minutes % 3600

Minutes = Remaining_Minutes // 60
Remaining_Sec  = Remaining_Minutes % 60

print(f"{hours} Hours {Minutes} Minutes {Remaining_Sec} Seconds")
