#string_manipulation.py
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

highlighted_poems_stripped=[]
for poem_strip in highlighted_poems_list:
  highlighted_poems_stripped.append(poem_strip.strip())

print(highlighted_poems_stripped)

highlighted_poems_details=[]
for poem_split in highlighted_poems_stripped:
  highlighted_poems_details.append(poem_split.split(':'))

print(highlighted_poems_details)

titles=[]
poets=[]
dates=[]
for poem_detail in highlighted_poems_details:
  for ctr in range(3):
    if ctr == 0:
      titles.append(poem_detail[ctr])
    elif ctr == 1:
      poets.append(poem_detail[ctr])
    elif ctr == 2:
      dates.append(poem_detail[ctr])

print(titles)
print(poets)
print(dates)

ctr2 = 0
while ctr2 < len(titles):
  print("The poem {t} was published by {p} in {d}".format(t=titles[ctr2],p=poets[ctr2],d=dates[ctr2]))
  ctr2 += 1