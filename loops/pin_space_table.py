# pin_space_table.py
# # Program to calculate the time required to guess PINs of 4 to 8 digits.

GUESSES_PER_SECOND = 10
digits = [100, 1000, 10000, 100000, 1000000,]

for digit in range(4, 9):
   pins = 10 ** digit
   seconds = pins // GUESSES_PER_SECOND
   time_minutes = seconds // 60
   hours = time_minutes // 60
   days = hours // 24

   print(f"{digit} digits: {pins} PINs, {time_minutes} minutes, {days} days")


