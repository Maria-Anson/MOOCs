# K Means Clustering
> ### 1.
> 
> Question 1
> 
> (True/False) Is the following statement True or False?
> 
> _“We initialize our K-means algorithm by taking 2 random points and these points are going to act as the centroids”._
> 
> 1 / 1 point
> 

      True 
> 
>  False 
> 
> Correct
> 
> Correct! We initialize the algorithm by taking 2 random points and these are going to act as the centroids, with our centroids initiated we determinate to which cluster belongs to, by computing the distance to the nearest centroid and seeing which one is closer. You can find more information in the lesson _K-means part 1._
> 
> ### 2.
> 
> Question 2
> 
> Which of the following statements best describes the iterative part of the K-means algorithm?
> 
> 1 / 1 point
> 
>  The k-means algorithm assigns a number of clusters at random. 
> 

      The k-means algorithm adjusts the centroids to the new mean of each cluster, and then it keeps repeating this process until no example is assigned to another cluster. 
> 
>  The k-means algorithm iteratively deletes outliers. 
> 
>  The k-means algorithm iteratively calculates the distance from each point to the centroid of each cluster. 
> 
> Correct
> 
> Correct! You can find more information in the lesson _K-means part 1._
> 
> ### 3.
> 
> Question 3
> 
> (True/False) Is the following statement True or False?
> 
> _“The problem with K-means algorithm is that is sensitive to the choice of the initial points, so different initial configurations may yield different results”._
> 
> 1 / 1 point
> 
>  False 
> 

      True 
> 
> Correct
> 
> Correct! This is a true problem for the K-mean algorithm, but there are ways to overcome this. You can find more information in the lesson _K-means part 1._
> 
> ### 4.
> 
> Question 4
> 
> Which statement describes better “The Smarter initialization of K-mean clusters?
> 
> 1 / 1 point
> 
>  “Draw a line between the data points to create 2 big clusters.” 
> 
>  “After we find our centroids, we calculate the distance between all our data points.” 
> 

      “Pick one point random as initial point and for the second pick instead of doing it randomly we prioritize by assigning the probability of the distance.” 
> 
>  “We start by having two centroids as far as possible between each other.” 
> 
> Correct
> 
> Correct! This one defines it and remember: The smarter initialization of K-mean clusters is called, K-means ++, and it helps to avoid getting stuck at these local optima. This is the default implementation of the K-means. You can find more information in the lesson _K-means part 2._
> 
> ### 5.
> 
> Question 5
> 
> What happen with our second cluster centroid when we use the probability formula?
> 
> 1 / 1 point
> 
>  When we use the probability formula, we put less weight on the points that are far away. So, our second cluster centroid is likely going to be closer. 
> 

      When we use the probability formula, we put more weight on the points that are far away. So, our second cluster centroid is likely going to be more distant. 
> 
>  When we use the probability formula, we put more weight on the lighter centroids, because it will take more computational power to draw our clusters. So, the second cluster centroid is likely going to be less distant. 
> 
>  When we use the probability formula, we put less weight on the points that are far away. So, our second cluster centroid is likely going to be more distant. 
> 
> Correct
> 
> Correct! This happens because it will take a larger proportion of the total distance square of all our points. You can find more information in the lesson _K-means part 2._
>
> -- https://www.coursera.org/learn/ibm-unsupervised-machine-learning/exam/R3bVi/k-means-clustering/view-attempt#HTlSI6-legend
