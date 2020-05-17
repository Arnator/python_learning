guests = ['Eminem', 'Tesla', 'Carl Jung', 'kant']
print (guests)
print ("\n\tI would fucking love to meet " + guests[0] + ".")
guests.append('Myself')
print (guests)
print ("\n\tI would like to personally invite " + guests[0].title() + ",and " + guests[3].title() + " to dinner tomorrow night. I still have to make up my mind on " + guests[2].title() + ".")
print ("\nSup folks were actually gonna get crunk tonight and invite some more thots")
guests.insert(2, 'Kendrick Lamar')
guests.append('j cole')
print ("\n\tSo ive taken the liberty of inviting " + guests[2].title() + ", and " + guests[6].title() + " to dinner with us this evening.")
print (guests)
#SORT will permanently change the lists order alphabetically
guests.sort()
print (guests)
#True must be capitalized! reverse function injected into sort
guests.sort(reverse=True)
print (guests)

#MOVE TO SORTLIST.PY FOR MORE INFO
