# Computer Vision
> 
> IBM Research creates innovative tools and resources to help unleash the power of AI. In this hands on lab, you will learn about IBM’s Adversarial Robustness Toolbox, and use it to mitigate simulated attacks by hackers.
> 
> ### Follow these steps to explore the demo:
> 
> 1\. Access the demo here: [Your AI model might be telling you this is not a cat.](https://art-demo.mybluemix.net/?cm_mc_uid=59963159489715526067556&cm_mc_sid_50200000=57143911561485594784&cm_mc_sid_52640000=48611511561485594790)
> 
> 2\. In the **Try it out** section, click the image of the Siamese cat.
> 
> _Figure 1 - Select an image_
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/CVVC7ZeTEemdeg7vqSp9lg_e832e1598e79489a15e640d956506bd2_Not-a-Cat-1.PNG?expiry=1592697600000&hmac=r7HwfGu_N7YlEEOuSmTmqtBIbfLqekcIYWwvUnSgCEg)
> 
> 3\. In the **Simulate Attack** section, ensure that no attack is selected, and that all the sliders are to the far left, indicating that all attacks and mitigation strategies are turned off.
> 
> What does Watson identify the image as, and at what confidence level? E.g. Siamese cat 92%
> 
> 4\. In the **Simulate Attack** section, under **Adversarial noise** **type**, select **Fast Gradient Method**. The strength slider will move to low.
> 
> _Figure 2 - Select an attack and level_
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/b_6yPZeTEemLWBJtO-Ty2g_20a2be865c47f0224fa5f1a8d747e469_Not-a-Cat-2.PNG?expiry=1592697600000&hmac=UObrMfjecW6tq2NlS_VHsuxIWMSCkQVprrXEMihmWd8)
> 
> What does Watson identify the image as now, and at what confidence level?
> 
> 3\. In the **Defend attack** section, move the **Gaussian Noise** slider to low.
> 
> _Figure 3 - Mitigate the attack_
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/zl16gpeTEemdeg7vqSp9lg_3ffba0df504d3027ac96e197fa60f692_Not-a-Cat-3.PNG?expiry=1592697600000&hmac=TU4mOk01hvqQErqJvqKgzXgYGbb7xL0umFBLcuFcco8)
> 
> 4\. What does Watson identify the image as now, and at what confidence level? Did the image recognition improve?
> 
> _Figure 4 - View the results_
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/_1TgvZeTEembvgrcYyyFsg_dee78346a3a7f9b55274d6fed272f0a5_Not-a-Cat-4.PNG?expiry=1592697600000&hmac=-fl6VCwwG1jx28HueGheYpaOjjiIWq7S8q51Olltkfs)
> 
> Note that you can use the slider on the image to see the original and modified images. 
> 
> 5\. Move the **Gaussian Noise** slider to **medium**, and then to **high**. For each level, note what Watson identifies the image as, and at what confidence level. Did the image recognition improve?
> 
> 6\. Move the **Gaussian Noise** slider to **None**.
> 
> 7\. In the **Defend attack** section, move the **Spatial Smoothing** slider to **low**. What does Watson identify the image as now, and at what confidence level? Did the image recognition improve?
> 
> 8\. Move the **Spatial Smoothing** slider to **medium**, and then to **high**. For each level, note what Watson identifies the image as, and at what confidence level. Did the image recognition improve?
> 
> 9\. Move the **Spatial Smoothing** slider to **None**.
> 
> 10\. In the **Defend attack** section, move the **Feature Squeezing** slider to **low**. What does Watson identify the image as now, and at what confidence level? Did the image recognition improve?
> 
> 11\. Move the **Feature Squeezing** slider to **medium**, and then to **high**. For each level, note what Watson identifies the image as, and at what confidence level. Did the image recognition improve?
> 
> 12\. Which of the three defenses would you use to defend against a Fast Gradient Attack?
> 
> **Optional:**
> 
> If you have time, use the same techniques to explore the other methods of attack (Projected Gradient Descent and C&W Attack) and evaluate which method of defense works best for each. If you want, try a different image.
> 
> Use the Discussion Forum to talk about the attacks and mitigation strategies with your fellow students.
>
> -- https://www.coursera.org/learn/introduction-to-ai/supplement/e49Ud/hands-on-lab-computer-vision#main
