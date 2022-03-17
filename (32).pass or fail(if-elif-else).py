per=float(input('Enter you percentage'))
if per>85:
    print('Grade A')
elif per>70 and per<=85:
    print('Grade B')
elif per>60 and per<=70:
    print('Grade C')
elif per>45 and per<=60:
    print('Grade D')
elif per>33 and per<=45:
    print('Grade E')
else:
    print('FAIL')
