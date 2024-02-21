# Practice quiz: Bias and variance
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0597681e-6ccc-4f13-bd62-6c322925cf90image5.png?expiry=1658966400000&hmac=4XzQLlSE7CffvSSNm-KvlFdGsdFyZq8uQFuKuvg0m2Y)
> 
> If the model's cross validation error JcvJ_{cv}Jcv​ is much higher than the training error JtrainJ_{train}Jtrain​, this is an indication that the model has…
> 
> 1 / 1 point
> 
>  Low bias 
> 

      high variance 
> 
>  high bias 
> 
>  Low variance 
> 
> Correct
> 
> When Jcv>>JtrainJ_{cv} >> J_{train}Jcv​>>Jtrain​ (whether JtrainJ_{train}Jtrain​ is also high or not, this is a sign that the model is overfitting to the training data and performing much worse on new examples.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0597681e-6ccc-4f13-bd62-6c322925cf90image3.png?expiry=1658966400000&hmac=n52rYmejZ2mx3SyfM0dG7ru2LIdF8KYpmsPqXCfeoAI)
> 
> Which of these is the best way to determine whether your model has high bias (has underfit the training data)?
> 
> 1 / 1 point
> 
>  See if the cross validation error is high compared to the baseline level of performance 
> 
>  Compare the training error to the cross validation error. 
> 
>  See if the training error is high (above 15% or so) 
> 

      Compare the training error to the baseline level of performance 
> 
> Correct
> 
> Correct. If comparing your model's training error to a baseline level of performance (such as human level performance, or performance of other well-established models), if your model's training error is much higher, then this is a sign that the model has high bias (has underfit).
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0597681e-6ccc-4f13-bd62-6c322925cf90image4.png?expiry=1658966400000&hmac=HiJcuq_SAPnqcCXVOD_PoA-EMdZPv3EzECrJT3NmCoM)
> 
> You find that your algorithm has high bias. Which of these seem like good options for improving the algorithm’s performance? Hint: two of these are correct.
> 
> 1 / 1 point
> 
>  Remove examples from the training set 
> 
>  Collect more training examples 
> 

      Collect additional features or add polynomial features 
> 
> Correct
> 
> Correct. More features could potentially help the model better fit the training examples.
> 

      Decrease the regularization parameter λ\lambdaλ (lambda) 
> 
> Correct
> 
> Correct. Decreasing regularization can help the model better fit the training data.
> 
> ### 4.
> 
> Question 4
> 
> You find that your algorithm has a training error of 2%, and a cross validation error of 20% (much higher than the training error). Based on the conclusion you would draw about whether the algorithm has a high bias or high variance problem, which of these seem like good options for improving the algorithm’s performance? Hint: two of these are correct.
> 
> 1 / 1 point
> 

      Increase the regularization parameter λ\lambdaλ 
> 
> Correct
> 
> Yes, the model appears to have high variance (overfit), and increasing regularization would help reduce high variance.
> 

      Collect more training data 
> 
> Correct
> 
> Yes, the model appears to have high variance (overfit), and collecting more training examples would help reduce high variance.
> 
>  Reduce the training set size 
> 
>  Decrease the regularization parameter λ\lambdaλ
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/FakV2/practice-quiz-bias-and-variance/attempt?redirectToCover=true#DIXDsh-legend
