# Implementing binary decision trees
> 
> The goal of this notebook is to implement your own binary decision tree classifier. You will:
> 
> *   Use SFrames to do some feature engineering.
> 
> *   Transform categorical variables into binary variables.
> 
> *   Write a function to compute the number of misclassified examples in an intermediate node.
> 
> *   Write a function to find the best feature to split on.
> 
> *   Build a binary decision tree from scratch.
> 
> *   Make predictions using the decision tree.
> 
> *   Evaluate the accuracy of the decision tree.
> 
> *   Visualize the decision at the root node.
> 
> **Important Note**: In this assignment, we will focus on building decision trees where the data contain **only binary (0 or 1) features**. This allows us to avoid dealing with:
> 
> *   Multiple intermediate nodes in a split
> 
> *   The thresholding issues of real-valued features.
> 
> This assignment **may be challenging**, so brace yourself :)
> 
> ## If you are doing the assignment with IPython Notebook
> 
> An IPython Notebook has been provided below to you for this assignment. This notebook contains the instructions, quiz questions and partially-completed code for you to use as well as some cells to test your code.
> 
> **Make sure that you are using the latest version of Turi Create.**
> 
> ## What you need to download
> 
> ### If you are using Turi Create:
> 
> *   Download the Lending club data In SFrame format:
> 
>  [ZIP File
> 
> lending-club-data.sframe
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/KVugjOI3Eemx8A5HK6Ls8g_4ae1e7ce863a4049b4ab5da425c6bd7a_lending-club-data.sframe.zip?Expires=1656115200&Signature=a1VBYfvZ~41lfYqQyTshRQBeM1TmrkPNaYvuUwElcbHCW~VzrRkuKYmZvUSOXj6HzwQ0gV9YqCQZ8sv2y7mMIparNAYL-ZYgCJizyz-1r~fLi36857w-nvr20J8LzxQyrXdY1Jdc56z68ULMzlDKvTOvb3ot85uv0x2e2VB7tIo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython Notebook:
> 
>  [ZIP File
> 
> CLA05-NB02.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/A__rCuI4Eem3eBKX1RzcIA_13cea6fbf4a442448ece9c9ffd04b5a6_CLA05-NB02.ipynb.zip?Expires=1656115200&Signature=aimuO~BiSWBcajFW82CGX~O6RvLLk2FQ40vE2ww4YE2~gTlM2MrzRrf3tQ3BVLNUbwoR4UWFfgeyi7dV6osLOotYEHeSeYDXw05rOVICZSAWJoWTwMgQxIHmpPBNkZ3pGP0Ax7vQa9nyjhdEQtx4sTGP~lHyXr6moyP4a5E3wUk_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Save both of these files in the same directory (where you are calling IPython notebook from) and unzip the data file.
> 
> *   Follow the instructions contained in the IPython notebook.
> 
> ### If you are not using Turi Create
> 
> *   If you are using SFrame, download the LendingClub dataset in SFrame format:
> 
>  [ZIP File
> 
> lending-club-data.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_35bdebdff61378878ea2247780005e52_lending-club-data.gl.zip?Expires=1656115200&Signature=K81gJdrTipG9IRREo4TtByL48uf82ev0g6RtxKuhzwowM~Es~ALNax0PHs8pefp4MI1idk-lQBlbnKxRDtwwnohRD~RnFwfIP2QM0NT0RJ-OpJQvzuvnFmmYPIxE8Kn-NciuPHma~W9mJpJoOziv8iKCN1AeLWdPRgTGZGaMifY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   If you are using a different package, download the LendingClub dataset in CSV format:
> 
>  [ZIP File
> 
> lending-club-data.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_c18ade74fb45f307917ac9c670944b84_lending-club-data.csv.zip?Expires=1656115200&Signature=Uqa4a9apkwPyWwoqAdYoiG6Jr848jVyw~-710VWQ~fSkc16VXFMYE~289LCta-Fj7hQmPx9AcbKBla~EbDoPbyJvD0~Z3HpS7iZu3t2qRZgd66x4AALbF7MYL-eWrGK1hJcxuNnSWA-L-RmPTNWV6iC2zfWTxkmt~LIJuZEdixQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> ## If you are using Turi Create and the companion IPython Notebook
> 
> Open the companion IPython notebook and follow the instructions in the notebook.
> 
> ## If you are using other tools
> 
> This section is designed for people using tools other than Turi Create. **You will not need any machine learning packages** since we will be implementing decision trees from scratch. **We highly suggest you use** [**SFrame**](https://github.com/turi-code/SFrame) **since it is open source.** In this part of the assignment, we describe general instructions, however we will tailor the instructions for SFrame.
> 
> *   If you choose to use SFrame, you should be able to follow the instructions in the next section and complete the assessment. **All code samples given here will be applicable to SFrame**.
> 
> *   You are free to experiment with any tool of your choice, but **some many not produce correct numbers for the quiz questions.**
> 
> ## If you are using [SFrame](https://github.com/turi-code/SFrame)
> 
> Make sure to download the companion IPython notebook:
> 
>  [ZIP File
> 
> module-5-decision-tree-assignment-2-blank.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_35bdebdff61378878ea2247780005e52_module-5-decision-tree-assignment-2-blank.ipynb.zip?Expires=1656115200&Signature=NHKmU1h579JdWvs5E-SPvmd2zzKgfytTdvR01RMUkPNqUGgsw1hwGDGmXpnek0JOk3J6gHDrm~osyCAtA0p8s7sKlsQVtbZA8h3jV6f8JXcu8stzKGtN1rqwO-O-YO0t7RGiXvGBTa0NuISHxWlpF1H9Smr5jwkEE58wxMyA0-M_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> You will be able to follow along exactly **if you replace the first two lines of code with these two lines:**
> 
>  `1
> 
> 2
> 
> 3
> 
> import sframe
> 
> loans = sframe.SFrame('lending-club-data.gl/')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_1 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_1.drop-target, .monaco-list.list_id_1 .monaco-list-rows.drop-target, .monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> After running this, **you can follow the rest of the IPython notebook and disregard the rest of this reading.**
> 
> **Note:** To install SFrame (without installing Turi Create), run
> 
>  `1
> 
> pip install sframe
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_2:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_2 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_2 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_2:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_2.drop-target, .monaco-list.list_id_2 .monaco-list-rows.drop-target, .monaco-list.list_id_2 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ## If you are NOT using SFrame
> 
> 1\. Load in the LendingClub dataset with the software of your choice.
> 
> 2\. Like the previous assignment, reassign the labels to have +1 for a safe loan, and -1 for a risky (bad) loan. You should have code analogous to
> 
>  `1
> 
> 2
> 
> loans['safe_loans'] = loans['bad_loans'].apply(lambda x : +1 if x==0 else -1)
> 
> loans = loans.remove_column('bad_loans')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 3\. Unlike the previous assignment, we will only be considering these four features:
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
> features = ['grade',              # grade of the loan
> 
>             'term',               # the term of the loan
> 
>             'home_ownership',     # home_ownership status: own, mortgage or rent
> 
>             'emp_length',         # number of years of employment
> 
>            ]
> 
> target = 'safe_loans'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_4:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_4 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_4 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_4:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_4.drop-target, .monaco-list.list_id_4 .monaco-list-rows.drop-target, .monaco-list.list_id_4 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Extract these feature columns from the dataset, and discard the rest of the feature columns.
> 
> ### Notes to people using other tools
> 
> **If you are using SFrame, proceed to the section "Subsample dataset to make sure classes are balanced".**
> 
> **If you are NOT using SFrame, download the list of indices for the training and test sets**:
> 
>  [ZIP File
> 
> module-5-assignment-2-train-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-5-assignment-2-train-idx.json.zip?Expires=1656115200&Signature=TKCkR-UKbutYOykbvfVxVgEq9EKvW0xqG5O7F7eIOlNGCy~2o-SLljX2UlCnnM6nwc8hQlkf-KSGlSjCK1F8w6UtKuxtGiLPqtpFK-3G4l9WpMHdy8jYCXytogKn7WCPJcedTxokkOiqMHmMLpc2BnlxY7MYq0A53Ox~Rjfg8j0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
>  [ZIP File
> 
> module-5-assignment-2-test-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-5-assignment-2-test-idx.json.zip?Expires=1656115200&Signature=fJuNnLySEKztx~Af5b0P1XmCHi8cSMKUsPVKzZKTVH526Z1eLEO0fm71WL57SjK8GYrX1ZT-HLFpDBBF1rMvb0qgGpQwnlLUqE9DPwYJA8zeUjzVyOdw~cXDPZc2z2NPKrSb8FGb-3Jw~DCApWu38eyVDAZAx6rR0LqqtwnFI7U_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> Then follow the following steps:
> 
> *   Apply one-hot encoding to **loans**. Your tool may have a function for one-hot encoding.
> 
> *   Load the JSON files into the lists **train_idx** and **test_idx**.
> 
> *   Perform train/validation split using **train_idx** and **test_idx**. In Pandas, for instance:
> 
>  `1
> 
> 2
> 
> train_data = loans.iloc[train_idx]
> 
> test_data = loans.iloc[test_idx]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_5:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_5 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_5 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_5:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_5.drop-target, .monaco-list.list_id_5 .monaco-list-rows.drop-target, .monaco-list.list_id_5 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> IMPORTANT: If you are using a programming language with 1-based indexing (e.g. R, Matlab), make sure to increment all indices by 1.
> 
> Note. Some elements in loans are included neither in **train_data** nor **test_data**. This is to perform sampling to achieve class balance.
> 
> Now proceed to the section "Decision tree implementation", skipping three sections below.
> 
> ### Subsample dataset to make sure classes are balanced
> 
> 4\. Just as we did in the previous assignment, we will undersample the larger class (safe loans) in order to balance out our dataset. This means we are throwing away many data points. You should have code analogous to
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> safe_loans_raw = loans[loans[target] == 1]
> 
> risky_loans_raw = loans[loans[target] == -1]
> 
> # Since there are less risky loans than safe loans, find the ratio of the sizes
> 
> # and use that percentage to undersample the safe loans.
> 
> percentage = len(risky_loans_raw)/float(len(safe_loans_raw))
> 
> safe_loans = safe_loans_raw.sample(percentage, seed = 1)
> 
> risky_loans = risky_loans_raw
> 
> loans_data = risky_loans.append(safe_loans)
> 
> print "Percentage of safe loans                 :", len(safe_loans) / float(len(loans_data))
> 
> print "Percentage of risky loans                :", len(risky_loans) / float(len(loans_data))
> 
> print "Total number of loans in our new dataset :", len(loans_data)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_6:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_6 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_6 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_6:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_6.drop-target, .monaco-list.list_id_6 .monaco-list-rows.drop-target, .monaco-list.list_id_6 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Note:** There are many approaches for dealing with imbalanced data, including some where we modify the learning algorithm. These approaches are beyond the scope of this course, but some of them are reviewed in this [paper](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=5128907&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F69%2F5173046%2F05128907.pdf%3Farnumber%3D5128907). For this assignment, we use the simplest possible approach, where we subsample the overly represented class to get a more balanced dataset. In general, and especially when the data is highly imbalanced, we recommend using more advanced methods.
> 
> ### Transform categorical data into binary features
> 
> In this assignment, we will implement **binary decision trees** (decision trees for binary features, a specific case of categorical variables taking on two values, e.g., true/false). Since all of our features are currently categorical features, we want to turn them into binary features.
> 
> For instance, the **home_ownership** feature represents the home ownership status of the loanee, which is either own, mortgage or rent. For example, if a data point has the feature
> 
>  `1
> 
>    {'home_ownership': 'RENT'}
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_7:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_7 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_7 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_7:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_7.drop-target, .monaco-list.list_id_7 .monaco-list-rows.drop-target, .monaco-list.list_id_7 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> we want to turn this into three features:
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
>  { 
> 
>    'home_ownership = OWN'      : 0, 
> 
>    'home_ownership = MORTGAGE' : 0, 
> 
>    'home_ownership = RENT'     : 1
> 
>  }
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_8:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_8 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_8 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_8:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_8.drop-target, .monaco-list.list_id_8 .monaco-list-rows.drop-target, .monaco-list.list_id_8 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 5\. This technique of turning categorical variables into binary variables is called one-hot encoding. Using the software of your choice, perform one-hot encoding on the four features described above. **You should now have 25 binary features.**
> 
> ### Train-test split
> 
> 6\. Split the data into a train test split with 80% of the data in the training set and 20% of the data in the test set. Call these datasets **train_data** and **test_data**, respectively. Using SFrame, this would look like:
> 
>  `1
> 
> train_data, test_data = loans_data.random_split(.8, seed=1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_9:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_9 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_9 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_9:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_9.drop-target, .monaco-list.list_id_9 .monaco-list-rows.drop-target, .monaco-list.list_id_9 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> (with **seed=1** to ensure people get the same results.)
> 
> ### Decision tree implementation
> 
> In this section, we will implement binary decision trees from scratch. There are several steps involved in building a decision tree. For that reason, we have split the entire assignment into several sections.
> 
> ### Function to count number of mistakes while predicting majority class
> 
> Recall from the lecture that prediction at an intermediate node works by predicting the **majority class** for all data points that belong to this node. Now, we will write a function that calculates the number of **misclassified examples** when predicting the **majority class**. This will be used to help determine which feature is the best to split on at a given node of the tree.
> 
> **Note**: Keep in mind that in order to compute the number of mistakes for a majority classifier, we only need the label (y values) of the data points in the node.
> 
> Steps to follow:
> 
> *   Step 1: Calculate the number of safe loans and risky loans.
> 
> *   Step 2: Since we are assuming majority class prediction, all the data points that are not in the majority class are considered mistakes.
> 
> *   Step 3: Return the number of mistakes.
> 
> 7\. Now, let us write the function _intermediate_node_num_mistakes_ which computes the number of misclassified examples of an intermediate node given the set of labels (y values) of the data points contained in the node. Your code should be analogous to
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
> 10
> 
> 11
> 
> def intermediate_node_num_mistakes(labels_in_node):
> 
>     # Corner case: If labels_in_node is empty, return 0
> 
>     if len(labels_in_node) == 0:
> 
>         return 0    
> 
>     # Count the number of 1's (safe loans)
> 
>     ## YOUR CODE HERE    
> 
>     # Count the number of -1's (risky loans)
> 
>     ## YOUR CODE HERE                
> 
>     # Return the number of mistakes that the majority classifier makes.
> 
>     ## YOUR CODE HERE    
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_10:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_10 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_10 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_10:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_10.drop-target, .monaco-list.list_id_10 .monaco-list-rows.drop-target, .monaco-list.list_id_10 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 8\. Because there are several steps in this assignment, we have introduced some stopping points where you can check your code and make sure it is correct before proceeding. To test your _intermediate_node_num_mistakes_ function, run the following code until you get a **Test passed!**, then you should proceed. Otherwise, you should spend some time figuring out where things went wrong. Again, remember that this code is specific to SFrame, but using your software of choice, you can construct similar tests.
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> 16
> 
> 17
> 
> 18
> 
> 19
> 
> 20
> 
> # Test case 1
> 
> example_labels = graphlab.SArray([-1, -1, 1, 1, 1])
> 
> if intermediate_node_num_mistakes(example_labels) == 2:
> 
>     print 'Test passed!'
> 
> else:
> 
>     print 'Test 1 failed... try again!'
> 
> # Test case 2
> 
> example_labels = graphlab.SArray([-1, -1, 1, 1, 1, 1, 1])
> 
> if intermediate_node_num_mistakes(example_labels) == 2:
> 
>     print 'Test passed!'
> 
> else:
> 
>     print 'Test 3 failed... try again!'
> 
> # Test case 3
> 
> example_labels = graphlab.SArray([-1, -1, -1, -1, -1, 1, 1])
> 
> if intermediate_node_num_mistakes(example_labels) == 2:
> 
>     print 'Test passed!'
> 
> else:
> 
>     print 'Test 3 failed... try again!'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_11:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_11 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_11 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_11:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_11.drop-target, .monaco-list.list_id_11 .monaco-list-rows.drop-target, .monaco-list.list_id_11 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Function to pick best feature to split on
> 
> The function _best_splitting_feature_ takes 3 arguments:
> 
> 1.  The data
> 
> 2.  The features to consider for splits (a list of strings of column names to consider for splits)
> 
> 3.  The name of the target/label column (string)
> 
> The function will loop through the list of possible features, and consider splitting on each of them. It will calculate the classification error of each split and return the feature that had the smallest classification error when split on.
> 
> Recall that the **classification error** is defined as follows:
> 
> classification error=# mistakes# total examples\mbox{classification error} = \dfrac{\mbox{# mistakes}}{\mbox{# total examples}}
> 
> 9\. Follow these steps to implement _best_splitting_feature_:
> 
> *   **Step 1:** Loop over each feature in the feature list
> 
> *   **Step 2:** Within the loop, split the data into two groups: one group where all of the data has feature value 0 or False (we will call this the **left** split), and one group where all of the data has feature value 1 or True (we will call this the **right** split). Make sure the **left** split corresponds with 0 and the **right** split corresponds with 1 to ensure your implementation fits with our implementation of the tree building process.
> 
> *   **Step 3:** Calculate the number of misclassified examples in both groups of data and use the above formula to compute the**classification error**.
> 
> *   **Step 4:** If the computed error is smaller than the best error found so far, store this **feature and its error**.
> 
> **Note:** Remember that since we are only dealing with binary features, we do not have to consider thresholds for real-valued features. This makes the implementation of this function much easier.
> 
> Your code should be analogous to
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> 16
> 
> 17
> 
> 18
> 
> 19
> 
> 20
> 
> 21
> 
> 22
> 
> 23
> 
> 24
> 
> 25
> 
> 26
> 
> 27
> 
> 28
> 
> 29
> 
> 30
> 
> 31
> 
> 32
> 
> 33
> 
> 34
> 
> 35
> 
> 36
> 
> 37
> 
> 38
> 
> 39
> 
> 40
> 
> def best_splitting_feature(data, features, target):
> 
>     target_values = data[target]
> 
>     best_feature = None # Keep track of the best feature 
> 
>     best_error = 10     # Keep track of the best error so far 
> 
>     # Note: Since error is always <= 1, we should intialize it with something larger than 1.
> 
>     # Convert to float to make sure error gets computed correctly.
> 
>     num_data_points = float(len(data))  
> 
>     # Loop through each feature to consider splitting on that feature
> 
>     for feature in features:
> 
>         # The left split will have all data points where the feature value is 0
> 
>         left_split = data[data[feature] == 0]
> 
>         # The right split will have all data points where the feature value is 1
> 
>         ## YOUR CODE HERE
> 
>         right_split =  
> 
>         # Calculate the number of misclassified examples in the left split.
> 
>         # Remember that we implemented a function for this! (It was called intermediate_node_num_mistakes)
> 
>         # YOUR CODE HERE
> 
>         left_mistakes =             
> 
>         # Calculate the number of misclassified examples in the right split.
> 
>         ## YOUR CODE HERE
> 
>         right_mistakes = 
> 
>         # Compute the classification error of this split.
> 
>         # Error = (# of mistakes (left) + # of mistakes (right)) / (# of data points)
> 
>         ## YOUR CODE HERE
> 
>         error = 
> 
>         # If this is the best error we have found so far, store the feature as best_feature and the error as best_error
> 
>         ## YOUR CODE HERE
> 
>         if error < best_error:
> 
>     return best_feature # Return the best feature we found
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_12:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_12 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_12 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_12:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_12.drop-target, .monaco-list.list_id_12 .monaco-list-rows.drop-target, .monaco-list.list_id_12 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Building the tree
> 
> With the above functions implemented correctly, we are now ready to build our decision tree. Each node in the decision tree is represented as a dictionary which contains the following keys and possible values:
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
> { 
> 
>    'is_leaf'            : True/False.
> 
>    'prediction'         : Prediction at the leaf node.
> 
>    'left'               : (dictionary corresponding to the left tree).
> 
>    'right'              : (dictionary corresponding to the right tree).
> 
>    'splitting_feature'  : The feature that this node splits on
> 
> }
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_13:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_13 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_13 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_13:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_13.drop-target, .monaco-list.list_id_13 .monaco-list-rows.drop-target, .monaco-list.list_id_13 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 10\. First, we will write a function that creates a leaf node given a set of target values. Your code should be analogous to
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> 16
> 
> 17
> 
> 18
> 
> 19
> 
> 20
> 
> def create_leaf(target_values):    
> 
>     # Create a leaf node
> 
>     leaf = {'splitting_feature' : None,
> 
>             'left' : None,
> 
>             'right' : None,
> 
>             'is_leaf':     }   ## YOUR CODE HERE 
> 
>     # Count the number of data points that are +1 and -1 in this node.
> 
>     num_ones = len(target_values[target_values == +1])
> 
>     num_minus_ones = len(target_values[target_values == -1])    
> 
>     # For the leaf node, set the prediction to be the majority class.
> 
>     # Store the predicted class (1 or -1) in leaf['prediction']
> 
>     if num_ones > num_minus_ones:
> 
>         leaf['prediction'] =          ## YOUR CODE HERE
> 
>     else:
> 
>         leaf['prediction'] =          ## YOUR CODE HERE        
> 
>     # Return the leaf node
> 
>     return leaf 
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_14:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_14 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_14 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_14:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_14.drop-target, .monaco-list.list_id_14 .monaco-list-rows.drop-target, .monaco-list.list_id_14 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> We have provided a function that learns the decision tree recursively and implements 3 stopping conditions:
> 
> 1.  **Stopping condition 1:** All data points in a node are from the same class.
> 
> 2.  **Stopping condition 2:** No more features to split on.
> 
> 3.  **Additional stopping condition:** In addition to the above two stopping conditions covered in lecture, in this assignment we will also consider a stopping condition based on the **max_depth** of the tree. By not letting the tree grow too deep, we will save computational effort in the learning process.
> 
> 11\. Now, we will provide a Python skeleton of the learning algorithm. Note that this code is not complete; it needs to be completed by you if you are using Python. Otherwise, your code should be analogous to
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> 16
> 
> 17
> 
> 18
> 
> 19
> 
> 20
> 
> 21
> 
> 22
> 
> 23
> 
> 24
> 
> 25
> 
> 26
> 
> 27
> 
> 28
> 
> 29
> 
> 30
> 
> 31
> 
> 32
> 
> 33
> 
> 34
> 
> 35
> 
> 36
> 
> 37
> 
> 38
> 
> 39
> 
> 40
> 
> def decision_tree_create(data, features, target, current_depth = 0, max_depth = 10):
> 
>     remaining_features = features[:] # Make a copy of the features.
> 
>     target_values = data[target]
> 
>     print "--------------------------------------------------------------------"
> 
>     print "Subtree, depth = %s (%s data points)." % (current_depth, len(target_values))
> 
>     # Stopping condition 1
> 
>     # (Check if there are mistakes at current node.
> 
>     # Recall you wrote a function intermediate_node_num_mistakes to compute this.)
> 
>     if  == 0:  ## YOUR CODE HERE
> 
>         print "Stopping condition 1 reached."     
> 
>         # If not mistakes at current node, make current node a leaf node
> 
>         return create_leaf(target_values)
> 
>     # Stopping condition 2 (check if there are remaining features to consider splitting on)
> 
>     if remaining_features == :   ## YOUR CODE HERE
> 
>         print "Stopping condition 2 reached."    
> 
>         # If there are no remaining features to consider, make current node a leaf node
> 
>         return create_leaf(target_values)    
> 
>     # Additional stopping condition (limit tree depth)
> 
>     if current_depth >= :  ## YOUR CODE HERE
> 
>         print "Reached maximum depth. Stopping for now."
> 
>         # If the max tree depth has been reached, make current node a leaf node
> 
>         return create_leaf(target_values)
> 
>     # Find the best splitting feature (recall the function best_splitting_feature implemented above)
> 
>     ## YOUR CODE HERE
> 
>     # Split on the best feature that we found. 
> 
>     left_split = data[data[splitting_feature] == 0]
> 
>     right_split =       ## YOUR CODE HERE
> 
>     remaining_features.remove(splitting_feature)
> 
>     print "Split on feature %s. (%s, %s)" % (\
> 
>                       splitting_feature, len(left_split), len(right_split))
> 
>     # Create a leaf node if the split is "perfect"
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_15:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_15 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_15 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_15:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_15.drop-target, .monaco-list.list_id_15 .monaco-list-rows.drop-target, .monaco-list.list_id_15 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Build the tree!
> 
> 12\. Train a tree model on the **train_data**. Limit the depth to 6 (**max_depth = 6**) to make sure the algorithm doesn't run for too long. Call this tree **my_decision_tree**. **Warning**: The tree may take 1-2 minutes to learn.
> 
> ### Making predictions with a decision tree
> 
> 13\. As discussed in the lecture, we can make predictions from the decision tree with a simple recursive function. Write a function called _classify_, which takes in a learned tree and a test point x to classify. Include an option annotate that describes the prediction path when set to True. Your code should be analogous to
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> def classify(tree, x, annotate = False):
> 
>        # if the node is a leaf node.
> 
>     if tree['is_leaf']:
> 
>         if annotate:
> 
>              print "At leaf, predicting %s" % tree['prediction']
> 
>         return tree['prediction']
> 
>      else:
> 
>         # split on feature.
> 
>         split_feature_value = x[tree['splitting_feature']]
> 
>         if annotate:
> 
>              print "Split on %s = %s" % (tree['splitting_feature'], split_feature_value)
> 
>         if split_feature_value == 0:
> 
>             return classify(tree['left'], x, annotate)
> 
>         else:
> 
>                ### YOUR CODE HERE
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 14\. Now, let's consider the first example of the test set and see what **my_decision_tree** model predicts for this data point.
> 
>  `1
> 
> 2
> 
> 3
> 
> print test_data[0]
> 
> print 'Predicted class: %s ' % classify(my_decision_tree, test_data[0])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 15\. Let's add some annotations to our prediction to see what the prediction path was that lead to this predicted class:
> 
>  `1
> 
> classify(my_decision_tree, test_data[0], annotate=True)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz question**: What was the feature that **my_decision_tree** first split on while making the prediction for test_data[0]?
> 
> **Quiz question**: What was the first feature that lead to a right split of test_data[0]?
> 
> **Quiz question**: What was the last feature split on before reaching a leaf node for test_data[0]?
> 
> ### Evaluating your decision tree
> 
> 16\. Now, we will write a function to evaluate a decision tree by computing the classification error of the tree on the given dataset. Write a function called _evaluate_classification_error_ that takes in as input:
> 
> 1.  tree (as described above)
> 
> 2.  data (a data frame of data points)
> 
> This function should return a prediction (class label) for each row in data using the decision tree. Your code should be analogous to
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
> def evaluate_classification_error(tree, data):
> 
>     # Apply the classify(tree, x) to each row in your data
> 
>     prediction = data.apply(lambda x: classify(tree, x))
> 
>     # Once you've made the predictions, calculate the classification error and return it
> 
>     ## YOUR CODE HERE
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 17\. Now, use this function to evaluate the classification error on the test set.
> 
>  `1
> 
> evaluate_classification_error(my_decision_tree, test_data)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question:** Rounded to 2nd decimal point, what is the classification error of **my_decision_tree** on the **test_data**?
> 
> ### Printing out a decision stump
> 
> 18\. As discussed in the lecture, we can print out a single decision stump (printing out the entire tree is left as an exercise to the curious reader). Here we provide Python code to visualize a decision stump. If you are using different software, make sure your code is analogous to:
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
> 10
> 
> 11
> 
> 12
> 
> 13
> 
> 14
> 
> 15
> 
> 16
> 
> 17
> 
> 18
> 
> def print_stump(tree, name = 'root'):
> 
>     split_name = tree['splitting_feature'] # split_name is something like 'term. 36 months'
> 
>     if split_name is None:
> 
>         print "(leaf, label: %s)" % tree['prediction']
> 
>         return None
> 
>     split_feature, split_value = split_name.split('.')
> 
>     print '                       %s' % name
> 
>     print '         |---------------|----------------|'
> 
>     print '         |                                |'
> 
>     print '         |                                |'
> 
>     print '         |                                |'
> 
>     print '  [{0} == 0]               [{0} == 1]    '.format(split_name)
> 
>     print '         |                                |'
> 
>     print '         |                                |'
> 
>     print '         |                                |'
> 
>     print '    (%s)                         (%s)' \
> 
>         % (('leaf, label: ' + str(tree['left']['prediction']) if tree['left']['is_leaf'] else 'subtree'),
> 
>            ('leaf, label: ' + str(tree['right']['prediction']) if tree['right']['is_leaf'] else 'subtree'))
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> 19\. Using this function, we can print out the root of our decision tree:
> 
>  `1
> 
> print_stump(my_decision_tree)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_22:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_22 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_22 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_22:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_22.drop-target, .monaco-list.list_id_22 .monaco-list-rows.drop-target, .monaco-list.list_id_22 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question:** What is the feature that is used for the split at the root node?
> 
> ### Exploring the intermediate left subtree
> 
> The tree is a recursive dictionary, so we do have access to all the nodes! We can use
> 
> *   my_decision_tree['left'] to go left
> 
> *   my_decision_tree['right'] to go right
> 
> 20\. We can print out the left subtree by running the code
> 
>  `1
> 
> print_stump(my_decision_tree['left'], my_decision_tree['splitting_feature'])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_23:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_23 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_23 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_23:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_23.drop-target, .monaco-list.list_id_23 .monaco-list-rows.drop-target, .monaco-list.list_id_23 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> We can similarly print out the left subtree of the left subtree of the root by running the code
> 
>  `1
> 
> print_stump(my_decision_tree['left']['left'], my_decision_tree['left']['splitting_feature'])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_24:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_24 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_24 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_24:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_24.drop-target, .monaco-list.list_id_24 .monaco-list-rows.drop-target, .monaco-list.list_id_24 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz question**: What is the path of the first 3 feature splits considered along the left-most branch of my_decision_tree?
> 
> **Quiz question**: What is the path of the first 3 feature splits considered along the right-most branch of my_decision_tree?
>
> -- https://www.coursera.org/learn/ml-classification/supplement/seWHJ/implementing-binary-decision-trees#main
