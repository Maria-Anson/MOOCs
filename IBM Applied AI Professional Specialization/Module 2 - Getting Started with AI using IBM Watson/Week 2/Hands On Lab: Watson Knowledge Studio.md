> ## Hands On Lab: Watson Knowledge Studio
> 
> * * *
> 
> ## Exploring Watson Knowledge Studio
> 
> IBM provides an online demo of Watson Knowledge Studio at: [Watson Knowledge Studio](http://knowledge-studio-demo.ng.bluemix.net/) (or from the product page, click View demo).  
> 
> The demo environment provides two models  for analysis:
> 
> *   The Default Model, which is a bare-bones annotation model based on a superficial grammatical analysis.
> *   A Knowledge Studio Custom Model, which is a sophisticated annotation model based on machine learning training in a specific domain.
> 
> In this demo, you will use Watson Knowledge Studio to analyze three pieces of text, first with the default model, and then with the Knowledge Studio Custom Model. You will then compare the results.
> 
> ### Use the following steps to explore the demo:
> 
> **Crash Report**
> 
> 1.  Access the online demo here: [Watson Knowledge Studio](http://knowledge-studio-demo.ng.bluemix.net/)
> 2.  Under **Text to be analyzed**, click in the **Crash Report** text box to ensure that it is selected.
> 3.  Under **Model to be used**, click **Default Model**.
> 4.  In the **Analysis result**, find the items identified as **Vehicle**.
> 5.  In the fourth paragraph, follow the lines from the vehicle references. What actions and objects do they link?
> 6.  In the fourth paragraph, what is identified as a **Person**?
> 7.  Under **Model to be used**, click **Knowledge Studio Custom Model**.
> 8.  In the Analysis result, find the items identified as **PART_OF_CAR**. Note that some of the items identified as Vehicle by the Default Model are identified as PART_OF_CAR, along with  many other items.
> 9.  How is the item previously identified as **Person** now identified?
> 10.  Which of the two models do you think is more accurate?
> 
> **Medicine**
> 
> 1.  On the Watson Knowledge Studio page, under**Text to be analyzed**, click in the **Medicine** text box to ensure that it is selected.
> 2.  Under **Model to be used**, click **Default Model**.
> 3.  In the**Analysis result**, find the two occurrences of the word **morphine**. Are both correctly identified?
> 4.  Under **Model to be used**, click **Knowledge Studio Custom Model**.
> 5.  In the **Analysis result**, find the items identified as **MEDICINE**. Are the two occurrences of the word morphine now correctly identified? What about other items identified as **MEDICINE**?
> 6.  Follow the lines from each **DISEASE** label to the **EFFECT** label, and note the item each identifies. Has Watson Knowledge Studio identified the items which are adverse drug reactions?
> 7.  Which  of the two models do you think is more accurate for this piece of text?
> 
> **Fantasy Football**
> 
> 1.  On the Watson Knowledge Studio page, under **Text to be analyzed**, click in the **Fantasy Football** text box to ensure that it is selected.
> 2.  Under **Model to be used**, click **Default Model**.
> 3.  In the **Analysis result**, find the three  items identified as **Organisation**.
> 4.  How is **Sammy Watkins** identified?
> 5.  Under **Model to be used**, click **Knowledge Studio Custom Model**.
> 6.  In the **Analysis result**, find the items previously identified as **Organisations**.
> 7.  How is **Sammy Watkins** identified? What is his relationship to **Chiefs**?
> 8.  Which model provides more information?
> 
> Given what you have learned, would you use the default model, or create your own custom model to suit your specific domain?
>
> -- https://www.coursera.org/learn/ai-with-ibm-watson/supplement/ZFqrk/hands-on-lab-watson-knowledge-studio#main
