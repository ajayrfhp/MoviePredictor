#MOVIE SUCCESS PREDICTOR ENGINE 



#####Sriram Sundaraj,Ajay Prasadh 

#####National Institute Of Technology,Trichy

###Introduction
    The intelligent machine is an evil genie, escaped from its bottle.
                                        -   BRIAN HERBERT & KEVIN J. ANDERSON, The Butlerian Jihad



Movie Success Predictor engine  is an application of  machine learning, that builds a system that predicts the sucess of a movie.Billions of dollars are spent by various production houses across the globe to make movies year after year.What determines the success of a movie is an intriguing question ,and one that cannot be explained in a single sentence.Do good directors always make good movies ? .Is it independent of the actors involed ?.How crucial is the contribution of writer towards the sucess of the movie ? Does the genre of the movie matter ?. These are some of the questions that we attempt to find a solution using our engine .


###Related Work

* Several models have been made to solve this problem like Predicting Movie Success:
 Review of Existing Literature [1] which uses Artificial Neural Networks to build the model .The Feature Vector they have used consists of analyzing the previous 10 movies of the Actors,Actresses,Director,Producer,Music Director,Writer,Marketting Budget and a factor for time of release. The weights used for the networks are number of movies that were hit in the last 10 movies . 2 types of weights are assigned to take into account release time ,example : festival times . A movie can do realtively better releasing on a festival time .Marketing budget has also been parameterized ,with a base value of Rs 10 Crore.    

* Another paper that deals with predictive modelling of movie success  is Early Prediction of Movie Box Office Success Based on Wikipedia Activity Big Data [2] .Using activity on the wikipedia pages of the movies ,the sucess is predicted.Popularity of the movie is estimated by 4 main measures ,Number of views of the article page,number of users ,that is the human editors who contributed to that page,Number of edits made by human editors on the article and Collaborative Rigor.In addition to this ,they also used a parameter to indicate the number of screens the movie is being released .Corelation of above paremeters with box office revenue is determined and regression model is built using the paremeters.User generated data in social media enhances the ability to predict the popularity of the movie and the reaction of people to it .
Other models have also been  built using Youtube data,twitter data etc.


Our model principally uses the crew of the team as the important contributing factor .We did not use social media data.



###FEATURE EXTRACTION

* One of the  important  ideas used in  this engine is that ,good directors  make good movies .Feature Vector consists of 33 features .

######GENRE BIT VECTOR (21 features)

**List Of Genres**      
        Action , Adventure , Animation , Comedy , Crime , Documentary , Drama , Family , Fantasy , Foreign , History , Horror , Music , Mystery ,Romance ,Science Fiction , TV movie , Thriller , War , Western 

* Each movie has multiple genres.A genre bit vector of length 21 is generated to indicate if that movie is that of a particular genre .        



######CREW FEATURES  (12 features)
**Director**
    The previous movies of the director are determined . Revenue / Budget ratio and Critic Reviews are used .Average ,Best and worst of the above 2 factors are used .6 features in all representing the director .

**Writer**
    The previous movies of the writer are determined . Revenue / Budget ratio and Critic Reviews are used .Average ,Best and worst of the above 2 factors are used .6 features in all representing the writer .

   We did not restrict ourselves to just average because ,there are movies like jaws which made 75 times the money as its budget , so the average Revenue / Budget ratio of all Spielberg movies will be high ,hence all Spielberg movies would be predicted as blockbuster .To compensate this effect , we considered all 3 factors .Average,Best and Worst.

   





###Dataset Preparation 
* The Movie DataBase (TMDB) is a freely available database for hollywood movies .We used tmdbsimple ,a python package, a wrapper over existing TMDB API's to extract information about movies .
* First ,the names of  50  popular movies and 50 mediocore of every year  from 1978 to 2015 were extracted.Using the TMDB Search API and People API ,the crew of the movie and the genre were determined .Using the information of the crew , calls were made to Search API again to extract information about the director's movies and the writer's previous movies .
    


    

######DATA CLEANING:

* Genre converted from string to integers through a map to suit models construction and prediction.

* Target class of the movies was determined to simplify the problem and reduce it to a classification problem .

######BLOCKBUSTER 
    review >= 6.5 and (revenue / budget) >= 3

######CRITICAL WINNER
    review >= 6.5 and (revenue / budget) < 3

######COMMERCIAL VENTURE 
    review < 6.5 and review >= 5 and (revenue / budget) >= 3


######HORRIBLE (ARSENAL )
    review < 6.5 and review >= 5 and (revenue / budget) < 3




###MODELS          


For building the models, we used the SCIKIT [8] library.The models we used are the standard classification algorithm Support Vector Machine .


###RESULTS

| Model                 | Electronica   | Urban     | Alternative & Punk    | Pop       | Rock  | Overall Model Accuracy    |
|---------------------- |-------------  |-------    |--------------------   |-------    |------ |------------------------   |
| Logistic Regression   | 0             | 56.52     | 49.1                  | 28.57     | 50    | 44.55                     |
| KMeans                | 33.33         | 42.85     | 59.45                 | 30.0      | 0     | 41.21                     |
| SVM                   | 25            | 56.25     | 57.14                 | 29.16     | 25.0  | 45.25                     |
|                       |               |           |                       |           |       |                           |


###CONCLUSION:
* Support Vector Machines showd the maximum accuracy.Model has been built to do music genre classifier .Accuracy still remains a concern .This is not a model for a standard dataset,dataset has been built from API's and model has been built for the custom data set.Suggestions for area of improvement ,get more features from the API's ,then do dimensionality reduction techniques and then build the model .Only a  limited number of   features from the API's has been chosen in this system . 



#####References:
* 1.[ Movie Sucess Predictor - Arundeep Kaur, AP Gurpinder Kaur ](http://www.ijarcsse.com/docs/papers/Volume_3/6_June2013/V3I6-0631.pdf) 

* 2.[ Mestyán M, Yasseri T, Kertész J (2013) Early Prediction of Movie Box Office Success Based on Wikipedia Activity Big Data. ] (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0071226)

* 3.[ George Tzanetakis,Georg Essl,Perry Cook.Automatic Music Genre Classification for audio signals ](http://ismir2001.ismir.net/pdf/tzanetakis.pdf)

* 4.[ Scikits Audiolab ](https://pypi.python.org/pypi/scikits.audiolab/)

* 5.[ MFCC Calculation Theory ](http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)

* 6.[ eyeD3 ](https://pypi.python.org/pypi/eyeD3)

* 7.[ pygn ](https://github.com/cweichen/pygn)

* 8.[ scikit ](http://scikit-learn.org/stable/)