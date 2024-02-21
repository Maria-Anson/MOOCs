# Practice quiz: Decision tree learning
> ### 1.
> 
> Question 1
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f1fed11a-1ade-4b8c-b5cf-e6f9b11a2b23image4.png?expiry=1658966400000&hmac=JkqeDFPlcpV_8zHew09aAvCT4OUoV095VgmYvH2w7yI)
> 
> Recall that entropy was defined in lecture as H(p_1) = - p_1 log_2(p_1) - p_0 log_2(p_0), where p_1 is the fraction of positive examples and p_0 the fraction of negative examples.
> 
> At a given node of a decision tree, , 6 of 10 examples are cats and 4 of 10 are not cats. Which expression calculates the entropy H(p1)H(p_1)H(p1​) of this group of 10 animals?
> 
> 1 / 1 point
> 

      −(0.6)log2(0.6)−(0.4)log2(0.4)
> 
>  (0.6)log2(0.6)+(0.4)log2(0.4)(0.6) log_2(0.6) + (0.4)log_2(0.4)(0.6)log2​(0.6)+(0.4)log2​(0.4) 
> 
>  (0.6)log2(0.6)+(1−0.4)log2(1−0.4)(0.6) log_2(0.6) + (1 - 0.4)log_2(1 - 0.4)(0.6)log2​(0.6)+(1−0.4)log2​(1−0.4) 
> 
>  −(0.6)log2(0.6)−(1−0.4)log2(1−0.4)-(0.6) log_2(0.6) - (1 - 0.4)log_2(1 - 0.4)−(0.6)log2​(0.6)−(1−0.4)log2​(1−0.4) 
> 
> Correct
> 
> Correct. The expression is −(p1)log2(p1)−(p0)log2(p0)-(p_1) log_2(p_1) - (p_0)log_2(p_0)−(p1​)log2​(p1​)−(p0​)log2​(p0​)
> 
> ### 2.
> 
> Question 2
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f1fed11a-1ade-4b8c-b5cf-e6f9b11a2b23image2.png?expiry=1658966400000&hmac=SeOrmGqUwK8S4Flb3aYwatnNzcb3wkaPjJVpYld2Epg)
> 
> Recall that information was defined as follows:
> 
> H(p1root)−(wleftH(p1left)+wrightH(p1right))H(p_1^{root}) - \left ( w^{left} H(p_1^{left}) + w^{right} H(p_1^{right}) \right ) H(p1root​)−(wleftH(p1left​)+wrightH(p1right​))
> 
> Before a split, the entropy of a group of 5 cats and 5 non-cats is H(5/10)H(5/10) H(5/10). After splitting on a particular feature, a group of 7 animals (4 of which are cats) has an entropy of H(4/7)H(4/7)H(4/7). The other group of 3 animals (1 is a cat) and has an entropy of H(1/3)H(1/3)H(1/3). What is the expression for information gain?
> 
> 1 / 1 point
> 
>  H(0.5)−(47∗H(4/7)+47∗H(1/3))H(0.5) - \left ( \frac{4}{7} * H(4/7) + \frac{4}{7} * H(1/3) \right )H(0.5)−(74​∗H(4/7)+74​∗H(1/3)) 
> 
>  H(0.5)−(7∗H(4/7)+3∗H(1/3))H(0.5) - \left ( 7 * H(4/7) + 3 * H(1/3) \right )H(0.5)−(7∗H(4/7)+3∗H(1/3)) 
> 

      H(0.5)−(710H(4/7)+310H(1/3))
> 
>  H(0.5)−(H(4/7)+H(1/3))H(0.5) - \left ( H(4/7) + H(1/3) \right )H(0.5)−(H(4/7)+H(1/3)) 
> 
> Correct
> 
> Correct. The general expression is H(p1root)−(wleftH(p1left)+wrightH(p1right))H(p_1^{root}) - \left ( w^{left} H(p_1^{left}) + w^{right} H(p_1^{right}) \right ) H(p1root​)−(wleftH(p1left​)+wrightH(p1right​))
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f1fed11a-1ade-4b8c-b5cf-e6f9b11a2b23image5.png?expiry=1658966400000&hmac=56peZJEZBSkWWF2Hx9gtQDvYa4gUp57tETzgfdcY8O0)
> 
> To represent 3 possible values for the ear shape, you can define 3 features for ear shape: pointy ears, floppy ears, oval ears. For an animal whose ears are not pointy, not floppy, but are oval, how can you represent this information as a feature vector?
> 
> 1 / 1 point
> 
>  [0, 1, 0] 
> 

      [0, 0, 1] 
> 
>  [1, 1, 0] 
> 
>  [1,0,0] 
> 
> Correct
> 
> Yes! 0 is used to represent the absence of that feature (not pointy, not floppy), and 1 is used to represent the presence of that feature (oval).
> 
> ### 4.
> 
> Question 4
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/f1fed11a-1ade-4b8c-b5cf-e6f9b11a2b23image6.png?expiry=1658966400000&hmac=my4wOhxlDt8nmhav94dNaBvjMkMLmbEZawstKd87W-Y)
> 
> For a continuous valued feature (such as weight of the animal), there are 10 animals in the dataset. According to the lecture, what is the recommended way to find the best split for that feature?
> 
> 1 / 1 point
> 
>  Use a one-hot encoding to turn the feature into a discrete feature vector of 0’s and 1’s, then apply the algorithm we had discussed for discrete features. 
> 

      Choose the 9 mid-points between the 10 examples as possible splits, and find the split that gives the highest information gain. 
> 
>  Use gradient descent to find the value of the split threshold that gives the highest information gain. 
> 
>  Try every value spaced at regular intervals (e.g., 8, 8.5, 9, 9.5, 10, etc.) and find the split that gives the highest information gain. 
> 
> Correct
> 
> Correct. This is what is proposed in the lectures.
> 
> ### 5.
> 
> Question 5
> 
> Which of these are commonly used criteria to decide to stop splitting? (Choose two.)
> 
> 1 / 1 point
> 
>  When a node is 50% one class and 50% another class (highest possible value of entropy) 
> 

      When the number of examples in a node is below a threshold 
> 
> Correct
> 
> Yes!
> 

      When the tree has reached a maximum depth 
> 
> Correct
> 
> Yes!
> 
>  When the information gain from additional splits is too large
>
> -- https://www.coursera.org/learn/advanced-learning-algorithms/exam/1gwEW/practice-quiz-decision-tree-learning/attempt?redirectToCover=true#lSL1QW-legend
