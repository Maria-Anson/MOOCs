# Module 1 Graded Quiz Logisitic Regression
> ### 1.
> 
> Question 1
> 
> The output of a logistic regression model applied to a data sample _____________.
> 
> 1 / 1 point
> 
>  tells you which class the sample belongs to. 
> 
>  is the log odds of the sample, which you can use for interpretive purposes. 
> 

      is the probability of the sample being in a certain class. 
> 
>  tells you the odds of the sample belonging to a certain class. 
> 
> Correct
> 
> Correct. Logistic regression outputs a value between zero and one which can be thought of as the probability of the sample being in a certain class.
> 
> ### 2.
> 
> Question 2
> 
> Describe how any binary classification model can be extended from its basic form on two classes, to work on multiple classes.
> 
> 1 / 1 point
> 
>  Fit the binary classifier to all of the classes simultaneously. 
> 

      Use a one-versus all technique, where for each class you fit a binary classifier to that class versus all of the other classes. 
> 
>  Use process of elimination to discard any unimportant classes. 
> 
>  Use the coefficients from a linear regression model to weight the classes. 
> 
> Correct
> 
> Correct. With each class, we're going to be estimating the binary logistic regression versus all other classes. And the estimated category is going to be the class with the highest estimated probability for each one of those one-versus-all classifiers.
> 
> ### 3.
> 
> Question 3
> 
> Which tool is most appropriate for measuring the performance of a classifier on unbalanced classes?
> 
> 1 / 1 point
> 
>  The true positive rate. 
> 
>  The Receiver Operating Characteristic (ROC) curve. 
> 

      The precision-recall curve. 
> 
>  The false positive rate. 
> 
> Correct
> 
> Correct. The precision-recall curve displays the precision vs recall for different probability thresholds. Both precision and recall are focused on the positive class, which is normally the minority class in imbalanced classification problems.
> 
> ### 4.
> 
> Question 4
> 
> (True/False) One of the requirements of logistic regression is that you need a variable with two classes.
> 
> 1 / 1 point
> 
>  True 
> 

      False 
> 
> Correct
> 
> Correct! You can use a multinomial logistic regression if you have more than two classes. You can review the demo in lesson 2 of this module, in which you did a multinomial logistic to predict a target variable with more than two classes.
> 
> ### 5.
> 
> Question 5
> 
> (True/False) The shape of ROC curves are the leading indicator of an overfitted logistic regression.
> 
> 1 / 1 point
> 
>  True 
> 

      False 
> 
> Correct
> 
> Correct! Although overfitted models tend to have really high ROC curves with high values of area under the curve, a classification matrix or a measure like accuracy can be more reliable. Please review the lesson _Confusion Matrix, Accuracy, Specificity, Precision, and Recall._
> 
> ### 6.
> 
> Question 6
> 
> **Consider this scenario for Questions 3 to 7.**
> 
> **You are evaluating a binary classifier. There are 50 positive outcomes in the test data, and 100 observations. Using a 50% threshold, the classifier predicts 40 positive outcomes, of which 10 are incorrect.**
> 
> What is the classifier’s Precision on the test sample?
> 
> 1 / 1 point
> 
>  25% 
> 
>  60% 
> 

      75% 
> 
>  80% 
> 
> Correct
> 
> Correct! You can find more information in the lesson _Confusion Matrix, Accuracy, Specificity, Precision, and Recall_.
> 
> ### 7.
> 
> Question 7
> 
> **Consider this scenario for Questions 3 to 7.**
> 
> **You are evaluating a binary classifier. There are 50 positive outcomes in the test data, and 100 observations. Using a 50% threshold, the classifier predicts 40 positive outcomes, of which 10 are incorrect.**
> 
> What is the classifier’s Recall on the test sample?
> 
> 1 / 1 point
> 
>  25% 
> 

      60% 
> 
>  75% 
> 
>  80% 
> 
> Correct
> 
> Correct! You can find more information in the lesson _Confusion Matrix, Accuracy, Specificity, Precision, and Recall_.
> 
> ### 8.
> 
> Question 8
> 
> **Consider this scenario for Questions 3 to 7.**
> 
> **You are evaluating a binary classifier. There are 50 positive outcomes in the test data, and 100 observations. Using a 50% threshold, the classifier predicts 40 positive outcomes, of which 10 are incorrect.**
> 
> What is the classifier’s F1 score on the test sample?
> 
> 1 / 1 point
> 
>  50% 
> 

      66.7% 
> 
>  67.5% 
> 
>  70% 
> 
> Correct
> 
> Correct! You can find more information in the lesson _Confusion Matrix, Accuracy, Specificity, Precision, and Recall_.
> 
> ### 9.
> 
> Question 9
> 
> **Consider this scenario for Questions 3 to 7.**
> 
> **You are evaluating a binary classifier. There are 50 positive outcomes in the test data, and 100 observations. Using a 50% threshold, the classifier predicts 40 positive outcomes, of which 10 are incorrect.**
> 
> Increasing the threshold to 60% results in 5 additional positive predictions, all of which are correct. Which of the following statements about this new model (compared with the original model that had a 50% threshold) is TRUE?
> 
> 1 / 1 point
> 
>  The F1 score of the classifier would decrease. 
> 
>  The area under the ROC curve would decrease. 
> 
>  The F1 score of the classifier would remain the same. 
> 

      The area under the ROC curve would remain the same. 
> 
> Correct
> 
> Correct! For more information, please review the lesson _ROC and Precision-Recall Curves_.
> 
> ### 10.
> 
> Question 10
> 
> **Consider this scenario for Questions 3 to 7.**
> 
> **You are evaluating a binary classifier. There are 50 positive outcomes in the test data, and 100 observations. Using a 50% threshold, the classifier predicts 40 positive outcomes, of which 10 are incorrect.**
> 
> The threshold is now increased further, to 70%. Which of the following statements is TRUE?
> 
> 1 / 1 point
> 
>  The Recall of the classifier would decrease. 
> 
>  The Precision of the classifier would decrease. 
> 
>  The Recall of the classifier would increase or remain the same. 
> 

      The Precision of the classifier would increase or remain the same.
>
> -- https://www.coursera.org/learn/supervised-machine-learning-classification/exam/1gp9n/module-1-graded-quiz-logisitic-regression/view-attempt#sLUyJKoWEey4Ego8x7Otyw-legend
