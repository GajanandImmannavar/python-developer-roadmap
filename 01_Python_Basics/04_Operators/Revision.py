
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



