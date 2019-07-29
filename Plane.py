from Worker_class import Worker
from other_func import monthes, month_in_year, days_in_month, by_shift, days

class Plane():
    def __init__(self, January1):
        self.January1 = January1
        self.week =  days[days.index(self.January1):] + days[:days.index(self.January1)]

        self.workers = []

    def add_workers(self, *name_list):
        if len(name_list) > 11:
            for name in name_list:
                self.workers.append(Worker(name))
        else:
            return print('You need at least 12 persons!')

    def free_workers(self, day):
        free = []
        for worker in self.workers:
            if worker.can_work(day) and worker.can_work(day + 1):
                free.append(worker)

        free.sort(key=by_shift)
        free_2 = [wrk.id for wrk in free]
       # print("Ther's id of free workers for day " + str(day) + ':', free_2)
        return list(free)


    def sort_shifts(self, month):
        if month == 'year':
            rng = (1, 366)
        else:
            rng = [month_in_year(month)[0], month_in_year(month)[1]]
        if month in ('январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь'):
            rng[1] += 1

        for day in range(rng[0], rng[1], 2):
            free = self.free_workers(day)
            if len(free) < 5:
                free = self.free_workers(day + 1)
            if len(free) >= 5 or len(self.whos_working(day)) == 5:
                #print(day, 'working', len(self.whos_working(day)))
                for worker in free[:5]:
                    if len(self.whos_working(day)) < 5:
                        worker.workup(day)
                    if len(self.whos_working(day + 1)) < 5:
                        worker.workup(day + 1)
            else:
                print('Not enough workers for shift!')



    def whos_working(self, day):
        working = []
        for worker in self.workers:
            if day in worker.shift:
                working.append(worker.id)
       # print("Ther's id of busy workers for day " + str(day) + ':', working)
        return working

    def day(self, d):
        #print(self.week[d % 7 - 1])
        return self.week[d % 7 - 1]

    def date(self, num):
        res = 0
        for month in monthes:
            res += days_in_month(month)
            if num <= res:
                return (self.day(num), month)

    def graphic(self, start, end):
        '''(day, month), (day, month)'''
        for i in range(month_in_year(start[1])[0] + start[0], month_in_year(end[1])[0] + (end[0] + 1)):
            print(self.date(i)[0], self.date(i)[1], 'working', self.whos_working(i))

    def ill(self, worker, day):
        z = self.free_workers(day)
        print(z)
        z[0].workup(day)
        worker.shift.remove(day)