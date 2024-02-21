# Practice quiz: Decision trees
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2f88deea-2113-4c00-9f88-79e87fa4e329image3.png?expiry=1658966400000&hmac=iJ3bhhazOmfvk20qXhEiEQCJoMpUMJfNMqLkxOlVSFc)
> 
> Based on the decision tree shown in the lecture, if an animal has floppy ears, a round face shape and has whiskers, does the model predict that it's a cat or not a cat?
> 
> 1 / 1 point
> 

      cat 
> 
>  Not a cat 
> 
> Correct
> 
> Correct. If you follow the floppy ears to the right, and then from the whiskers decision node, go left because whiskers are present, you reach a leaf node for "cat", so the model would predict that this is a cat.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2f88deea-2113-4c00-9f88-79e87fa4e329image4.png?expiry=1658966400000&hmac=x8TWWvMyI8OxPOCvKxnJIyDrE5disYd1qluiRbmaKHo)
> 
> Take a decision tree learning to classify between spam and non-spam email. There are 20 training examples at the root note, comprising 10 spam and 10 non-spam emails. If the algorithm can choose from among four features, resulting in four corresponding splits, which would it choose (i.e., which has highest purity)?
> 
> 1 / 1 point
> 
>  Left split: 7 of 8 emails are spam. Right split: 3 of 12 emails are spam. 
> 
>  Left split: 5 of 10 emails are spam. Right split: 5 of 10 emails are spam. 
> 

      Left split: 10 of 10 emails are spam. Right split: 0 of 10 emails are spam. 
> 
>  Left split: 2 of 2 emails are spam. Right split: 8 of 18 emails are spam. 
> 
> Correct
> 
> Yes!
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/oLdIe/practice-quiz-decision-trees/attempt?redirectToCover=true#6E6iqx-legend
