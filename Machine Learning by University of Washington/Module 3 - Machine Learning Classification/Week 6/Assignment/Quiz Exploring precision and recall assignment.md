## Exploring precision and recall
> 
> Total points 13
> 
> ### 1.
> 
> Question 1
> 
> Consider the logistic regression model trained on **amazon_baby.sframe** using Turi Create.
> 
> Using accuracy as the evaluation metric, was our **logistic regression model** better than the **majority class classifier**?
> 
> 1 point
> 

      Yes 
> 
>  No 
> 
> ### 2.
> 
> Question 2
> 
> How many predicted values in the **test set** are **false positives**?
> 
> 1 point
> 

     2390
> 
> ### 3.
> 
> Question 3
> 
> Consider the scenario where each false positive costs $100 and each false negative $1.
> 
> Given the stipulation, what is the cost associated with the logistic regression classifier's performance on the **test set**?
> 
> 1 point
> 
>  Between $0 and $100,000 
> 

      Between $100,000 and $200,000 
> 
>     Between $200,000 and $300,000 
> 
>  Above $300,000 
> 
> ### 4.
> 
> Question 4
> 
> Out of all reviews in the **test set** that are predicted to be positive, what fraction of them are **false positives**? (Round to the second decimal place e.g. 0.25)
> 
> 1 point
> 

     0.04
> 
> ### 5.
> 
> Question 5
> 
> Based on what we learned in lecture, if we wanted to reduce this fraction of false positives to be below 3.5%, we would:
> 
> 1 point
> 
>  Discard a sufficient number of positive predictions 
> 
>  Discard a sufficient number of negative predictions 
> 

      Increase threshold for predicting the positive class (y^=+1\hat{y} = +1y^​=+1) 
> 
>  Decrease threshold for predicting the positive class (y^=+1\hat{y} = +1y^​=+1) 
> 
> ### 6.
> 
> Question 6
> 
> What fraction of the positive reviews in the **test_set** were correctly predicted as positive by the classifier? Round your answer to 2 decimal places.
> 
> 1 point
> 

     0.94
> 
> ### 7.
> 
> Question 7
> 
> What is the recall value for a classifier that predicts **+1** for all data points in the **test_data**?
> 
> 1 point
> 

      1
> 
> ### 8.
> 
> Question 8
> 
> What happens to the number of positive predicted reviews as the threshold increased from 0.5 to 0.9?
> 
> 1 point
> 
>  More reviews are predicted to be positive. 
> 

      Fewer reviews are predicted to be positive. 
> 
> ### 9.
> 
> Question 9
> 
> Consider the metrics obtained from setting the threshold to 0.5 and to 0.9\.
> 
> Does the **recall** increase with a higher threshold?
> 
> 1 point
> 
>  Yes 
> 

      No 
> 
> ### 10.
> 
> Question 10
> 
> Among all the threshold values tried, what is the **smallest** threshold value that achieves a precision of 96.5% or better? Round your answer to 3 decimal places.
> 
> 1 point
> 

      0.838
> 
> ### 11.
> 
> Question 11
> 
> Using threshold = 0.98, how many **false negatives** do we get on the **test_data**? (**Hint**: You may use the turicreate.evaluation.confusion_matrix function implemented in Turi Create.)
> 
> 1 point
> 

     5826
> 
> ### 12.
> 
> Question 12
> 
> Questions 13 and 14 are concerned with the reviews that contain the word **baby**.
> 
> Among all the threshold values tried, what is the **smallest** threshold value that achieves a precision of 96.5% or better for the reviews of data in **baby_reviews**? Round your answer to 3 decimal places.
> 
> 1 point
> 
      0.864     
> 
> ### 13.
> 
> Question 13
> 
> Questions 13 and 14 are concerned with the reviews that contain the word **baby**.
> 
> Is this threshold value smaller or larger than the threshold used for the entire dataset to achieve the same specified precision of 96.5%?
> 
> 1 point
> 

      Larger 
> 
>  Smaller
>
> -- https://www.coursera.org/learn/ml-classification/exam/ObhEq/exploring-precision-and-recall/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
