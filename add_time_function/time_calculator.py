def sperate_time(timestr):
    time_list = timestr.split(':')
    for k, item in enumerate(time_list):
        time_list[k] = int(item)
    return time_list


def seperate_time_str(timestr):
    time, am_or_pm = timestr.split(' ')
    time_list = sperate_time(time)
    for k, item in enumerate(time_list):
        time_list[k] = int(item)
    time_list.append(am_or_pm)
    return time_list


def add_time(start, duration, day_of_week=None):
    s_tuple = seperate_time_str(start)
    d_tuple = sperate_time(duration)
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    new_list = [0, 0, 0]
    if s_tuple[2] == 'PM':
        s_tuple[0] += 12

    new_list[0] = s_tuple[0] + d_tuple[0]
    new_list[1] = s_tuple[1] + d_tuple[1]
    n_days_later = 0

    print(new_list)
    if new_list[1] > 59:
        new_list[0] +=new_list[1] // 60
        new_list[1] = new_list[1] % 60
    if new_list[0] > 23:
        n_days_later = new_list[0] // 24
        new_list[0] = new_list[0] % 24

    if new_list[0] > 11:
        new_list[0] -= 12
        new_list[2] = 'PM'
    else:
        new_list[2] = 'AM'

    if new_list[0] == 0:
        new_list[0] = 12

    if new_list[1] < 10:
        result = str(new_list[0]) + ':0' + str(new_list[1]) + ' ' + str(new_list[2])
    else:
        result = str(new_list[0]) + ':' + str(new_list[1]) + ' ' + str(new_list[2])

    if day_of_week != None:
        index = weekdays.index(day_of_week.lower())
        next_day_of_week = weekdays[(index + n_days_later) % 7]
        result += ', '+ next_day_of_week.capitalize()

    if n_days_later != 0:
        if n_days_later == 1:
            result += ' (next day)'
        else:
            result += ' (' + str(n_days_later) + ' days later)'
    return result
