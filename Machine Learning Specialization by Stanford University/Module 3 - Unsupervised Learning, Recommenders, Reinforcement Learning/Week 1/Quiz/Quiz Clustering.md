# Clustering
> ### 1.
> 
> Question 1
> 
> Which of these best describes unsupervised learning?
> 
> 1 / 1 point
> 
>  A form of machine learning that finds patterns without using a cost function. 
> 
>  A form of machine learning that finds patterns using labeled data (x, y) 
> 

      A form of machine learning that finds patterns using unlabeled data (x). 
> 
>  A form of machine learning that finds patterns in data using only labels (y) but without any inputs (x) . 
> 
> Correct
> 
> Unsupervised learning uses unlabeled data. The training examples do not have targets or labels "y". Recall the T-shirt example. The data was height and weight but no target size.
> 
> ### 2.
> 
> Question 2
> 
> Which of these statements are true about K-means? Check all that apply.
> 
> 1 / 1 point
> 

      The number of cluster assignment variables c(i)c^{(i)}c(i) is equal to the number of training examples. 
> 
> Correct
> 
> c(i)c^{(i)}c(i) describes which centroid example(i)(i)(i) is assigned to.
> 

      If you are running K-means with K=3K=3K=3 clusters, then each c(i)c^{(i)}c(i) should be 1, 2, or 3\. 
> 
> Correct
> 
> c(i)c^{(i)}c(i) describes which centroid example(iii) is assigned to. If K=3K=3K=3, then c(i)c^{(i)}c(i) would be one of 1,2 or 3 assuming counting starts at 1.
> 
>  The number of cluster centroids μk\mu_kμk​ is equal to the number of examples. 
> 

      If each example x is a vector of 5 numbers, then each cluster centroid μk\mu_kμk​ is also going to be a vector of 5 numbers. 
> 
> Correct
> 
> The dimension of μk\mu_kμk​ matches the dimension of the examples.
> 
> ### 3.
> 
> Question 3
> 
> You run K-means 100 times with different initializations. How should you pick from the 100 resulting solutions?
> 
> 1 / 1 point
> 
>  Pick the last one (i.e., the 100th random initialization) because K-means always improves over time 
> 
>  Pick randomly -- that was the point of random initialization. 
> 
>  Average all 100 solutions together. 
> 

      Pick the one with the lowest cost JJJ 
> 
> Correct
> 
> K-means can arrive at different solutions depending on initialization. After running repeated trials, choose the solution with the lowest cost.
> 
> ### 4.
> 
> Question 4
> 
> You run K-means and compute the value of the cost function J(c(1),…,c(m),μ1,…,μK)J(c^{(1)}, …, c^{(m)}, \mu_1, …, \mu_K)J(c(1),…,c(m),μ1​,…,μK​) after each iteration. Which of these statements should be true?
> 
> 1 / 1 point
> 

      The cost will either decrease or stay the same after each iteration. . 
> 
>  The cost can be greater or smaller than the cost in the previous iteration, but it decreases in the long run. 
> 
>  There is no cost function for the K-means algorithm. 
> 
>  Because K-means tries to maximize cost, the cost is always greater than or equal to the cost in the previous iteration. 
> 
> Correct
> 
> The cost never increases. K-means always converges.
> 
> ### 5.
> 
> Question 5
> 
> In K-means, the elbow method is a method to
> 
> 1 / 1 point
> 
>  Choose the best number of samples in the dataset 
> 
>  Choose the maximum number of examples for each cluster 
> 
>  Choose the best random initialization 
> 

      Choose the number of clusters K 
> 
> Correct
> 
> The elbow method plots a graph between the number of clusters K and the cost function. The ‘bend’ in the cost curve can suggest a natural value for K. Note that this feature may not exist or be significant in some data sets.
>
> -- https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning/exam/pThlX/clustering/attempt?redirectToCover=true#4fcmtK-legend
