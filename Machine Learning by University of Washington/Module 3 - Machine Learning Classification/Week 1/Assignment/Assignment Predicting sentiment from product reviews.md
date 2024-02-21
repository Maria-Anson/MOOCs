> # Predicting sentiment from product reviews
> 
> The goal of this assignment is to explore logistic regression and feature engineering with existing Turi Create functions.
> 
> In this assignment, you will use product review data from Amazon.com to predict whether the sentiments about a product (from its reviews) are positive or negative. You will:
> 
> *   Use SFrames to do some feature engineering
> 
> *   Train a logistic regression model to predict the sentiment of product reviews.
> 
> *   Inspect the weights (coefficients) of a trained logistic regression model.
> 
> *   Make a prediction (both class and probability) of sentiment for a new product review.
> 
> *   Given the logistic regression weights, predictors and ground truth labels, write a function to compute the **accuracy** of the model.
> 
> *   Inspect the coefficients of the logistic regression model and interpret their meanings.
> 
> *   Compare multiple logistic regression models.
> 
> ## If you are doing the assignment with Jupyter Notebook
> 
> A Jupyter Notebook has been provided below to you for this assignment. This notebook contains the instructions, quiz questions and partially-completed code for you to use as well as some cells to test your code.
> 
> **Make sure that you are using the latest version Turi Create.**
> 
> ## What you need to download
> 
> ### If you are using Turi Create:
> 
> *   Download the Amazon product review data In SFrame format:
> 
>  [ZIP File
> 
> amazon_baby.sframe
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/z2MqguI0Eemm5A4ynZyB2A_fb01f0fbfc2b4701913139e2e54281af_amazon_baby.sframe.zip?Expires=1655769600&Signature=RV0ZZE3CQG3h6YMvRtWIJxg3uyjAMlOS5FzkJTwoNgGNKpz4~AXGSuxqJ9qiULjMFgOi4Fzk7UZ9Y0c65UCGuiYGXqU~BT-HFmsOwJAgLXZfGsI4zvgN30JlLUrGKKYLQiBuKtNIdWhpCsKEmKzQvxQ83QFX6UJWsfLV78Omx8c_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion Jupyter Notebook:
> 
>  [ZIP File
> 
> CLA02-NB01.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/xNzmahsUS8Kc5mobFGvCag_c9cb67842a5d46cfa9e0013faf338b5a_CLA02-NB01.ipynb.zip?Expires=1655769600&Signature=Zfhxh2O3kLpwURZq9NPqbLPXmTjlOYycBtMUCFeTRYPuNifV5wY-pPVIMfvLY-ZdjdPGg3yK-owfZyv6mdP-aYyxuVq4nKXqqH~uKZChkvx60kWNysuhKCKtqiDiBCPWcXhjxlvQwoumsGHwTOH8r1NCpn-oBoke95RE~F8qiO8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> Save both of these files in the same directory (where you are calling Jupyter notebook from) and unzip the data file.
> 
> *   Follow the instructions contained in the Jupyter notebook.
> 
> ### If you are not using Turi Create
> 
> *   If you are using SFrame, download the Amazon product review data in SFrame format:
> 
>  [ZIP File
> 
> amazon_baby.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_35bdebdff61378878ea2247780005e52_amazon_baby.gl.zip?Expires=1655769600&Signature=V0290zTv1RwcMqS-qvuSdvR0G0A4~0VKPq7eRmW18ssc2m1EFQaEAyqG7G9L5FzXN3bVyK8wYThUpRMh1j0av78hQFvzgUJ4QN4aA4ruhTn3J335az2dhj8LJANOkCtq~h7afo6AbwqQCwdTfbTNz8RD9Uhzc5UmZZiIiHKHzU8_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   If you are using a different package, download the Amazon product review data in CSV format:
> 
>  [ZIP File
> 
> amazon_baby.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_596922c59a7068d4eb7baa104c01a685_amazon_baby.csv.zip?Expires=1655769600&Signature=Z9MmsUKVqXoKzDEW6iTljUhhy1bAhKpwGzSWsFuJWpbAUNZNyyLWxAdcWtgzJnlV-RyyoGyS934sDmEZIFbxAMUyWBxGqYHe50m2MCCcJCOI-uOq4ZyeuAMInSg-fc5OXneW96-4m9BtwM0DfwaPuPGEG4yqe6ZUM7kCYTXMbVc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> ## If you are using Turi Create and the companion Jupyter Notebook
> 
> Open the companion Jupyter notebook and follow the instructions in the notebook.
> 
> ## If you are using other tools
> 
> **This section is designed for people using tools other than Turi Create. Even though some instructions are specific to scikit-learn, most part of the assignment should be applicable to other tools as well. However, we highly suggest you use** [**SFrame**](https://github.com/turi-code/SFrame) **since it is open source. In this part of the assignment, we describe general instructions, however we will tailor the instructions for SFrame and scikit-learn.**
> 
> *   If you choose to use SFrame and scikit-learn, you should be able to follow the instructions here and complete the assessment. **All code samples given here will be applicable to SFrame and scikit-learn**.
> 
> *   You are free to experiment with any tool of your choice, but **some many not produce correct numbers for the quiz questions.**
> 
> ### Load Amazon dataset
> 
> **1\.** Load the dataset consisting of baby product reviews on Amazon.com. Store the data in a data frame **products**. In SFrame, you would run
> 
>  `1
> 
> 2
> 
> import sframe
> 
> products = sframe.SFrame('amazon_baby.gl/')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Note:** To install SFrame (without installing Turi Create), run
> 
>  `1
> 
> pip install sframe
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Perform text cleaning
> 
> **2.** We start by removing punctuation, so that words "cake." and "cake!" are counted as the same word.
> 
> *   Write a function **remove_punctuation** that strips punctuation from a line of text
> 
> *   Apply this function to every element in the **review** column of **products**, and save the result to a new column **review_clean**.
> 
> Refer to your tool's manual for string processing capabilities. Python lets us express the operation in a succinct way, as follows:
> 
>  `1
> 
> 2
> 
> 3
> 
> 4
> 
> 5
> 
> def remove_punctuation(text):
> 
>     import string
> 
>     return text.translate(None, string.punctuation) 
> 
> products['review_clean'] = products['review'].apply(remove_punctuation)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Aside**. In this notebook, we remove all punctuation for the sake of simplicity. A smarter approach to punctuation would preserve phrases such as "I'd", "would've", "hadn't" and so forth. See [this page](https://www.cis.upenn.edu/~treebank/tokenization.html) for an example of smart handling of punctuation.
> 
> **IMPORTANT**. Make sure to fill n/a values in the **review** column with empty strings (if applicable). The n/a values indicate empty reviews. For instance, Pandas's the fillna() method lets you replace all N/A's in the **review** columns as follows:
> 
>  `1
> 
> products = products.fillna({'review':''})  # fill in N/A's in the review column
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Extract Sentiments
> 
> **3\.** We will **ignore** all reviews with _rating = 3_, since they tend to have a neutral sentiment. In SFrame, for instance,
> 
>  `1
> 
> products = products[products['rating'] != 3]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **4\.** Now, we will assign reviews with a rating of 4 or higher to be _positive_ reviews, while the ones with rating of 2 or lower are _negative_. For the sentiment column, we use +1 for the positive class label and -1 for the negative class label. A good way is to create an anonymous function that converts a rating into a class label and then apply that function to every element in the **rating** column. In SFrame, you would use apply():
> 
>  `1
> 
> products['sentiment'] = products['rating'].apply(lambda rating : +1 if rating > 3 else -1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Now, we can see that the dataset contains an extra column called **sentiment** which is either positive (+1) or negative (-1).
> 
> ### Split into training and test sets
> 
> **5\.** Let's perform a train/test split with 80% of the data in the training set and 20% of the data in the test set. If you are using SFrame, make sure to use seed=1 so that you get the same result as everyone else does. (This way, you will get the right numbers for the quiz.)
> 
>  `1
> 
> train_data, test_data = products.random_split(.8, seed=1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_22:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_22 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_22 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_22:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_22.drop-target, .monaco-list.list_id_22 .monaco-list-rows.drop-target, .monaco-list.list_id_22 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> If you are not using SFrame, download the list of indices for the training and test sets:
> 
>  [ZIP File
> 
> module-2-assignment-train-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-2-assignment-train-idx.json.zip?Expires=1655769600&Signature=d4j9gkV456IwDoJaKNQkwS6Xv1evhxaqXMxtHFQsjpQefr6IX6H7s7cqMIF8GTR-zzTqjUTCW6zwOTJUA5cfdwJxq17r7K5W8AefqALAqSGq9PIyvSN0~zQRBryYXb~RxJzOsugoDiZJogCrkl2do-wyMxfTA3MMJ6RBFtxMp9k_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
>  [ZIP File
> 
> module-2-assignment-test-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-2-assignment-test-idx.json.zip?Expires=1655769600&Signature=bwASrax~d25yU-eTrIgg-GpiswglEBSqJuA4qeGNmxn3YBBkHeagkkcVF73CJjVM4C5u1NTpMhPbPZSvSZjbCdqkrW1CO9zxumJElhiMnc7J50JQ6YM148gB7dUGhXwSM7CDsmmlucwgFZ1GyRHzUkFKgKEJnV7vZC6lKFJWC4o_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> . IMPORTANT: If you are using a programming language with 1-based indexing (e.g. R, Matlab), make sure to increment all indices by 1.
> 
> Call the training and test sets **train_data** and **test_data**, respectively.
> 
> ### Build the word count vector for each review
> 
> **6.** We will now compute the word count for each word that appears in the reviews. A vector consisting of word counts is often referred to as **bag-of-word features**. Since most words occur in only a few reviews, word count vectors are sparse. For this reason, scikit-learn and many other tools use sparse matrices to store a collection of word count vectors. Refer to appropriate manuals to produce sparse word count vectors. General steps for extracting word count vectors are as follows:
> 
> *   Learn a vocabulary (set of all words) from the training data. Only the words that show up in the training data will be considered for feature extraction.
> 
> *   Compute the occurrences of the words in each review and collect them into a row vector.
> 
> *   Build a sparse matrix where each row is the word count vector for the corresponding review. Call this matrix **train_matrix**.
> 
> *   Using the same mapping between words and columns, convert the test data into a sparse matrix **test_matrix**.
> 
> The following cell uses CountVectorizer in scikit-learn. Notice the **token_pattern** argument in the constructor.
> 
>  `1
> 
> 2
> 
> 3
> 
> 4
> 
> 5
> 
> 6
> 
> 7
> 
> 8
> 
> 9
> 
> from sklearn.feature_extraction.text import CountVectorizer
> 
> vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
> 
>      # Use this token pattern to keep single-letter words
> 
> # First, learn vocabulary from the training data and assign columns to words
> 
> # Then convert the training data into a sparse matrix
> 
> train_matrix = vectorizer.fit_transform(train_data['review_clean'])
> 
> # Second, convert the test data into a sparse matrix, using the same word-column mapping
> 
> test_matrix = vectorizer.transform(test_data['review_clean'])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_23:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_23 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_23 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_23:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_23.drop-target, .monaco-list.list_id_23 .monaco-list-rows.drop-target, .monaco-list.list_id_23 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Keep in mind that the test data must be transformed in the same way as the training data.
> 
> ### Train a sentiment classifier with logistic regression
> 
> We will now use logistic regression to create a sentiment classifier on the training data.
> 
> **7\.** Learn a logistic regression classifier using the training data. If you are using scikit-learn, you should create an instance of the [LogisticRegression class](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) and then call the method fit() to train the classifier. This model should use the sparse word count matrix (**train_matrix**)as features and the column **sentiment** of **train_data** as the target. Use the default values for other parameters. Call this model **sentiment_model**.
> 
> **8\.** There should be over 100,000 coefficients in this **sentiment_model**. Recall from the lecture that positive weights w_j correspond to weights that cause positive sentiment, while negative weights correspond to negative sentiment. Calculate the number of positive (>= 0, which is actually nonnegative) coefficients.
> 
> **Quiz question:** How many weights are >= 0?
> 
> ### Making predictions with logistic regression
> 
> **9\.** Now that a model is trained, we can make predictions on the **test data**. In this section, we will explore this in the context of 3 data points in the test data. Take the 11th, 12th, and 13th data points in the test data and save them to **sample_test_data**. The following cell extracts the three data points from the SFrame **test_data** and print their content:
> 
>  `1
> 
> 2
> 
> sample_test_data = test_data[10:13]
> 
> print sample_test_data
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_24:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_24 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_24 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_24:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_24.drop-target, .monaco-list.list_id_24 .monaco-list-rows.drop-target, .monaco-list.list_id_24 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's dig deeper into the first row of the **sample_test_data**. Here's the full review:
> 
>  `1
> 
> sample_test_data[0]['review']
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_25:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_25 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_25 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_25:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_25.drop-target, .monaco-list.list_id_25 .monaco-list-rows.drop-target, .monaco-list.list_id_25 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> That review seems pretty positive.
> 
> Now, let's see what the next row of the **sample_test_data** looks like. As we could guess from the rating (-1), the review is quite negative.
> 
>  `1
> 
> sample_test_data[1]['review']
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_26:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_26 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_26 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_26:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_26.drop-target, .monaco-list.list_id_26 .monaco-list-rows.drop-target, .monaco-list.list_id_26 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **10\.** We will now make a class prediction for the **sample_test_data**. The **sentiment_model** should predict **+1** if the sentiment is positive and **-1** if the sentiment is negative. Recall from the lecture that the score (sometimes called margin) for the logistic regression model is defined as:
> 
> scorei=w⊺h(xi)\mbox{score}_i = \mathbf{w}^\intercal h(\mathbf{x}_i)
> 
> where h(xi)h(\mathbf{x}_i)h(xi​) represents the features for data point i. We will write some code to obtain the scores. For each row, the score (or margin) is a number in the range (-inf, inf). Use a pre-built function in your tool to calculate the score of each data point in **sample_test_data**. In scikit-learn, you can call the decision_function() function.
> 
> **Hint**: You'd probably need to convert sample_test_data into the sparse matrix format first.
> 
>  `1
> 
> 2
> 
> 3
> 
> sample_test_matrix = vectorizer.transform(sample_test_data['review_clean'])
> 
> scores = sentiment_model.decision_function(sample_test_matrix)
> 
> print scores
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_27:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_27 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_27 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_27:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_27.drop-target, .monaco-list.list_id_27 .monaco-list-rows.drop-target, .monaco-list.list_id_27 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Prediciting Sentiment
> 
> **11\.** These scores can be used to make class predictions as follows:
> 
> y^i={+1if w⊺h(xi)>0−1if w⊺h(xi)≤0\hat{y}_i =
> 
> {+1−1if w⊺h(xi)>0if w⊺h(xi)≤0
> 
> \begin{cases} +1 & \text{if } \mathbf{w}^\intercal h(\mathbf{x}_i) > 0\\ -1 &\text{if } \mathbf{w}^\intercal h(\mathbf{x}_i) \leq 0 \end{cases}y^​i​={+1−1​if w⊺h(xi​)>0if w⊺h(xi​)≤0​
> 
> Using scores, write code to calculate predicted labels for **sample_test_data**.
> 
> **Checkpoint**: Make sure your class predictions match with the ones obtained from **sentiment_model**. The logistic regression classifier in scikit-learn comes with the **predict** function for this purpose.
> 
> ### Probability Predictions
> 
> **12.** Recall from the lectures that we can also calculate the probability predictions from the scores using:
> 
> P(yi=+1∣xi,w)=11+exp⁡(−w⊺h(xi))P(y_i = +1 | \mathbf{x}_i, \mathbf{w}) = \dfrac{1}{1+\exp{(-\mathbf{w}^\intercal h(\mathbf{x}_i))}}P(yi​=+1∣xi​,w)=1+exp(−w⊺h(xi​))1​
> 
> Using the scores calculated previously, write code to calculate the probability that a sentiment is positive using the above formula. For each row, the probabilities should be a number in the range **[0, 1]**.
> 
> **Checkpoint**: Make sure your probability predictions match the ones obtained from **sentiment_model**.
> 
> **Quiz question:** Of the three data points in **sample_test_data**, which one (first, second, or third) has the **lowest probability** of being classified as a positive review?
> 
> ### Find the most positive (and negative) review
> 
> **13\.** We now turn to examining the full test dataset, **test_data**, and use sklearn.linear_model.LogisticRegression to form predictions on all of the test data points.
> 
> Using the sentiment_model, find the 20 reviews in the entire **test_data** with the **highest probability** of being classified as a **positive review**. We refer to these as the "most positive reviews."
> 
> To calculate these top-20 reviews, use the following steps:
> 
> 1.  Make probability predictions on **test_data** using the **sentiment_model**.
> 
> 2.  Sort the data according to those predictions and pick the top 20.
> 
> **Quiz Question**: Which of the following products are represented in the 20 most positive reviews?
> 
> **14.** Now, let us repeat this exercise to find the "most negative reviews." Use the prediction probabilities to find the 20 reviews in the **test_data** with the **lowest probability** of being classified as a **positive review**. Repeat the same steps above but make sure you **sort in the opposite order**.
> 
> **Quiz Question**: Which of the following products are represented in the 20 most negative reviews?
> 
> ### Compute accuracy of the classifier
> 
> **15.** We will now evaluate the accuracy of the trained classifier. Recall that the accuracy is given by
> 
> accuracy=# correctly classified examples# total examples\mbox{accuracy} = \dfrac{\mbox{# correctly classified examples}}{\mbox{# total examples}}
> 
> This can be computed as follows:
> 
> *   **Step 1:** Use the **sentiment_model** to compute class predictions.
> 
> *   **Step 2:** Count the number of data points when the predicted class labels match the ground truth labels.
> 
> *   **Step 3:** Divide the total number of correct predictions by the total number of data points in the dataset.
> 
> **Quiz Question**: What is the accuracy of the **sentiment_model** on the **test_data**? Round your answer to 2 decimal places (e.g. 0.76).
> 
> **Quiz Question**: Does a higher accuracy value on the **training_data** always imply that the classifier is better?
> 
> ### Learn another classifier with fewer words
> 
> **16\.** There were a lot of words in the model we trained above. We will now train a simpler logistic regression model using only a subet of words that occur in the reviews. For this assignment, we selected 20 words to work with. These are:
> 
>  `1
> 
> 2
> 
> 3
> 
> significant_words = ['love', 'great', 'easy', 'old', 'little', 'perfect', 'loves', 
> 
>       'well', 'able', 'car', 'broke', 'less', 'even', 'waste', 'disappointed', 
> 
>       'work', 'product', 'money', 'would', 'return']
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_28:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_28 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_28 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_28:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_28.drop-target, .monaco-list.list_id_28 .monaco-list-rows.drop-target, .monaco-list.list_id_28 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Compute a new set of word count vectors using only these words. The CountVectorizer class has a parameter that lets you limit the choice of words when building word count vectors:
> 
>  `1
> 
> 2
> 
> 3
> 
> vectorizer_word_subset = CountVectorizer(vocabulary=significant_words) # limit to 20 words
> 
> train_matrix_word_subset = vectorizer_word_subset.fit_transform(train_data['review_clean'])
> 
> test_matrix_word_subset = vectorizer_word_subset.transform(test_data['review_clean'])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_29:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_29 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_29 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_29:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_29.drop-target, .monaco-list.list_id_29 .monaco-list-rows.drop-target, .monaco-list.list_id_29 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Compute word count vectors for the training and test data and obtain the sparse matrices **train_matrix_word_subset** and **test_matrix_word_subset**, respectively.
> 
> ### Train a logistic regression model on a subset of data
> 
> **17\.** Now build a logistic regression classifier with **train_matrix_word_subset** as features and **sentiment** as the target. Call this model **simple_model**.
> 
> **18\.** Let us inspect the weights (coefficients) of the **simple_model.** First, build a table to store (word, coefficient) pairs. If you are using SFrame with scikit-learn, you can combine words with coefficients by running
> 
>  `1
> 
> 2
> 
> simple_model_coef_table = sframe.SFrame({'word':significant_words,
> 
>                                          'coefficient':simple_model.coef_.flatten()})
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_30:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_30 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_30 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_30:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_30.drop-target, .monaco-list.list_id_30 .monaco-list-rows.drop-target, .monaco-list.list_id_30 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Sort the data frame by the coefficient value in descending order.
> 
> **Note**: Make sure that the intercept term is excluded from this table.
> 
> **Quiz Question**: Consider the coefficients of **simple_model**. How many of the 20 coefficients (corresponding to the 20 **significant_words**) are positive for the **simple_model**?
> 
> **Quiz Question**: Are the positive words in the **simple_model** also positive words in the **sentiment_model**?
> 
> ### Comparing models
> 
> **19.** We will now compare the accuracy of the **sentiment_model** and the **simple_model**.
> 
> First, compute the classification accuracy of the **sentiment_model** on the **train_data.**
> 
> Now, compute the classification accuracy of the **simple_model** on the **train_data.**
> 
> **Quiz Question**: Which model (**sentiment_model** or **simple_model**) has higher accuracy on the TRAINING set?
> 
> **20.** Now, we will repeat this exercise on the **test_data**. Start by computing the classification accuracy of the **sentiment_model** on the **test_data**.
> 
> Next, compute the classification accuracy of the **simple_model** on the **test_data.**
> 
> **Quiz Question**: Which model (**sentiment_model** or **simple_model**) has higher accuracy on the TEST set?
> 
> ### Baseline: Majority class prediction
> 
> **21\.** It is quite common to use the **majority class classifier** as the a baseline (or reference) model for comparison with your classifier model. The majority classifier model predicts the majority class for all data points. At the very least, you should healthily beat the majority class classifier, otherwise, the model is (usually) pointless.
> 
> **Quiz Question**: Enter the accuracy of the majority class classifier model on the **test_data**. Round your answer to two decimal places (e.g. 0.76).
> 
> **Quiz Question**: Is the **sentiment_model** definitely better than the majority class classifier (the baseline)?
>
> -- https://www.coursera.org/learn/ml-classification/supplement/NtMAS/predicting-sentiment-from-product-reviews#main
