## Implementing EM for Gaussian mixtures
> 
> Total points 6
> 
> ### 1.
> 
> Question 1
> 
> What is the weight that EM assigns to the first component after running the above codeblock? Round your answer to 3 decimal places.
> 
> 1 point
> 

     0.300
> 
> ### 2.
> 
> Question 2
> 
> Using the same set of results, obtain the mean that EM assigns the second component. What is the mean in the first dimension? Round your answer to 3 decimal places.
> 
> 1 point
> 

     4.942
> 
> ### 3.
> 
> Question 3
> 
> Using the same set of results, obtain the covariance that EM assigns the third component. What is the variance in the first dimension? Round your answer to 3 decimal places.
> 
> 1 point
> 

     0.671
> 
> ### 4.
> 
> Question 4
> 
> Is the loglikelihood plot monotonically increasing, monotonically decreasing, or neither?
> 
> 1 point
> 

      Monotonically increasing 
> 
>  Monotonically decreasing 
> 
>  Neither 
> 
> ### 5.
> 
> Question 5
> 
> Calculate the likelihood (score) of the first image in our data set (img[0]) under each Gaussian component through a call to `multivariate_normal.pdf`. Given these values, what cluster assignment should we make for this image?
> 
> 1 point
> 
>  Cluster 0 
> 
>  Cluster 1 
> 
>  Cluster 2 
> 

      Cluster 3 
> 
> ### 6.
> 
> Question 6
> 
> **Four** of the following images are **not** in the list of top 5 images in the **first cluster**. Choose these four.
> 
> 1 point
> 
>  Image 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8jt0GI3SEea4XAqR8EpoMw_a80c51950292f316db6999e7a8c63501_ANd9GcRuM9jj0NZmoAvB5jMOtCg01f-Ng27IjKjCMX_1cqa9rKk4gqOt.jpg?expiry=1657843200000&hmac=wDAQk6sQMZnr7Ys8zOa4iOyLjfw790OQBkbeYiqscxY) 

      Correct
> 
>  Image 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/UhifLI3TEea4XAqR8EpoMw_68b8546c2f0e3f6d9ef04a3ed958a9d1_ANd9GcT852qrQI1RcoAd9-3xnqMPC37O-2cfwHHZiRKSd8ek0PoZ5fA0dg.jpg?expiry=1657843200000&hmac=7XeFNmpEXM_tok7CIv2GZPR-zfH5gQFd8i8lcoY-xio) 

      Correct
> 
>  Image 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/gja9fo3TEea7Xg7ev7rZkQ_a7010f931d59651ebf66a09fc0a6a7b1_ANd9GcQHd24C1XCc_Yk0g2Co75Il2vnze29GXLZEj8x9ut76iFEb3SvIpw.jpg?expiry=1657843200000&hmac=EskgUYU-H10wgiUfsLxdTx0GdslEsqZAAYOwRCRBf88) 
> 
>  Image 4
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Ly0mV43UEea0sQoj9h_9jQ_620d84b1853375f193dd527ca984ab10_ANd9GcTtUbQ7FRfFRLZ6I9bQElBVx7MYfx6a3rPLcrUrGSPwzY40wP9tiA.jpg?expiry=1657843200000&hmac=LRY8AIUpG6L4N5BRm3UwD68SDhaVEfwQuNTztf8_lGY) 
> 
>  Image 5
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0_9dnY3UEea7Xg7ev7rZkQ_23181f65e67404e1807af3f4a3e0b73f_ANd9GcTGWO6pnQzfs0rffCsdiz7puprjB5hTm--LYws1ju7VuyBvyqDB_g.jpg?expiry=1657843200000&hmac=6cI8hSQnLF5bT11Qz6xUKMaOVQcgm1alZY6a6w8T6l8) 
> 
>  Image 6
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/RblI_I3VEea9qA4Z6lKA3Q_345ccb519a0dda1dc82cf0c60c74544c_ANd9GcRNqNFV9XD8qS8ed-r0a61AUeDqZXSDL93sRqNzOWecjAVBI0czoA.jpg?expiry=1657843200000&hmac=Qwp_hEsAjuVcLbqRaEl7SQEzXH0i1v6a4Kz_qW4T4No) 
> 
>  Image 7
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/VV7ewI3VEeaapgob0rvkxw_f07c2ef737619db0e6670c55f5cbde2b_ANd9GcRb8NpM-WDNu3Y9jxvbruIdbG0cO2k00D7R0qeWOtRj5uMinpyi.jpg?expiry=1657843200000&hmac=rHM-AVsCj9s83RoN58Nnvh_-TF1u357u0V_0iopnAnE)
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/exam/UnnXU/implementing-em-for-gaussian-mixtures/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
