> ## Overfitting & Regularization in Logistic Regression
> 
> Total points 8
> 
> ### 1.
> 
> Question 1
> 
> Consider four classifiers, whose classification performance is given by the following table:
> 
> Classification error on training set
> 
> Classification error on validation set
> 
> Classifier 1
> 
> 0.2
> 
> 0.6
> 
> Classifier 2
> 
> 0.8
> 
> 0.6
> 
> Classifier 3
> 
> 0.2
> 
> 0.2
> 
> Classifier 4
> 
> 0.5
> 
> 0.4
> 
> Which of the four classifiers is most likely overfit?
> 
> 1 point
> 

      Classifier 1 
> 
>
>  Classifier 2 
> 
>  Classifier 3 
> 
>  Classifier 4 
> 
> ### 2.
> 
> Question 2
> 
> Suppose a classifier classifies 23100 examples correctly and 1900 examples incorrectly. Compute error by hand. Round your answer to 3 decimal places.
> 
> 1 point
> 

     0.076
> 
> ### 3.
> 
> Question 3
> 
> (True/False) Accuracy and error measured on the same dataset always sum to 1.
> 
> 1 point
> 

      True 
> 
>  False 
> 
> ### 4.
> 
> Question 4
> 
> Which of the following is NOT a correct description of complex models?
> 
> 1 point
> 
>  Complex models accommodate many features. 
> 
>  Complex models tend to produce lower training error than simple models. 
> 

      Complex models tend to generalize better than simple models. 
> 
>  Complex models tend to exhibit high variance in response to perturbation in the training data. 
> 
>  Complex models tend to exhibit low bias, capturing many patterns in the training data that simple models may have missed. 
> 
> ### 5.
> 
> Question 5
> 
> Which of the following is a symptom of overfitting in the context of logistic regression? Select all that apply.
> 
> 1 point
> 

      Large estimated coefficients 
> 
>  Good generalization to previously unseen data 
> 
>  Simple decision boundary 
> 

      Complex decision boundary 
> 

      Overconfident predictions of class probabilities 
> 
> ### 6.
> 
> Question 6
> 
> Suppose we perform L2 regularized logistic regression to fit a sentiment classifier. Which of the following plots does NOT describe a possible coefficient path? Choose all that apply.
> 
> **Note.** Assume that the algorithm runs for a wide range of L2 penalty values and each coefficient plot is zoomed out enough to capture all long-term trends.
> 
> 1 point
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/s0aljeWUEeWufRJaRfO1AQ_3134541d802ae1aaee26daec7ef39ca3_L_3SbuBaEeW--hK2gi_BIw_fbbbb77fd44af452b3d337434cdb7702_Capture.png?expiry=1656028800000&hmac=Ll_USXGWcftIEKAJfPE11YfEmTyxROgel9xcH61n1d8) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/xUjv0uWUEeWuUgrcWIxPhQ_ac77661c16c2fb40c0c3abfbf076a424_rvPx2eD1EeWOVQ68c1xy2w_ad1639c57963f5eaea6612cb568c4d86_Capture.png?expiry=1656028800000&hmac=LjWcgh-01Qz3JCMRkxTaAcaicHVMTBlXtZrwLM2kJjg) 

    True
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2f4k6eWUEeWIdgqHxZs34w_1ee2b9e5512622d0ad3a587b44c49922_JcoDWuBbEeWufRJaRfO1AQ_ff849715b543c56709a46f7be7a14c5d_Capture.png?expiry=1656028800000&hmac=E0OngLtSTdMrLxUFCIcH32m3f8_DNkpyf6C3yKYHAlU) 

    True
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/5YNc7eWUEeWOVQ68c1xy2w_768b146d738d6e1991ac9d5f678dbef6_9wGVMuBbEeW--hK2gi_BIw_27e6398723f122d80d4caae557763566_Capture.png?expiry=1656028800000&hmac=m8TKUj340hdjbugpTf0qslPbJwlILLFdZu4QXVVTrQQ) 
> 
> ### 7.
> 
> Question 7
> 
> Suppose we perform L1 regularized logistic regression to fit a sentiment classifier. Which of the following plots does NOT describe a possible coefficient path? Choose all that apply.
> 
> **Note.** Assume that the algorithm runs for a wide range of L1 penalty values and each coefficient plot is zoomed out enough to capture all long-term trends.
> 
> 1 point

    True
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/A16k-eWVEeW--hK2gi_BIw_0d7afdaf1bd9730fd7b5c51c424f1b95_aJDg6eD2EeWuUgrcWIxPhQ_81584c7620804c5d7093ee0063171269_Capture.png?expiry=1656028800000&hmac=dzi37lXgQRuDArkHSubnc3oXHK4aqNoOJQK0h0-_3Jo) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/D3JhYeWVEeWufRJaRfO1AQ_0569b1c0c9a8bd6798c91d817f3aef7c_aJbicuBcEeW--hK2gi_BIw_d09a4fde17773e1f5f1a270b3b6d357a_Capture.png?expiry=1656028800000&hmac=YFCFRRVjR1ksWUKjcvpM0irqkmwchgxUDUSWDSSgwVY) 
> 
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Ht-B8uWVEeWufRJaRfO1AQ_bd596c09a8282ec2de28b358ca5f171d_cLTtQeD2EeWufRJaRfO1AQ_4f1f5b7a19b8e305c40e11e7578b1d38_Capture2.png?expiry=1656028800000&hmac=_Pg6JtMoTHvBZFObD3_ZQKsRch3NGco50HVbSEPVBLk) 

    True
>  ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Mf6t5uWVEeWuUgrcWIxPhQ_2a643ffaf830d9218db5a6314936d52f_V4_Ld-BdEeWIdgqHxZs34w_dfc3556048dfc2bc157ce8bf58d6d74a_Capture.png?expiry=1656028800000&hmac=OSO_HEsrX1xyBcinEHTi8G3Phr57nr2gFKkpL3lGwVg) 
> 
> ### 8.
> 
> Question 8
> 
> In the context of L2 regularized logistic regression, which of the following occurs as we increase the L2 penalty λ\lambdaλ? Choose all that apply.
> 
> 1 point
> 

      The L2 norm of the set of coefficients gets smaller 
> 
>  Region of uncertainty becomes narrower, i.e., the classifier makes predictions with higher confidence. 
> 

      Decision boundary becomes less complex 
> 
>  Training error decreases 
> 

      The classifier has lower variance 
> 
>  Some features are excluded from the classifier
>
> -- https://www.coursera.org/learn/ml-classification/exam/jp0Yp/overfitting-regularization-in-logistic-regression/attempt#TUNNELVISIONWRAPPER_CONTENT_ID
