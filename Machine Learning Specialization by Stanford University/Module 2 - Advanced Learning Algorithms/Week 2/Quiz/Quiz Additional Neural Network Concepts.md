# Practice quiz: Additional Neural Network Concepts
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/b08fec87-b710-4ece-9022-9dcf48ab1305image3.png?expiry=1658966400000&hmac=RLfFjhY548uFbd2cv5qXl_adT0ehCwvplmcBTtVOyio)
> 
> The Adam optimizer is the recommended optimizer for finding the optimal parameters of the model. How do you use the Adam optimizer in TensorFlow?
> 
> 1 / 1 point
> 
>  The call to model.compile() uses the Adam optimizer by default 
> 
>  The call to model.compile() will automatically pick the best optimizer, whether it is gradient descent, Adam or something else. So there’s no need to pick an optimizer manually. 
> 

      When calling model.compile, set optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3). 
> 
>  The Adam optimizer works only with Softmax outputs. So if a neural network has a Softmax output layer, TensorFlow will automatically pick the Adam optimizer. 
> 
> Correct
> 
> Correct. Set the optimizer to Adam.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/b08fec87-b710-4ece-9022-9dcf48ab1305image4.png?expiry=1658966400000&hmac=Iau86SEWN2mWKDuBYHX6Otj3fyRuC7W6C9V0SaUtYmA)
> 
> The lecture covered a different layer type where each single neuron of the layer does not look at all the values of the input vector that is fed into that layer. What is this name of the layer type discussed in lecture?
> 
> 1 / 1 point
> 
>  1D layer or 2D layer (depending on the input dimension) 
> 
>  A fully connected layer 
> 

      convolutional layer 
> 
>  Image layer 
> 
> Correct
> 
> Correct. For a convolutional layer, each neuron takes as input a subset of the vector that is fed into that layer.
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/ljlgM/practice-quiz-additional-neural-network-concepts/attempt?redirectToCover=true#fqlUB2-legend
