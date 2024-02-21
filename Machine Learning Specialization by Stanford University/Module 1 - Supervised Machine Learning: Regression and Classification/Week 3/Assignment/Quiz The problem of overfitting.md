# Practice quiz: The problem of overfitting
> ### 1.
> 
> Question 1
> 
> Which of the following can address overfitting?
> 
> 1 / 1 point
> 

      Collect more training data 
> 
> Correct
> 
> If the model trains on more data, it may generalize better to new examples.
> 

      Apply regularization 
> 
> Correct
> 
> Regularization is used to reduce overfitting.
> 
>  Remove a random set of training examples 
> 

      Select a subset of the more relevant features. 
> 
> Correct
> 
> If the model trains on the more relevant features, and not on the less useful features, it may generalize better to new examples.
> 
> ### 2.
> 
> Question 2
> 
> You fit logistic regression with polynomial features to a dataset, and your model looks like this.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/335acb2e-4819-4d1f-920c-1b1d682eeb37image2.png?expiry=1658620800000&hmac=3414-Z-4UJLfHSsbRXtOk3_XRQxBpcrlvWvtHpx-JKo)
> 
> What would you conclude? (Pick one)
> 
> 1 / 1 point
> 
>  The model has high bias (underfit). Thus, adding data is likely to help 
> 
>  The model has high bias (underfit). Thus, adding data is, by itself, unlikely to help much. 
> 
>  The model has high variance (overfit). Thus, adding data is, by itself, unlikely to help much. 
> 

      The model has high variance (overfit). Thus, adding data is likely to help 
> 
> Correct
> 
> The model has high variance (it overfits the training data). Adding data (more training examples) can help.
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/ujk9ltT9RAC5PZbU_YQALQ_7bc73e8e2f3a48cf800d1a504f55ecf1_Screen-Shot-2022-06-14-at-3.38.02-PM.png?expiry=1658620800000&hmac=Aw6mteDE-3CqRCulrqZP9moYIEETFQUOlmhWEapfAkI)
> 
> Suppose you have a regularized linear regression model.  If you increase the regularization parameter λ\lambdaλ, what do you expect to happen to the parameters w1,w2,...,wnw_1,w_2,...,w_nw1​,w2​,...,wn​?
> 
> 1 / 1 point
> 

      This will reduce the size of the parameters w1,w2,...,wn
> 
>  This will increase the size of the parameters w1,w2,...,wnw_1,w_2,..., w_nw1​,w2​,...,wn​ 
> 
> Correct
> 
> Regularization reduces overfitting by reducing the size of the parameters w1,w2,...wnw_1,w_2,...w_nw1​,w2​,...wn​.
>
> -- https://www.coursera.org/learn/machine-learning/exam/8Kf7N/practice-quiz-the-problem-of-overfitting/attempt?redirectToCover=true#f4Iywy-legend
