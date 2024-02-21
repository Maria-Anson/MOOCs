## Training Logistic Regression via Stochastic Gradient Ascent
> 
> Total points 12
> 
> ### 1.
> 
> Question 1
> 
> In Module 3 assignment, there were 194 features (an intercept + one feature for each of the 193 important words). In this assignment, we will use stochastic gradient ascent to train the classifier using logistic regression. How does the changing the solver to stochastic gradient ascent affect the number of features?
> 
> 1 point
> 
>  Increases 
> 
>  Decreases 
> 

      Stays the same 
> 
> ### 2.
> 
> Question 2
> 
> Recall from the lecture and the earlier assignment, the log likelihood (without the averaging term) is given by
> 
> ℓℓ(w)=∑i=1N((1[yi=+1]−1)wTh(xi)−ln⁡(1+exp⁡(−wTh(xi))))\displaystyle{\ell\ell(\mathbf{w}) = \sum_{i=1}^N \Big( (\mathbf{1}[y_i = +1] - 1)\mathbf{w}^T h(\mathbf{x}_i) - \ln\left(1 + \exp(-\mathbf{w}^T h(\mathbf{x}_i))\right) \Big)}ℓℓ(w)=i=1∑N​((1[yi​=+1]−1)wTh(xi​)−ln(1+exp(−wTh(xi​))))
> 
> whereas the average log likelihood is given by
> 
> ℓℓA(w)=1N∑i=1N((1[yi=+1]−1)wTh(xi)−ln⁡(1+exp⁡(−wTh(xi))))\displaystyle{\ell\ell_A(\mathbf{w}) = \color{red}{\frac{1}{N}} \sum_{i=1}^N \Big( (\mathbf{1}[y_i = +1] - 1)\mathbf{w}^T h(\mathbf{x}_i) - \ln\left(1 + \exp(-\mathbf{w}^T h(\mathbf{x}_i))\right) \Big)}ℓℓA​(w)=N1​i=1∑N​((1[yi​=+1]−1)wTh(xi​)−ln(1+exp(−wTh(xi​))))
> 
> How are the functions ℓℓ(w)\ell\ell(\mathbf{w})ℓℓ(w) and ℓℓA(w)\ell\ell_A(\mathbf{w})ℓℓA​(w) related?
> 
> 1 point
> 
>  ℓℓA(w)=ℓℓ(w)\ell\ell_A(\mathbf{w}) = \ell\ell(\mathbf{w})ℓℓA​(w)=ℓℓ(w) 
> 

      ℓℓA(w)=(1/N)⋅ℓℓ(w)
> 
>  ℓℓA(w)=N⋅ℓℓ(w)\ell\ell_A(\mathbf{w}) = N \cdot \ell\ell(\mathbf{w})ℓℓA​(w)=N⋅ℓℓ(w) 
> 
>  ℓℓA(w)=ℓℓ(w)−∥w∥\ell\ell_A(\mathbf{w}) = \ell\ell(\mathbf{w}) - \|\mathbf{w}\|ℓℓA​(w)=ℓℓ(w)−∥w∥ 
> 
> ### 3.
> 
> Question 3
> 
> Refer to the sub-section **Computing the gradient for a single data point.**
> 
> The code block above computed
> 
> ∂ℓi(w)∂wj\dfrac{\partial\ell_{\color{red}{i}}(\mathbf{w})}{\partial w_j}∂wj​∂ℓi​(w)​
> 
> for j = 1 and i = 10\. Is this quantity a scalar or a 194-dimensional vector?
> 
> 1 point
> 

      A scalar 
> 
>  A 194-dimensional vector 
> 
> ### 4.
> 
> Question 4
> 
> Refer to the sub-section **Modifying the derivative for using a batch of data points**.
> 
> The code block computed
> 
> ### ∑s=ii+B∂ℓs(w)∂wj\displaystyle{\color{red}{\sum_{s = i}^{i+B}}\frac{\partial\ell_{s}(\mathbf{w})}{\partial w_j}}s=i∑i+B​∂wj​∂ℓs​(w)​
> 
> ### for j = 10, i = 10, and B = 10\. Is this a scalar or a 194-dimensional vector?
> 
> 1 point
> 

      A scalar 
> 
>  A 194-dimensional vector 
> 
> ### 5.
> 
> Question 5
> 
> For what value of **B** is the term
> 
> ∑s=1B∂ℓs(w)∂wj\displaystyle{\color{red}{\sum_{s = 1}^{B}}\frac{\partial\ell_{s}(\mathbf{w})}{\partial w_j}}s=1∑B​∂wj​∂ℓs​(w)​
> 
> the same as the full gradient
> 
> ∂ℓ(w)∂wj\dfrac{\partial\ell(\mathbf{w})}{\partial w_j}∂wj​∂ℓ(w)​
> 
> ? A numeric answer is expected for this question. Hint: consider the training set we are using now.
> 
> 1 point
> 

     47780
> 
> ### 6.
> 
> Question 6
> 
> For what value of batch size **B** above is the stochastic gradient ascent function **logistic_regression_SG** act as a standard gradient ascent algorithm? A numeric answer is expected for this question. Hint: consider the training set we are using now.
> 
> 1 point
> 

     47780
> 
> ### 7.
> 
> Question 7
> 
> When you set batch_size = 1, as each iteration passes, how does the average log likelihood in the batch change?
> 
> 1 point
> 
>  Increases 
> 
>  Decreases 
> 

      Fluctuates 
> 
> ### 8.
> 
> Question 8
> 
> When you set batch_size = len(feature_matrix_train), as each iteration passes, how does the average log likelihood in the batch change?
> 
> 1 point
> 
    
      Increases 
> 
>  Decreases 
> 
>  Fluctuates 
> 
> ### 9.
> 
> Question 9
> 
> Suppose that we run stochastic gradient ascent with a batch size of 100\. How many gradient updates are performed at the end of two passes over a dataset consisting of 50000 data points?
> 
> 1 point
> 

     1000
> 
> ### 10.
> 
> Question 10
> 
> Refer to the section **Stochastic gradient ascent vs gradient ascent**.
> 
> In the first figure, how many passes does batch gradient ascent need to achieve a similar log likelihood as stochastic gradient ascent?
> 
> 1 point
> 
>  It's always better 
> 
>  10 passes 
> 
>  20 passes 
> 

      150 passes or more 
> 
> ### 11.
> 
> Question 11
> 
> Questions 11 and 12 refer to the section **Plotting the log likelihood as a function of passes for each step size**.
> 
> Which of the following is the worst step size? Pick the step size that results in the lowest log likelihood in the end.
> 
> 1 point
> 
>  1e-2 
> 
>  1e-1 
> 
>  1e0 
> 
>  1e1 
> 

      1e2 
> 
> ### 12.
> 
> Question 12
> 
> Questions 11 and 12 refer to the section **Plotting the log likelihood as a function of passes for each step size**.
> 
> Which of the following is the best step size? Pick the step size that results in the highest log likelihood in the end.
> 
> 1 point
> 
>  1e-4 
> 
>  1e-2 
> 

      1e0 
> 
>  1e1 
> 
>  1e2
>
> -- https://www.coursera.org/learn/ml-classification/exam/UWEJn/training-logistic-regression-via-stochastic-gradient-ascent/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
