import tmdbsimple as tmdb
from glb import *
from functions import *
import io

APIKEY='5b248f61321474b5f3e42b34ac06d315'

tmdb.API_KEY=APIKEY
discover=tmdb.Discover()
responses=discover.movie(year=1994)
movies=[]
f=open("output.txt",'w')
for y in range(1977,2015):
	print(y)
	for p in range(2):
		cnt=0
		responses=discover.movie(page=p+1,year=y)
		for result in responses['results']:
			movies.append(result['title'])
			cnt+=1
			
			movieInfo=movieSearch(result['title'])

			for ij in range(len(movieInfo['production_companies'])):
				if(movieInfo['production_companies'][ij]['name'] not in productionCompaniesPopluate):
					productionCompaniesPopluate.append(movieInfo['production_companies'][ij]['name'])
					



			for ij in range(len(movieInfo['genres'])):
				if(movieInfo['genres'][ij]['name'] not in genreTest):
					genreTest.append(movieInfo['genres'][ij]['name'])	
			if(cnt>10):
				break


print productionCompaniesPopluate
print genreTest


'''
movie=tmdb.Movies(responses['results'][0]['id'])
movie.info()
'''