## Identifying safe loans with decision trees
> 
> Total points 6
> 
> ### 1.
> 
> Question 1
> 
> What percentage of the predictions on sample_validation_data did decision_tree_model get correct?
> 
> 1 point
> 
>  25% 
> 

      50% 
> 
>  75% 
> 
>  100% 
> 
> ### 2.
> 
> Question 2
> 
> Which loan has the highest probability of being classified as a safe loan?
> 
> 1 point
> 
>  First 
> 
>  Second 
> 
>  Third 
> 

      Fourth 
> 
> ### 3.
> 
> Question 3
> 
> Notice that the probability preditions are the exact same for the 2nd and 3rd loans. Why would this happen?
> 
> 1 point
> 

      During tree traversal both examples fall into the same leaf node. 
> 
>  This can only happen with sheer coincidence. 
> 
> ### 4.
> 
> Question 4
> 
> What is the accuracy of decision_tree_model on the validation set, rounded to the nearest .01 (e.g. 0.76)?
> 
> 1 point
> 

     0.64
> 
> ### 5.
> 
> Question 5
> 
> How does the performance of big_model on the validation set compare to decision_tree_model on the validation set? Is this a sign of overfitting?
> 
> 1 point
> 
>  big_model has higher accuracy on the validation set than decision_tree_model. This is overfitting. 
> 
>  big_model has higher accuracy on the validation set than decision_tree_model. This is not overfitting. 
> 

      big_model has lower accuracy on the validation set than decision_tree_model. This is overfitting. 
> 
>  big_model has lower accuracy on the validation set than decision_tree_model. This is not overfitting. 
> 
> ### 6.
> 
> Question 6
> 
> Let us assume that each mistake costs money:
> 
> *   Assume a cost of $10,000 per false negative.
> 
> *   Assume a cost of $20,000 per false positive.
> 
> What is the total cost of mistakes made by decision_tree_model on validation_data? Please enter your answer as a plain integer, without the dollar sign or the comma separator, e.g. 3002000.
> 
> 1 point
> 

        50390000    
>
> -- https://www.coursera.org/learn/ml-classification/exam/xHRYe/identifying-safe-loans-with-decision-trees/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
