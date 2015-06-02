import tmdbsimple as tmdb

APIKEY='5b248f61321474b5f3e42b34ac06d315'

tmdb.API_KEY=APIKEY
discover=tmdb.Discover()
responses=discover.movie(year=1994)
movies=[]

for p in range(responses['total_pages']):
	cnt=0
	responses=discover.movie(page=p+1,year=2014)
	for result in responses['results']:
		movies.append(result['title'])
		cnt+=1
		print(result['title'])
		if(cnt>1000):
			break



'''
movie=tmdb.Movies(responses['results'][0]['id'])
movie.info()
'''