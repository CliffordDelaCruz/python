hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
if dura >= 60:
    addhour = dura // 60
    addmins = (dura - (addhour * 60))
else:
    addhour = 0
    addmins = dura

newhour = hour
newmins = mins + addmins
if newmins >= 60:
    addhour += newmins // 60
    newmins = newmins %60

if (newhour + addhour) >= 24:
    newhour += addhour
    newhour %= 24
else:
    newhour += addhour



print("Expected Output: {}:{}".format(str(newhour),str(newmins)))