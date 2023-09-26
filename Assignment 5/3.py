s = input()
if len(s)<2:
    print('empty string')
else:
    result=s[:2]+s[-2:]
    print(result)