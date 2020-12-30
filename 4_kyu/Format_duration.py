class CountTime:
    def __init__(self, seconds):
        self.seconds = seconds
        self.formatted_time = []

    def __str__(self):
        return ''.join(self.formatted_time)

    def count_years(self):
        if self.seconds / 31536000 >= 1:
            years = int(self.seconds / 31536000)
            self.seconds -= 31536000*years
            if years == 1:
                self.formatted_time.append('{} year'.format(years))
            elif years > 1:
                self.formatted_time.append('{} years'.format(years))

    def count_days(self):
        if self.seconds / 86400 >= 1:
            days = int(self.seconds / 86400)
            self.seconds -= 86400 * days
            if days == 1:
                self.formatted_time.append('{} day'.format(days))
            elif days > 1:
                self.formatted_time.append('{} days'.format(days))

    def count_hours(self):
        if self.seconds / 3600 >= 1:
            hours = int(self.seconds / 3600)
            self.seconds -= 3600 * hours
            if hours == 1:
                self.formatted_time.append('{} hour'.format(hours))
            elif hours > 1:
                self.formatted_time.append('{} hours'.format(hours))

    def count_mins(self):
        if self.seconds / 60 >= 1:
            mins = int(self.seconds / 60)
            self.seconds -= 60 * mins
            if mins == 1:
                self.formatted_time.append('{} minute'.format(mins))
            elif mins > 1:
                self.formatted_time.append('{} minutes'.format(mins))

    def count_secs(self):
        if self.seconds > 1:
            self.formatted_time.append('{} seconds'.format(self.seconds))
        elif self.seconds == 1:
            self.formatted_time.append('{} second'.format(self.seconds))

    def format_time(self):
        self.count_years()
        self.count_days()
        self.count_hours()
        self.count_mins()
        self.count_secs()


def format_duration(seconds):
    time = CountTime(seconds)
    time.format_time()
    if len(time.formatted_time) == 1:
        return ''.join(time.formatted_time)
    elif len(time.formatted_time) == 0:
        return 'now'
    else:
        return ', '.join(time.formatted_time[:-1]).strip(', ') + ' and {}'.format(time.formatted_time[-1])


print(format_duration(0))
