# Practice quiz: Classification with logistic regression
> ### 1.
> 
> Question 1
> 
> Which is an example of a classification task?
> 
> 1 / 1 point
> 

      Based on the size of each tumor, determine if each tumor is malignant (cancerous) or not. 
> 
>  Based on a patient's age and blood pressure, determine how much blood pressure medication (measured in milligrams) the patient should be prescribed. 
> 
>  Based on a patient's blood pressure, determine how much blood pressure medication (a dosage measured in milligrams) the patient should be prescribed. 
> 
> Correct
> 
> This task predicts one of two classes, malignant or not malignant.
> 
> ### 2.
> 
> Question 2
> 
> Recall the sigmoid function is g(z)=11+e−zg(z) = \frac{1}{1+e^{-z}}g(z)=1+e−z1​
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/d60aeff4-f74f-459c-b70d-9c06c64458d7image3.png?expiry=1658534400000&hmac=dekV5v-rrtff_jmD9A-v7nFkzlOyx1N9PhGsG8ctH1M)
> 
> If z is a large positive number, then:
> 
> 1 / 1 point
> 

      g(z)g(z)g(z) is near one (1) 
> 
>  g(z)g(z)g(z) will be near 0.5 
> 
>  g(z)g(z)g(z) is near negative one (-1) 
> 
>  g(z)g(z)g(z) will be near zero (0) 
> 
> Correct
> 
> Say z = +100+100+100. So e−ze^{-z}e−z is then e−100e^{-100}e−100, a really small positive number. So, g(z)=11+a small positive numberg(z) = \frac{1}{1+ \text{a small positive number}}g(z)=1+a small positive number1​ which is close to 111
> 
> ### 3.
> 
> Question 3
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/d60aeff4-f74f-459c-b70d-9c06c64458d7image2.png?expiry=1658534400000&hmac=AayHEs30YYXW3poj8syJ1iqN9v4WWWrMIhppJsjZlWE)
> 
> A cat photo classification model predicts 1 if it's a cat, and 0 if it's not a cat. For a particular photograph, the logistic regression model outputs g(z)g(z)g(z) (a number between 0 and 1). Which of these would be a reasonable criteria to decide whether to predict if it’s a cat?
> 
> 1 / 1 point
> 
>  Predict it is a cat if g(z) < 0.7 
> 
>  Predict it is a cat if g(z) = 0.5 
> 

      Predict it is a cat if g(z) >= 0.5 
> 
>  Predict it is a cat if g(z) < 0.5 
> 
> Correct
> 
> Think of g(z) as the probability that the photo is of a cat. When this number is at or above the threshold of 0.5, predict that it is a cat.
> 
> ### 4.
> 
> Question 4
> 
> True/False? No matter what features you use (including if you use polynomial features), the decision boundary learned by logistic regression will be a linear decision boundary.
> 
> 1 / 1 point
> 

      False 
> 
>  True 
> 
> Correct
> 
> The decision boundary can also be non-linear, as described in the lectures.
>
> -- https://www.coursera.org/learn/machine-learning/exam/jkmDN/practice-quiz-classification-with-logistic-regression/view-attempt#g85ULK-legend
