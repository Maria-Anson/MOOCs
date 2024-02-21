## Week 1 Quiz
> 
> Latest Submission Grade 100%
> 
> ### 1.
> 
> Question 1
> 
> The regression technique described in class is called **least-squares** regression because:
> 
> 1 / 1 point
> 

      The estimated model parameters are learned by minimizing the sum of the squares of the residuals. 
> 
>  It always produces predictions that are perfect squares. 
> 
>  The solution technique involves a square design matrix. 
> 
> Correct
> 
> Your answer is correct.
> 
> ### 2.
> 
> Question 2
> 
> Given the following three regression models for **SepalLength,** indicate which model has the **best** fit.
> 
> ![OLS Regression Results from Python's Statsmodels library. ](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/rgKsC_AATEeCrAvwABxHIA_25660caa5e384d3cb7a3f1cbacf5caf1_Screen-Shot-2021-09-11-at-12.05.50-PM.png?expiry=1657929600000&hmac=pKAp85gJpSOmAh_cu-Vxj_WdpRhHnjSiND4EUTMKcvI)OLS Regression Results summary table. Dependent variable equals Sepal Length. Model is OLS. Method is Least Squares. Number of observations equals 150\. Df residuals is 148\. Df Model is 1\. Covariance Type is non-robust. R-squared is 0.760\. Adjusted R-squared is 0.758\. F-statistic is 468.6\. Prob (F-statistic) uses scientific notation. Prob (F-statistic) is 1.04 times 10 to the power of negative 47\. Log-likelihood is negative 77.020\. AIC is 158.0\. BIC is 164.1.![OLS Regression Results from Python library Statsmodels. ](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/zBFVYP8JQ0GRVWD_CQNBgw_251155f420c443548a3b335fa80cdaf1_Screen-Shot-2021-09-11-at-12.06.04-PM.png?expiry=1657929600000&hmac=7HXbouLcCYYhwU6ZpS88rg4WPvIz7D1rCn65cyQri58)OLS Regression Results summary. Dependent variable is Sepal Length. Model is OLS. Method is Least Squares. Number of observations is 150\. Df Residuals is 148\. Df Model is 1\. Covariance Type is non-robust. R-squared is 0.012\. Adjusted R-squared is 0.005\. F-statistic is 1.792\. Prob (F-statistic) is 0.183\. Log-Likelihood is negative 183.14\. AIC is 370.3\. BIC is 376.3.![OLS Regression Results from Python library StatsModels. ](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bNZ8BE6DRTaWfAROg-U2jA_45c0f6f8b33149caa966e6934abf12f1_Screen-Shot-2021-09-11-at-12.06.20-PM.png?expiry=1657929600000&hmac=5jnXC2FHvsEcTs2uECllYAUWMM-gbJPTb040S3fgAx4)OLS Regression Results summary. Dependent variable is Sepal Length. Model is OLS. Method is Least Squares. Number of observations is 150\. DF Residuals is 147\. Df Model is 2\. Covariance Type is non-robust. R-squared is 0.840\. Adjusted R-squared is 0.838\. F-statistic is 386.8\. Prob (F-statistic) is in scientific notation. Prob (F-statistic) is 2.74 times 10 to the power of negative 59\. Log-Likelihood is negative 46.442\. AIC is 98.88\. BIC is 107.9\.
> 
> 1 / 1 point
> 
>  A. 
> 
>  B. 
> 

      C. 
> 
> Correct
> 
> Your answer is correct. R-squared is used to measure fit. Model C. has the highest r-squared value of the three models.
> 
> ### 3.
> 
> Question 3
> 
> Given the following regression model information for the model **SepalLength** **~** **PetalLength**,answer the question below.
> 
> ![OLS Regression Results from Python library StatsModels. ](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/CEkik-OGSHqJIpPjhsh66A_af913e585a724bc0889745f0533780f1_Screen-Shot-2021-09-11-at-12.19.36-PM.png?expiry=1657929600000&hmac=HNh7Sk2gGqkMCCuoGSEJQKqxeeRQw5YSBuLUOqshhB8)Dependent Variable is Sepal Length. Model is OLS. Method is Least Squares. Number of Observations is 150\. Df Residuals is 148\. Df Model is 1\. Covariance Type is non-robust. The following apply to the Intercept: the coefficient is 4.3056\. Standard error is 0.078\. t is 54.895\. P greater than absolute value of t is 0.000\. The 95 percent confidence interval for the coefficient is 4.151 to 4.461\. The following apply to the Petal Length. For Petal Length, the coefficient is 0.4091\. Standard error is 0.019\. t is 21.646\. P greater than absolute value of t is 0.000\. The 95 percent confidence interval for the coefficient is 0.372 to 0.446\.
> 
> When the PetalLength increases by 1, how much does the SepalLength increase by?
> 
> 1 / 1 point
> 

     0.4091
> 
> Correct
> 
> Your answer is correct. The SepalLength increases by 0.4091 when the PetalLength increases by 1.
> 
> ### 4.
> 
> Question 4
> 
> Assume you are modeling Y∼X Y \sim X Y∼X where X is a discrete or categorical variable and Y is a continuous variable.
> 
> Is this a regression or classification problem?
> 
> 1 / 1 point
> 
>  C​lassification 
> 
>  E​ither technique could be used. 
> 

      R​egression 
> 
> Correct
> 
> Y​our answer is correct.
> 
> Because the dependent variable, Y, is continuous, this is a regression problem. We can use regression with either continuous or categorical independent variables (X).
> 
> The correct answer is: Regression
> 
> ### 5.
> 
> Question 5
> 
> It makes sense to use a **correlation matrix** to select multiple features by choosing features in order of correlation.
> 
> 1 / 1 point
> 
>  T​rue 
> 

      F​alse 
> 
> Correct
> 
> Y​our answer is correct.
> 
> A correlation matrix gives good information to select a single feature. However, the correlation matrix does not help select multiple features in the right order.
> 
> ### 6.
> 
> Question 6
> 
> We have a linear regression model with an intercept in the form y = ax + b. We create a new model with no intercept in the form y = ax. The r-squared value for the model with no intercept is higher than the r-squared value model with an intercept. We can feel confident that the model with no intercept is better than the model with an intercept.  
> 
> 1 / 1 point
> 
>  T​rue 
> 

      F​alse 
> 
> Correct
> 
> Y​our answer is correct. The r-squared value for the model with no intercept is uncentered. We can't compare the r-squared value for the model with an intercept and the uncentered r-squared value for the model with no intercept head to head.
> 
> ### 7.
> 
> Question 7
> 
> Suppose you fit a multiple linear regression model to a dataset with p=7p=7p=7 features and n=1000n=1000n=1000 data points.  Answer the following question: Hint:  (Design matrix) X (coefficients vector) = (Y vector)
> 
> The design matrix X{\bf X}X has __________ rows 
> 
> 1 / 1 point
> 

     1000
> 
> Correct
> 
> The number of rows matches n, the number of data points which in this case is 1000\.
> 
> ### 8.
> 
> Question 8
> 
>  Assume you've run a regression model Y∼β0+β1X Y \sim \beta_0 + \beta_1 X Y∼β0​+β1​X for a single factor 'X'. The value of R2=0.932 R^2 = 0.932 R2=0.932 and the model is y^=5.5000−9.1667x \hat y = 5.5000 - 9.1667 x y^​=5.5000−9.1667x.
> 
> The _t-_value for β0\beta_0β0​ is 0.625 with a corresponding _p_-value of 0.555\. The _t_-value for β1\beta_1β1​ is 5.257 with a corresponding _p-value_ of 0.002\. The confidence interval for β0 \beta_0 β0​ is [-16.048, 27.048] and the confidence interval for β1 \beta_1 β1​ is [4.900, 13.434].
> 
> Is the model a poor, good or perfect fit to the available data?
> 
> 1 / 1 point
> 
>  P​oor 
> 

      G​ood 
> 
>  P​erfect 
> 
> Correct
> 
> Y​our answer is correct. The model is a good fit to the data because the R2 R^2 is 0.932.
> 
> ### 9.
> 
> Question 9
> 
>  Assume you've run a regression model Y∼β0+β1X Y \sim \beta_0 + \beta_1 X Y∼β0​+β1​X for a single factor 'X'. The value of R2=0.932 R^2 = 0.932 R2=0.932 and the model is y^=5.5000−9.1667x \hat y = 5.5000 - 9.1667 x y^​=5.5000−9.1667x.
> 
> The _t-_value for β0\beta_0β0​ is 0.625 with a corresponding _p_-value of 0.555\. The _t_-value for β1\beta_1β1​ is 5.257 with a corresponding _p-value_ of 0.002\. The confidence interval for β0 \beta_0 β0​ is [-16.048, 27.048] and the confidence interval for β1 \beta_1 β1​ is [4.900, 13.434].
> 
> Is the intercept ( β0\beta_0 ) statistically significant?
> 
> 1 / 1 point
> 
>  Y​es 
> 

      N​o 
> 
> Correct
> 
> Y​our answer is correct. The intercept is not statistically significant because the p-value 0.555 is high and the t-value 0.625 is low relative to the mean value. Moreover, the confidence interval [-16.048, 27.048] includes zero.
> 
> ### 10.
> 
> Question 10
> 
>  Assume you've run a regression model Y∼β0+β1X Y \sim \beta_0 + \beta_1 X Y∼β0​+β1​X for a single factor 'X'. The value of R2=0.932 R^2 = 0.932 R2=0.932 and the model is y^=5.5000−9.1667x \hat y = 5.5000 - 9.1667 x y^​=5.5000−9.1667x.
> 
> The _t-_value for β0\beta_0β0​ is 0.625 with a corresponding _p_-value of 0.555\. The _t_-value for β1\beta_1β1​ is 5.257 with a corresponding _p-value_ of 0.002\. The confidence interval for β0 \beta_0 β0​ is [-16.048, 27.048] and the confidence interval for β1 \beta_1 β1​ is [4.900, 13.434].
> 
>  Is the slope ( β1\beta_1 ) statistically significant?
> 
> 1 / 1 point
> 

      Y​es 
> 
>  N​o 
> 
> Correct
> 
> Y​our answer is correct. The slope is statistically significant because the p-value 0.002 is low and the t-value 5.257 is high relative to the mean value. Moreover, the confidence interval [4.900, 13.434] does not include zero, indicating that changes in X X result in changes in Y Y .
>
