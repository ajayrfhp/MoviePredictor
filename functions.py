import tmdbsimple as tmdb
from glb import *

def movieSearch(movieName):
	search=tmdb.Search()
	responses=search.movie(query=movieName)
	
	movie=tmdb.Movies(responses['results'][0]['id'])

	info=movie.info()

	return info



def peopleSearch(personId,answer,answerDepartment):
	person=tmdb.People(personId)
	previousMoviesPerson=person.movie_credits()[answerDepartment]

	avgRevenuePerson=0
	avgRatingPerson=0
	cntRatingPerson=0
	cntRevenuePerson=0
	bestRatingPerson=0
	bestRevenuePerson=0
	worstRatingPerson=999999999999999999
	worstRevenuePerson=999999999999999999
	if(answer=='Directing' or answer=='Writing' or answer=='Production' ):

		for i in range(len(previousMoviesPerson)):
			if(previousMoviesPerson[i]['department']==answer):
				movieInfo=movieSearch(previousMoviesPerson[i]['title'])
				if(movieInfo['budget'] and movieInfo['revenue']):
					cntRevenuePerson+=1
					movieInfo['budget']=float(movieInfo['budget'])
					movieInfo['revenue']=float(movieInfo['revenue'])
					
					avgRevenuePerson=avgRevenuePerson+(movieInfo['revenue']/movieInfo['budget'])
					bestRevenuePerson=max(bestRevenuePerson,(movieInfo['revenue']/movieInfo['budget']))
					worstRevenuePerson=min(worstRevenuePerson,(movieInfo['revenue']/movieInfo['budget']))



				if(movieInfo['vote_average']!=0):
					avgRatingPerson=float(avgRatingPerson+movieInfo['vote_average'])
					bestRatingPerson=max(bestRatingPerson,movieInfo['vote_average'])
					worstRatingPerson=min(worstRatingPerson,movieInfo['vote_average'])
					cntRatingPerson+=1
	else:
		for i in range(len(previousMoviesPerson)):
			movieInfo=movieSearch(previousMoviesPerson[i]['title'])
			if(movieInfo['budget'] and movieInfo['revenue']):
				cntRevenuePerson+=1
				movieInfo['budget']=float(movieInfo['budget'])
				movieInfo['revenue']=float(movieInfo['revenue'])
				ratio=(movieInfo['revenue']/movieInfo['budget'])
				if(movieInfo['revenue']/movieInfo['budget']>100 ):	
					ratio=1
				elif(movieInfo['revenue']/movieInfo['budget']<0.1):
					ratio=0.1	

				avgRevenuePerson=avgRevenuePerson+(ratio)
				bestRevenuePerson=max(bestRevenuePerson,ratio)
				worstRevenuePerson=min(worstRevenuePerson,(ratio))


				


			if(movieInfo['vote_average']!=0):
				avgRatingPerson=float(avgRatingPerson+movieInfo['vote_average'])
				bestRatingPerson=max(bestRatingPerson,movieInfo['vote_average'])
				worstRatingPerson=min(worstRatingPerson,movieInfo['vote_average'])
				cntRatingPerson+=1						
	if(cntRatingPerson>0):
		avgRatingPerson=(avgRatingPerson/cntRatingPerson)
	else:
		avgRatingPerson=5
	if(cntRevenuePerson>0):	
		avgRevenuePerson=(avgRevenuePerson/cntRevenuePerson)
	else:
		avgRevenuePerson=1
	result={}
	for key in result:
		if(result[key]>10):
			result[key]=6


	result['avgRatingPerson']=avgRatingPerson
	result['avgRevenuePerson']=avgRevenuePerson
	result['bestRatingPerson']=bestRatingPerson
	result['bestRevenuePerson']=bestRevenuePerson
	result['worstRatingPerson']=worstRatingPerson
	result['worstRevenuePerson']=worstRevenuePerson
	if(result['worstRatingPerson']>10):
		result['worstRatingPerson']=6
	
	if(result['worstRevenuePerson']>10):
		result['worstRevenuePerson']=6

	return result


def findBitVector(thisMovieGenres):
	a=[]
	for i in range(len(thisMovieGenres)):
		a.append(thisMovieGenres[i]['name'])
	thisMovieGenre=a
	ans=[]
	for i in range(len(genres)):
		ans.append(0)
	cnt=0
	for genre in genres :
		if(genre in thisMovieGenre):
			ans[cnt]=1
		cnt+=1		
	return ans	

