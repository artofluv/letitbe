def previous_month_workers(self, month):
    if month == 'январь':
        return print('This is start of a new year')
    elif month in monthes:
        last_day = []
        before_last_day = []
        for worker in self.workers:
            if month_in_year(month)[0] - 1 in worker.shift:
                last_day.append(worker.id)
            if month_in_year(month)[0] - 2 in worker.shift:
                before_last_day.append(worker.id)
        # print(days_in_month(monthes[monthes.index(month) - 1]), monthes[monthes.index(month) - 1], 'working', last_day)
        # print(days_in_month(monthes[monthes.index(month) - 1]) - 1, monthes[monthes.index(month) - 1], 'working', before_last_day)
        return (last_day, before_last_day)
    else:
        print('No month with name ' + month + '!')



    def dayoffs(self):
        #print([day + 2 for day in self.shift])
        return [day + 2 for day in self.shift]



        self.worker_1 = Worker(1)
        self.worker_2 = Worker(2)
        self.worker_3 = Worker(3)
        self.worker_4 = Worker(4)
        self.worker_5 = Worker(5)
        self.worker_6 = Worker(6)
        self.worker_7 = Worker(7)
        self.worker_8 = Worker(8)
        self.worker_9 = Worker(9)
        self.worker_10 = Worker(10)
        self.worker_11 = Worker(11)
        self.worker_12 = Worker(12)

        self.workers = [self.worker_1, self.worker_2, self.worker_3, self.worker_4, self.worker_5, self.worker_6,
                        self.worker_7, self.worker_8, self.worker_9, self.worker_10, self.worker_11, self.worker_12
                        ]
