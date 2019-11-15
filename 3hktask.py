import re

def hackerrankInString(s):
    pattern = ".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*"
    m = re.search(pattern, s)
    if m is not None:
        print('YES')
    else:
        print("NO")

hackerrankInString('hhaacckkekraraannk')