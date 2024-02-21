# Content-based filtering
> ### 1.
> 
> Question 1
> 
> Vector xux_uxu​ and vector xmx_mxm​ must be of the same dimension, where xux_uxu​ is the input features vector for a user (age, gender, etc.) xmx_mxm​ is the input features vector for a movie (year, genre, etc.) True or false?
> 
> 1 / 1 point
> 
>  True 
> 

      False 
> 
> Correct
> 
> These vectors can be different dimensions.
> 
> ### 2.
> 
> Question 2
> 
> If we find that two movies, iii and kkk, have vectors vm(i)v_m^{(i)}vm(i)​ and vm(k)v_m^{(k)}vm(k)​ that are similar to each other (i.e., ∣∣vm(i)−vm(k)∣∣||v_m^{(i)} - v_m^{(k)}||∣∣vm(i)​−vm(k)​∣∣ is small), then which of the following is likely to be true? Pick the best answer.
> 
> 1 / 1 point
> 

      The two movies are similar to each other and will be liked by similar users. 
> 
>  The two movies are very dissimilar. 
> 
>  A user that has watched one of these two movies has probably watched the other as well. 
> 
>  We should recommend to users one of these two movies, but not both. 
> 
> Correct
> 
> Similar movies generate similar vmv_mvm​’s.
> 
> ### 3.
> 
> Question 3
> 
> Which of the following neural network configurations are valid for a content based filtering application? Please note carefully the dimensions of the neural network indicated in the diagram. Check all the options that apply:
> 
> 1 / 1 point
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/62d86c86-30aa-41a3-a88b-bad03438f032image3.png?expiry=1659225600000&hmac=5VFlp-olJcfX1mkBpO93O0bb4KKoTy987BKV45InYGQ)
> 
> The user and the item networks have different architectures 
> 

     Correct
> 
> User and item networks can be the same or different sizes.
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/62d86c86-30aa-41a3-a88b-bad03438f032image4.png?expiry=1659225600000&hmac=H-_wA6ssbM-LO7JEynXME5IvXPKtxSlNX-uHNcYVvOA)
> 
> Both the user and the item networks have the same architecture 
> 

     Correct
> 
> User and item networks can be the same or different sizes.
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/62d86c86-30aa-41a3-a88b-bad03438f032image2.png?expiry=1659225600000&hmac=bxB9Xlm-X6ULUxzm4Vj16oUVeO-CmDRpw5ub6FXPqBY)
> 
> The user and item networks have 64 dimensional v_u and v_m vector respectively 
> 

     Correct
> 
> Feature vectors can be any size so long as vuv_uvu​ and vmv_mvm​ are the same size.
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/62d86c86-30aa-41a3-a88b-bad03438f032image5.png?expiry=1659225600000&hmac=AB4ds0JdzaNfBIWozw-VMt7f1wooCP2NOIAk0Rpj7mw)
> 
> The user vector v_u is 32 dimensional, and the item vector v_m is 64 dimensional 
> 
> ### 4.
> 
> Question 4
> 
> You have built a recommendation system to retrieve musical pieces from a large database of music, and have an algorithm that uses separate retrieval and ranking steps. If you modify the algorithm to add more musical pieces to the retrieved list (i.e., the retrieval step returns more items), which of these are likely to happen? Check all that apply.
> 
> 1 / 1 point
> 

      The system’s response time might increase (i.e., users have to wait longer to get recommendations) 
> 
> Correct
> 
> A larger retrieval list may take longer to process which may_increase_ response time.
> 
>  The quality of recommendations made to users should stay the same or worsen. 
> 
>  The system’s response time might decrease (i.e., users get recommendations more quickly) 
> 

      The quality of recommendations made to users should stay the same or improve. 
> 
> Correct
> 
> A larger retrieval list gives the ranking system more options to choose from which should maintain or improve recommendations.
> 
> ### 5.
> 
> Question 5
> 
> To speed up the response time of your recommendation system, you can pre-compute the vectors v_m for all the items you might recommend. This can be done even before a user logs in to your website and even before you know the xux_uxu​ or vuv_uvu​ vector. True/False?
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Correct
> 
> The output of the item/movie neural network, vmv_mvm​ is not dependent on the user network when making predictions. Precomputing the results speeds up the prediction process.
>
> -- https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning/exam/Ydam1/content-based-filtering/attempt?redirectToCover=true#vnB0pg-legend
