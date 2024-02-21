## Preventing Overfitting in Decision Trees
> 
> Total points 11
> 
> ### 1.
> 
> Question 1
> 
> (True/False) When learning decision trees, smaller depth USUALLY translates to lower training error.
> 
> 1 point
> 
>  True 
> 

      False 
> 
> ### 2.
> 
> Question 2
> 
> (True/False) If no two data points have the same input values, we can always learn a decision tree that achieves 0 training error.
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 3.
> 
> Question 3
> 
> (True/False) If decision tree T1 has lower training error than decision tree T2, then T1 will always have better test error than T2.
> 
> 1 point
> 
>  True 
> 

      False 
> 
> ### 4.
> 
> Question 4
> 
> Which of the following is true for decision trees?
> 
> 1 point
> 
>  Model complexity increases with size of the data. 
> 

      Model complexity increases with depth. 
> 
>  None of the above 
> 
> ### 5.
> 
> Question 5
> 
> Pruning and early stopping in decision trees is used to
> 
> 1 point
> 

      combat overfitting 
> 
>  improve training error 
> 
>  None of the above 
> 
> ### 6.
> 
> Question 6
> 
> Which of the following is NOT an early stopping method?
> 
> 1 point
> 
>  Stop when the tree hits a certain depth 
> 
>  Stop when node has too few data points (minimum node “size”) 
> 

      Stop when every possible split results in the same amount of error reduction 
> 
>  Stop when best split results in too small of an error reduction 
> 
> ### 7.
> 
> Question 7
> 
> Consider decision tree T1 learned with minimum node size parameter = 1000\. Now consider decision tree T2 trained on the same dataset and parameters, except that the minimum node size parameter is now 100\. Which of the following is always true?
> 
> 1 point
> 

      The depth of T2 >= the depth of T1 
> 

      The number of nodes in T2 >= the number of nodes in T1 
> 
>  The test error of T2 <= the test error of T1 
> 

      The training error of T2 <= the training error of T1 
> 
> ### 8.
> 
> Question 8
> 
> Questions 8 to 11 refer to the following common scenario:
> 
> Imagine we are training a decision tree, and we are at a node. Each data point is (x1, x2, y), where x1,x2 are features, and y is the label. The data at this node is:
> 
> x1
> 
> x2
> 
> y
> 
> 0
> 
> 1
> 
> +1
> 
> 1
> 
> 0
> 
> +1
> 
> 0
> 
> 1
> 
> +1
> 
> 1
> 
> 1
> 
> -1
> 
> What is the classification error at this node (assuming a majority class classifier)?
> 
> 1 point
> 

     0.25
> 
> ### 9.
> 
> Question 9
> 
> Refer to the scenario presented in Question 8.
> 
> If we split on x1, what is the classification error?
> 
> 1 point
> 

     0.25
> 
> ### 10.
> 
> Question 10
> 
> Refer to the scenario presented in Question 8.
> 
> If we split on x2, what is the classification error?
> 
> 1 point
> 

     0.25
> 
> ### 11.
> 
> Question 11
> 
> Refer to the scenario presented in Question 8.
> 
> If our parameter for minimum gain in error reduction is 0.1, do we split or stop early?
> 
> 1 point
> 
>  Split 
> 

      Stop early
>
> -- https://www.coursera.org/learn/ml-classification/exam/NDTdJ/preventing-overfitting-in-decision-trees/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
