# Modeling text data with a hierarchy of clusters
> 
> **Hierarchical clustering** refers to a class of clustering methods that seek to build a **hierarchy** of clusters, in which some clusters contain others. In this assignment, we will explore a top-down approach, recursively bipartitioning the data using k-means.
> 
> ## If you are using Turi Create
> 
> An IPython Notebook has been provided below to you for this assignment. This notebook contains the instructions, quiz questions and partially-completed code for you to use as well as some cells to test your code.
> 
> *   Download the Wikipedia people dataset in SFrame format:
> 
>  [ZIP File
> 
> people_wiki.sframe
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5zBDt4bEemhxxJUtZcQoA_7fb43aab245846f09a8c48977883f0b6_people_wiki.sframe.zip?Expires=1657929600&Signature=Ok7RNrwAYuCyFcYrS38y7NEyzfN96MqFMNW9Lp1JPlSZqeugvyLOS5-I1Wu9yKXx4M5mV4uSQ4F9pF3TR3lmra-r-BKnHaqk3YJae5jUAWAPshR0SC4uFm-pLLXmmMDG84c2dsDPa3OpiaYiimEVMp6RlNQao2ivVmACxMq59bU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython notebook:
> 
>  [ZIP File
> 
> CLU06-NB01.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/EZW10-I8EemJfgqR2HI2sA_97cfb8979d704bf299ddc0b287ba68a6_CLU06-NB01.ipynb.zip?Expires=1657929600&Signature=VnFzdnwhU5NWsfoPH4~qIMAy~bL0zxYS2iSIZFSqJdRbXvOrvsOzQ~eXpVeNrmtWj0zPID2XEs0q1jLNJ33UWRMg41Yp2oeVNIHpyw-prtBFMFGlQw~oSkEGNZDzVsA2~l1f4-IBRd1WhTvV5sSevfHmaixwT9rt4Xs8oDF0Mqw_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download a collection of helper functions:
> 
>  [ZIP File
> 
> em_utilities.py
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/DCphrd4eEemzYQ60aJAwVA_fc87f6033fa34a2ab644e47ef86539cc_em_utilities.py.zip?Expires=1657929600&Signature=gXpB0EGRbVoDuJjqEeTAjVWmjBYVfJ~-LQPdNR02EU8h9OSDUSndGofcq5RkdSC2pR7OxZL3RlTVpipj358YWxjg4u7mMmeJfBp7JkbRay6YKtCuaeN2ds1ZAy9wZinpsujnlt5Lb1CLikvou9T0ctZm8YY~9vLtCk4mD9IT1vQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Save the files in the same directory (where you are calling IPython notebook from) and unzip the data file and model file.
> 
> **Open the companion IPython notebook and follow the instructions in the notebook. The instructions below do not apply to users of Turi Create.**
> 
> ## If you are not using Turi Create
> 
> It is possible to complete this assignment without using Turi Create. The instructions below are geared towards Python users, but you are free to adapt them to your specific environment.
> 
> **Disclaimer**. We have tested the assessment using the standard Python installation (with access to scikit-learn). However, the assessment may not be compatible with other tools (e.g. Matlab, R).
> 
> ### Download the dataset
> 
> *   Download the Wikipedia people dataset in SFrame format
> 
>  [ZIP File
> 
> people_wiki.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_a20552cf806c54b71b3b87cb593b9968_people_wiki.gl.zip?Expires=1657929600&Signature=KgSYu1KUOf1sOf92Ib671ldMfiQ49MyMNgHSwaB27qUygLAYG8w3WmTiSKw7Ulw9aPMDdSr4tSflPyUzCsWh-buuBxlO7FqX6Cz1kJ2JH7rjxig8uIDF6v2FzP3X8795H6E7XGvZotxtEapwYVp9fAIGhyNSnso~Chs2KtleeWk_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> people_wiki.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_167fc84b78dc145609e919983b475aaa_people_wiki.csv.zip?Expires=1657929600&Signature=hdFTCbmgTP-vXJKE0XsM6WF4CV9lWTlGJthP-TQWTx63clRjpOwhGRpMbb5MdqqHrzItTjAmgrha3UBheCyaNiGlTGogKGguLTVq3U7ajJftkD~1IP7MbKJc369yNV2sTYZDeKCF6NRCAO9KUtTLKq5JihPb3K0icqRQt9hmpkY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the mapping between words and integer indices:
> 
>  [ZIP File
> 
> people_wiki_map_index_to_word.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_96eadbec4d43a0b0870dde27d0652fb2_people_wiki_map_index_to_word.gl.zip?Expires=1657929600&Signature=L6zwvmXeTng3SJSk7-PMEr9YjcxXxD4~2cDgwGBHmY39hIH6bTFByjPgp-ceVCEbYJWgyuVNIFxMgJ6Ttif493glbQ1jJdnMU78acnDsFOEz14DOArnWd99cYTYv5ngSS4Ps7YaB2IdI077KJsZvZORM3v7njnVm5O5JBbQyuKs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> people_wiki_map_index_to_word.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_96eadbec4d43a0b0870dde27d0652fb2_people_wiki_map_index_to_word.json.zip?Expires=1657929600&Signature=AEvfC5GqHoWXa-T8O6zuT4e2eS8nljWUOVFcYJV4h8uk41BKuZMBOxIFVdyDhnq1F6VUMNPs4K7m5MGf0a7eMTgaS7cfN0bJxfdoKCV5OoCpYZajJ4PfrBrj~qUCHjQmn7OCXyZ672rxFHCyd4YvmpGV5z154UogpesnGF8CSvE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the pre-processed set of TF-IDF scores:
> 
>  [ZIP File
> 
> people_wiki_tf_idf.npz
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_395a4cfb2299d1655f1ef6bf6cc4f71b_people_wiki_tf_idf.npz.zip?Expires=1657929600&Signature=U3nciWRVSJi7NXxiaM7LlQuD3pIqB7KMbfIg3Y33rp7J9DEdgkkyyxRgnMUpqtRNDGzkvUzPLsIr3j9TCW~eKGu5wx-K7jW10I7E4~9t5VbGHQ9P8lG1n4t8qLE8p1n6qEYocJkKsAtI7x~68~IkEZ6EC39ONz4~S0NvQ~X8EoM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> ### Import packages
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
> import sframe                                     # see below for install instruction
> 
> import matplotlib.pyplot as plt
> 
> import numpy as np
> 
> from scipy.sparse import csr_matrix
> 
> from sklearn.cluster import KMeans                # we'll be using scikit-learn's KMeans for this assignment
> 
> from sklearn.metrics import pairwise_distances
> 
> from sklearn.preprocessing import normalize
> 
> %matplotlib inline
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_1 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_1 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_1.drop-target, .monaco-list.list_id_1 .monaco-list-rows.drop-target, .monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **About SFrame**. SFrame is a dataframe library Turi has released free-of-charge. Its source code is available [here](https://github.com/turi-code/SFrame). You may install SFrame via pip:
> 
>  `1
> 
> pip install --upgrade sframe
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_2:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_2:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_2 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_2 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_2 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_2:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_2.drop-target, .monaco-list.list_id_2 .monaco-list-rows.drop-target, .monaco-list.list_id_2 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Load in the dataset
> 
>  `1
> 
> wiki = sframe.SFrame('people_wiki.gl/')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> As in the previous assignment, we extract the TF-IDF vector of each document.
> 
> For your convenience, we extracted the TF-IDF vectors from the dataset. The vectors are packaged in a sparse matrix, where the i-th row gives the TF-IDF vectors for the i-th document. Each column corresponds to a unique word appearing in the dataset.
> 
> To load in the TF-IDF vectors, run
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
> def load_sparse_csr(filename):
> 
>     loader = np.load(filename)
> 
>     data = loader['data']
> 
>     indices = loader['indices']
> 
>     indptr = loader['indptr']
> 
>     shape = loader['shape']
> 
>     return csr_matrix( (data, indices, indptr), shape)
> 
> tf_idf = load_sparse_csr('people_wiki_tf_idf.npz')
> 
> map_index_to_word = sframe.SFrame('people_wiki_map_index_to_word.gl/')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_4:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_4 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_4 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_4:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_4.drop-target, .monaco-list.list_id_4 .monaco-list-rows.drop-target, .monaco-list.list_id_4 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> To be consistent with the k-means assignment, let's normalize all vectors to have unit norm.
> 
>  `1
> 
> tf_idf = normalize(tf_idf)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_5:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_5 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_5 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_5:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_5.drop-target, .monaco-list.list_id_5 .monaco-list-rows.drop-target, .monaco-list.list_id_5 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> _(Optional) Extracting TF-IDF vectors yourself_. We provide the pre-computed TF-IDF vectors to minimize potential compatibility issues. You are free to experiment with other tools to compute the TF-IDF vectors yourself. A good place to start is [sklearn.TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). Note. Due to variations in [tokenization](https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis)) and other factors, your TF-IDF vectors may differ from the ones we provide. For the purpose the assessment, we ask you to use the vectors from people_wiki_tf_idf.npz.
> 
> ### Bipartition the Wikipedia dataset using k-means
> 
> Recall our workflow for clustering text data with k-means:
> 
> 1.  Load the dataframe containing a dataset, such as the Wikipedia text dataset.
> 
> 2.  Extract the data matrix from the dataframe.
> 
> 3.  Run k-means on the data matrix with some value of k.
> 
> 4.  Visualize the clustering results using the centroids, cluster assignments, and the original dataframe. We keep the original dataframe around because the data matrix does not keep auxiliary information (in the case of the text dataset, the title of each article).
> 
> Let us modify the workflow to perform bipartitioning:
> 
> 1.  Load the dataframe containing a dataset, such as the Wikipedia text dataset.
> 
> 2.  Extract the data matrix from the dataframe.
> 
> 3.  Run k-means on the data matrix with k=2.
> 
> 4.  Divide the data matrix into two parts using the cluster assignments.
> 
> 5.  Divide the dataframe into two parts, again using the cluster assignments. This step is necessary to allow for visualization.
> 
> 6.  Visualize the bipartition of data.
> 
> We'd like to be able to repeat Steps 3-6 multiple times to produce a **hierarchy** of clusters such as the following:
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
>                       (root)
> 
>                          |
> 
>             +------------+-------------+
> 
>             |                          |
> 
>          Cluster                    Cluster
> 
>      +------+-----+             +------+-----+
> 
>      |            |             |            |
> 
>    Cluster     Cluster       Cluster      Cluster
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_6:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_6 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_6 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_6:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_6.drop-target, .monaco-list.list_id_6 .monaco-list-rows.drop-target, .monaco-list.list_id_6 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Each **parent cluster** is bipartitioned to produce two **child clusters**. At the very top is the **root cluster**, which consists of the entire dataset.
> 
> Now we write a wrapper function to bipartition a given cluster using k-means. There are three variables that together comprise the cluster:
> 
> *   dataframe: a subset of the original dataframe that correspond to member rows of the cluster
> 
> *   matrix: same set of rows, stored in sparse matrix format
> 
> *   centroid: the centroid of the cluster (not applicable for the root cluster)
> 
> Rather than passing around the three variables separately, we package them into a Python dictionary. The wrapper function takes a single dictionary (representing a parent cluster) and returns two dictionaries (representing the child clusters).
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
> def bipartition(cluster, maxiter=400, num_runs=4, seed=None):
> 
>     '''cluster: should be a dictionary containing the following keys
> 
>                 * dataframe: original dataframe
> 
>                 * matrix:    same data, in matrix format
> 
>                 * centroid:  centroid for this particular cluster'''
> 
>     data_matrix = cluster['matrix']
> 
>     dataframe   = cluster['dataframe']
> 
>     # Run k-means on the data matrix with k=2. We use scikit-learn here to simplify workflow.
> 
>     kmeans_model = KMeans(n_clusters=2, max_iter=maxiter, n_init=num_runs, random_state=seed, n_jobs=1)    
> 
>     kmeans_model.fit(data_matrix)
> 
>     centroids, cluster_assignment = kmeans_model.cluster_centers_, kmeans_model.labels_
> 
>     # Divide the data matrix into two parts using the cluster assignments.
> 
>     data_matrix_left_child, data_matrix_right_child = data_matrix[cluster_assignment==0], \
> 
>                                                       data_matrix[cluster_assignment==1]
> 
>     # Divide the dataframe into two parts, again using the cluster assignments.
> 
>     cluster_assignment_sa = sframe.SArray(cluster_assignment) # minor format conversion
> 
>     dataframe_left_child, dataframe_right_child     = dataframe[cluster_assignment_sa==0], \
> 
>                                                       dataframe[cluster_assignment_sa==1]
> 
>     # Package relevant variables for the child clusters
> 
>     cluster_left_child  = {'matrix': data_matrix_left_child,
> 
>                            'dataframe': dataframe_left_child,
> 
>                            'centroid': centroids[0]}
> 
>     cluster_right_child = {'matrix': data_matrix_right_child,
> 
>                            'dataframe': dataframe_right_child,
> 
>                            'centroid': centroids[1]}
> 
>     return (cluster_left_child, cluster_right_child)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_7:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_7 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_7 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_7:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_7.drop-target, .monaco-list.list_id_7 .monaco-list-rows.drop-target, .monaco-list.list_id_7 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The following cell performs bipartitioning of the Wikipedia dataset. Allow 20-60 seconds to finish.
> 
> Note. For the purpose of the assignment, we set an explicit seed (seed=1) to produce identical outputs for every run. In pratical applications, you might want to use different random seeds for all runs.
> 
>  `1
> 
> 2
> 
> wiki_data = {'matrix': tf_idf, 'dataframe': wiki} # no 'centroid' for the root cluster
> 
> left_child, right_child = bipartition(wiki_data, maxiter=100, num_runs=6, seed=1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_8:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_8 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_8 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_8:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_8.drop-target, .monaco-list.list_id_8 .monaco-list-rows.drop-target, .monaco-list.list_id_8 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's examine the contents of one of the two clusters, which we call the left_child, referring to the tree visualization above.
> 
>  `1
> 
> 2
> 
> print left_child
> 
> print right_child
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_9:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_9 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_9 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_9:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_9.drop-target, .monaco-list.list_id_9 .monaco-list-rows.drop-target, .monaco-list.list_id_9 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Visualize the bipartition
> 
> We provide you with a modified version of the visualization function from the k-means assignment. For each cluster, we print the top 5 words with highest TF-IDF weights in the centroid and display excerpts for the 8 nearest neighbors of the centroid.
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
> def display_single_tf_idf_cluster(cluster, map_index_to_word):
> 
>     '''map_index_to_word: SFrame specifying the mapping betweeen words and column indices'''
> 
>     wiki_subset   = cluster['dataframe']
> 
>     tf_idf_subset = cluster['matrix']
> 
>     centroid      = cluster['centroid']
> 
>     # Print top 5 words with largest TF-IDF weights in the cluster
> 
>     idx = centroid.argsort()[::-1]
> 
>     for i in xrange(5):
> 
>         print('{0:s}:{1:.3f}'.format(map_index_to_word['category'][idx[i]], centroid[idx[i]])),
> 
>     print('')
> 
>     # Compute distances from the centroid to all data points in the cluster.
> 
>     distances = pairwise_distances(tf_idf_subset, [centroid], metric='euclidean').flatten()
> 
>     # compute nearest neighbors of the centroid within the cluster.
> 
>     nearest_neighbors = distances.argsort()
> 
>     # For 8 nearest neighbors, print the title as well as first 180 characters of text.
> 
>     # Wrap the text at 80-character mark.
> 
>     for i in xrange(8):
> 
>         text = ' '.join(wiki_subset[nearest_neighbors[i]]['text'].split(None, 25)[0:25])
> 
>         print('* {0:50s} {1:.5f}\n  {2:s}\n  {3:s}'.format(wiki_subset[nearest_neighbors[i]]['name'],
> 
>               distances[nearest_neighbors[i]], text[:90], text[90:180] if len(text) > 90 else ''))
> 
>     print('')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_10:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_10 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_10 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_10:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_10.drop-target, .monaco-list.list_id_10 .monaco-list-rows.drop-target, .monaco-list.list_id_10 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's visualize the two child clusters:
> 
>  `1
> 
> 2
> 
> display_single_tf_idf_cluster(left_child, map_index_to_word)
> 
> display_single_tf_idf_cluster(right_child, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_11:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_11 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_11 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_11:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_11.drop-target, .monaco-list.list_id_11 .monaco-list-rows.drop-target, .monaco-list.list_id_11 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The left cluster consists of athletes, whereas the right cluster consists of non-athletes. So far, we have a single-level hierarchy consisting of two clusters, as follows:
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
>                                            Wikipedia
> 
>                                                +
> 
>                                                |
> 
>                     +--------------------------+--------------------+
> 
>                     |                                               |
> 
>                     +                                               +
> 
>                  Athletes                                      Non-athletes
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_12:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_12 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_12 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_12:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_12.drop-target, .monaco-list.list_id_12 .monaco-list-rows.drop-target, .monaco-list.list_id_12 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Is this hierarchy good enough? **When building a hierarchy of clusters, we must keep our particular application in mind.** For instance, we might want to build a **directory** for Wikipedia articles. A good directory would let you quickly narrow down your search to a small set of related articles. The categories of athletes and non-athletes are too general to facilitate efficient search. For this reason, we decide to build another level into our hierarchy of clusters with the goal of getting more specific cluster structure at the lower level. To that end, we subdivide both the athletes and non-athletes clusters.
> 
> ### Perform recursive bipartitioning
> 
> **Cluster of athletes.** To help identify the clusters we've built so far, let's give them easy-to-read aliases:
> 
>  `1
> 
> 2
> 
> athletes = left_child
> 
> non_athletes = right_child
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_13:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_13 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_13 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_13:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_13.drop-target, .monaco-list.list_id_13 .monaco-list-rows.drop-target, .monaco-list.list_id_13 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Using the bipartition function, we produce two child clusters of the athlete cluster:
> 
>  `1
> 
> 2
> 
> # Bipartition the cluster of athletes
> 
> left_child_athletes, right_child_athletes = bipartition(athletes, maxiter=100, num_runs=6, seed=1)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_14:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_14 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_14 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_14:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_14.drop-target, .monaco-list.list_id_14 .monaco-list-rows.drop-target, .monaco-list.list_id_14 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The left child cluster mainly consists of baseball players:
> 
>  `1
> 
> display_single_tf_idf_cluster(left_child_athletes, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_15:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_15 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_15 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_15:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_15.drop-target, .monaco-list.list_id_15 .monaco-list-rows.drop-target, .monaco-list.list_id_15 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> On the other hand, the right child cluster is a mix of players in association football, Austrailian rules football and ice hockey:
> 
>  `1
> 
> display_single_tf_idf_cluster(right_child_athletes, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Our hierarchy of clusters now looks like this:
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
>                                            Wikipedia
> 
>                                                +
> 
>                                                |
> 
>                     +--------------------------+--------------------+
> 
>                     |                                               |
> 
>                     +                                               +
> 
>                  Athletes                                      Non-athletes
> 
>                     +
> 
>                     |
> 
>         +-----------+--------+
> 
>         |                    |
> 
>         |            association football/
> 
>         +          Austrailian rules football/
> 
>      baseball             ice hockey
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Should we keep subdividing the clusters? If so, which cluster should we subdivide? To answer this question, we again think about our application. Since we organize our directory by topics, it would be nice to have topics that are about as coarse as each other. For instance, if one cluster is about baseball, we expect some other clusters about football, basketball, volleyball, and so forth. That is, **we would like to achieve similar level of granularity for all clusters.**
> 
> Notice that the right child cluster is more coarse than the left child cluster. The right cluster posseses a greater variety of topics than the left (ice hockey/association football/Australian football vs. baseball). So the right child cluster should be subdivided further to produce finer child clusters.
> 
> Let's give the clusters aliases as well:
> 
>  `1
> 
> 2
> 
> baseball            = left_child_athletes
> 
> ice_hockey_football = right_child_athletes
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Cluster of ice hockey players and football players.** In answering the following quiz question, take a look at the topics represented in the top documents (those closest to the centroid), as well as the list of words with highest TF-IDF weights.
> 
> Let us bipartition the cluster of ice hockey and football players.
> 
>  `1
> 
> 2
> 
> 3
> 
> left_child_ihs, right_child_ihs = bipartition(ice_hockey_football, maxiter=100, num_runs=6, seed=1)
> 
> display_single_tf_idf_cluster(left_child_ihs, map_index_to_word)
> 
> display_single_tf_idf_cluster(right_child_ihs, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**. Which diagram best describes the hierarchy right after splitting the **ice_hockey_football** cluster? Refer to the quiz form for the diagrams.
> 
> **Caution**. The granularity criteria is an imperfect heuristic and must be taken with a grain of salt. It takes a lot of manual intervention to obtain a good hierarchy of clusters.
> 
> *   **If a cluster is highly mixed, the top articles and words may not convey the full picture of the cluster.** Thus, we may be misled if we judge the purity of clusters solely by their top documents and words.
> 
> *   **Many interesting topics are hidden somewhere inside the clusters but do not appear in the visualization.** We may need to subdivide further to discover new topics. For instance, subdividing the ice_hockey_football cluster led to the appearance of golf.
> 
> **Cluster of non-athletes**. Now let us subdivide the cluster of non-athletes.
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
> # Bipartition the cluster of non-athletes
> 
> left_child_non_athletes, right_child_non_athletes = bipartition(non_athletes, maxiter=100, num_runs=6, seed=1)
> 
> display_single_tf_idf_cluster(left_child_non_athletes, map_index_to_word)
> 
> display_single_tf_idf_cluster(right_child_non_athletes, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Neither of the clusters show clear topics, apart from the genders. Let us divide them further.
> 
>  `1
> 
> 2
> 
> male_non_athletes = left_child_non_athletes
> 
> female_non_athletes = right_child_non_athletes
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**. Let us bipartition the clusters **male_non_athletes** and **female_non_athletes**. Which diagram best describes the resulting hierarchy of clusters for the non-athletes? Refer to the quiz for the diagrams.
> 
> **Note**. Use maxiter=100, num_runs=6, seed=1 for consistency of output.
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/57vnY/modeling-text-data-with-a-hierarchy-of-clusters#main
