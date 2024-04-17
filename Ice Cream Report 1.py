salesdata = {}
with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            salesdata[flavor] = sales

print(salesdata)