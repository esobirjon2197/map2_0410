
# 11-m
roy = [1, '2', 3, '4', 5]
print(roy)

t = str(map(lambda el: el.abs(), roy))
print(t)


# 12-m
roy = input("Son kirit: ")

t = list(map(lambda el: el ** 2, roy))
print(t)


# 13-m
roy = ["salom dunyo"]
print(roy)

t = list(map(lambda el: f"{el}!", roy))
print(t)


# 14-m
roy = [1, 2, 3, 4, 5]
roy2 = [1, 2, 3, 4, 5]
roy3 = [1, 2, 3, 4, 5]
print(roy)
print(roy2)
print(roy3)

t = list(map(lambda a, b, c: a + b + c, roy, roy2, roy3))
print(t)


# 15-m
roy = [1.2, 2.3, 3.4, 4.5, 5.6]
print(roy)

t = list(map(lambda el: el // 2, roy))
print(t)


# 16-m
roy = ["SALOM DUNYO"]
print(roy)

t = list(map(lambda el: el.lower(), roy))
print(t)


# 17-m
roy = [1, 2, 3, 4, 5]
print(roy)

t = list(map(lambda el: f"{el}%", roy))
print(t)


# 18-m
roy = ["salom dunyo"]
print(roy)

t = list(map(lambda el: el[-1], roy))
print(t)


# 19-m
roy = [1, 2, 3, 4, 5]
print(roy)

t = list(map(lambda el: bin(el), roy))
print(t)

