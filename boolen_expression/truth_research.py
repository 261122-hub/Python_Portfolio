# الملف : truth_research.py 
# هذا البرنامج يختبر القيم المنطقية و العمليات المنطقية و يطبع النتائج
# المصدر : https://docs.python.org/3/builtins/stdtypes.html

# التوقعات : 
# bool("") ----> false لان القيمة فارغة 
# bool("0") ----> true لان النص  غير فارغ ويحتوي ع حرف صفر 
# bool(0) ----> false لان القيمة صفر
# bool(0.0) ----> false "float" لان القيمة صفر كمان بس 
# bool("False") ----> true لان النص غير فارغ ويحتوي ع كلمة 

print(bool(""))
print(bool("0"))
print(bool(0))
print(bool(0.0))
print(bool("False"))