#Practice quiz: TensorFlow implementation
> ### 1.
> 
> Question 1
> 
> For the the following code:
> 
> model = Sequential([
> 
> Dense(units=25, activation="sigmoid"),
> 
> Dense(units=15, activation="sigmoid"),
> 
> Dense(units=10, activation="sigmoid"),
> 
> Dense(units=1, activation="sigmoid")])
> 
> This code will define a neural network with how many layers?
> 
> 1 / 1 point
> 

      4 
> 
>  25 
> 
>  5 
> 
>  3 
> 
> Correct
> 
> Yes! Each call to the "Dense" function defines a layer of the neural network.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/98c635c3-33fc-4d9c-9af5-6f1f18da35aeimage2.png?expiry=1658793600000&hmac=xys_QBnLwL4yl6gtrQQ8phpbOfyv3njt5XEBGsLNxtc)
> 
> How do you define the second layer of a neural network that has 4 neurons and a sigmoid activation?
> 
> 1 / 1 point
> 
>  Dense(units=[4], activation=[‘sigmoid’]) 
> 
>  Dense(layer=2, units=4, activation = ‘sigmoid’) 
> 
>  Dense(units=4) 
> 

      Dense(units=4, activation=‘sigmoid’) 
> 
> Correct
> 
> Yes! This will have 4 neurons and a sigmoid activation.
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/98c635c3-33fc-4d9c-9af5-6f1f18da35aeimage3.png?expiry=1658793600000&hmac=gLZPXFYW5gCwPrHshASLTCiLodFCVR-uXHdxG3g_wP8)
> 
> If the input features are temperature (in Celsius) and duration (in minutes), how do you write the code for the first feature vector x shown above?
> 
> 1 / 1 point
> 

      x = np.array([[200.0, 17.0]]) 
> 
>  x = np.array([[200.0],[17.0]]) 
> 
>  x = np.array([[‘200.0’, ’17.0’]]) 
> 
>  x = np.array([[200.0 + 17.0]]) 
> 
> Correct
> 
> Yes! A row contains all the features of a training example. Each column is a feature.
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/75mlV/practice-quiz-tensorflow-implementation/view-attempt#XyANLg-legend
