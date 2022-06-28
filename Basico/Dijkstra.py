jewels = set()

while True:
    try:
        jewel = input()
        jewels.add(jewel)
    except:
        break

print(len(jewels))