## Clustering text data with K-means
> 
> Total points 7
> 
> ### 1.
> 
> Question 1
> 
> (True/False) The clustering objective (heterogeneity) is non-increasing for this example.
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 2.
> 
> Question 2
> 
> Let's step back from this particular example. If the clustering objective (heterogeneity) would ever increase when running K-means, that would indicate: (choose one)
> 
> 1 point
> 
>  K-means algorithm got stuck in a bad local minimum 
> 

      There is a bug in the K-means code 
> 
>  All data points consist of exact duplicates 
> 
>  Nothing is wrong. The objective should generally go down sooner or later. 
> 
> ### 3.
> 
> Question 3
> 
> Refer to the output of K-means for K=3 and seed=0\. Which of the three clusters contains the greatest number of data points in the end?
> 
> 1 point
> 
>  Cluster #0 
> 
>  Cluster #1 
> 

      Cluster #2 
> 
> ### 4.
> 
> Question 4
> 
> Another way to capture the effect of changing initialization is to look at the distribution of cluster assignments. Compute the size (# of member data points) of clusters for each of the multiple runs of K-means.
> 
> Look at the size of the largest cluster (most # of member data points) across multiple runs, with seeds 0, 20000, ..., 120000\. What is the **minimum** value this quantity takes?
> 
> 1 point
> 

     15779
> 
> ### 5.
> 
> Question 5
> 
> Refer to the section "Visualize clusters of documents". Which of the 10 clusters above contains the **greatest** number of articles?
> 
> 1 point
> 

      Cluster 0: artists, books, him/his 
> 
>  Cluster 4: music, orchestra, symphony 
> 
>  Cluster 5: female figures from various fields 
> 
>  Cluster 7: law, courts, justice 
> 
>  Cluster 9: academia 
> 
> ### 6.
> 
> Question 6
> 
> Refer to the section "Visualize clusters of documents". Which of the 10 clusters above contains the **least** number of articles?
> 
> 1 point
> 
>  Cluster 1: film, theater, tv, actor 
> 
>  Cluster 3: elections, ministers 
> 
>  Cluster 6: composers, songwriters, singers, music producers 
> 

       Cluster 7: law, courts, justice 
> 
>  Cluster 8: football 
> 
> ### 7.
> 
> Question 7
> 
> Another sign of too large K is having lots of small clusters. Look at the distribution of cluster sizes (by number of member data points). How many of the 100 clusters have fewer than 236 articles, i.e. 0.4% of the dataset?
> 
> 1 point
> 

     29
>
