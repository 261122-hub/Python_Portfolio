Seconds=int(input("session length in seconds:"))
minutes = Seconds//60
ramaning_seconds = Seconds%60
print(f"session length in seconds : {minutes} minutes and {ramaning_seconds} seconds")

# 905----- min = 15  sec = 5
# 60 ----- min = 1   sec = 0
# 59 ----- min = 0   sec = 59