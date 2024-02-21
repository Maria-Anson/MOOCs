## Selecting and Training a Model
> 
> Total points 4
> 
> ### 1.
> 
> Question 1
> 
> Which of these is a more accurate description of a data-centric approach to ML development?
> 
> 1 point
> 

      Holding the neural network architecture fixed, work to improve the data to do well on the problem. 
> 
>  Holding the training data fixed, work to improve your neural network’s architecture to do well on the problem. 
> 
> ### 2.
> 
> Question 2
> 
> Say you have an algorithm that diagnoses illnesses from medical X-rays, and achieves high average test set accuracy. What can you now say with high confidence about this algorithm? Check all that apply. 
> 
> 1 point
> 
>  It does well even on rare classes of diseases. 
> 
>  Its diagnoses are roughly equally accurate on all genders and ethnicities, so we are confident it is not biased against any gender or ethnicity. 
> 
>  The system can be safely deployed in a healthcare setting. 
> 

      None of the above. 
> 
> ### 3.
> 
> Question 3
> 
> Which of these statements about establishing a baseline are accurate? Check all that apply.
> 
> 1 point
> 
>  Open-source software should not be used to establish a baseline, since the performance of a good open source implementation might be too good and thus too hard to beat. 
> 

      It can be established based on an older ML system 
> 

      Human level performance (HLP) is generally more effective for establishing a baseline on unstructured data problems (such as images and audio) than structured data problems 
> 

      For unstructured data problems, using human-level performance as the baseline can give an estimate of the irreducible error/Bayes error and what performance is reasonable to achieve. 
> 
> ### 4.
> 
> Question 4
> 
> On a speech recognition problem, say you run the sanity-check test of trying to overfit a single training example. You pick a clearly articulated clip of someone saying “Today’s weather”, and the algorithm fails to fit even this single audio clip, and outputs “______”. What should you do?
> 
> 1 point
> 

      Debug the code/algorithm/hyperparameters to make it pass this sanity-check test first, before moving to larger datasets. 
> 
>  Use data augmentation on this one audio clip to make sure the algorithm hears a variety of examples of “today’s weather” to fit this phrase better. 
> 
>  Create a training set of this example repeated 100 times to force the algorithm to learn to fit this example well. 
> 
>  Train the algorithm on a larger dataset to help it to fit the data better.
>
> -- https://www.coursera.org/learn/introduction-to-machine-learning-in-production/exam/XQM8q/selecting-and-training-a-model/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
