import tmdbsimple as tmdb
from glb import *
from functions import *
import io

APIKEY='5b248f61321474b5f3e42b34ac06d315'

tmdb.API_KEY=APIKEY
discover=tmdb.Discover()
responses=discover.movie(year=1994)
movies=[]

with open('output.txt','w') as f:
	for y in range(1977,2015):
		print(y)
		responses=discover.movie(page=1,year=y)
		cnt=0
		for result in responses['results']:
			result['title']=result['title'].encode('ascii','ignore')
			movies.append(result['title'])
			cnt+=1
			
			movieInfo=movieSearch(result['title'])
			x=movieInfo['title'].encode('ascii','ignore')
			print x
			f.write("'"+str(x)+"',")	
			if(cnt>20):
				break

print movies

'''
movie=tmdb.Movies(responses['results'][0]['id'])
movie.info()
'''