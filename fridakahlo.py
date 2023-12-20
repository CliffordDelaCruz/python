#fridakahlo.py
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]

dates = [1939, 1933, 1946, 1940]

paintings = list(zip(paintings, dates))

paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

print(len(paintings))

audio_tour_number = []
for tour in range(1, len(paintings)+1):
    audio_tour_number.append(tour)

print(audio_tour_number)

master_list = list(zip(audio_tour_number, paintings))

print(master_list)