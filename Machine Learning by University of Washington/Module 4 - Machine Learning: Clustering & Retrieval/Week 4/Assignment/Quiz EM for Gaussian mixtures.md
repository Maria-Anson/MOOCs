## EM for Gaussian mixtures
> 
> Total points 10
> 
> ### 1.
> 
> Question 1
> 
> (True/False) While the EM algorithm maintains uncertainty about the cluster assignment for each observation via soft assignments, the model assumes that every observation comes from only one cluster.
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
> (True/False) In high dimensions, the EM algorithm runs the risk of setting cluster variances to zero.
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 3.
> 
> Question 3
> 
> In the EM algorithm, what do the E step and M step represent, respectively?
> 
> 1 point
> 

      **E**stimate cluster responsibilities, **M**aximize likelihood over parameters 
> 
>  **E**stimate likelihood over parameters, **M**aximize cluster responsibilities 
> 
>  **E**stimate number of parameters, **M**aximize likelihood over parameters 
> 
>  **E**stimate likelihood over parameters, **M**aximize number of parameters 
> 
> ### 4.
> 
> Question 4
> 
> Suppose we have data that come from a mixture of 6 Gaussians (i.e., that is the true data structure). Which model would we expect to have the highest log-likelihood after fitting via the EM algorithm?
> 
> 1 point
> 
>  A mixture of Gaussians with 2 component clusters 
> 
>  A mixture of Gaussians with 4 component clusters 
> 
>  A mixture of Gaussians with 6 component clusters 
> 
>  A mixture of Gaussians with 7 component clusters 
> 

      A mixture of Gaussians with 10 component clusters 
> 
> ### 5.
> 
> Question 5
> 
> Which of the following correctlydescribes the differences between EM for mixtures of Gaussians and k-means? Choose all that apply.
> 
> 1 point
> 
>  k-means often gets stuck in a local minimum, while EM tends not to 
> 

      EM is better at capturing clusters of different sizes and orientations 
> 

      EM is better at capturing clusters with overlaps 
> 
>  EM is less prone to overfitting than k-means 
> 

      k-means is equivalent to running EM with infinitesimally small diagonal covariances. 
> 
> ### 6.
> 
> Question 6
> 
> Suppose we are running the EM algorithm. After an E-step, we obtain the following responsibility matrix:
> 
> Cluster responsibilities
> 

     Cluster A
> 
> Cluster B
> 
> Cluster C
> 
> Data point 1
> 
> 0.20
> 
> 0.40
> 
> 0.40
> 
> Data point 2
> 
> 0.50
> 
> 0.10
> 
> 0.40
> 
> Data point 3
> 
> 0.70
> 
> 0.20
> 
> 0.10
> 
> Which is the **least probable** cluster for data point 1?
> 
> 1 point
> 
>  Cluster A 
> 
>  Cluster B 
> 
>  Cluster C 
> 
> ### 7.
> 
> Question 7
> 
> Suppose we are running the EM algorithm. After an E-step, we obtain the following responsibility matrix:
> 
> Cluster responsibilities
> 
> Cluster A
> 
> Cluster B
> 
> Cluster C
> 
> Data point 1
> 
> 0.20
> 
> 0.40
> 
> 0.40
> 
> Data point 2
> 
> 0.50
> 
> 0.10
> 
> 0.40
> 
> Data point 3
> 
> 0.70
> 
> 0.20
> 
> 0.10
> 
> Suppose also that the data points are as follows:
> 
> Dataset
> 
> X
> 
> Y
> 
> Z
> 
> Data point 1
> 
> 3
> 
> 1
> 
> 2
> 
> Data point 2
> 
> 0
> 
> 0
> 
> 3
> 
> Data point 3
> 
> 1
> 
> 3
> 
> 7
> 
> Let us compute the new mean for Cluster A. What is the **Z coordinate** of the new mean? Round your answer to 3 decimal places.
> 
> 1 point
> 

     4.86
> 
> ### 8.
> 
> Question 8
> 
> Which of the following contour plots describes a Gaussian distribution with diagonal covariance? Choose all that apply.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/hTE9KD64EeaGyBLfiQeo_w_0dac54a9dcf1da65d3b7f8062d27b068_Capture.PNG?expiry=1657756800000&hmac=rFe6to2ijdehlBQHdlKIy6VAs8xlofFn91OxmCLoPqY)
> 
> 1 point
> 
>  (1) 
> 
>  (2) 
> 

      (3) 
> 

      (4) 
> 
>  (5) 
> 
> ### 9.
> 
> Question 9
> 
> Suppose we initialize EM for mixtures of Gaussians (using full covariance matrices) with the following clusters:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/6b37ij66Eea5kQp9N8_TZQ_f5602186b001115e77eccf5a1dead717_Capture.PNG?expiry=1657756800000&hmac=pw3ObArdxjagCvYvZiGJcBhhSDrl0A9UfScoxuOqlVw)
> 
> Which of the following best describes the updated clusters after the first iteration of EM?
> 
> 2 points
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Zpt3vD67EeaHVA5o9gyGmQ_070bd7bcbdf085a0b95d592a76cd9aab_Capture.PNG?expiry=1657756800000&hmac=RhFKO1Otep5V8v8LNE1PRZAMuPcicdMk4mTBLs3HVAQ) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/v2MStj7mEeaHVA5o9gyGmQ_2506929de3620fa1fed58ddaf822d986_Capture.PNG?expiry=1657756800000&hmac=yGcnpH7sjY3aT6AMx1OoBkQR1Zxrh42k5unqfK5OnW8) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/uOFP3T7nEea5kQp9N8_TZQ_114e6409c4fbdd31784dd0a2c612e9d1_Capture.PNG?expiry=1657756800000&hmac=uNMf0rvfpD6bBepglfP3jdzi1goRTeOngvOadYWAfx4) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/N80SZz7oEeaIVA5M-C6oUw_7717cda4e5628b80b9c124e1ddee7829_Capture.PNG?expiry=1657756800000&hmac=9a4z0l7XF3az3D5YinJIO4ANOYDE58h7rp8okHMU5cw) 

      Correct
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/tjV0PD7oEeaIVA5M-C6oUw_f83843d1f1cce752efa98a8a27cf19f4_Capture.PNG?expiry=1657756800000&hmac=io4X16OQjWaARDOqE57fsXeja55BKtjcnYwJkJhVDNI)
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/exam/QVHj1/em-for-gaussian-mixtures/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
