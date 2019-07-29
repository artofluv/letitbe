from Plane import Plane
from almosttest import sum_of_shifts
from other_func import monthes, month_in_year, days_in_month, days
plane = Plane('вт')
plane.add_workers('Sasha', 'Vahtang', 'Nick', 'Nina', 'Yana', 'Bek', 'Tort', 'Person', 'Kot', 'Jay', 'Bob', 'Chert')
print(plane.week)
plane.sort_shifts('март')
plane.sort_shifts('апрель')
plane.graphic((11, 'март'), (19, 'апрель'))
#r = 7
#print(month_in_year(monthes[r]))
#prp = (4, 10)
#for z in monthes[prp[0]:prp[1]]:
 #   plane.sort_shifts(z)
  #  print(month_in_year(z))




#for i in plane.workers:
 #   print(i.shift[-1])

#for i in plane.workers:
 #   print(len(i.shift))
  #  print([z for z in i.shift if 212 < z])

#for i in range(200, 244):

   # print(plane.whos_working(i), i)
#for i in range(month_in_year(monthes[prp[0]])[0], month_in_year(monthes[prp[1]])[0]):
 #   print(i, plane.whos_working(i))
  #  if len(plane.whos_working(i)) < 5:
   #     print('ERR!!!!!!!!!!!!!!!', i)

##   print(i.count_shifts())

plane.date(363)