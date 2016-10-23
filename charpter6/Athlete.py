class Althlete:
    def __init__(self, a_name, a_dob=None, a_times=None):
        if a_times is None:
            a_times = []
        self.a_name = a_name
        self.a_dob = a_dob
        self.a_times = a_times

    def top3(self):
        return sorted(self.a_times)[0:3]

    def add_time(self, tiem):
        print(self.a_times)
        self.a_times.append(tiem)
        return self.a_times

    def all_times(self, times):
        self.a_times.extend(times)
        return self.a_times
