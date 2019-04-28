from operator import attrgetter
from itertools import groupby
from operator import itemgetter
from itertools import compress

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"user({self.user_id})"

    def sort_notcompare(self):
        global users
        users = [User(23), User(3), User(99)]
        print(users)
        print(sorted(users, key=lambda u: u.user_id))


def group_():
    rows = [
        {"address": "5412 N CLARK", "date": "07/01/2012"},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


def filtter_list():
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    # 先创建了一个boolean 序列,指示哪些元素符合条件
    print(more5)  # >>[False, False, True, False, False, True, True, False]
    # 把more5中对应位置为True的adresses输出到列表中
    print(list(compress(addresses, more5)))
    # >>['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']

def main():
    filtter_list()
    group_()
    # 将不支持进行比较的User类通过 attrgetter 来进行比较
    users = [User(23), User(3), User(99)]
    print(sorted(users, key=attrgetter('user_id')))



if __name__ == "__main__":
    main()