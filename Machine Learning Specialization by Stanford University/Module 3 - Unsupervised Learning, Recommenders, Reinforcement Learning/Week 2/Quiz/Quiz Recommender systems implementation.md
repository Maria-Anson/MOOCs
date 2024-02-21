# Recommender systems implementation
> ### 1.
> 
> Question 1
> 
> Lecture described using ‘mean normalization’ to do feature scaling of the ratings. What equation below best describes this algorithm?
> 
> 1 / 1 point
> 

      ynorm(i,j)μiσ2i=y(i,j)−μiσiwhere=1∑jr(i,j)∑j:r(i,j)=1y(i,j)=1∑jr(i,j)∑j:r(i,j)=1(y(i,j)−μj)2
> 
>  ynorm(i,j)μi=y(i,j)−μiwhere=1∑jr(i,j)∑j:r(i,j)=1y(i,j)\begin{align}y_{norm}(i,j) &= y(i,j) - \mu_i \quad \quad \text{where}\\ \mu_i &= \frac{1}{\sum_{j} r(i,j)} \sum_{j:r(i,j)=1} y(i,j) \end{align} 
> 
>  ynorm(i,j)μi=y(i,j)−μimaxi−miniwhere=1∑jr(i,j)∑j:r(i,j)=1y(i,j)\begin{align}y_{norm}(i,j) &= \frac {y(i,j) - \mu_i}{max_i - min_i} \quad \text{where}\\ \mu_i &= \frac{1}{\sum_{j} r(i,j)} \sum_{j:r(i,j)=1} y(i,j) \end{align} 
> 
> Correct
> 
> This is the mean normalization algorithm described in lecture. This will result in a zero average value on a per-row basis.
> 
> ### 2.
> 
> Question 2
> 
> The implementation of collaborative filtering utilized a custom training loop in TensorFlow. Is it true that TensorFlow always requires a custom training loop?
> 
> 1 / 1 point
> 
>  Yes. TensorFlow gains flexibility by providing the user primitive operations they can combine in many ways. 
> 

      No: TensorFlow provides simplified training operations for some applications. 
> 
> Correct
> 
> Recall in Course 2, you were able to build a neural network using a ‘model’, ‘compile’, ‘fit’, sequence which managed the training for you. A custom training loop was utilized in this situation because training www, bbb, and xxx does not fit the standard layer paradigm of TensorFlow's neural network flow. There are alternate solutions such as custom layers, however, it is useful in this course to introduce you to this powerful feature of TensorFlow.
> 
> ### 3.
> 
> Question 3
> 
> Once a model is trained, the 'distance' between features vectors gives an indication of how similar items are.
> 
> The squared distance between the two vectors x(k)\mathbf{x}^{(k)}x(k) and x(i)\mathbf{x}^{(i)}x(i) is:
> 
> distance=∥x(k)−x(i)∥2=∑l=1n(xl(k)−xl(i))2 distance = \left\Vert \mathbf{x^{(k)}} - \mathbf{x^{(i)}} \right\Vert^2 = \sum_{l=1}^{n}(x_l^{(k)} -x_l^{(i)})^2distance=∥∥∥​x(k)−x(i)∥∥∥​2=∑l=1n​(xl(k)​−xl(i)​)2
> 
> Using the table below, find the closest item to the movie "Pies, Pies, Pies".
> 
> Movie
> 
> User 1
> 
> …
> 
> User n
> 
> x0x_0x0​
> 
> x1x_1x1​
> 
> x2x_2x2​
> 
> Pastries for Supper
> 
> 2.0
> 
> 2.0
> 
> 1.0
> 
> Pies, Pies, Pies
> 
> 2.0
> 
> 3.0
> 
> 4.0
> 
> Pies and You
> 
> 5.0
> 
> 3.0
> 
> 4.0
> 
> 1 / 1 point
> 
>  Pastries for Supper 
> 

      Pies and You 
> 
> Correct
> 
> The distance from ‘Pies, Pies, Pies’ is 9 + 0 + 0 = 9.
> 
> ### 4.
> 
> Question 4
> 
> Which of these is an example of the cold start problem? (Check all that apply.)
> 
> 1 / 1 point
> 
>  A recommendation system is so computationally expensive that it causes your computer CPU to heat up, causing your computer to need to be cooled down and restarted. 
> 
>  A recommendation system takes so long to train that users get bored and leave. 
> 

      A recommendation system is unable to give accurate rating predictions for a new product that no users have rated. 
> 
> Correct
> 
> A recommendation system uses product feedback to fit the prediction model.
> 

      A recommendation system is unable to give accurate rating predictions for a new user that has rated few products. 
> 
> Correct
> 
> A recommendation system uses user feedback to fit the prediction model.
>
> -- https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning/exam/Bz0pI/recommender-systems-implementation/attempt?redirectToCover=true#RFNLvt-legend
