def check_day(plane):
    err = 0
    for i in range(1, 366):
        res = 0
        for worker in plane.workers:
            if i in worker.shift:
                res += 1
        if res != 5:
            err += 1
            print(i, res)

    if err == 0:
        print('No errs')

def check_weekends(plane):
    err = 0
    for worker in plane.workers:
        shifts = worker.shift
        if shifts[0] != shifts[1] - 1:
            err += 1
            print('Check days pair!')
        for i in range(2):
            shifts.pop(0)
            if shifts.pop(0) + 2 in shifts:
                err += 1
                print('Error with wwek!', shifts.pop(0), worker.id)

    if err == 0:
        print('No errs')

def sum_of_shifts(plane):
    res = 0
    for worker in plane.workers:
        res += len(worker.shift)
    return print(res)
