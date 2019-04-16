from sys import stdout
import datetime
today = datetime.datetime.now()
class A:
    def __repr__(self):
        return "天行健,君子以自强不息."
#stdout.write(today.__repr__())
#stdout.write(today.__str__())
for i in range(1, 8, 2):
    print("{:^7}".format("*"*i))
for j in range(5, 0, -2):
    print("{:^7}".format("*"*j))
x = 1234567
x = "{:,}".format(x)
a, b, c = str(x).split(",")
print(a)