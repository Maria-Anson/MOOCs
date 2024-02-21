# Practice quiz: Neural network implementation in Python
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/38b928e9-0b01-456d-9549-be803e348303image3.png?expiry=1658793600000&hmac=EC7bEDFKIn50z7UTmFI8OsXviIsgCXXu8gPKPvULKM4)
> 
> According to the lecture, how do you calculate the activation of the third neuron in the first layer using NumPy?
> 
> 1 / 1 point
> 
>  layer_1 = Dense(units=3, activation='sigmoid')
> 
> a_1 = layer_1(x) 
> 
>  z1_3 =w1_3 * x + b
> 
> a1_3 = sigmoid(z1_3) 
> 

      z1_3 = np.dot(w1_3, x) + b
      a1_3 = sigmoid(z1_3) 
> 
> Correct
> 
> Correct. Use the numpy.dot function to take the dot product. The sigmoid function shown in lecture can be a function that you write yourself (see course 1, week 3 of this specialization), and that will be provided to you in this course.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/38b928e9-0b01-456d-9549-be803e348303image1.png?expiry=1658793600000&hmac=hnKIAOGTlzLEE6dBV5SHg3vVR5PZfQTTeLwCxW6OEnI)
> 
> According to the lecture, when coding up the numpy array W, where would you place the w parameters for each neuron?
> 
> 1 / 1 point
> 

      In the columns of W. 
> 
>  In the rows of W. 
> 
> Correct
> 
> Correct. The w parameters of neuron 1 are in column 1\. The w parameters of neuron 2 are in column 2, and so on.
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/38b928e9-0b01-456d-9549-be803e348303image1.png?expiry=1658793600000&hmac=hnKIAOGTlzLEE6dBV5SHg3vVR5PZfQTTeLwCxW6OEnI)
> 
> For the code above in the "dense" function that defines a single layer of neurons, how many times does the code go through the "for loop"? Note that W has 2 rows and 3 columns.
> 
> 1 / 1 point
> 
>  6 times 
> 
>  2 times 
> 
>  5 times 
> 

      3 times 
> 
> Correct
> 
> Yes! For each neuron in the layer, there is one column in the numpy array W. The for loop calculates the activation value for each neuron. So if there are 5 columns in W, there are 5 neurons in the dense layer, and therefore the for loop goes through 5 iterations (one for each neuron).
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/w8v2m/practice-quiz-neural-network-implementation-in-python/attempt?redirectToCover=true#hYOxLP-legend
