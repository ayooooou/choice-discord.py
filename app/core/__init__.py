class Choice():
    def __init__(self,founder, option_num, num):
        self.founder = founder
        self.option_num = option_num
        self.num = num
        self.option_name = []
        self.people = {}
        self.result = []
    def to_dict(self):
        return self.__dict__

