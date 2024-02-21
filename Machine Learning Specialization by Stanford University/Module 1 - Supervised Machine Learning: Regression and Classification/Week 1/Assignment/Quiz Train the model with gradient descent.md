## Practice quiz: Train the model with gradient descent
> ### 1.
> 
> Question 1
> 
> Gradient descent is an algorithm for finding values of parameters w and b that minimize the cost function J.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/9d6af8aa-0910-478f-b535-192f5c901014image3.png?expiry=1658448000000&hmac=C-Lqtcb-E1fbLvLw2PMepjVpAU11L45Uo5FOBXcNhwM)
> 
> When ∂J(w,b)∂w\frac{\partial J(w,b)}{\partial w}∂w∂J(w,b)​ is a negative number (less than zero), what happens to www after one update step?
> 
> 1 / 1 point
> 
>  It is not possible to tell if www will increase or decrease. 
> 
>  www decreases 
> 
>  www stays the same 
> 

      www increases. 
> 
> Correct
> 
> The learning rate is always a positive number, so if you take W minus a negative number, you end up with a new value for W that is larger (more positive).
> 
> ### 2.
> 
> Question 2
> 
> For linear regression, what is the update step for parameter b?
> 
> 1 / 1 point
> 

      b=b−α1m∑i=1m(fw,b(x(i))−y(i))
> 
>  b=b−α1m∑i=1m(fw,b(x(i))−y(i))x(i)
> 
> Correct
> 
> The update step is b=b−α∂J(w,b)∂wb = b - \alpha \frac{\partial J(w,b)}{\partial w}b=b−α∂w∂J(w,b)​ where ∂J(w,b)∂b\frac{\partial J(w,b)}{\partial b}∂b∂J(w,b)​ can be computed with this expression: ∑i=1m(fw,b(x(i))−y(i))\sum\limits_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})i=1∑m​(fw,b​(x(i))−y(i))
>
> -- https://www.coursera.org/learn/machine-learning/exam/sWDb5/practice-quiz-train-the-model-with-gradient-descent/view-attempt#Zsj3f6-legend
