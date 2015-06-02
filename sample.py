import tmdbsimple as tmdb
from glb import *
from functions import *

tmdb.API_KEY=APIKEY


movieInfo=movieSearch(MOVIENAME)
genre=movieInfo['genres']
revenue=float(movieInfo['revenue'])



budget=float(movieInfo['budget'])
review=movieInfo['vote_average']
popularity=movieInfo['popularity']

print genre
print revenue


print budget
print review
print popularity
'''
writerId=helperSearch(MOVIENAME,'Writing','crew')[0]
print writerId
writerAvgRating=peopleSearch(writerId,'Writing','crew')
print writerAvgRating



		
directorId=helperSearch(MOVIENAME,'Directing','crew')[0]
print directorId



actorIdList=helperSearch(MOVIENAME,'Actor','cast')
print actorIdList




#SCAN PREVIOUS MOVIE DIRECTOR AND GET DETAILS
directorAvgRating=peopleSearch(directorId,'Directing','crew')
print directorAvgRating
actor1AvgRating=peopleSearch(actorIdList[0],'Actress','cast')
print actor1AvgRating
actor2AvgRating=peopleSearch(actorIdList[1],'Actress','cast')
print actor2AvgRating
actor3AvgRating=peopleSearch(actorIdList[2],'Actress','cast')
print actor3AvgRating



genreBitVector=findBitVector(genre)
print genreBitVector

inputFeature=[]
inputFeature.append(genreBitVector)
inputFeature.append(revenue/budget)

for key in directorAvgRating.keys():
	inputFeature.append(directorAvgRating[key])

for key in writerAvgRating.keys():
	inputFeature.append(writerAvgRating[key])


for key in actor1AvgRating.keys():
	inputFeature.append(actor1AvgRating[key])

for key in actor2AvgRating.keys():
	inputFeature.append(actor2AvgRating[key])

for key in actor3AvgRating.keys():
	inputFeature.append(actor3AvgRating[key])


for key in directorAvgRating.keys():
	inputFeature.append(directorAvgRating[key])		



'''
target=-1


if(review>=6.5 and (revenue/budget)>=3):
	target=0##BLOCKBUSTER
elif(review>=6.5 and (revenue/budget)<3):
	target=1##CRITICAL WINNER
elif(review<6.5 and review>=5 and (revenue/budget)>=3):	
	target=2 ##PROFITABLE VENTURE
elif(review<6.5 and review>=5 and (revenue/budget)<3):	
	target=3 ##AVERAGE
elif(review<5 and (revenue/budget)>=1):	
	target=4 ##MEDIOCORE
elif((revenue/budget)<1):	
	target=5 ##DISASTER		



#print inputFeature

print target

