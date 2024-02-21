# Practice quiz: Cost function for logistic regression
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/30800c78-5d39-4239-a323-c65b911d1bfcimage2.png?expiry=1658620800000&hmac=2ex3QOrPjLuDixVuR73KgX819zTrPvvZB60lmozKPXQ)
> 
> In this lecture series, "cost" and "loss" have distinct meanings. Which one applies to a single training example?
> 
> 1 / 1 point
> 

      Loss 
> 
> Correct
> 
> In these lectures, loss is calculated on a single training example. It is worth noting that this definition is not universal. Other lecture series may have a different definition.
> 
>  Cost 
> 
>  Both Loss and Cost 
> 
>  Neither Loss nor Cost 
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/30800c78-5d39-4239-a323-c65b911d1bfcimage3.png?expiry=1658620800000&hmac=67B3Ny7q_b09JPfPoSkOFey7DeBEz10HCJq3J3FPMkY)
> 
> For the simplified loss function, if the label y(i)=0y^{(i)}=0y(i)=0, then what does this expression simplify to?
> 
> 1 / 1 point
> 

      −log⁡(1−fw⃗,b(x(i)))
> 
>  log⁡(fw⃗,b(x(i)) \log(f_{\vec{w},b}(\mathbf{x}^{(i)})log(fw,b​(x(i)) 
> 
>  −log⁡(1−fw⃗,b(x(i)))−log(1−fw⃗,b(x(i)))- \log(1-f_{\mathbf{\vec{w}},b}(\mathbf{x}^{(i)})) - log(1-f_{\mathbf{\vec{w}},b}(\mathbf{x}^{(i)}))−log(1−fw,b​(x(i)))−log(1−fw,b​(x(i))) 
> 
>  log⁡(1−fw⃗,b(x(i)))+log(1−fw⃗,b(x(i)))\log(1-f_{\mathbf{\vec{w}},b}(\mathbf{x}^{(i)})) + log(1-f_{\mathbf{\vec{w}},b}(\mathbf{x}^{(i)}))log(1−fw,b​(x(i)))+log(1−fw,b​(x(i))) 
> 
> Correct
> 
> When y(i)=0y^{(i)}=0y(i)=0, the first term reduces to zero.
>
> -- https://www.coursera.org/learn/machine-learning/exam/tGUIZ/practice-quiz-cost-function-for-logistic-regression/view-attempt#xROIvy-legend
