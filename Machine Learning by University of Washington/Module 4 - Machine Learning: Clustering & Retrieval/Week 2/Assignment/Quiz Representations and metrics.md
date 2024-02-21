## Representations and metrics
> 
> Total points 6
> 
> ### 1.
> 
> Question 1
> 
> Consider three data points with two features as follows:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Dhfrv0L4EeaBig4GYhAaLQ_76c61cc4f127f8b69344930aa882ff15_Capture.PNG?expiry=1656979200000&hmac=60oARDOpFU9tgWpmiofU2Etkfsyro4QH8pQH7a0F_sI)
> 
> Among the three points, which two are closest to each other in terms of having the **​smallest Euclidean distance**?
> 
> 1 point
> 
>  A and B 
> 
>  A and C 
> 

      B and C 
> 
> ### 2.
> 
> Question 2
> 
> Consider three data points with two features as follows:
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/GqMiEkL4EeaKKwrxnBB_sQ_603034ce2b1d8074f7aaf73886c66643_Capture.PNG?expiry=1656979200000&hmac=QcYaShmSQR5Onm7k_rN2lY91Igs9Gr7CyRnAY3-ZzN0)
> 
> Among the three points, which two are closest to each other in terms of having the **​largest cosine similarity** (or equivalently, **​smallest cosine distance**)?
> 
> 1 point
> 

      A and B 
> 
>  A and C 
> 
>  B and C 
> 
> ### 3.
> 
> Question 3
> 
> Consider the following two sentences.
> 
> *   Sentence 1: The quick brown fox jumps over the lazy dog.
> 
> *   Sentence 2: A quick brown dog outpaces a quick fox.
> 
> Compute the Euclidean distance using word counts. To compute word counts, turn all words into lower case and strip all punctuation, so that "The" and "the" are counted as the same token. That is, document 1 would be represented as
> 
> x=[# the,# a,# quick,# brown,# fox,# jumps,# over,# lazy,# dog,# outpaces]x = [\text{# the}, \text{# a}, \text{# quick}, \text{# brown}, \text{# fox}, \text{# jumps}, \text{# over}, \text{# lazy}, \text{# dog}, \text{# outpaces}]
> 
> where # word\text{# word} is the count of that word in the document.
> 
> Round your answer to 3 decimal places.
> 
> 1 point
> 

     3.606
> 
> ### 4.
> 
> Question 4
> 
> Consider the following two sentences.
> 
> *   Sentence 1: The quick brown fox jumps over the lazy dog.
> 
> *   Sentence 2: A quick brown dog outpaces a quick fox.
> 
> Recall that
> 
> cosine distance = 1 - cosine similarity = 1−xTy∣∣x∣∣∣∣y∣∣1- \frac{x^T y}{||x|| ||y||}1−∣∣x∣∣∣∣y∣∣xTy​
> 
> Compute the **cosine distance** between sentence 1 and sentence 2 using word counts. To compute word counts, turn all words into lower case and strip all punctuation, so that "The" and "the" are counted as the same token. That is, document 1 would be represented as
> 
> x=[# the,# a,# quick,# brown,# fox,# jumps,# over,# lazy,# dog,# outpaces]x = [\text{# the}, \text{# a}, \text{# quick}, \text{# brown}, \text{# fox}, \text{# jumps}, \text{# over}, \text{# lazy}, \text{# dog}, \text{# outpaces}]
> 
> where # word\text{# word} is the count of that word in the document.
> 
> Round your answer to 3 decimal places.
> 
> 1 point
> 

     0.565
> 
> ### 5.
> 
> Question 5
> 
> (True/False) For positive features, cosine similarity is always between 0 and 1.
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 6.
> 
> Question 6
> 
> Which of the following does **not** describe the word count document representation? (Note: this is different from TF-IDF document representation.)
> 
> 1 point
> 
>  Ignores the order of the words 
> 
>  Assigns a high score to a frequently occurring word 
> 

      Penalizes words that appear in every document
>
