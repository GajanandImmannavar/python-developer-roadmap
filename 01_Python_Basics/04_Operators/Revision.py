
# Problem 1 — Total Seconds

# Store:

# Seconds = 5432

# Print:

# 1 Hours
# 30 Minutes
# 32 Seconds



Seconds = 5432

Hours = Seconds // 3600
Remaining =  Seconds % 3600

Minutes = Remaining // 60
REMAINING = Remaining % 60


print(f"{Hours} Hours ")
print(f"{Minutes} Minutes")
print(f"{REMAINING} Seconds")




# Minutes = 8432

Minutes = 8432
Hours = Minutes // 3600
Remaining = Minutes % 3600
Minutes = Remaining // 60
Sec = Remaining % 60
print(f"{Hours}:Hours {Minutes}:Minutes {Sec}:Seconds")


# Time

# Convert

# 98765 seconds

# into

# Days
# Hours
# Minutes
# Seconds

Seconds = 98765

Day = Seconds // 86400
Remaining = Seconds % 86400

Hours = Remaining // 3600
Left = Remaining % 3600

Minutes = Left // 60
Second = Left % 60


print(f"{Day}: Day {Hours}: Hour {Minutes}:Minutes {Second}: Seconds")

