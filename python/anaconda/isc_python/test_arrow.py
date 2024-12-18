'''
conda install conda-forge::arrow
'''

import arrow

now = arrow.now()
print(now)
print(now.format('DD-MM-YYYY HH:mm:ss'))

plus_1_week = now.shift(weeks=1)
print(plus_1_week)
hier = now.shift(days=-1)
print(hier)

if plus_1_week > hier:
    print('Ok')

utc_now = arrow.utcnow()
print(utc_now)
print('Local :', utc_now.to('Asia/Shanghai'))

timestamp = 1703467200
date = arrow.get(timestamp)
print(date)

debut = arrow.get('01/01/2024', 'DD/MM/YYYY')
fin = arrow.get('08/01/2024', 'DD/MM/YYYY')

for date in arrow.Arrow.range('day', debut, fin):
    print(date)

humain = debut.humanize(locale='fr')
print(humain)
