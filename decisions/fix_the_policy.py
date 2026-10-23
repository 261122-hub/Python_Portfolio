# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# syntax ----> :ناسي ال 
if len(password) < MIN_LENGTH: 
    print("- Too short.")
# semantic ----> طبعت الاول بس elif  في الجواب الي ع يمين السؤال ظاهر جواب الشرطين لو كانت 
if password == username: 
    print("- Same as the username.") 

# semantic
if len(password) >= 16:
    strength = "long"  
# المفروض هاي تيجي مكان ل 12 لانه اي عدد اكبر من 16 
# lراح تطبع الشرط الاول لانه العدد بكون اكبر من 12  وهيك الكشرط الثاني ملوش لزو

elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
print(f"Length: {len(password)} ({strength})")    

# semantic -----> لانه اذا تحقق واحد من 3 شروط الي فوق ما بطبع اشي print  لازم نزيل المسافات الي قبل 