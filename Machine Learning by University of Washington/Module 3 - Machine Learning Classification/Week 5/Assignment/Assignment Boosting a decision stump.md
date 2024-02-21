# Boosting a decision stump
> 
> [Practice with Lab Sandbox](https://www.coursera.org/learn/ml-classification/lab-sandbox)
> 
> # Boosting a decision stump
> 
> In this homework you will implement your own boosting module.
> 
> **Brace yourselves**! This is going to be a fun and challenging assignment.
> 
> *   Use SFrames to do some feature engineering.
> 
> *   Train a boosted ensemble of decision-trees (gradient boosted trees) on the lending club dataset.
> 
> *   Predict whether a loan will default along with prediction probabilities (on a validation set).
> 
> *   Evaluate the trained model and compare it with a baseline.
> 
> *   Find the most positive and negative loans using the learned model.
> 
> *   Explore how the number of trees influences classification performance.
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
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/KVugjOI3Eemx8A5HK6Ls8g_4ae1e7ce863a4049b4ab5da425c6bd7a_lending-club-data.sframe.zip?Expires=1656288000&Signature=cgUGZohwJY0ay71TPmxrS6e4msz102EFvBx0AiHq0W8A6xcL-Ewvik56tgpi7vJRjOaCP2B8utsKaZUybgmcYN8ceTgygBOkA3gyF3HnP~zvx0zqb0nTUBH6-YsOYuveYnnFwz6HFAL27UyqMrpOf3CN-4ZJOEjqlaWjeckUWbQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython Notebook:
> 
>  [ZIP File
> 
> CLA08-NB02.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/SIyhqeI5EemJfgqR2HI2sA_201632dbff1e4b8dbe1e1d729da6ee27_CLA08-NB02.ipynb.zip?Expires=1656288000&Signature=XFv8Vb~QJU5-CXDCgQszCd3nfYLgudQ-l8iLJOGwH~TMZGr8YSQATR1dSKS6koYppDPdU7TSP3o3DlqmXT3oOPN7YAKT27J6hvjGjRidm7Kk5jAlTk1HIgjwyBmctJoe7lwyX74trpsv2n0EZDyslBk-XvGXTVKP118--jyCzTI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
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
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_35bdebdff61378878ea2247780005e52_lending-club-data.gl.zip?Expires=1656288000&Signature=YfnBXuM00XxP-poqi3PAgmtdbSJMhA-sydi~Hue4GLK2BQOznEdXcb-ODiGDOZ3Qquc4wbdLwS31jXmYjScKcggLo90XPi09xCVAxj62cSl5yvkL7seHFcmvWSRB3KERlJ78uxi3rIxD0w2O3il5KK7~bb2Qi9jc9ViI88WO4Bc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   If you are using a different package, download the LendingClub dataset in CSV format:
> 
>  [ZIP File
> 
> lending-club-data.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_c18ade74fb45f307917ac9c670944b84_lending-club-data.csv.zip?Expires=1656288000&Signature=Jr1V0hd~3snEvWepShtifuGeK01IiNjoRvXP74GxgAdbSwc0hxrofwj9y4f1eykPlS20LFkmqPsUdr0ml9eYVndxfdLLFwTLsgAsPo7iRPDkwzy7dQVozDx4H7pp1-dx-feYyVUrQ5a2fr51onuwJJYGlqZvJ5Jtc3aBlhRi2aU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
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
> module-8-boosting-assignment-2-blank.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_35bdebdff61378878ea2247780005e52_module-8-boosting-assignment-2-blank.ipynb.zip?Expires=1656288000&Signature=fJ1E27g2F2fRZW4tmXJMbr0uMj9EguTwvUOaREvHWPNkVuJslrt9FoFeyyAZ4AXymjkE28hGd0JDNYDBvOqGsUL0B4lS1KWTimD8HE0kWuTcRMZ1Qwkcq2orwU1ajql~TPZTKRk4e0eXh7HelGT7gVWXUgfcbqvr1W5Vq8HfPAs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> You will be able to follow along exactly **if you replace the first two lines of code with these two lines:**
> 
>  `1
> 
> 2
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
> ### Getting the data ready
> 
> We will be using a dataset from the [LendingClub](https://eventing.coursera.org/api/redirectStrict/sRCvyJuzchskIq6WjhmOFSFNKrQ6AhowESVXaBBj3NQeo-YA0abmp0KA1m-s6k_e4gTLn1iGsPn1zeEhZKKgTA.TqKzouAqnDBw3AViulrLFw.iGteQ--zSiz3aMbfkZEYfXYBYMyTyTb4yrsnIl3yVustmPO8DIE8Q4utkx6Nc-Rp5ZYwcGPPZRbZbyLkp4OejU6AQuSpvO3XG_RhV3TTZolJ-6zOiRnTvMKr8I6aZVe69pwpILQBTuj0AcnI5NYapoiwXEL7mHAkoBHNyJRcQfhgfWifZZEUFfgfvmlkZGcnKw6EquhbVZIVq8jkAwH3wpO6TnK-htQJXDVZhQQbjiebWzTlDiR_PDUkZdZWFed5R2Z0Kncl2-O3sPVrd0WzSO-YIUu1zdVOUR1yOCjhrLuUX6K6iK87l6E7XleosO6JXLSxzddZEo9dyU3jUCF0tIKWEtOlM2pu61UXDpviO-ZPHkWwm-5a9w37vFEMuQkjchMxSPQmt5GeLbViERQLHedvmEXhLD9uEny7nZE4x8J1XeNhXiVMn5Zfyg5UyoXOutF0Dcq0Pd_hh8ZV-LzQ7nmp1rTPniVqr9WPH8ZcfF1T_t-NdLheT7kk4FEYQKviAkvXicDgrGpqxUEWmMvpA-Osu_lTkCdr43gfPLMw4OkE61SauKL0t-vFmA0t1c1VJ6wiH0RaUy4mEdG19pEkT3mhKFPnzHaNDQZ6HAe42_hYtG-HgVkJybZEVDjsMmuHgTLQSqoDfrJNK9LTiKR-hmM7IUJr9W4mZE0qWzfIxqzoDiJHFk-9WP9Itr2gag0aj4WCJwCrSTM_08KyBPwRAJKdqcuNUdljsGTrU5BV2KlVAvMVJOE4__ALYZWPDdbXdzSJDhOvrFatsLUhiJ_tS6Fa6LLfOY8vLo7yVAufUsN0O3wmI1IQEbBeSh4z4-CFGk-7q3IKoBCdcvwaBBayPypZjRu6i1G0YUYA1-jkGpigp7DlBDq6SD14Uf_J2IkBzo-ayMAPe0px0QJd7ofsiUTidl8u3OX20fscXbhbmipXeXMNyC7os_BWwEmlIdg64rLfvhO6S6Sfv0bvhoe_fyHuzXGgqMwfu2crOr6wEtSXsWQ2xkpgalNvghK8bvfb8R7r3u-YNaDP1SIWM2mjj_8lagrsHym1fbDfX7hbqm5j5d5QIadVnbB0pcX-CSWgHUZ-Kz7O1qEuE-wJ-bN1U-fzIQbfcPyCUE4SUkf5y-E9Nq26s_iHD5S3Lv01wj0_AU1ssfClorFY0z7r6SrYHu4zFLaDHa_GShWnLUn_qWKUFpnvXqdMnD7KV2MBZJQQie6LCAff2TaQGHN3zD8KHv52jy4pQJLrjs5on-7q7p5-YuaukDgEpBJrUg62A9ERhNKNqdyWI0SNfGZ7qkIBGXfYOhKxgw7vxeIKLde00AeAUhvUa3zGnm94p62tlZ7Z0fLWqTn_4etXGtWqANL_bCPcI1ns1ZKBp4QQrYiZ992QD6xlyZQ6YCxzSBpkHwiqLHyCVZOqlyuvdKlmgzznZrhMDps2t9niyX22ScXxJUw).
> 
> **1.** Load the dataset into a data frame named **loans**.
> 
> **Extracting the target and the feature columns**
> 
> **2\.** We will now repeat some of the feature processing steps that we saw in the previous assignment:
> 
> First, we re-assign the target to have +1 as a safe (good) loan, and -1 as a risky (bad) loan.
> 
> Next, we select four categorical features:
> 
> *   grade of the loan
> 
> *   the length of the loan term
> 
> *   the home ownership status: own, mortgage, rent
> 
> *   number of years of employment.
> 
> Your code should be analogous to the following:
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
> features = ['grade',              # grade of the loan
> 
>             'term',               # the term of the loan
> 
>             'home_ownership',     # home ownership status: own, mortgage or rent
> 
>             'emp_length',         # number of years of employment
> 
>            ]
> 
> loans['safe_loans'] = loans['bad_loans'].apply(lambda x : +1 if x==0 else -1)
> 
> loans.remove_column('bad_loans')
> 
> target = 'safe_loans'
> 
> loans = loans[features + [target]]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Notes to people using other tools
> 
> **If you are using SFrame, proceed to the section "Subsample dataset to make sure classes are balanced".**
> 
> **If you are NOT using SFrame, download the list of indices for the training and test sets**:
> 
>  [ZIP File
> 
> module-8-assignment-2-train-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-8-assignment-2-train-idx.json.zip?Expires=1656288000&Signature=XjcZrjcHeA-eKZcgnuDz3igTOjYVSi-TJQ0FoMnVDmu~UHtELoX~S8t~NQLSO2PiiGNxcJ-Iu0-P6jGqnrLv3KdYto1c6mDSYaFS863z2CoUAZMIC~dVdcdPfYT-s4uy-WAIVGU94T8zYMb2rZO0KvWWilQPxn9Q7F~OL5iyUoA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
>  [ZIP File
> 
> module-8-assignment-2-test-idx.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_1ccb9ec834e6f4b9afb46f4f5ab56402_module-8-assignment-2-test-idx.json.zip?Expires=1656288000&Signature=fQTclq~WBOHNmjRQrYckXyWxFIqVFiwF8~Rhza2s2rgjYkVrjYXVKxbi9KovjnJe9focbbQOxddcGWgmMKvGq2TuyMPR~AeAvZJIgeFKGvjys7-XlJa5O9WmiHSGbsZnCOwt~KvE2jw73XWIHX5mmqP~wnNTCJBIDZWq05~kOpA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> Then follow the following steps:
> 
> *   Apply one-hot encoding to **loans**. Your tool may have a function for one-hot encoding. Alternatively, see #7 for implementation hints.
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
> .monaco-list.list_id_4:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_4 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_4 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_4:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_4.drop-target, .monaco-list.list_id_4 .monaco-list-rows.drop-target, .monaco-list.list_id_4 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> IMPORTANT: If you are using a programming language with 1-based indexing (e.g. R, Matlab), make sure to increment all indices by 1.
> 
> Note. Some elements in loans are included neither in **train_data** nor **test_data**. This is to perform sampling to achieve class balance.
> 
> Now proceed to the section "Weighted decision trees", skipping three sections below.
> 
> **Subsample dataset to make sure classes are balanced**
> 
> **3\.** Just as we did in the previous assignment, we will undersample the larger class (safe loans) in order to balance out our dataset. This means we are throwing away many data points. We use seed=1 so everyone gets the same results. Your code should be analogous to the following:
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
> safe_loans_raw = loans[loans[target] == 1]
> 
> risky_loans_raw = loans[loans[target] == -1]
> 
> # Undersample the safe loans.
> 
> percentage = len(risky_loans_raw)/float(len(safe_loans_raw))
> 
> risky_loans = risky_loans_raw
> 
> safe_loans = safe_loans_raw.sample(percentage, seed=1)
> 
> loans_data = risky_loans_raw.append(safe_loans)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_5:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_5 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_5 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_5:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_5.drop-target, .monaco-list.list_id_5 .monaco-list-rows.drop-target, .monaco-list.list_id_5 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Note:** There are many approaches for dealing with imbalanced data, including some where we modify the learning algorithm. These approaches are beyond the scope of this course, but some of them are reviewed in this [paper](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=5128907&url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F69%2F5173046%2F05128907.pdf%3Farnumber%3D5128907). For this assignment, we use the simplest possible approach, where we subsample the overly represented class to get a more balanced dataset. In general, and especially when the data is highly imbalanced, we recommend using more advanced methods.
> 
> **Transform categorical data into binary features**
> 
> **4\.** Just like the previous assignment, we will implement **binary decision trees**. Since all of our features are currently categorical features, we want to turn them into binary features. Here is a reminder of what one-hot encoding is.
> 
> For instance, the **home_ownership** feature represents the home ownership status of the loanee, which is either own, mortgage or rent. For example, if a data point has the feature
> 
>  `1
> 
>    {'home_ownership': 'RENT'}
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_6:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_6 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_6 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_6:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_6.drop-target, .monaco-list.list_id_6 .monaco-list-rows.drop-target, .monaco-list.list_id_6 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
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
> .monaco-list.list_id_7:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_7 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_7 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_7:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_7.drop-target, .monaco-list.list_id_7 .monaco-list-rows.drop-target, .monaco-list.list_id_7 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **5.** This technique of turning categorical variables into binary variables is called one-hot encoding. Using the software of your choice, perform one-hot encoding on the four features described above. **You should now have 25 binary features.**
> 
> ### Train-test split
> 
> **6.** We split the data into training and test sets with 80% of the data in the training set and 20% of the data in the test set. We use seed=1 so that everyone gets the same result. Using SFrame, this would look like:
> 
>  `1
> 
> train_data, test_data = loans_data.random_split(.8, seed=1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_8:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_8 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_8 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_8:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_8.drop-target, .monaco-list.list_id_8 .monaco-list-rows.drop-target, .monaco-list.list_id_8 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> (with **seed=1** to ensure people get the same results.)
> 
> Call the training and test sets **train_data** and **test_data**, respectively.
> 
> ### Weighted decision trees
> 
> **7.** Let's modify our decision tree code from Module 5 to support weighting of individual data points.
> 
> **Weighted error definition**
> 
> **8\.** Consider a model with N data points with:
> 
> *   Predictions y^1,…,y^n\hat{y}_1, \ldots, \hat{y}_n
> 
> *   Target y1,…,yny_1, \ldots, y_n
> 
> *   Data point weights α1,…,αn\alpha_1, \ldots, \alpha_n
> 
> Then the **weighted error** is defined by:
> 
> E(α,y^)=∑i=1nαi×1[yi≠yi^]∑i=1nαi\mathrm{E}(\mathbf{\alpha}, \mathbf{\hat{y}}) = \dfrac{\sum_{i=1}^{n} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}]}{\sum_{i=1}^{n} \alpha_i}E(α,y^​)=∑i=1n​αi​∑i=1n​αi​×1[yi​​=yi​^​]​
> 
> where 1[yi≠y^i]\mathbf{1}[ y_i \neq \hat{y}_i ]1[yi​​=y^​i​] is an indicator function that is set to 1 if yi≠y^iy_i \neq \hat{y}_iyi​​=y^​i​.
> 
> **Write a function to compute weight of mistakes**
> 
> **9\.** Write a function that calculates the weight of mistakes for making the "weighted-majority" predictions for a dataset. The function accepts two inputs:
> 
> *   **labels_in_node**: y1,…,yny_1, \ldots, y_n
> 
> *   **data_weights**: Data point weights α1,…,αn\alpha_1, \ldots, \alpha_n
> 
> We are interested in computing the (total) weight of mistakes, i.e.
> 
> WM(α,y^)=∑i=1nαi×1[yi≠yi^]\displaystyle \mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}}) = \sum_{i=1}^{n} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}]WM(α,y^​)=i=1∑n​αi​×1[yi​​=yi​^​]
> 
> This quantity is analogous to the number of mistakes, except that each mistake now carries different weight. It is related to the weighted error in the following way:
> 
> E(α,y^)=WM(α,y^)∑i=1nαi\displaystyle \mathrm{E}(\mathbf{\alpha}, \mathbf{\hat{y}}) = \frac{\mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}})}{\sum_{i=1}^{n} \alpha_i}E(α,y^​)=∑i=1n​αi​WM(α,y^​)​
> 
> The function **intermediate_node_weighted_mistakes** should first compute two weights:
> 
> *   WM−1\mathrm{WM}_{-1}: weight of mistakes when all predictions are y^i=−1\hat{y}_i = -1 i.e. WM(α,−1)\mathrm{WM}(\mathbf{\alpha}, \mathbf{-1})
> 
> *   WM+1\mathrm{WM}_{+1}: weight of mistakes when all predictions are y^i=+1\hat{y}_i = +1 i.e. WM(α,+1)\mathrm{WM}(\mathbf{\alpha}, \mathbf{+1})
> 
> where **−1** and **+1** are vectors where all values are -1 and +1 respectively.
> 
> After computing WM−1\mathrm{WM}_{-1}WM−1​ and WM+1\mathrm{WM}_{+1}WM+1​, the function **intermediate_node_weighted_mistakes** should return the lower of the two weights of mistakes, along with the class associated with that weight. The function should be analogous to the following Python function:
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
> def intermediate_node_weighted_mistakes(labels_in_node, data_weights):
> 
>     # Sum the weights of all entries with label +1
> 
>     total_weight_positive = sum(data_weights[labels_in_node == +1])
> 
>     # Weight of mistakes for predicting all -1's is equal to the sum above
> 
>     ### YOUR CODE HERE
> 
>     weighted_mistakes_all_negative = ...
> 
>     # Sum the weights of all entries with label -1
> 
>     ### YOUR CODE HERE
> 
>     total_weight_negative = ...
> 
>     # Weight of mistakes for predicting all +1's is equal to the sum above
> 
>     ### YOUR CODE HERE
> 
>     weighted_mistakes_all_positive = ...
> 
>     # Return the tuple (weight, class_label) representing the lower of the two weights
> 
>     #    class_label should be an integer of value +1 or -1.
> 
>     # If the two weights are identical, return (weighted_mistakes_all_positive,+1)
> 
>     ### YOUR CODE HERE
> 
>     ...
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_9:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_9 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_9 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_9:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_9.drop-target, .monaco-list.list_id_9 .monaco-list-rows.drop-target, .monaco-list.list_id_9 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **10\.** Recall that the **classification error** is defined as follows:
> 
> classification error=# mistakes# all data points\mbox{classification error} = \frac{\mbox{# mistakes}}{\mbox{# all data points}}
> 
> **Quiz Question:** If we set the weights α=1\alpha =1α=1 for all data points, how is the weight of mistakes WM(α,y^)\mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}})WM(α,y^​) related to the classification error?
> 
> **Function to pick best feature to split on**
> 
> **11\.** We continue modifying our decision tree code from the earlier assignment to incorporate weighting of individual data points. The next step is to pick the best feature to split on.
> 
> The **best_splitting_feature** function is similar to the one from the earlier assignment with two minor modifications:
> 
> *   The function **best_splitting_feature** should now accept an extra parameter data_weights to take account of weights of data points.
> 
> *   Instead of computing the number of mistakes in the left and right side of the split, we compute the weight of mistakes for both sides, add up the two weights, and divide it by the total weight of the data.
> 
> Your function should be analogous to the following Python function:
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
> # If the data is identical in each feature, this function should return None
> 
> def best_splitting_feature(data, features, target, data_weights):
> 
>     # These variables will keep track of the best feature and the corresponding error
> 
>     best_feature = None
> 
>     best_error = float('+inf') 
> 
>     num_points = float(len(data))
> 
>     # Loop through each feature to consider splitting on that feature
> 
>     for feature in features:
> 
>         # The left split will have all data points where the feature value is 0
> 
>         # The right split will have all data points where the feature value is 1
> 
>         left_split = data[data[feature] == 0]
> 
>         right_split = data[data[feature] == 1]
> 
>         # Apply the same filtering to data_weights to create left_data_weights, right_data_weights
> 
>         ## YOUR CODE HERE
> 
>         left_data_weights = ...
> 
>         right_data_weights = ...
> 
>         # DIFFERENT HERE
> 
>         # Calculate the weight of mistakes for left and right sides
> 
>         ## YOUR CODE HERE
> 
>         left_weighted_mistakes, left_class = ...
> 
>         right_weighted_mistakes, right_class = ...
> 
>         # DIFFERENT HERE
> 
>         # Compute weighted error by computing
> 
>         #  ( [weight of mistakes (left)] + [weight of mistakes (right)] ) / [total weight of all data points]
> 
>         ## YOUR CODE HERE
> 
>         error = ...
> 
>         # If this is the best error we have found so far, store the feature and the error
> 
>         if error < best_error:
> 
>             best_feature = feature
> 
>             best_error = error
> 
>     # Return the best feature we found
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_10:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_10 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_10 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_10:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_10.drop-target, .monaco-list.list_id_10 .monaco-list-rows.drop-target, .monaco-list.list_id_10 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Very Optional**. Relationship between weighted error and weight of mistakes
> 
> By definition, the weighted error is the weight of mistakes divided by the weight of all data points, so
> 
> E(α,y^)=∑i=1nαi×1[yi≠yi^]∑i=1nαi=WM(α,y^)∑i=1nαi.\mathrm{E}(\mathbf{\alpha}, \mathbf{\hat{y}}) = \dfrac{\sum_{i=1}^{n} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}]}{\sum_{i=1}^{n} \alpha_i} = \dfrac{\mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}})}{\sum_{i=1}^{n} \alpha_i}.E(α,y^​)=∑i=1n​αi​∑i=1n​αi​×1[yi​​=yi​^​]​=∑i=1n​αi​WM(α,y^​)​.
> 
> In the code above, we obtain E(α,y^)\mathrm{E}(\mathbf{\alpha}, \mathbf{\hat{y}})E(α,y^​) from the two weights of mistakes from both sides, WM(αleft,y^left)\mathrm{WM}(\mathbf{\alpha}_{\mathrm{left}}, \mathbf{\hat{y}}_{\mathrm{left}})WM(αleft​,y^​left​) and WM(αright,y^right)\mathrm{WM}(\mathbf{\alpha}_{\mathrm{right}}, \mathbf{\hat{y}}_{\mathrm{right}})WM(αright​,y^​right​). First, notice that the overall weight of mistakes WM(α,y^)\mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}})WM(α,y^​) can be broken into two weights of mistakes over either side of the split:
> 
> WM(α,y^)=∑i=1nαi×1[yi≠yi^]=∑leftαi×1[yi≠yi^]+∑rightαi×1[yi≠yi^]=WM(αleft,y^left)+WM(αright,y^right)\displaystyle \begin{align} \mathrm{WM}(\mathbf{\alpha}, \mathbf{\hat{y}}) &= \sum_{i=1}^{n} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}] \\ &= \sum_{\mathrm{left}} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}] + \sum_{\mathrm{right}} \alpha_i \times \mathbf{1}[y_i \neq \hat{y_i}]\\ &= \mathrm{WM}(\mathbf{\alpha}_{\mathrm{left}}, \mathbf{\hat{y}}_{\mathrm{left}}) + \mathrm{WM}(\mathbf{\alpha}_{\mathrm{right}}, \mathbf{\hat{y}}_{\mathrm{right}}) \end{align}
> 
> We then divide through by the total weight of all data points to obtain E(α,y^)\mathrm{E}(\alpha, \mathbf{\hat{y}})E(α,y^​):
> 
> E(α,y^)=WM(αleft,y^left)+WM(αright,y^right)∑i=1nαi\mathrm{E}(\mathbf{\alpha}, \mathbf{\hat{y}}) = \dfrac{\mathrm{WM}(\mathbf{\alpha}_{\mathrm{left}}, \mathbf{\hat{y}}_{\mathrm{left}}) + \mathrm{WM}(\mathbf{\alpha}_{\mathrm{right}}, \mathbf{\hat{y}}_{\mathrm{right}})}{\sum_{i=1}^{n} \alpha_i}E(α,y^​)=∑i=1n​αi​WM(αleft​,y^​left​)+WM(αright​,y^​right​)​
> 
> ### Building the tree
> 
> **12.** With the above functions implemented correctly, we are now ready to build our decision tree. Recall from the previous assignments that each node in the decision tree is represented as a dictionary which contains the following keys:
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
>    'features_remaining' : List of features that are posible splits.
> 
> }
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_11:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_11 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_11 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_11:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_11.drop-target, .monaco-list.list_id_11 .monaco-list-rows.drop-target, .monaco-list.list_id_11 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let us start with a function that creates a leaf node given a set of target values. The **create_leaf** function should be analogous to the following cell:
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
> def create_leaf(target_values, data_weights):
> 
>     # Create a leaf node
> 
>     leaf = {'splitting_feature' : None,
> 
>             'is_leaf': True}
> 
>     # Computed weight of mistakes.
> 
>     # Store the predicted class (1 or -1) in leaf['prediction']
> 
>     weighted_error, best_class = intermediate_node_weighted_mistakes(target_values, data_weights)
> 
>     leaf['prediction'] = ... ## YOUR CODE HERE
> 
>     return leaf
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_12:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_12 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_12 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_12:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_12.drop-target, .monaco-list.list_id_12 .monaco-list-rows.drop-target, .monaco-list.list_id_12 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **13.** Now write a function that learns a weighted decision tree recursively and implements 3 stopping conditions:
> 
> *   All data points in a node are from the same class.
> 
> *   No more features to split on.
> 
> *   Stop growing the tree when the tree depth reaches **max_depth**.
> 
> Since there are many steps involved, we provide you with a Python skeleton, along with explanatory comments.
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
> def weighted_decision_tree_create(data, features, target, data_weights, current_depth = 1, max_depth = 10):
> 
>     remaining_features = features[:] # Make a copy of the features.
> 
>     target_values = data[target]
> 
>     print "--------------------------------------------------------------------"
> 
>     print "Subtree, depth = %s (%s data points)." % (current_depth, len(target_values))
> 
>     # Stopping condition 1. Error is 0.
> 
>     if intermediate_node_weighted_mistakes(target_values, data_weights)[0] <= 1e-15:
> 
>         print "Stopping condition 1 reached."                
> 
>         return create_leaf(target_values, data_weights)
> 
>     # Stopping condition 2. No more features.
> 
>     if remaining_features == []:
> 
>         print "Stopping condition 2 reached."                
> 
>         return create_leaf(target_values, data_weights)    
> 
>     # Additional stopping condition (limit tree depth)
> 
>     if current_depth > max_depth:
> 
>         print "Reached maximum depth. Stopping for now."
> 
>         return create_leaf(target_values, data_weights)
> 
>     # If all the datapoints are the same, splitting_feature will be None. Create a leaf
> 
>     splitting_feature = best_splitting_feature(data, features, target, data_weights)
> 
>     remaining_features.remove(splitting_feature)
> 
>     left_split = data[data[splitting_feature] == 0]
> 
>     right_split = data[data[splitting_feature] == 1]
> 
>     left_data_weights = data_weights[data[splitting_feature] == 0]
> 
>     right_data_weights = data_weights[data[splitting_feature] == 1]
> 
>     print "Split on feature %s. (%s, %s)" % (\
> 
>               splitting_feature, len(left_split), len(right_split))
> 
>     # Create a leaf node if the split is "perfect"
> 
>     if len(left_split) == len(data):
> 
>         print "Creating leaf node."
> 
>         return create_leaf(left_split[target], data_weights)
> 
>     if len(right_split) == len(data):
> 
>         print "Creating leaf node."
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_13:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_13 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_13 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_13:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_13.drop-target, .monaco-list.list_id_13 .monaco-list-rows.drop-target, .monaco-list.list_id_13 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **14\.** Finally, write a recursive function to count the nodes in your tree. The function should be analogous to
> 
>  `1
> 
> 2
> 
> 3
> 
> 4
> 
> def count_nodes(tree):
> 
>     if tree['is_leaf']:
> 
>         return 1
> 
>     return 1 + count_nodes(tree['left']) + count_nodes(tree['right'])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_14:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_14 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_14 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_14:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_14.drop-target, .monaco-list.list_id_14 .monaco-list-rows.drop-target, .monaco-list.list_id_14 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Making predictions with a weighted decision tree
> 
> **15.** To make a single prediction, we must start at the root and traverse down the decision tree in recursive fashion. Write a function **classify** that makes a single prediction. It should be analogous to the following:
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
>     # If the node is a leaf node.
> 
>     if tree['is_leaf']:
> 
>         if annotate: 
> 
>             print "At leaf, predicting %s" % tree['prediction']
> 
>         return tree['prediction'] 
> 
>     else:
> 
>         # Split on feature.
> 
>         split_feature_value = x[tree['splitting_feature']]
> 
>         if annotate: 
> 
>             print "Split on %s = %s" % (tree['splitting_feature'], split_feature_value)
> 
>         if split_feature_value == 0:
> 
>             return classify(tree['left'], x, annotate)
> 
>         else:
> 
>             return classify(tree['right'], x, annotate)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_15:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_15 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_15 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_15:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_15.drop-target, .monaco-list.list_id_15 .monaco-list-rows.drop-target, .monaco-list.list_id_15 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Evaluating the tree
> 
> **16.** Create a function called **evaluate_classification_error**. It takes in as input:
> 
> *   **tree** (as described above)
> 
> *   **data** (an data frame)
> 
> The function does not change because of adding data point weights. It is analogous to this Python function:
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
> def evaluate_classification_error(tree, data):
> 
>     # Apply the classify(tree, x) to each row in your data
> 
>     prediction = data.apply(lambda x: classify(tree, x))
> 
>     # Once you've made the predictions, calculate the classification error
> 
>     return (prediction != data[target]).sum() / float(len(data))
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Example: Training a weighted decision tree
> 
> **17\.** To build intuition on how weighted data points affect the tree being built, consider the following:
> 
> Suppose we only care about making good predictions for the **first 10 and last 10 items** in train_data, we assign weights:
> 
> *   1 to the last 10 items
> 
> *   1 to the first 10 items
> 
> *   and 0 to the rest.
> 
> Let us fit a weighted decision tree with max_depth = 2\. Then compute the classification error on the **subset_20**, i.e. the subset of data points whose weight is 1 (namely the first and last 10 data points).
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
> # Assign weights
> 
> example_data_weights = graphlab.SArray([1.] * 10 + [0.]*(len(train_data) - 20) + [1.] * 10)
> 
> # Train a weighted decision tree model.
> 
> small_data_decision_tree_subset_20 = weighted_decision_tree_create(train_data, features, target,
> 
>                          example_data_weights, max_depth=2)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **18\.** Now, we will compute the classification error on the **subset_20**, i.e. the subset of data points whose weight is 1 (namely the first and last 10 data points).
> 
>  `1
> 
> evaluate_classification_error(small_data_decision_tree_subset_20, train_data)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The model small_data_decision_tree_subset_20 performs **a lot** better on subset_20 than on train_data.
> 
> So, what does this mean?
> 
> *   The points with higher weights are the ones that are more important during the training process of the weighted decision tree.
> 
> *   The points with zero weights are basically ignored during training.
> 
> **Quiz Question**: Will you get the same model as **small_data_decision_tree_subset_20** if you trained a decision tree with only the 20 data points with non-zero weights from the set of points in **subset_20**?
> 
> ### Implementing your own Adaboost (on decision stumps)
> 
> **19\.** Now that we have a weighted decision tree working, it takes only a bit of work to implement Adaboost. For the sake of simplicity, let us stick with decision tree stumps by training trees with max_depth=1\.
> 
> Recall from the lecture the procedure for Adaboost:
> 
> * Start with unweighted data with αj=1\alpha_j = 1αj​=1
> 
> * For t=1,...,T:
> 
> *   Learn ft(x)f_t(x) with data weights αj\alpha_j
> 
> *   Compute coefficient w^t\hat{w}_t:
> 
> w^t=12ln(1−E(α,y^)E(α,y^))\hat{w}_t = \dfrac{1}{2}\ln{\left(\dfrac{1- \mbox{E}(\mathbf{\alpha}, \mathbf{\hat{y}})}{\mbox{E}(\mathbf{\alpha}, \mathbf{\hat{y}})}\right)}
> 
> *   Re-compute weights αj\alpha_j:
> 
> αj←{αjexp⁡(−w^t) if ft(xj)=yjαjexp⁡(w^t) if ft(xj)≠yj\alpha_j \gets
> 
> {αjexp(−w^t)αjexp(w^t) if ft(xj)=yj if ft(xj)≠yj
> 
> \begin{cases} \alpha_j \exp{(-\hat{w}_t)} & \text{ if }f_t(x_j) = y_j\\\alpha_j \exp{(\hat{w}_t)} & \text{ if }f_t(x_j) \neq y_j \end{cases}αj​←{αj​exp(−w^t​)αj​exp(w^t​)​ if ft​(xj​)=yj​ if ft​(xj​)​=yj​​
> 
> *   Normalize weights αj\alpha_j:
> 
> αj←αj∑i=1Nαi\alpha_j \gets \dfrac{\alpha_j}{\sum_{i=1}^{N}{\alpha_i}}αj​←∑i=1N​αi​αj​​
> 
> Now write your own Adaboost function. The function accepts 4 parameters:
> 
> *   data: a data frame with binary features
> 
> *   features: list of feature names
> 
> *   target: name of target column
> 
> *   num_tree_stumps: number of tree stumps to train for the ensemble
> 
> The function should return the list of tree stumps, along with the list of corresponding tree stump weights.
> 
> It should be analogous to the following code skeleton:
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
> from math import log
> 
> from math import exp
> 
> def adaboost_with_tree_stumps(data, features, target, num_tree_stumps):
> 
>     # start with unweighted data
> 
>     alpha = graphlab.SArray([1.]*len(data))
> 
>     weights = []
> 
>     tree_stumps = []
> 
>     target_values = data[target]
> 
>     for t in xrange(num_tree_stumps):
> 
>         print '====================================================='
> 
>         print 'Adaboost Iteration %d' % t
> 
>         print '====================================================='        
> 
>         # Learn a weighted decision tree stump. Use max_depth=1
> 
>         tree_stump = weighted_decision_tree_create(data, features, target, data_weights=alpha, max_depth=1)
> 
>         tree_stumps.append(tree_stump)
> 
>         # Make predictions
> 
>         predictions = data.apply(lambda x: classify(tree_stump, x))
> 
>         # Produce a Boolean array indicating whether
> 
>         # each data point was correctly classified
> 
>         is_correct = predictions == target_values
> 
>         is_wrong   = predictions != target_values
> 
>         # Compute weighted error
> 
>         # YOUR CODE HERE
> 
>         weighted_error = ...
> 
>         # Compute model coefficient using weighted error
> 
>         # YOUR CODE HERE
> 
>         weight = ...
> 
>         weights.append(weight)
> 
>         # Adjust weights on data point
> 
>         adjustment = is_correct.apply(lambda is_correct : exp(-weight) if is_correct else exp(weight))
> 
>         # Scale alpha by multiplying by adjustment
> 
>         # Then normalize data points weights
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Reminders**
> 
> *   Stump weights (w^\mathbf{\hat{w}}) and data point weights (α\mathbf{\alpha}) are two different concepts.
> 
> *   Stump weights (w^\mathbf{\hat{w}}) tell you how important each stump is while making predictions with the entire boosted ensemble.
> 
> *   Data point weights (α\mathbf{\alpha}) tell you how important each data point is while training a decision stump.
> 
> ### Training a boosted ensemble of 10 stumps
> 
> **20\.** Let us train an ensemble of 10 decision tree stumps with Adaboost. We run the **adaboost_with_tree_stumps** function with the following parameters:
> 
> *   train_data
> 
> *   features
> 
> *   target
> 
> *   num_tree_stumps = 10
> 
> Making predictions
> 
> **21\.** Recall from the lecture that in order to make predictions, we use the following formula:
> 
> y^=sign(∑t=1Tw^tft(x))\displaystyle \hat{y} = \mathrm{sign}\left(\sum_{t=1}^T \hat{w}_t f_t(x)\right)y^​=sign(t=1∑T​w^t​ft​(x))
> 
> Do the following things in a new function **predict_adaboost**:
> 
> *   Compute the predictions ft(x)f_t(x) using the tt-th decision tree
> 
> *   Compute w^tft(x)\hat{w}_t f_t(x) by multiplying the stump_weights with the predictions ft(x)f_t(x) from the decision trees
> 
> *   Sum the weighted predictions over each stump in the ensemble.
> 
> In the end, your **predict_adaboost** should be analogous to this Python function:
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
> def predict_adaboost(stump_weights, tree_stumps, data):
> 
>     scores = graphlab.SArray([0.]*len(data))
> 
>     for i, tree_stump in enumerate(tree_stumps):
> 
>         predictions = data.apply(lambda x: classify(tree_stump, x))
> 
>         # Accumulate predictions on scaores array
> 
>         # YOUR CODE HERE
> 
>         ...
> 
>     return scores.apply(lambda score : +1 if score > 0 else -1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Use this function to answer the following question:
> 
> **Quiz Question:** Are the weights monotonically decreasing, monotonically increasing, or neither?
> 
> **Reminder**: Stump weights (w^\mathbf{\hat{w}}w^) tell you how important each stump is while making predictions with the entire boosted ensemble.
> 
> ### Performance plots
> 
> **How does accuracy change with adding stumps to the ensemble?**
> 
> **22\.** We will now train an ensemble with:
> 
> *   train_data
> 
> *   features
> 
> *   target
> 
> *   num_tree_stumps = 30
> 
> Once we are done with this, we will then do the following:
> 
> *   Compute the classification error at the end of each iteration.
> 
> *   Plot a curve of classification error vs iteration.
> 
> First, let's train the model.
> 
> **Computing training error at the end of each iteration**
> 
> **23\.** Let us compute the classification error on the **train_data** and see how it is reduced as trees are added.
> 
> For n = 1 to 30, do the following:
> 
> *   Make predictions on **train_data** using tree stumps 0, ..., n-1.
> 
> *   Compute classification error for the predictions
> 
> *   Record the classification error for that n.
> 
> The loop should be analogous to the following:
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
> error_all = []
> 
> for n in xrange(1, 31):
> 
>     predictions = predict_adaboost(stump_weights[:n], tree_stumps[:n], train_data)
> 
>     error = 1.0 - graphlab.evaluation.accuracy(train_data[target], predictions)
> 
>     error_all.append(error)
> 
>     print "Iteration %s, training error = %s" % (n, error_all[n-1])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Visualizing training error vs number of iterations**
> 
> **24\.** Let us generate the plot of classification error as a function of the number of iterations. Use the classification error values recorded in #23.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/dYhG2947EeWOVQ68c1xy2w_f068916ce9f47cdbe68ae3a5193e1280_download.png?expiry=1656288000000&hmac=9FXHzpo8Dc0ls4jW-Qu1V5ZyOybweu5CGfPkrn5kTz0)
> 
> For inspiration, we provide you with matplotlib plotting code.
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
> plt.rcParams['figure.figsize'] = 7, 5
> 
> plt.plot(range(1,31), error_all, '-', linewidth=4.0, label='Training error')
> 
> plt.title('Performance of Adaboost ensemble')
> 
> plt.xlabel('# of iterations')
> 
> plt.ylabel('Classification error')
> 
> plt.legend(loc='best', prop={'size':15})
> 
> plt.rcParams.update({'font.size': 16})
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_22:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_22 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_22 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_22:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_22.drop-target, .monaco-list.list_id_22 .monaco-list-rows.drop-target, .monaco-list.list_id_22 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**: Which of the following best describes a **general trend in accuracy** as we add more and more components? Answer based on the 30 components learned so far.
> 
> *   Training error goes down monotonically, i.e. the training error reduces with each iteration but never increases.
> 
> *   Training error goes down in general, with some ups and downs in the middle.
> 
> *   Training error goes up in general, with some ups and downs in the middle.
> 
> *   Training error goes down in the beginning, achieves the best error, and then goes up sharply.
> 
> *   None of the above
> 
> ### Evaluation on the test data
> 
> **25\.** Performing well on the training data is cheating, so lets make sure it works on the test_data as well. Here, we will compute the classification error on the test_data at the end of each iteration.
> 
> For n = 1 to 30, do the following:
> 
> *   Make predictions on **test_data** using tree stumps 0, ..., n-1.
> 
> *   Compute classification error for the predictions
> 
> *   Record the classification error for that n.
> 
> ### Visualize both the training and test errors
> 
> **26.** Let us plot the training & test error with the number of iterations.
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/OhOFvt48EeWBDQ73-3lhaw_c8d35d6a442015dc00ea3570cc0c8508_download2.png?expiry=1656288000000&hmac=n4qiceCt6YpV9CbQLGPHY_pGDo6qnF6af5cMTQV4lC4)
> 
> Again, for inspiration, we provide you with matplotlib code.
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
> plt.rcParams['figure.figsize'] = 7, 5
> 
> plt.plot(range(1,31), error_all, '-', linewidth=4.0, label='Training error')
> 
> plt.plot(range(1,31), test_error_all, '-', linewidth=4.0, label='Test error')
> 
> plt.title('Performance of Adaboost ensemble')
> 
> plt.xlabel('# of iterations')
> 
> plt.ylabel('Classification error')
> 
> plt.rcParams.update({'font.size': 16})
> 
> plt.legend(loc='best', prop={'size':15})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_23:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_23 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_23 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_23:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_23.drop-target, .monaco-list.list_id_23 .monaco-list-rows.drop-target, .monaco-list.list_id_23 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question:** From this plot (with 30 trees), is there massive overfitting as the # of iterations increases?
>
> -- https://www.coursera.org/learn/ml-classification/supplement/3TYwk/boosting-a-decision-stump#main
