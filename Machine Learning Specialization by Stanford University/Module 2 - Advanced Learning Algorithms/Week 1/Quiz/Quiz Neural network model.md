#Practice quiz: Neural network model
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/5f7ddfc8-51f8-4824-8be3-b9710fa4f466image3.png?expiry=1658707200000&hmac=RXd0ytYKhyUQoAZtZdjsqG3KtFeJBx3-EqfmWl_7BZw)
> 
> For a neural network, what is the expression for calculating the activation of the third neuron in layer 2? Note, this is different from the question that you saw in the lecture video.
> 
> 1 / 1 point
> 
>  a3[2]=g(w⃗2[3]⋅a⃗[1]+b2[3])
> 

      a3[2]=g(w⃗3[2]⋅a⃗[1]+b3[2])
> 
>  a3[2]=g(w⃗3[2]⋅a⃗[2]+b3[2])
> 
>  a3[2]=g(w⃗2[3]⋅a⃗[2]+b2[3])
> 
> Correct
> 
> Yes! The superscript [2] refers to layer 2\. The subscript 3 refers to the neuron in that layer. The input to layer 2 is the activation vector from layer 1.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/5f7ddfc8-51f8-4824-8be3-b9710fa4f466image4.png?expiry=1658707200000&hmac=9KpYvIJhAzAWoDWHGSt1AG6L7LbiM9lsgB2Jdv0MnGk)
> 
> For the handwriting recognition task discussed in lecture, what is the output a1[3]a^{[3]}_1a1[3]​?
> 
> 1 / 1 point
> 
>  A number that is either exactly 0 or 1, comprising the network’s prediction 
> 
>  A vector of several numbers that take values between 0 and 1 
> 

      The estimated probability that the input image is of a number 1, a number that ranges from 0 to 1. 
> 
>  A vector of several numbers, each of which is either exactly 0 or 1 
> 
> Correct
> 
> Yes! The neural network outputs a single number between 0 and 1.
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/9MHpG/practice-quiz-neural-network-model/attempt?redirectToCover=true#BKMK5R-legend
