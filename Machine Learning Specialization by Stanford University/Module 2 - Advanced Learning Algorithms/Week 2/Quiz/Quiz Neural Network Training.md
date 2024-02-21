# Practice quiz: Neural Network Training
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/141c2e0d-b88f-4876-a375-6b18af36255fimage3.png?expiry=1658880000000&hmac=ayDYwEE1Xe89heh8rSTO2vcpH5AJExEQtI0Db6iupWI)
> 
> Here is some code that you saw in the lecture:
> 
> ```
> 
> model.compile(loss=BinaryCrossentropy())
> 
> ```
> 
> For which type of task would you use the binary cross entropy loss function?
> 
> 1 / 1 point
> 
>  regression tasks (tasks that predict a number) 
> 

      binary classification (classification with exactly 2 classes) 
> 
>  A classification task that has 3 or more classes (categories) 
> 
>  BinaryCrossentropy() should not be used for any task. 
> 
> Correct
> 
> Yes! Binary cross entropy, which we've also referred to as logistic loss, is used for classifying between two classes (two categories).
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/141c2e0d-b88f-4876-a375-6b18af36255fimage3.png?expiry=1658880000000&hmac=ayDYwEE1Xe89heh8rSTO2vcpH5AJExEQtI0Db6iupWI)
> 
> Here is code that you saw in the lecture:
> 
> ```
> 
> model = Sequential([
> 
> Dense(units=25, activation='sigmoid’),
> 
> Dense(units=15, activation='sigmoid’),
> 
> Dense(units=1, activation='sigmoid’)
> 
> ])
> 
> model.compile(loss=BinaryCrossentropy())
> 
> model.fit(X,y,epochs=100)
> 
> ```
> 
> Which line of code updates the network parameters in order to reduce the cost?
> 
> 1 / 1 point
> 

      model.fit(X,y,epochs=100) 
> 
>  model = Sequential([...]) 
> 
>  None of the above -- this code does not update the network parameters. 
> 
>  model.compile(loss=BinaryCrossentropy()) 
> 
> Correct
> 
> Yes! The third step of model training is to train the model on data in order to minimize the loss (and the cost)
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/nBZd2/practice-quiz-neural-network-training/attempt?redirectToCover=true#uD55vO-legend
