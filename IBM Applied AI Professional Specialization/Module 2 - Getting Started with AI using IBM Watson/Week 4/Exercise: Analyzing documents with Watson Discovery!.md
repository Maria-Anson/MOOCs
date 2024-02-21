## Exercise: Analyzing documents with Watson Discovery!

*****

In this hands-on exercise you will utilize Watson Discovery to extract valuable
information from documents. When handling an enormous amount of text documents,
Watson Discovery is a valuable tool to optimize your work flow by applying
Natural Language Processing (NLP) algorithm to extract, valuable information,
sentiment, concepts, semantic roles from your collection of documents.

NOTE: For learners working to get a certificate for this course (i.e. not
auditing), please go through this exercise carefully and thoroughly it will be
used for the graded assignment.

FYI: In order to complete this exercise you will be creating an IBM Cloud
account and provisioning an instance for Watson Discovery service. A credit card
is NOT required to sign up for IBM Cloud Lite account and there is no charge
associated in creating a Lite plan instance of the Watson Discovery service.

## Step 1: Create an IBM Cloud Account

Click on the link below to create an IBM cloud account:

[Sign Up for IBM Watson Visual Recognition on IBM
Cloud](https://cocl.us/ibm_watson_visual_recognition_ai101_coursera)

On the page to which you get redirected by clicking on the link above, enter
your **email address**, **first name, last name, country or region, **and set
your **password**. 

NOTE: To get enhanced benefits, please sign up with you business or corporate
**email address** rather than a free email ID like Gmail, Hotmail, etc.

If you would like IBM to contact you for any changes to services or new
offerings, then check the box to accept the box to get notified by email. Then
click on the Create Account button to create your IBM Cloud account.

**If you already have an IBM Cloud account you can just log in using the link
above the Email field (top right in the screenshot below).



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/gO2crpOFEemODxK6RFJwEA_f5568cd3ef444fd6e598fd32848e1e9e_a7JG-__WEeiAgQrXx6bp4g_f1178892c3eee12618090d5c79abebb9_02_Register.png?expiry=1595376000000&hmac=LNekIUavcZHVil-_kj1YAeSAoLy5iZXPSXcaBTpZkYw)

## Step 2: Confirm Your Email Address

An email is sent to your email address to confirm your account.



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/msvGTJOFEemD9Q58qDY9yA_e3413b038ac86da792553c7f5c89533f_owJH7f_WEeiTKQ5ajE7PqA_4f4861e461f2895f19c17a586c258465_03_Complete_Registration.png?expiry=1595376000000&hmac=2ni-XJMs03Z45GB2pN4nlMQnxv8_6Mk3QC6RcDm35XI)

Go to your email account, and click on the "**Confirm Account**" link in the
email that was sent to you.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/qmlFRf_WEeiixgqCUDoEfA_1210631e5e9fc5b42b99f4afffdae61d_04_Email_Confirmation.png?expiry=1595376000000&hmac=RJg0F9vlFGVonkdDLzXMHHqp6yxpudUfwZntkNRwi4c)

## Step 3: Login to Your Account



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2iWTov_WEeiTKQ5ajE7PqA_374d994f47ec7fa09387640503bf0bb7_05_Successfully_Signed_Up.png?expiry=1595376000000&hmac=tITFou-06IVF9YNTSr4ARPS4BofjCB2HpdJhM9SMDm4)

When you click [Log in](https://cloud.ibm.com/login), you will be redirected to
a page to log into your IBM Cloud account.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/5sIvPv_WEeiixgqCUDoEfA_06d7a9caeed3b8e3c0a02bd62bb2e352_06_Login_IBM.png?expiry=1595376000000&hmac=A6lPnTEKdeh1oYqMdf6euMA_4BAW9a9UBNnp-JbWxYU)





## Step 4: Create a New Resource

On your dashboard page, click on the **Create a resource **on the top right to
create a new source.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/No2IA1bCEemPcBIa2xz0qA_21f10ad311d4f63b46da6fa38ff0a773_dashboard_resource.png?expiry=1595376000000&hmac=P1XA6eidD0b5SgYSy0iDdMieDZCcW6uWjUZHj6FB7ho)



## Step 5: Create a Watson Discovery Resource

On the **Catalog** page, select the **AI **category from the left pane, and then
select the **Watson Discovery **resource.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/JGvxYpOIEemD9Q58qDY9yA_4a0e89a92a57ac66ccc1efb6a0db96c9_Select_Watson_Discovery.png?expiry=1595376000000&hmac=t3tJhjySjmmiMS31JjVVZnoPfvgL1Fh8FYrNzO3cROc)

On the next page, you will get to name your service instance and choose your
region. Click on the arrow to reveal the drop-down menu of regions. Make sure to
select the region that is closest to you. Since I am located in Canada, then I
am choosing **Dallas** as my region since it is the closest region to me

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/m6ypHJOIEemD9Q58qDY9yA_cc19abc6b55652a074052563ed7ca89c_Naming_Discovery.png?expiry=1595376000000&hmac=4YCyWIMJLNj00lZJqoMuRs-lMG4sO7yz3Cl6QQYKJTg)

Then scroll down and make sure that the **lite** plan is selected, and click the
**Create **button.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/39Z2K5OIEemX8g5wksC5BA_47c0558336f2b226345f32574ab76c08_Create_Service.png?expiry=1595376000000&hmac=yzCuvvdb_rfHRb2LzGcPt0NzwDsLXT87sYbEbRdG3oY)

This will start provisioning your Watson Discovery instance. Once the service
has been provisioned, you can get into your Watson Discovery instance by
clicking the Discovery instance under the Services tab.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/DH_0LZOLEembFRJWuM9x-g_9252164e9c9f54cea960e07b2d50bef7_Provision_Service.png?expiry=1595376000000&hmac=tBpYoZX34rjiUPRvNlGlUAPETus5D62N-OgBSZ1cXSc)

Launch your service by clicking "Launch Watson Discovery".

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/j4SaK5OLEemGqAqLppoP9A_94e511c25682293dcc9c0a981291a818_Launch_Discovery.png?expiry=1595376000000&hmac=Yo_ZdAhn63zld2LAUq6ZPUu9dn2PamH7uB-cxOR_NuU)



## Step 6: Setting up Your Collection

Your collection will be hosted in a Collection, click on "Upload your own data"
to create your collection.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/NvnL4ZOOEemX8g5wksC5BA_73240f083d330c252d287a886b76cc90_Upload_Dataset.png?expiry=1595376000000&hmac=qXN6x8L2bD_MQd7opYjBA8YCAZGSJjD1Hm-oQzf_BWU)

You will be prompted to upgrade to the Advance plan, but for this exercise you
only need the Lite plan, so you could Set up with current plan.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/1m5Ct5OOEemODxK6RFJwEA_393a50079592860db12fd9a47e367cb6_Set_With_Current_Plan.png?expiry=1595376000000&hmac=owL7rOSn284Y15dal9-belD5FMjI0SaD_icbqgp5_Dk)

Since we are creating a collection for our documents, you can give your
Collection a name, and set the language of your documents to English.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/o5iJkJOPEemX8g5wksC5BA_6daaf7ec60d188257526266ebf3c5c73_Screen-Shot-2019-06-20-at-3.10.11-PM.png?expiry=1595376000000&hmac=rOuvdzKJGQzWjyC2x_DT3yIo364PCIJf-PGn9uinCyM)

## Step 7: Uploading your Documents

For the purpose of this lab, we will be analyzing IBM's 2018 Annual Report, you
can download the report from the following link.

[IBM_Annual_Report_2018.pdf](https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/IntroductionToAI/IBM_Annual_Report_2018.pdf)

Upload the IBM 2018 Annual Report onto Watson Discovery.

Click on "select document" and choose the IBM 2018 Annual Report.

Note! You can upload documents in the form of PDF, HTML, JSON, WORD, Excel,
PowerPoint, PNG, TIFF, JPG. Any of the above filetypes for up to 50 megabytes.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/7phoLJOQEemM1Qp4z8fLhg_b64d3a72aa254b66d0ba310aca6269bb_Upload_Document.png?expiry=1595376000000&hmac=po5zbxlYwebVRQbruDvYu-oORDvOtIq0npY41Xf4GQU)

## Step 8: Analyzing your Document

After your document has finished processing, click on the "Schema" tag
highlighted by the red box, and click on document view. As you scroll down you
can see the sentiment level of each entity. In this case it is positive for IBM
Watson, IBM Services, IBM Cloud, and AI. So this tool has improved my workflow
by providing me the sentiment for IBM Watson, IBM Services, and IBM Cloud
without someone reading through the whole document.



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/oHF47JOSEemODxK6RFJwEA_28486da1a71e45fda85316b2113209a0_Analyzing_Your_Schema.png?expiry=1595376000000&hmac=kQLmfHIIyay3frgCD8kAzhp3neTpvXpQYeYJXPC1xio)

## Step 9: Querying your Document

You can also extract important information from your document by using keywords.
Click on the Search tab, and enter your keywords in the Search for documents
section. In this case we are searching for "Intellectual Property", Watson
Discovery has returned the result for "Intellectual Property" in our document.



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/M-CK8ZOTEemGqAqLppoP9A_6fc05e630ed49eb5f7b8753d77f4da13_Search_In_Document.png?expiry=1595376000000&hmac=UtRFd-oA29tT-UvG7iBBONYAMvSINkgdRxm5CJOvMHg)



## Step 10: Save a screen shot

NOTE: This step is Optional for those Auditing the course. The screenshot saved
in this step will be required as part of the Graded Final Assignment for those
pursuing a certificate for this course.

From Steps 8 take and save a screenshot in .jpeg or .jpg format including the
Watson Discovery sentiment analysis of the document. See a sample screenshot
below.



![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/6BS-1JOTEemD9Q58qDY9yA_02c287e1276483d29feb2dd91e245562_Screen-Shot-2019-06-20-at-3.44.57-PM.png?expiry=1595376000000&hmac=bWFVeJWTrJk7O3xRr0TBCJTQMpqwB2tctuBNZYoMAiE)

## Step 15: Share Your Results!

Follow us on Twitter and send us some of your funniest and most interesting
results you found with IBM Watson Visual Recognition!

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/WVGQQ4r8EemVeg5DpI4LqA_1237efe95f1d0be3a3059cbe6667fd75_Tweet.jpg?expiry=1595376000000&hmac=NFM-qcQ6TeDi14N9pjZ5_yYZ4-Tda3BnLhirUmWcTEs)



[Click here](https://twitter.com/intent/tweet?text=I just learned how to use
Artificial Intelligence to classify images with @IBMWatson in this Introduction
to AI course by @ravahuja on Coursera -
https://www.coursera.org/learn/introduction-to-ai) to share the above Tweet.

[Follow Rav Ahuja](https://twitter.com/ravahuja)










