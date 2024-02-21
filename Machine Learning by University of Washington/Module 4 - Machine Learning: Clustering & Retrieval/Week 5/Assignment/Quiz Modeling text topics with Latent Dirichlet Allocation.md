## Modeling text topics with Latent Dirichlet Allocation
> 
> Total points 10
> 
> ### 1.
> 
> Question 1
> 
> Identify the top 3 most probable words for the first topic.
> 
> 1 point
> 

      institute 
> 

      university 
> 

      president 
> 
>  business 
> 
>  board 
> 
>  game 
> 
>  coach 
> 
> ### 2.
> 
> Question 2
> 
> What is the sum of the probabilities assigned to the top 50 words in the 3rd topic? Round your answer to 3 decimal places.
> 
> 1 point
> 

    0.210
> 
> ### 3.
> 
> Question 3
> 
> What is the topic most closely associated with the article about former US President George W. Bush? Use the average results from 100 topic predictions.
> 
> 1 point
> 

    general politics
> 
> ### 4.
> 
> Question 4
> 
> What are the top 3 topics corresponding to the article about English football (soccer) player Steven Gerrard? Use the average results from 100 topic predictions.
> 
> 1 point
> 

      international athletics 
> 

      Great Britain and Australia 
> 

      team sports 
> 
>  general music 
> 
>  science and research 
> 
> ### 5.
> 
> Question 5
> 
> What was the value of alpha used to fit our original topic model?
> 
> 1 point
> 

     5.0
> 
> ### 6.
> 
> Question 6
> 
> What was the value of gamma used to fit our original topic model? Remember that Turi Create uses "beta" instead of "gamma" to refer to the hyperparameter that influences topic distributions over words.
> 
> 1 point
> 

     0.1
> 
> ### 7.
> 
> Question 7
> 
> How many topics are assigned a weight greater than 0.3 or less than 0.05 for the article on Paul Krugman in the **low alpha** model? Use the average results from 100 topic predictions.
> 
> 1 point
> 

     8
> 
> ### 8.
> 
> Question 8
> 
> How many topics are assigned a weight greater than 0.3 or less than 0.05 for the article on Paul Krugman in the **high alpha** model? Use the average results from 100 topic predictions.
> 
> 1 point
> 

     2
> 
> ### 9.
> 
> Question 9
> 
> For each topic of the **low gamma model**, compute the number of words required to make a list with total probability 0.5\. What is the average number of words required across all topics? (HINT: use the get_topics() function from Turi Create with the cdf_cutoff argument.)
> 
> 1 point
> 

     252.4
> 
> ### 10.
> 
> Question 10
> 
> For each topic of the **high gamma model**, compute the number of words required to make a list with total probability 0.5\. What is the average number of words required across all topics? (HINT: use the get_topics() function from Turi Create with the _cdf___cutoff_ argument).
> 
> 1 point
> 

     576.2
>
