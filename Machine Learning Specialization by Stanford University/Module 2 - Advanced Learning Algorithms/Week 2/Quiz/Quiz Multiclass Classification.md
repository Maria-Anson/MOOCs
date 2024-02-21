# Practice quiz: Multiclass Classification
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f38d2d9d-5e70-4900-bd84-baf812439294image2.png?expiry=1658966400000&hmac=NVX2mBj0g7h2J6abD3V5yADeOaqEvz41YVP1PMcPoUM)
> 
> For a multiclass classification task that has 4 possible outputs, the sum of all the activations adds up to 1\. For a multiclass classification task that has 3 possible outputs, the sum of all the activations should add up to ….
> 
> 1 / 1 point
> 

      1 
> 
>  Less than 1 
> 
>  It will vary, depending on the input x. 
> 
>  More than 1 
> 
> Correct
> 
> Yes! The sum of all the softmax activations should add up to 1\. One way to see this is that if ez1=10,ez2=20,ez3=30e^{z_1}=10, e^{z_2}=20,e^{z_3}=30ez1​=10,ez2​=20,ez3​=30, then the sum of a1+a2+a3a_1 + a_2 + a_3a1​+a2​+a3​ is equal to ez1+ez2+ez3ez1+ez2+ez3\frac{e^{z_1} + e^{z_2} + e^{z_3}}{e^{z_1} + e^{z_2} + e^{z_3}}ez1​+ez2​+ez3​ez1​+ez2​+ez3​​ which is 1.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f38d2d9d-5e70-4900-bd84-baf812439294image4.png?expiry=1658966400000&hmac=C-5wUISJcVQvP_8IQs4bpACa66jscIiisyzoSeP6DlI)
> 
> For multiclass classification, the cross entropy loss is used for training the model. If there are 4 possible classes for the output, and for a particular training example, the true class of the example is class 3 (y=3), then what does the cross entropy loss simplify to? [Hint: This loss should get smaller when a3a_3a3​ gets larger.]
> 
> 1 / 1 point
> 

      −log(a3)
> 
>  z_3 
> 
>  −log(a1)+−log(a2)+−log(a3)+−log(a4)4\frac{-log(a_1) + -log(a_2) + -log(a_3) + -log(a_4) }{4}4−log(a1​)+−log(a2​)+−log(a3​)+−log(a4​)​ 
> 
>  z_3/(z_1+z_2+z_3+z_4) 
> 
> Correct
> 
> Correct. When the true label is 3, then the cross entropy loss for that training example is just the negative of the log of the activation for the third neuron of the softmax. All other terms of the cross entropy loss equation (−log(a1),−log(a2),and−log(a4)-log(a_1),-log(a_2), and -log(a_4) −log(a1​),−log(a2​),and−log(a4​)) are ignored
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f38d2d9d-5e70-4900-bd84-baf812439294image5.png?expiry=1658966400000&hmac=lsRPCLK-C7QemepCIQ7SqxH_bAQjcWeRbbYLx0LShxc)
> 
> For multiclass classification, the recommended way to implement softmax regression is to set from_logits=True in the loss function, and also to define the model's output layer with…
> 
> 1 / 1 point
> 
>  a 'softmax' activation 
> 

      a 'linear' activation 
> 
> Correct
> 
> Yes! Set the output as linear, because the loss function handles the calculation of the softmax with a more numerically stable method.
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/d9Buy/practice-quiz-multiclass-classification/attempt?redirectToCover=true#z9DT0J-legend
