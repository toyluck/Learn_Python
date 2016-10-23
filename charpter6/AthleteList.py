class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=None):
        if a_times is None:
            a_times = []
        list.__init__([])
        self.a_name = a_name
        self.a_dob = a_dob
        """
           类似于继承自list
        """
        self.extend(a_times)

    def top3(self):
        return sorted(self)[0:3]

    def add_time(self, tiem):
        self.append(tiem)
        return self

    def all_times(self, times):
        self.extend(times)
        return self
