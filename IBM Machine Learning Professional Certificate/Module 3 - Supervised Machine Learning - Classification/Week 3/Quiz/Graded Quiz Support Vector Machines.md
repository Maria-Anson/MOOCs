# Module 3 Graded Quiz: Support Vector Machines
> ### 1.
> 
> Question 1
> 
> Select the TRUE statement regarding the cost function for SVMs:
> 
> 1 / 1 point
> 
>  SVMs use a loss function that penalizes vectors prone to misclassification 
> 
>  SVMs do not use a cost function. They use regularization instead of a cost function. 
> 
>  SVMs use same loss function as logistic regression 
> 

      SVMs use the Hinge Loss function as a cost function 
> 
> Correct
> 
> Correct! You can find more information in the lesson _The Support Vector Machines Cost Function_.
> 
> ### 2.
> 
> Question 2
> 
> Which statement about Support Vector Machines is TRUE?
> 
> 1 / 1 point
> 
>  Support Vector Machine models can be used for regression but not for classification. 
> 
>  Support Vector Machine models can be used for classification but not for regression. 
> 
>  Support Vector Machine models are non-linear. 
> 

      Support Vector Machine models rarely overfit on training data. 
> 
> Correct
> 
> Correct! You can find more information in the lesson _Regularization in Support Vector Machines_.
> 
> ### 3.
> 
> Question 3
> 
> (True/False) A large _c_ term will penalize the SVM coefficients more heavily.
> 
> 1 / 1 point
> 
>  True 
> 

      False 
> 
> Correct
> 
> Correct! You can find more information in the lesson Regularization in Support Vector Machines.
> 
> ### 4.
> 
> Question 4
> 
> Regularization in the context of support vector machine (SVM) learning is meant to _________________.
> 
> 1 / 1 point
> 
>  encourage the model to ignore outliers during training 
> 
>  bring all features to a common scale to ensure they have equal weight 
> 
>  smooth the input data to reduce the chance of overfitting 
> 

      lessen the impact that some minor misclassifications have on the cost function 
> 
> Correct
> 
> Correct. In SVM, you have to come up with a way of optimizing to allow for some points to be misclassified within the process. This is where the regularization in SVM comes into play.
> 
> ### 5.
> 
> Question 5
> 
> Support vector machines can be extended to work with nonlinear classification boundaries by ___________________.
> 
> 1 / 1 point
> 

      using the kernel trick 
> 
>  modifying the standard sigmoid function 
> 
>  projecting the feature space onto a lower dimensional space 
> 
>  incorporating polynomial regression 
> 
> Correct
> 
> Correct. Support vector machines can be extended to non-linear classifiers using the kernel trick.
> 
> ### 6.
> 
> Question 6
> 
> Select the image that displays the line at the optimal point in the phone usage that the data can be split to create a decision boundary.
> 
> 1 / 1 point
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage3.png?expiry=1660176000000&hmac=4m9SeamwfzgIlBlpLa9Sek2Z-XKVzZnP723OvI69tRc) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage1.png?expiry=1660176000000&hmac=8ISb2w6x3TFaCcSnJtqHMgM6qwUkam_r6OG--vWsScI) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage4.png?expiry=1660176000000&hmac=R3ZedLgOLO6HLGJs1JXFZZ2DY1owWIWFHUxR6HTBppc) 

     Correct
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage2.png?expiry=1660176000000&hmac=HZT792w839G6TjkoLsh8rMvFFsBoMcYcSxHwwIqfrJA) 
> 
> 
> Correct. This is the optimal point in the phone usage to split the data and create a decision boundary.
> 
> ### 7.
> 
> Question 7
> 
> The below image shows the decision boundary with a clear margin, such decision boundary belongs to what type machine learning model?
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage5.png?expiry=1660176000000&hmac=Hyz0YIfSsofS9f2_io3bkUCB3GV0iiuaab9hflCr5IQ)
> 
> 1 / 1 point
> 
>  Support Version Machine 
> 
>  Machine Learning 
> 

      Support Vector Machine 
> 
>  Super Vector Machine 
> 
> Correct
> 
> Correct. This is a model of a Support Vector Machine because the blue and red samples that define the margin, the dotted lines, are called support vectors.
> 
> ### 8.
> 
> Question 8
> 
> SVM with kernals can be very slow on large datasets. To speed up SVM training, which methods may you perform to map low dimensional data into high dimensional beforehand?
> 
> 1 / 1 point
> 

      Nystroem 
> 
> Correct
> 
> Correct. The Nystroem method can be used to map low dimensional data into high dimensional data.
> 

      RBF Sampler 
> 
> Correct
> 
> Correct. The RBF Sampler method can be used to map low dimensional data into high dimensional data.
> 
>  Linear SVC 
> 
>  Regularization 
> 
> ### 9.
> 
> Question 9
> 
> Concerning the Machine Learning workflow what model choice would you pick if you have "Few" features and a "Medium" amount of data?
> 
> 1 / 1 point
> 

      SVC with RBF 
> 
>  Add features, or Logistic 
> 
>  Simple, Logistic or LinearSVC 
> 
>  LinearSVC, or Kernal Approximation 
> 
> Correct
> 
> Correct. You would use SVC with RBF as your model with “Few” features and a “Medium” amount of data.
> 
> ### 10.
> 
> Question 10
> 
> Select the image that best displays the line that separates the classes.
> 
> 1 / 1 point
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage6.png?expiry=1660176000000&hmac=CpMexkoLJISaEO0EwabThe_hO5TqbIwfKZuHeoPltvk) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage9.png?expiry=1660176000000&hmac=-zBoeAs-oepWP9hqZgtCsR4LFMa_jgnEaijMQ-5zLOA) 
    
     Correct
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage7.png?expiry=1660176000000&hmac=t6uSBTdPz82H_CldWEOfswhhpo3Emn753c2tve1DVi4) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/57d0e9a6-6d29-49d2-a6be-73ddeeb9ff4eimage8.png?expiry=1660176000000&hmac=0WuWJw3iq25sPqFrTfZLd2PTqx028CbhCGl3K50iZwQ) 
> 
> 
> Correct. This image displays the line that best separates the classes.
>
> -- https://www.coursera.org/learn/supervised-machine-learning-classification/exam/PAsR0/module-3-graded-quiz-support-vector-machines/attempt?redirectToCover=true#zZHFTx-legend
