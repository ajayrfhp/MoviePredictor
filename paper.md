#MOVIE SUCCESS PREDICTOR ENGINE 



#####Sriram Sundaraj,Ajay Prasadh 

#####National Institute Of Technology,Trichy

###Introduction
    The intelligent machine is an evil genie, escaped from its bottle.
                                        -   BRIAN HERBERT & KEVIN J. ANDERSON, The Butlerian Jihad



Movie Success Predictor engine  is an application of  machine learning, that builds a system that predicts the sucess of a movie.Billions of dollars are spent by various production houses across the globe to make movies year after year.What determines the success of a movie is an intriguing question ,and one that cannot be explained in a single sentence.Do good directors always make good movies ? .Is it independent of the actors involed ?.How crucial is the contribution of writer towards the sucess of the movie ? Does the genre of the movie matter ?. These are some of the questions that we attempt to find a solution using our engine .


###Related Work

* Several models have been made to solve this problem like Predicting Movie Success: Review of Existing Literature which uses Artificial Neural Networks to build the model .The Feature Vector they have used consists of analyzing the previous 10 movies of the Actors,Actresses,Director,Producer,Music Director,Writer,Marketting Budget and a factor for time of release. The weights used for the networks are number of movies that were hit in the last 10 movies . 2 types of weights are assigned to take into account release time ,ex : festival times . A movie can do realtively better releasing on a festival time .Marketing budget has also been parameterized ,with a base value of Rs 10 Crore.

* Another paper along the same lines is Automatic Musical Genre Classification Of Audio Signals [3]. A vector of size 9 (mean-Centroid, mean-Rolloff, mean-Flux, mean-ZeroCrossings, std-Centroid, std-Rolloff, std-Flux, std-ZeroCrossings, LowEnegry) was used as their MusicalSurfaceFeatures vector. Rhythm features were determined and their model was built using both the vectors.

Our work differs from the previous two with respect to the feature vector under consideration. The song has been analyzed as a wave and as a song well.


##FLOW DIAGRAM

![Flow Diagram](figures/flow.jpg "FLOW DIAGRAM")

###FEATURE EXTRACTION

* One of the  important  ideas used in  this engine is that ,good directors  make good movies .Feature Vector consists of 34 features .

######GENRE BIT VECTOR (21 features)

**List Of Genres**      
        Action , Adventure , Animation , Comedy , Crime , Documentary , Drama , Family , Fantasy , Foreign , History , Horror , Music , Mystery ,Romance ,Science Fiction , TV movie , Thriller , War , Western 

* Each movie has multiple genres.A genre bit vector of length 21 is generated to indicate if that movie is that of a particular genre .        



######CALCULATION OF MFCC  (13 features)
* MFCC is a representation of the power spectrum of sound .
* MFCC was calculated using the open source scikit audiolabs library.
* A highlevel description of MFCC Calulcation [5] is explained below: 
 Frame the signal into short frames.
 For each frame calculate the periodogram estimate of the power spectrum.
 Apply the mel filterbank to the power spectra, sum the energy in each filter.
 Take the logarithm of all filterbank energies.
 Take the Discrete Cosine Transform (DCT)  of the log filterbank energies.
 Keep Discrete Cosing Transform (DCT) coefficients 2-13, discard the rest.
    

######CALCULATION OF SCALE (5 features)

* We used an approximation to calculate the scale of the song. We took the five most frequently occuring frequencies in the song in groups of 5.
* This led to the the length of the frequency vector being 5.
* This doesn't exactly represent the scale, but we felt that it would be a better representation than just the average pitch of the song.



######CALCULATION OF TEMPO (1 feature)

* We felt that tempo of the song would be a good indicator of the genre, hence we selected tempo as the other feature.
* We used @scaperot's BPM tool to find the BPM of the song.


###Dataset Description
* FingerPrinting the songs was done using the eyeD3 library[6]. Artist, album name and title of the song were obtained. Pygn [7], a wrapper over rhytm API was used to obtain the genre of the song. Using a local collection of 637 songs, we extracted features and with the genre obtained from Pygn [7] our dataset was prepared.

* The target genres were 'Urban,'Classical,'Electronica,'Jazz,'Pop,'Soundtrack,'Alternative & Punk,'Rock,'Other'.
    

![alt text](figures/figure.jpg "Bargraph of the dataset")
    

######DATA CLEANING:
* Soundtrack, Other, Jazz, Classical and traditional were ignored due to low number of samples.

* Genre converted from string to integers through a map to suit models construction and prediction.

* Samples with missing genres were ignored.




###MODELS          


For building the models, we used the SCIKIT [8] library.The models we used are the standard classification algorithms Logistic Regression, Support Vector Machine and KMeans.



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
* 1.[ Movie Sucess Predictor,Arundeep Kaur, AP Gurpinder Kaur ](http://www.ijarcsse.com/docs/papers/Volume_3/6_June2013/V3I6-0631.pdf) 

* 2.M. Muller. Information retrieval for music and motion. In Springer, 2007.

* 3.[ George Tzanetakis,Georg Essl,Perry Cook.Automatic Music Genre Classification for audio signals ](http://ismir2001.ismir.net/pdf/tzanetakis.pdf)

* 4.[ Scikits Audiolab ](https://pypi.python.org/pypi/scikits.audiolab/)

* 5.[ MFCC Calculation Theory ](http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)

* 6.[ eyeD3 ](https://pypi.python.org/pypi/eyeD3)

* 7.[ pygn ](https://github.com/cweichen/pygn)

* 8.[ scikit ](http://scikit-learn.org/stable/)