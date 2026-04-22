class MyCalendar(object):
    def __init__(self):
        self.bookings = []

    def book(self, startTime, endTime):
        for s, e in self.bookings:
            if max(s, startTime) < min(e, endTime):
                return False
        self.bookings.append((startTime, endTime))
        return True