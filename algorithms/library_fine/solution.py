from datetime import datetime

returned = datetime.strptime(input(), "%d %m %Y")
expected = datetime.strptime(input(), "%d %m %Y")

if returned <= expected:
    print("0")
elif returned.year <= expected.year and returned.month <= expected.month:
    print(15 * (returned.day - expected.day))
elif returned.year <= expected.year:
    print(500 * (returned.month - expected.month))
else:
    print("10000")
