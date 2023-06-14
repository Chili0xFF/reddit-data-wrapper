import praw

reddit = praw.Reddit(client_id='udcdKTownglb-AhydKqRAg', client_secret='drJj_SbjjoqOotrBxrax3SiL5rGvXQ', user_agent='UsernameDownload')

communities={"rpg_gamers":[],"DnD":[],"BaldursGate3":[],"DivinityOriginalSin":[],"projecteternity":[],"AndroidGaming":[],"iosgaming":[]}#"Pathfinder_RPG":[],"Pathfinder_Kingmaker":[],,"MobileGaming":[]


matrix = [[0 for col in range(len(communities))] for row in range(len(communities))]
    
#Filling communities dict with values
for communist in communities:
    try:
        hot_posts = reddit.subreddit(communist).hot(limit=500)
    except:
        hot_posts = []
    authors =[]
    
    for post in hot_posts:
        authors.append(post.author.name)
    communities.update({communist:authors})
    print("Community "+communist+" accessed. Size:"+str(len(communities[communist])))
#Filling the matrix
x=0
for key_x in communities.keys():
    y=0
    for key_y in communities.keys():
        p = set(communities[key_x])&set(communities[key_y])
        if "Automoderator" in p:
            p.remove("Automoderator")
        #print(len(p))
        matrix[x][y]=len(p)
        print(str(matrix[x][y])+",",end="")
        y+=1
    x+=1
    print("")


#print(communities.get("rpg_gamers"))
#print(matrix[0][0])
