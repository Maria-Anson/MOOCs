# Anomaly detection
> ### 1.
> 
> Question 1
> 
> You are building a system to detect if computers in a data center are malfunctioning. You have 10,000 data points of computers functioning well, and no data from computers malfunctioning. What type of algorithm should you use?
> 
> 1 / 1 point


      Anomaly detection 
> 
>  Supervised learning 
> 
> Correct
> 
> Creating an anomaly detection model does not require labeled data.
> 
> ### 2.
> 
> Question 2
> 
> You are building a system to detect if computers in a data center are malfunctioning. You have 10,000 data points of computers functioning well, and 10,000 data points of computers malfunctioning. What type of algorithm should you use?
> 
> 1 / 1 point
> 
>  Anomaly detection 


      Supervised learning 
> 
> Correct
> 
> You have a sufficient number of anomalous examples to build a supervised learning model.
> 
> ### 3.
> 
> Question 3
> 
> Say you have 5,000 examples of normal airplane engines, and 15 examples of anomalous engines. How would you use the 15 examples of anomalous engines to evaluate your anomaly detection algorithm?
> 
> 1 / 1 point
> 
>  Because you have data of both normal and anomalous engines, don’t use anomaly detection. Use supervised learning instead. 
> 
>  Use it during training by fitting one Gaussian model to the normal engines, and a different Gaussian model to the anomalous engines. 


      Put the data of anomalous engines (together with some normal engines) in the cross-validation and/or test sets to measure if the learned model can correctly detect anomalous engines. 
> 
>  You cannot evaluate an anomaly detection algorithm because it is an unsupervised learning algorithm. 
> 
> Correct
> 
> Anomalous examples are used to evaluate rather than train the model.
> 
> ### 4.
> 
> Question 4
> 
> Anomaly detection flags a new input xxx as an anomaly if p(x)<ϵp(x) < \epsilonp(x)<ϵ. If we reduce the value of ϵ\epsilonϵ, what happens?
> 
> 1 / 1 point
> 
>  The algorithm is more likely to classify new examples as an anomaly. 


      The algorithm is less likely to classify new examples as an anomaly. 
> 
>  The algorithm is more likely to classify some examples as an anomaly, and less likely to classify some examples as an anomaly. It depends on the example xxx. 
> 
>  The algorithm will automatically choose parameters μ\muμ and σ\sigmaσ to decrease p(x)p(x)p(x) and compensate. 
> 
> Correct
> 
> When ϵ\epsilonϵ is reduced, the probability of an event being classified as an anomaly is reduced.
> 
> ### 5.
> 
> Question 5
> 
> You are monitoring the temperature and vibration intensity on newly manufactured aircraft engines. You have measured 100 engines and fit the Gaussian model described in the video lectures to the data. The 100 examples and the resulting distributions are shown in the figure below.
> 
> The measurements on the latest engine you are testing have a temperature of 17.5 and a vibration intensity of 48\. These are shown in magenta on the figure below. What is the probability of an engine having these two measurements?
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0b4675ef-89e7-487f-a8a8-3e089a81a817image2.png?expiry=1659139200000&hmac=RfHUYme5v2ENHbTcA70Hy1uBqTHWJFoK1m3iPc9CEh0)
> 
> 1 / 1 point
> 
>  17.5 + 48 = 65.5 
> 
>  17.5 * 48 = 840 
> 
>  0.0738 + 0.02288 = 0.0966 

      0.0738 * 0.02288 = 0.00169 
> 
> Correct
> 
> According to the model described in lecture, p(A, B) = p(A) * p(B). .
>
> -- https://www.coursera.org/learn/unsupervised-learning-recommenders-reinforcement-learning/exam/afUuX/anomaly-detection/view-attempt#oHQS1e-legend
