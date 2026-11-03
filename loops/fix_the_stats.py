# fix_the_stats.py
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]
failed = 0

# The error is that `failed = 0` must come before the loop.
for event in events:
    
     if event == "FAILED":

      failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0

for value in minutes:

    if value > 0:
      total += value
      count += 1
# I changed // to / based on the corrected answer , i also deleted the space.
# It should be printed after the turkey is finished, not inside it.
print(f"Average session: {total / count} minutes")

# In answer 4, it is included, so I will set the interval as (1, 5).
for level in range(1, 5):
    print(f"Level {level}")