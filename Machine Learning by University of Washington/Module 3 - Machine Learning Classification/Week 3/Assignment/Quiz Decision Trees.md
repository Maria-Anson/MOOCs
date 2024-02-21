## Decision Trees
> 
> Total points 11
> 
> ### 1.
> 
> Question 1
> 
> Questions 1 to 6 refer to the following common scenario:
> 
> Consider the following dataset:
> 
> x1
> 
> x2
> 
> x3
> 
> y
> 
> 1
> 
> 1
> 
> 1
> 
> +1
> 
> 0
> 
> 1
> 
> 0
> 
> -1
> 
> 1
> 
> 0
> 
> 1
> 
> -1
> 
> 0
> 
> 0
> 
> 1
> 
> +1
> 
> Let us train a decision tree with this data. Let’s call this tree T1\. What feature will we split on at the root?
> 
> 1 point
> 
>  x1 
> 
>  x2 
> 

      x3 
> 
> ### 2.
> 
> Question 2
> 
> Refer to the dataset presented in Question 1 to answer the following.
> 
> Fully train T1 (until each leaf has data points of the same output label). What is the depth of T1?
> 
> 1 point
> 

     3
> 
> ### 3.
> 
> Question 3
> 
> Refer to the dataset presented in Question 1 to answer the following.
> 
> What is the training error of T1?
> 
> 1 point
> 

     0
> 
> ### 4.
> 
> Question 4
> 
> Refer to the dataset presented in Question 1 to answer the following.
> 
> Now consider a tree T2, which splits on x1 at the root, and splits on x2 in the 1st level, and has leaves at the 2nd level. Note: this is the XOR function on features 1 and 2\. What is the depth of T2?
> 
> 1 point
> 

     2
> 
> ### 5.
> 
> Question 5
> 
> Refer to the dataset presented in Question 1 to answer the following.
> 
> What is the training error of T2?
> 
> 1 point
> 

     0
> 
> ### 6.
> 
> Question 6
> 
> Refer to the dataset presented in Question 1 to answer the following.
> 
> Which has smaller depth, T1 or T2?
> 
> 1 point
> 
>  T1 
> 

      T2 
> 
> ### 7.
> 
> Question 7
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
> -1
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
> +1
> 
> Which feature results in the best split?
> 
> 1 point
> 
>  x1 
> 

      x2 
> 
> ### 8.
> 
> Question 8
> 
> Let’s say we have learned a decision tree on dataset D. Consider the split learned at the root of the decision tree. Which of the following is true if one of the data points in D is removed and we re-train the tree?
> 
> 1 point
> 
>  The split at the root will be different 
> 
>  The split at the root will be exactly the same as before 
> 

      The split could be the same or could be different 
> 
> ### 9.
> 
> Question 9
> 
> Consider two datasets D1 and D2, where D2 has the same data points as D1, but has an extra feature for each data point. Let T1 be the decision tree trained with D1, and T2 be the tree trained with D2\. Which of the following is true?
> 
> 1 point
> 
>  T2 has better training error than T1 
> 
>  T2 has better test error than T1 
> 

      Too little information to guarantee anything 
> 
> ### 10.
> 
> Question 10
> 
> (True/False) Logistic regression with polynomial degree 1 features will always have equal or lower training error than decision stumps (depth 1 decision trees).
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 11.
> 
> Question 11
> 
> (True/False) Decision stumps (depth 1 decision trees) are always linear classifiers.
> 
> 1 point
> 

      True 
>
>
> False
>
> -- https://www.coursera.org/learn/ml-classification/exam/c4ssq/decision-trees/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
