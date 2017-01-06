import urllib2, string, webbrowser, time, sys, json


def pull_new_list(k):
    array = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json").read()
    data = json.loads(array)
    return data['query']['random']

def welcome():
    print """WELCOME TO WIKIPEDIA RANDOM LIST GENERATOR
    Press enter to skip article
    Downloading new list.
    type in any letter and press enter to view article
    """
welcome()

Keep_going = True
while Keep_going == True:
	random_list = pull_new_list(12)

	current = random_list.pop()
	print current["title"]

	decision = raw_input()
        if decision == "":
        	Keep_going=True
        elif decision =="Quit":
        	sys.exit()
     	else:
     		ID_code = str(current['id'])
     		print ID_code
     		website = "http://en.wikipedia.org/wiki?curid=" + ID_code
     		webbrowser.open(website)
     		Keep_going= False


#list2 = json.loads(random_list['query']['random'])

#pop
#popping removes the last item in the array
#if there are no more items, can't pop, need ot pull new list
#loop pull_new_list

