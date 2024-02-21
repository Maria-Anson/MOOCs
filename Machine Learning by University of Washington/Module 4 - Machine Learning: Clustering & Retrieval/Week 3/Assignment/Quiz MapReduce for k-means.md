## MapReduce for k-means
> 
> Total points 5
> 
> ### 1.
> 
> Question 1
> 
> Suppose we are operating on a 1D vector. Which of the following operation is **not** data parallel over the vector elements?
> 
> 1 point
> 
>  Add a constant to every element. 
> 
>  Multiply the vector by a constant. 
> 
>  Increment the vector by another vector of the same dimension. 
> 

      Compute the average of the elements. 
> 
>  Compute the sign of each element. 
> 
> ### 2.
> 
> Question 2
> 
> (True/False) A single mapper call can emit multiple (key,value) pairs.
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
> (True/False) More than one reducer can emit (key,value) pairs with the same key simultaneously.
> 
> 1 point
> 
>  True 
> 

      False 
> 
> ### 4.
> 
> Question 4
> 
> (True/False) Suppose we are running k-means using MapReduce. Some mappers may be launched for a new k-means iteration even if some reducers from the previous iteration are still running.
> 
> 1 point
> 
>  True 
> 

      False 
> 
> ### 5.
> 
> Question 5
> 
> Consider the following list of binary operations. Which can be used for the reduce step of MapReduce? Choose all that apply.
> 
> Hints: The reduce step requires a binary operator that satisfied **both** of the following conditions.
> 
> *   Commutative: OP(x1,x2)=OP(x2,x1)OP(x_1,x_2) = OP(x_2,x_1)OP(x1​,x2​)=OP(x2​,x1​)
> 
> *   Associative: OP(OP(x1,x2),x3)=OP(x1,OP(x2,x3))OP(OP(x_1, x_2), x_3) = OP(x_1, OP(x_2, x_3))OP(OP(x1​,x2​),x3​)=OP(x1​,OP(x2​,x3​))
> 
> 1 point
> 

      OP1(x1,x2)=max(x1,x2) 
> 

      OP2(x1,x2)=x1+x2−2 
> 
>  OP3(x1,x2)=3x1+2x2\mbox{OP3}(x_1,x_2) = 3 x_1 + 2 x_2 
> 
>  OP4(x1,x2)=x21+x2\mbox{OP4}(x_1,x_2) = x_1^2 + x_2 
> 
>  OP5(x1,x2)=(x1+x2)/2
>
