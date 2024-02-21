# Reinforcement learning introduction
> ### 1.
> 
> Question 1
> 
> You are using reinforcement learning to control a four legged robot. The position of the robot would be its _____.
> 
> 1 / 1 point
> 

      state 
> 
>  return 
> 
>  reward 
> 
>  action 
> 
> Correct
> 
> ### 2.
> 
> Question 2
> 
> You are controlling a Mars rover. You will be very very happy if it gets to state 1 (significant scientific discovery), slightly happy if it gets to state 2 (small scientific discovery), and unhappy if it gets to state 3 (rover is permanently damaged). To reflect this, choose a reward function so that:
> 
> 1 / 1 point
> 
>  R(1) > R(2) > R(3), where R(1), R(2) and R(3) are negative. 
> 

      R(1) > R(2) > R(3), where R(1) and R(2) are positive and R(3) is negative. 
> 
>  R(1) > R(2) > R(3), where R(1), R(2) and R(3) are positive. 
> 
>  R(1) < R(2) < R(3), where R(1) and R(2) are negative and R(3) is positive. 
> 
> Correct
> 
> Good job!
> 
> ### 3.
> 
> Question 3
> 
> You are using reinforcement learning to fly a helicopter. Using a discount factor of 0.75, your helicopter starts in some state and receives rewards -100 on the first step, -100 on the second step, and 1000 on the third and final step (where it has reached a terminal state). What is the return?
> 
> 1 / 1 point
> 
>  -0.75*100 - 0.75^2*100 + 0.75^3*1000 
> 
>  -100 - 0.25*100 + 0.25^2*1000 
> 
>  -0.25*100 - 0.25^2*100 + 0.25^3*1000 
> 

      -100 - 0.75*100 + 0.75^2*1000 
> 
> Correct
> 
> ### 4.
> 
> Question 4
> 
> Given the rewards and actions below, compute the return from state 3 with a discount factor of γ\gammaγ = 0.25.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/9a62f981-987c-41e2-abc3-77a52420011aimage3.png?expiry=1659225600000&hmac=LAoTYqO8wwPSKOBXvL2U1TY_QUCJMVImtXcxMzxkByY)
> 
> 1 / 1 point
> 
>  25 
> 
>  0.39 
> 

      6.25 
> 
>  0 
> 
> Correct
> 
> If starting from state 3, the rewards are in states 3, 2, and 1\. The return is 0+(0.25)×0+(0.25)2×100=6.250 + (0.25)\times 0 + (0.25)^{2} \times 100 = 6.250+(0.25)×0+(0.25)2×100=6.25.
>
> -- https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning/exam/522R6/reinforcement-learning-introduction/attempt?redirectToCover=true#UOIqvA-legend
