## Implementing binary decision trees
> 
> Total points 7
> 
> ### 1.
> 
> Question 1
> 
> What was the feature that my_decision_tree first split on while making the prediction for test_data[0]?
> 
> 1 point
> 
>  emp_length.4 years 
> 
>  grade.A 
> 

      term. 36 months 
> 
>  home_ownership.MORTGAGE 
> 
> ### 2.
> 
> Question 2
> 
> What was the first feature that lead to a right split of test_data[0]?
> 
> 1 point
> 
>  emp_length.< 1 year 
> 
>  emp_length.10+ years 
> 
>  grade.B 
> 

      grade.D 
> 
> ### 3.
> 
> Question 3
> 
> What was the last feature split on before reaching a leaf node for test_data[0]?
> 
> 1 point
> 

      grade.D 
> 
>  grade.B 
> 
>  term. 36 months 
> 
>  grade.A 
> 
> ### 4.
> 
> Question 4
> 
> Rounded to 2nd decimal point (e.g. 0.76), what is the classification error of my_decision_tree on the test_data?
> 
> 1 point
> 

    0.38
> 
> ### 5.
> 
> Question 5
> 
> What is the feature that is used for the split at the root node?
> 
> 1 point
> 
>  grade.A 
> 

      term. 36 months 
> 
>  term. 60 months 
> 
>  home_ownership.OWN 
> 
> ### 6.
> 
> Question 6
> 
> What is the path of the first 3 feature splits considered along the left-most branch of my_decision_tree?
> 
> 1 point
> 

      term. 36 months, grade.A, grade.B 
> 
>  term. 36 months, grade.A, emp_length.4 years 
> 
>  term. 36 months, grade.A, no third feature because second split resulted in leaf 
> 
> ### 7.
> 
> Question 7
> 
> What is the path of the first 3 feature splits considered along the right-most branch of my_decision_tree?
> 
> 1 point
> 
>  term. 36 months, grade.D, grade.B 
> 
>  term. 36 months, grade.D, home_ownership.OWN 
> 

      term. 36 months, grade.D, no third feature because second split resulted in leaf
>
> -- https://www.coursera.org/learn/ml-classification/exam/WxrJw/implementing-binary-decision-trees/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
