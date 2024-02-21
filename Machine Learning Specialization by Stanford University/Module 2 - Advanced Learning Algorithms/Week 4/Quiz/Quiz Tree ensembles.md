# Practice quiz: Tree ensembles
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/178705ec-6d16-47e3-9bdd-b8d5fb8e8e98image3.png?expiry=1658966400000&hmac=duA0kG9E7ZIiym0vS42a86T0lPgcLtcTbSjzFiw-P_w)
> 
> For the random forest, how do you build each individual tree so that they are not all identical to each other?
> 
> 1 / 1 point
> 

      Sample the training data with replacement 
> 
>  Sample the training data without replacement 
> 
>  If you are training B trees, train each one on 1/B of the training set, so each tree is trained on a distinct set of examples. 
> 
>  Train the algorithm multiple times on the same training set. This will naturally result in different trees. 
> 
> Correct
> 
> Correct. You can generate a training set that is unique for each individual tree by sampling the training data with replacement.
> 
> ### 2.
> 
> Question 2
> 
> You are choosing between a decision tree and a neural network for a classification task where the input xxx is a 100x100 resolution image. Which would you choose?
> 
> 1 / 1 point
> 
>  A decision tree, because the input is structured data and decision trees typically work better with structured data. 
> 
>  A neural network, because the input is unstructured data and neural networks typically work better with unstructured data. 
> 

      A decision tree, because the input is unstructured and decision trees typically work better with unstructured data. 
> 
>  A neural network, because the input is structured data and neural networks typically work better with structured data. 
> 
> Correct
> 
> Yes!
> 
> ### 3.
> 
> Question 3
> 
> What does sampling with replacement refer to?
> 
> 1 / 1 point
> 
>  It refers to a process of making an identical copy of the training set. 
> 

      Drawing a sequence of examples where, when picking the next example, first replacing all previously drawn examples into the set we are picking from. 
> 
>  Drawing a sequence of examples where, when picking the next example, first remove all previously drawn examples from the set we are picking from. 
> 
>  It refers to using a new sample of data that we use to permanently overwrite (that is, to replace) the original data. 
> 
> Correct
> 
> Yes!
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/olkdC/practice-quiz-tree-ensembles/attempt?redirectToCover=true#FANsdc-legend
