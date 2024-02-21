# Practice quiz: Gradient descent in practice
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/91035b73-148b-4f43-be79-695519301becimage3.png?expiry=1658534400000&hmac=mO6CCHdB5T65a_HRc_c_Qy2dvUwAd1eMV8BAzmv-IoI)
> 
> Which of the following is a valid step used during feature scaling?
> 
> 1 / 1 point
> 

      Subtract the mean (average) from each value and then divide by the (max - min). 
> 
>  Add the mean (average) from each value and and then divide by the (max - min). 
> 
> Correct
> 
> This is called mean normalization.
> 
> ### 2.
> 
> Question 2
> 
> Suppose a friend ran gradient descent three separate times with three choices of the learning rate α\alphaα and plotted the learning curves for each (cost J for each iteration).
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/91035b73-148b-4f43-be79-695519301becimage4.png?expiry=1658534400000&hmac=3Fxz3KPN4XGRmPhdo3isuCL_NLPME5I9JEvrnOVvLLg)
> 
> For which case, A or B, was the learning rate α\alphaα likely too large?
> 
> 1 / 1 point
> 

      case B only 
> 
>  Both Cases A and B 
> 
>  Neither Case A nor B 
> 
>  case A only 
> 
> Correct
> 
> The cost is increasing as training continues, which likely indicates that the learning rate alpha is too large.
> 
> ### 3.
> 
> Question 3
> 
> Of the circumstances below, for which one is feature scaling particularly helpful?
> 
> 1 / 1 point
> 

      Feature scaling is helpful when one feature is much larger (or smaller) than another feature. 
> 
>  Feature scaling is helpful when all the features in the original data (before scaling is applied) range from 0 to 1. 
> 
> Correct
> 
> For example, the “house size” in square feet may be as high as 2,000, which is much larger than the feature “number of bedrooms” having a value between 1 and 5 for most houses in the modern era.
> 
> ### 4.
> 
> Question 4
> 
> You are helping a grocery store predict its revenue, and have data on its items sold per week, and price per item. What could be a useful engineered feature?
> 
> 1 / 1 point
> 
>  For each product, calculate the number of items sold divided by the price per item. 
> 

      For each product, calculate the number of items sold times price per item. 
> 
> Correct
> 
> This feature can be interpreted as the revenue generated for each product.
> 
> ### 5.
> 
> Question 5
> 
> True/False? With polynomial regression, the predicted values f_w,b(x) does not necessarily have to be a straight line (or linear) function of the input feature x.
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Correct
> 
> A polynomial function can be non-linear.  This can potentially help the model to fit the training data better.
>
> -- https://www.coursera.org/learn/machine-learning/exam/wAYb5/practice-quiz-gradient-descent-in-practice/attempt?redirectToCover=true#Q2Q6AP-legend
