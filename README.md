#MOVIE SUCCESS PREDICTOR ENGINE 

Given a movie title ,predicts the success of the movie .

* Success is defined by 2 main metrics ,the (revenue : budget) ratio and the average critic review .

* To simplify the problem , movies have been categorized into 4 classes .




######BLOCKBUSTER 
	review >= 6.5 and (revenue / budget) >= 3

######CRITICAL WINNER
	review >= 6.5 and (revenue / budget) < 3

######COMMERCIAL VENTURE 
	review < 6.5 and review >= 5 and (revenue / budget) >= 3


######HORRIBLE (ARSENAL )
	review < 6.5 and review >= 5 and (revenue / budget) < 3


* The review is NOT IMDB Rating 

* For detailed working of the engine ,refer paper.md 


