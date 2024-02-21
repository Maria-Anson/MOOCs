# Practice quiz: Activation Functions
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/abeab774-084a-4758-9d01-bc275c77c747image4.png?expiry=1658880000000&hmac=Q9i56wTcewZx_eTfHVJdcNXdH4OfsGSAe3I8g3siP18)
> 
> Which of the following activation functions is the most common choice for the hidden layers of a neural network?
> 
> 1 / 1 point
> 

      ReLU (rectified linear unit) 
> 
>  Linear 
> 
>  Sigmoid 
> 
>  Most hidden layers do not use any activation function 
> 
> Correct
> 
> Yes! A ReLU is most often used because it is faster to train compared to the sigmoid. This is because the ReLU is only flat on one side (the left side) whereas the sigmoid goes flat (horizontal, slope approaching zero) on both sides of the curve.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/abeab774-084a-4758-9d01-bc275c77c747image3.png?expiry=1658880000000&hmac=u7QD3KlSfDxYgZ9XdtRgJCjrioa39smrgMmmighKzVs)
> 
> For the task of predicting housing prices, which activation functions could you choose for the output layer? Choose the 2 options that apply.
> 
> 1 / 1 point
> 

      ReLU 
> 
> Correct
> 
> Yes! ReLU outputs values 0 or greater, and housing prices are positive values.
> 

      linear 
> 
> Correct
> 
> Yes! A linear activation function can be used for a regression task where the output can be both negative and positive, but it's also possible to use it for a task where the output is 0 or greater (like with house prices).
> 
>  Sigmoid 
> 
> ### 3.
> 
> Question 3
> 
> True/False? A neural network with many layers but no activation function (in the hidden layers) is not effective; that’s why we should instead use the linear activation function in every hidden layer.
> 
> 1 / 1 point
> 
>  True 
> 

      False 
> 
> Correct
> 
> Yes! A neural network with many layers but no activation function is not effective. A linear activation is the same as "no activation function".
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/7gq3P/practice-quiz-activation-functions/attempt?redirectToCover=true#CVrz63-legend
