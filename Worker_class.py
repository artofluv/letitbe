class Worker():
    def __init__(self, name):
        self.id = name
        self.shift = []

    def workup(self, a):
        '''add day as a shift'''
        self.shift.append(a)

    def count_shifts(self):
        #print('Worker', self.id, 'has', len(self.shift), 'shifts')
        return len(self.shift)

    def can_work(self, day):
        if 0 < day < 367:
            z, y = 2, 3
            if day < 3:
                z = day - 1
            if day > 363:
                y = 366 - day
            if set(i for i in range(day - z, day + y)).isdisjoint(set(self.shift)):
                #print('Worker', self.id, 'can work in day ', day)
                return True
            else:
                #print('Worker', self.id, "can't work in day ", day)
                return False
        else:
            return print('No such day in the month!', day)
