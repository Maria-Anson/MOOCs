# Modeling text topics with Latent Dirichlet Allocation
> 
> In many cases, it is good to think of data as belonging to more than one cluster or category. For example, if we have a model for text data that includes both "Politics" and "World News" categories, then an article about a recent meeting of the United Nations should have membership in both categories rather than being forced into just one.
> 
> With this in mind, we will use Turi Create tools to fit an LDA model to a corpus of Wikipedia articles and examine the results to analyze the impact of a mixed membership approach.
> 
> In this assignment you will
> 
> *   apply standard preprocessing techniques on Wikipedia text data
> 
> *   use Turi Create to fit a Latent Dirichlet allocation (LDA) model
> 
> *   explore and interpret the results, including topic keywords and topic assignments for a document
> 
> ## If you are using Turi Create
> 
> An IPython Notebook has been provided below to you for this assignment. This notebook contains the instructions, quiz questions and partially-completed code for you to use as well as some cells to test your code.
> 
> *   Download the Wikipedia people dataset in SFrame format:
> 
>  [ZIP File
> 
> people_wiki.sframe
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5zBDt4bEemhxxJUtZcQoA_7fb43aab245846f09a8c48977883f0b6_people_wiki.sframe.zip?Expires=1657929600&Signature=Ok7RNrwAYuCyFcYrS38y7NEyzfN96MqFMNW9Lp1JPlSZqeugvyLOS5-I1Wu9yKXx4M5mV4uSQ4F9pF3TR3lmra-r-BKnHaqk3YJae5jUAWAPshR0SC4uFm-pLLXmmMDG84c2dsDPa3OpiaYiimEVMp6RlNQao2ivVmACxMq59bU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the pretrained models:
> 
>  [ZIP File
> 
> topic_models
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5s6bd4bEemhxxJUtZcQoA_c835f3aa6f324f92a988939d2e1434ed_topic_models.zip?Expires=1657929600&Signature=ihUhKbRoHzFX-v66nQzZD8nOMj75TaApg872ak5RmHHF5uy2YKGz-YBfGO94-KeyGZP2RbJEanCLGMxEs1GwwZ0PkYqc-DdFLd-h2fCDH0UtwBTuCkwRTh1mXvaNSBlrta5BM1cOg0meRiZyaTg8e3AvGaQegAiUGDmRHwSa3YQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython notebook:
> 
>  [ZIP File
> 
> CLU05-NB01.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/EZv3cOI8EemELQpo9cj5Ig_a42f52180f6446e0946159f3f909e434_CLU05-NB01.ipynb.zip?Expires=1657929600&Signature=MXeMZxG8OhzMaM825OkWYXAZPtfjFadnGjBFrusb6wGWaQJMulm5LHymDPasXHxIBEtMDl1VEaYBoORAu5LRxVDFdZjoErr8CS3Wg3mGFKTnrlB2P3X8jLmd4Pl3QzW5KyW1cyNGf5WiZHboFWDF2CuuiFjkUE3bKRHH2UwV~I8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Save all of these files in the same directory (where you are calling IPython notebook from) and unzip the data file and model file.
> 
> ## This assignment will require the use of Turi Create, and here is why:
> 
> The method used to fit the LDA model is a _randomized algorithm_, which means that it involves steps that are random; in this case, the randomness comes from Gibbs sampling, as discussed in the LDA video lectures. Because of these random steps, the algorithm will be expected to yield slighty different output for different runs on the same data - note that this is different from previously seen algorithms such as k-means or EM, which will always produce the same results given the same input and initialization.
> 
> **It is important to understand that variation in the results is a fundamental feature of randomized methods. However, in the context of this assignment this variation makes it highly difficult to evaluate the correctness of your analysis, so we will load and analyze a pre-trained model.**
> 
> **You are free to experiment with an LDA implementation of your choice, but for this assessment, you should use Turi Create. However, feel free to re-create the analysis done in the IPython notebook for your personal enjoyment.**
> 
> We recommend that you spend some time exploring your own fitted topic model and compare our analysis of the pre-trained model to the same analysis applied to the model you trained above.
> 
> **The focus of this assignment is exploration of results, not implementation.** We will analyze the fitted model to understand what it has done with our data and whether it will be useful as a document classification system. This can be a challenging task in itself, particularly when the model that we use is complex. We will begin by outlining a sequence of objectives that will help us understand our model in detail. In particular, we will
> 
> *   get the top words in each topic and use these to identify topic themes
> 
> *   predict topic distributions for some example documents
> 
> *   compare the quality of LDA "nearest neighbors" to the NN output from the first assignment
> 
> *   understand the role of model hyperparameters alpha and gamma
> 
> **Don't want to install Turi Create?** [Consider using Amazon EC2.](https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/iF7Ji)
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/OL4J1/modeling-text-topics-with-latent-dirichlet-allocation#main
