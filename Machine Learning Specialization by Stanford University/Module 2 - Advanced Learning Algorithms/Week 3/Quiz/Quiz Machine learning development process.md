# Practice quiz: Machine learning development process
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/25ef86da-6935-47cf-a4af-8945fa6a0ed2image5.png?expiry=1658966400000&hmac=zpxy1-Xr4uB7JLEIFk90BRnSnIH2PCLVqtbat80ZnFw)
> 
> Which of these is a way to do error analysis?
> 
> 1 / 1 point
> 

      Manually examine a sample of the training examples that the model misclassified in order to identify common traits and trends. 
> 
>  Calculating the test error JtestJ_{test}Jtest​ 
> 
>  Collecting additional training data in order to help the algorithm do better. 
> 
>  Calculating the training error JtrainJ_{train}Jtrain​ 
> 
> Correct
> 
> Correct. By identifying similar types of errors, you can collect more data that are similar to these misclassified examples in order to train the model to improve on these types of examples.
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/25ef86da-6935-47cf-a4af-8945fa6a0ed2image3.png?expiry=1658966400000&hmac=FShq2kUBb2qVwCtawCQ0t_OXi-4GvLS-v6NDEAp6exU)
> 
> We sometimes take an existing training example and modify it (for example, by rotating an image slightly) to create a new example with the same label. What is this process called?
> 
> 1 / 1 point
> 

      Data augmentation 
> 
>  Bias/variance analysis 
> 
>  Error analysis 
> 
>  Machine learning diagnostic 
> 
> Correct
> 
> Yes! Modifying existing data (such as images, or audio) is called data augmentation.
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/25ef86da-6935-47cf-a4af-8945fa6a0ed2image4.png?expiry=1658966400000&hmac=qGIBCsmqc9acg_9ZvwIggfx8JxuKnrGLh5JWwwXltD4)
> 
> What are two possible ways to perform transfer learning? Hint: two of the four choices are correct.
> 
> 1 / 1 point
> 

      You can choose to train just the output layers' parameters and leave the other parameters of the model fixed. 
> 
> Correct
> 
> Correct. The earlier layers of the model may be reusable as is, because they are identifying low level features that are relevant to your task.
> 

      You can choose to train all parameters of the model, including the output layers, as well as the earlier layers. 
> 
> Correct
> 
> Correct. It may help to train all the layers of the model on your own training set. This may take more time compared to if you just trained the parameters of the output layers.
> 
>  Given a dataset, pre-train and then further fine tune a neural network on the same dataset. 
> 
>  Download a pre-trained model and use it for prediction without modifying or re-training it.
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/eXHPZ/practice-quiz-machine-learning-development-process/attempt?redirectToCover=true#aDwwFH-legend
