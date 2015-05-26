import tmdbsimple as tmdb
from glb import *
from functions import *

tmdb.API_KEY=APIKEY

movieInfo=movieSearch(MOVIENAME)
genre=movieInfo['genres']
revenue=movieInfo['revenue']
productionCompanies=movieInfo['production_companies']
budget=movieInfo['budget']
review=movieInfo['vote_average']

print genre
print revenue
print productionCompanies
print budget
print review



		
directorId=helperSearch(MOVIENAME,'Directing','crew')[0]
print directorId

productionIdList=helperSearch(MOVIENAME,'Production','crew')
print productionIdList

actorIdList=helperSearch(MOVIENAME,'Actress','cast')
print actorIdList





person=tmdb.People(directorId)
previousMoviesDirector=person.movie_credits()['crew']
for i in range(len(previousMoviesDirector)):
	if(previousMoviesDirector[i]['department']=='Directing'):
		print previousMoviesDirector[i]['title']


