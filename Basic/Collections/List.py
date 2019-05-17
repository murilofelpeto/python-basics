friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[0])

print(friends[1:])
print(friends[1:3])
print(friends[-1])

luckyNumbers = [4,8,15,16,23,42]

friends.extend(luckyNumbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Murilo")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop() #remove last element
print(friends)

print(friends.index("Toby"))

friends.sort()
luckyNumbers.reverse()
print(friends)
print(luckyNumbers)
