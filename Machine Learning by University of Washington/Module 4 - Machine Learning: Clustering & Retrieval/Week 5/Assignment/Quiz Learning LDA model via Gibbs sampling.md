## Learning LDA model via Gibbs sampling
> 
> Total points 12
> 
> ### 1.
> 
> Question 1
> 
> (True/False) Each iteration of Gibbs sampling for Bayesian inference in topic models is guaranteed to yield a higher joint model probability than the previous sample.
> 
> 1 point
> 
>  True 
> 

        False 
> 
> ### 2.
> 
> Question 2
> 
> (Check all that are true) Bayesian methods such as Gibbs sampling can be advantageous because they
> 
> 1 point
> 

      Account for uncertainty over parameters when making predictions 
> 
>  Are faster than methods such as EM 
> 
>  Maximize the log probability of the data under the model 
> 
      Regularize parameter estimates to avoid extreme values 
> 
> ### 3.
> 
> Question 3
> 
> For the standard LDA model discussed in the lectures, how many parameters are required to represent the distributions defining the topics?
> 
> 1 point
> 
>  [# unique words] 
> 

      [# unique words] * [# topics] 
> 
>  [# documents] * [# unique words] 
> 
>  [# documents] * [# topics] 
> 
> ### 4.
> 
> Question 4
> 
> Suppose we have a collection of documents, and we are focusing our analysis to the use of the following 10 words. We ran several iterations of collapsed Gibbs sampling for an LDA model with K=2 topics and alpha=10.0 and gamma=0.1 (with notation as in the collapsed Gibbs sampling lecture). The corpus-wide assignments at our most recent collapsed Gibbs iteration are summarized in the following table of counts:
> 
> Word
> 
> Count in topic 1
> 
> Count in topic 2
> 
> baseball
> 
> 52
> 
> 0
> 
> homerun
> 
> 15
> 
> 0
> 
> ticket
> 
> 9
> 
> 2
> 
> price
> 
> 9
> 
> 25
> 
> manager
> 
> 20
> 
> 37
> 
> owner
> 
> 17
> 
> 32
> 
> company
> 
> 1
> 
> 23
> 
> stock
> 
> 0
> 
> 75
> 
> bankrupt
> 
> 0
> 
> 19
> 
> taxes
> 
> 0
> 
> 29
> 
> We also have a single document iii with the following topic assignments for each word:
> 
> topic
> 
> 1
> 
> 2
> 
> 1
> 
> 2
> 
> 1
> 
> word
> 
> baseball
> 
> manager
> 
> ticket
> 
> price
> 
> owner
> 
> Suppose we want to re-compute the topic assignment for the word “manager”. To sample a new topic, we need to compute several terms to determine how much the document likes each topic, and how much each topic likes the word “manager”. The following questions will all relate to this situation.
> 
> First, using the notation in the slides, what is the value of mmanager,1m_{\text{manager}, 1}mmanager,1​ (i.e., the number of times the word "manager" has been assigned to topic 1)?
> 
> 2 points
> 

     20
> 
> ### 5.
> 
> Question 5
> 
> Consider the situation described in Question 4\.
> 
> What is the value of ∑wmw,1\sum_w m_{w, 1}∑w​mw,1​, where the sum is taken over all words in the vocabulary?
> 
> 1 point
> 

     123
> 
> ### 6.
> 
> Question 6
> 
> Consider the situation described in Question 4.
> 
> Following the notation in the slides, what is the value of ni,1n_{i, 1}ni,1​ for this document iii (i.e., the number of words in document iii assigned to topic 1)?
> 
> 1 point
> 

      3    
> 
> ### 7.
> 
> Question 7
> 
> In the situation described in Question 4, “manager” was assigned to topic 2\. When we remove that assignment prior to sampling, we need to decrement the associated counts.
> 
> After decrementing, what is the value of ni,2n_{i, 2}ni,2​?
> 
> 1 point
> 

     1
> 
> ### 8.
> 
> Question 8
> 
> In the situation described in Question 4, “manager” was assigned to topic 2\. When we remove that assignment prior to sampling, we need to decrement the associated counts.
> 
> After decrementing, what is the value of mmanager,2m_{manager, 2}mmanager,2​?
> 
> 1 point
> 

     36
> 
> ### 9.
> 
> Question 9
> 
> In the situation described in Question 4, “manager” was assigned to topic 2\. When we remove that assignment prior to sampling, we need to decrement the associated counts.
> 
> After decrementing, what is the value of ∑wmw,2\sum_w m_{w, 2}∑w​mw,2​?
> 
> 1 point
> 

     241
> 
> ### 10.
> 
> Question 10
> 
> Consider the situation described in Question 4\.
> 
> As discussed in the slides, the unnormalized probability of assigning to topic 1 is
> 
> p1=ni,1+αNi−1+Kαmmanager,1+γ∑wmw,1+Vγp_1 = \frac{n_{i, 1} + \alpha}{N_i - 1 + K \alpha}\frac{m_{\text{manager}, 1} + \gamma}{\sum_w m_{w, 1} + V \gamma}p1​=Ni​−1+Kαni,1​+α​∑w​mw,1​+Vγmmanager,1​+γ​
> 
> where V is the total size of the vocabulary.
> 
> Similarly the unnormalized probability of assigning to topic 2 is
> 
> p2=ni,2+αNi−1+Kαmmanager,2+γ∑wmw,2+Vγp_2 = \frac{n_{i, 2} + \alpha}{N_i - 1 + K \alpha}\frac{m_{\text{manager}, 2} + \gamma}{\sum_w m_{w, 2} + V \gamma}p2​=Ni​−1+Kαni,2​+α​∑w​mw,2​+Vγmmanager,2​+γ​
> 
> Using the above equations and the results computed in previous questions, compute the probability of assigning the word “manager” to topic 1\.
> 
> (_Reminder: Normalize across the two topic options so that the probabilities of all possible assignments---topic 1 and topic 2---sum to 1._)
> 
> Round your answer to 3 decimal places.
> 
> 2 points
> 

     0.560
>
