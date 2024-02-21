# Clustering text data with k-means
> 
> In this assignment you will
> 
> *   Cluster Wikipedia documents using k-means
> 
> *   Explore the role of random initialization on the quality of the clustering
> 
> *   Explore how results differ after changing the number of clusters
> 
> *   Evaluate clustering, both quantitatively and qualitatively
> 
> When properly executed, clustering uncovers valuable insights from a set of unlabeled documents.
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
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5zBDt4bEemhxxJUtZcQoA_7fb43aab245846f09a8c48977883f0b6_people_wiki.sframe.zip?Expires=1657238400&Signature=C70528pvDDnYanxbpnPCzNqFslQP7WAawvF3EL36W~61HaVaJ6zRMfQd7CufXiURvJXcRMw4MdSovUn5oLOqhHPiDKU7cz5z-mcj9W3KuoTLaPVjke75FZVlZJEp5ADMxG9d3O7z-aOXyEJlp-jioYEbe0uJBlItAfGomELiI0k_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython notebook:
> 
>  [ZIP File
> 
> CLU03-NB01.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/EXaVHuI8EemELQpo9cj5Ig_5b411e6336c04a338442b785006b3598_CLU03-NB01.ipynb.zip?Expires=1657238400&Signature=Y3PPlAR95Ubg0Kms5LwVFlbncsIXUvpKsJzw7i9y2RcAawNnoTfYmjAtISHW-luDN8QvkIdZVkK6ddx2ewj4cRV9Rzi8vO33snmZ24chfSwsT~L-~EN39wT7W2KuPA42hgAzXuWCpaT4E0jYxLcSaW3xLPOeITIz~1TbbZjDb0g_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Save all the files in the same directory (where you are calling IPython notebook from) and unzip the data file.
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
> *   Download the Wikipedia people dataset in SFrame format:
> 
>  [ZIP File
> 
> people_wiki.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_a20552cf806c54b71b3b87cb593b9968_people_wiki.gl.zip?Expires=1657238400&Signature=LDOFqBobop72wED6gkrZAqLkDqlaGvcLCbmGO1cEjRBM5G7WgbgCfLOVJyftQ7E4MVHLBtEcBSz1epmUDi8aAFs2SKoWaspoRiTC~6-3wOStI0b0kWXBajYlqSQuqlNfUldVSfKbLdaO~S7tiaU8SQnatqL5HIoyGDuaPV9a~Gs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> people_wiki.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_167fc84b78dc145609e919983b475aaa_people_wiki.csv.zip?Expires=1657238400&Signature=Dv9KIUiULpu-iJ5HrMSya3--TZ1xF2nid~5yeSjuzcPD-nWVd00NQCmdtBO6SMyhQZtYCu1uozwPKbecJ8vAnUyuZEVD5c~eVUC3XWzCAJkN79ENRmAGIeHiEMEtdstWiDrqMZ97ZE2ITfloDO6Ejq-MGSrC2STqN9XltThENMU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the mapping between words and integer indices:
> 
>  [ZIP File
> 
> people_wiki_map_index_to_word.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_96eadbec4d43a0b0870dde27d0652fb2_people_wiki_map_index_to_word.gl.zip?Expires=1657238400&Signature=Upt6sEPag4mXQqtjoVX3Bhq~fdfwKL2DHi4j8E5pPKr6HAnK05gXV30UQqRAb65iyiECF537opZmgbCrjPW7fYudPFGLxoqR8OBUmTyPTATqwjqXXgRLYXNtIbBY2sgAeLJTNXyV6E91ZOJYIDkJb-~D2MImEIZTuWEm12PH03g_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> people_wiki_map_index_to_word.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_96eadbec4d43a0b0870dde27d0652fb2_people_wiki_map_index_to_word.json.zip?Expires=1657238400&Signature=lgWZMt9GMN3mpU6JplFXKOEcU6Xx28iffQzFiKaZKyZhZyRnbCl1rY3SSoPcIepCs65sCEiwskEQlAXyF8ykc~FMzmqFFgIW19EaAuzDHkHgub-SS0Ln0Zymy1e~omOB4j3sTTyKWOzRyxZibo8EOw5SEb81cOONyH9IdckiPv0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the pre-processed set of TF-IDF scores:
> 
>  [ZIP File
> 
> people_wiki_tf_idf.npz
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_395a4cfb2299d1655f1ef6bf6cc4f71b_people_wiki_tf_idf.npz.zip?Expires=1657238400&Signature=hEStGhYp7fQmD7Wzu7Rxvu-vl3-N2BHRCvHEbV~mnsBz4cSLhWax0CnG2Zup7YcOqMp0~v-gxFOvPaamNoF8eioyICIF01CeL2zmH8S8ZNYTrHA2va8-kbU6PWgcTvCq2RWJSfO9xMXzFApGS6-8jgWIMx2GT6hhe53aPLGcSUM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the NumPy array containing pre-computed list of clusters:
> 
>  [ZIP File
> 
> kmeans-arrays.npz
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_a20552cf806c54b71b3b87cb593b9968_kmeans-arrays.npz.zip?Expires=1657238400&Signature=B6kwAvci-ASHeNw8oT0MBRr-d1crQ1VIZvlTPEoQJdgurRnFG-xMPNsTpxU9ukHWzV-WVzk~ofhIhk3QMKrUOkYkGY2PbdbmmAWhh2qP33HggvtNHMUW76p4aaq7S1sANTU7I8dYMgzY1F-94M-04yfXELHddHbzUklw-2TOY8g_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
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
> 9
> 
> import sframe                                                  # see below for install instruction
> 
> import matplotlib.pyplot as plt                                # plotting
> 
> import numpy as np                                             # dense matrices
> 
> from scipy.sparse import csr_matrix                            # sparse matrices
> 
> from sklearn.preprocessing import normalize                    # normalizing vectors
> 
> from sklearn.metrics import pairwise_distances                 # pairwise distances
> 
> import sys      
> 
> import os
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
> ### Load data, extract features
> 
> To work with text data, we must first convert the documents into numerical features. As in the first assignment, let's extract TF-IDF features for each article.
> 
> For your convenience, we extracted the TF-IDF vectors from the dataset. The vectors are packaged in a sparse matrix, where the i-th row gives the TF-IDF vectors for the i-th document. Each column corresponds to a unique word appearing in the dataset.
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
> wiki = sframe.SFrame('people_wiki.gl/')
> 
> tf_idf = load_sparse_csr('people_wiki_tf_idf.npz')
> 
> map_index_to_word = sframe.SFrame('people_wiki_map_index_to_word.gl/')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> _(Optional) Extracting TF-IDF vectors yourself_. We provide the pre-computed TF-IDF vectors to minimize potential compatibility issues. You are free to experiment with other tools to compute the TF-IDF vectors yourself. A good place to start is [sklearn.TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). Note. Due to variations in [tokenization](https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis)) and other factors, your TF-IDF vectors may differ from the ones we provide. For the purpose the assessment, we ask you to use the vectors from people_wiki_tf_idf.npz.
> 
> ### Normalize all vectors
> 
> As discussed in the previous assignment, Euclidean distance can be a poor metric of similarity between documents, as it unfairly penalizes long articles. For a reasonable assessment of similarity, we should disregard the length information and use length-agnostic metrics, such as cosine distance.
> 
> The k-means algorithm does not directly work with cosine distance, so we take an alternative route to remove length information: we normalize all vectors to be unit length. It turns out that Euclidean distance closely mimics cosine distance when all vectors are unit length. In particular, the squared Euclidean distance between any two vectors of length one is directly proportional to their cosine distance.
> 
> We can prove this as follows. Let x\mathbf{x}x and y\mathbf{y}y be normalized vectors, i.e. unit vectors, so that ∥x∥=∥y∥=1\|\mathbf{x}\|=\|\mathbf{y}\|=1∥x∥=∥y∥=1. Write the squared Euclidean distance as the dot product of (x−y)(\mathbf{x}-\mathbf{y})(x−y) to itself:
> 
> ∥x−y∥2=(x−y)T(x−y)=∥x∥2−2(xTy)+∥y∥2=2−2(xTy)=2(1−xTy∥x∥∥y∥)\|\mathbf{x}-\mathbf{y}\|^2 = (\mathbf{x} - \mathbf{y})^T(\mathbf{x} - \mathbf{y}) = \|\mathbf{x}\|^2 - 2(\mathbf{x}^T \mathbf{y}) + \|\mathbf{y}\|^2 = 2 - 2(\mathbf{x}^T \mathbf{y}) = 2\left(1 - \dfrac{\mathbf{x}^T\mathbf{y}}{\|\mathbf{x}\|\|\mathbf{y}\|}\right)∥x−y∥2=(x−y)T(x−y)=∥x∥2−2(xTy)+∥y∥2=2−2(xTy)=2(1−∥x∥∥y∥xTy​)
> 
> This tells us that two **unit vectors** that are close in Euclidean distance are also close in cosine distance. Thus, the k-means algorithm (which naturally uses Euclidean distances) on normalized vectors will produce the same results as clustering using cosine distance as a distance metric.
> 
> We import the [normalize() function](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html) from scikit-learn to normalize all vectors to unit length.
> 
>  `1
> 
> tf_idf = normalize(tf_idf)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_4:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_4 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_4 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_4:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_4.drop-target, .monaco-list.list_id_4 .monaco-list-rows.drop-target, .monaco-list.list_id_4 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Implement k-means
> 
> Let us implement the k-means algorithm. First, we choose an initial set of centroids. A common practice is to choose randomly from the data points.
> 
> **Note:** We specify a seed here, so that everyone gets the same answer. In practice, we highly recommend to use different seeds every time (for instance, by using the current timestamp).
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
> def get_initial_centroids(data, k, seed=None):
> 
>     '''Randomly choose k data points as initial centroids'''
> 
>     if seed is not None: # useful for obtaining consistent results
> 
>         np.random.seed(seed)
> 
>     n = data.shape[0] # number of data points
> 
>     # Pick K indices from range [0, N).
> 
>     rand_indices = np.random.randint(0, n, k)
> 
>     # Keep centroids as dense format, as many entries will be nonzero due to averaging.
> 
>     # As long as at least one document in a cluster contains a word,
> 
>     # it will carry a nonzero weight in the TF-IDF vector of the centroid.
> 
>     centroids = data[rand_indices,:].toarray()
> 
>     return centroids
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_5:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_5 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_5 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_5:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_5.drop-target, .monaco-list.list_id_5 .monaco-list-rows.drop-target, .monaco-list.list_id_5 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> After initialization, the k-means algorithm iterates between the following two steps:
> 
> 1.  Assign each data point to the closest centroid.
> 
> 2.  Revise centroids as the mean of the assigned data points.
> 
> In pseudocode, we iteratively do the following:
> 
>  `1
> 
> 2
> 
> cluster_assignment = assign_clusters(data, centroids)
> 
> centroids = revise_centroids(data, k, cluster_assignment)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_6:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_6 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_6 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_6:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_6.drop-target, .monaco-list.list_id_6 .monaco-list-rows.drop-target, .monaco-list.list_id_6 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Assigning clusters.** How do we implement Step 1 of the main k-means loop above? First import pairwise_distances function from scikit-learn, which calculates Euclidean distances between rows of given arrays. See this documentation for more information.
> 
> For the sake of demonstration, let's look at documents 100 through 102 as query documents and compute the distances between each of these documents and every other document in the corpus. In the k-means algorithm, we will have to compute pairwise distances between the set of centroids and the set of documents.
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
> # Get the TF-IDF vectors for documents 100 through 102.
> 
> queries = tf_idf[100:102,:]
> 
> # Compute pairwise distances from every data point to each query vector.
> 
> dist = pairwise_distances(tf_idf, queries, metric='euclidean')
> 
> print dist
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_7:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_7 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_7 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_7:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_7.drop-target, .monaco-list.list_id_7 .monaco-list-rows.drop-target, .monaco-list.list_id_7 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> This cell outputs a 2D array of form
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
> [[ 1.41000789  1.36894636]
> 
>  [ 1.40935215  1.41023886]
> 
>  [ 1.39855967  1.40890299]
> 
>  ..., 
> 
>  [ 1.41108296  1.39123646]
> 
>  [ 1.41022804  1.31468652]
> 
>  [ 1.39899784  1.41072448]]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_8:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_8 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_8 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_8:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_8.drop-target, .monaco-list.list_id_8 .monaco-list-rows.drop-target, .monaco-list.list_id_8 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> More formally, dist[i,j] is assigned the distance between the ith row of X (i.e., X[i,:]) and the jth row of Y (i.e., Y[j,:]).
> 
> **Checkpoint:** For a moment, suppose that we initialize three centroids with the first 3 rows of tf_idf. Write code to compute distances from each of the centroids to all data points in tf_idf. Then find the distance between row 430 of tf_idf and the second centroid and save it to **dist**. Run the following cell to check your answer.
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
> '''Test cell'''
> 
> if np.allclose(dist, pairwise_distances(tf_idf[430,:], tf_idf[1,:])):
> 
>     print('Pass')
> 
> else:
> 
>     print('Check your code again')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_9:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_9 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_9 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_9:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_9.drop-target, .monaco-list.list_id_9 .monaco-list-rows.drop-target, .monaco-list.list_id_9 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint:** Next, given the pairwise distances, we take the minimum of the distances for each data point. Fittingly, NumPy provides an argmin function. See [this documentation](http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.argmin.html) for details.
> 
> Read the documentation and write code to produce a 1D array whose i-th entry indicates the centroid that is the closest to the i-th data point. Use the list of distances from the previous checkpoint and save them as distances. The value 0 indicates closeness to the first centroid, 1 indicates closeness to the second centroid, and so forth. Save this array as **closest_cluster**. Run the following cell to check your answer.
> 
> **Hint:** the resulting array should be as long as the number of data points.
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
> '''Test cell'''
> 
> reference = [list(row).index(min(row)) for row in distances]
> 
> if np.allclose(closest_cluster, reference):
> 
>     print('Pass')
> 
> else:
> 
>     print('Check your code again')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_10:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_10 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_10 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_10:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_10.drop-target, .monaco-list.list_id_10 .monaco-list-rows.drop-target, .monaco-list.list_id_10 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint:** Let's put these steps together. First, initialize three centroids with the first 3 rows of tf_idf. Then, compute distances from each of the centroids to all data points in tf_idf. Finally, use these distance calculations to compute cluster assignments and assign them to cluster_assignment. Run the following cell to check your code.
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
> if len(cluster_assignment)==59071 and \
> 
>    np.array_equal(np.bincount(cluster_assignment), np.array([23061, 10086, 25924])):
> 
>     print('Pass') # count number of data points for each cluster
> 
> else:
> 
>     print('Check your code again.')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_11:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_11 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_11 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_11:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_11.drop-target, .monaco-list.list_id_11 .monaco-list-rows.drop-target, .monaco-list.list_id_11 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Now we are ready to fill in the blanks in this function:
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
> def assign_clusters(data, centroids):
> 
>     # Compute distances between each data point and the set of centroids:
> 
>     # Fill in the blank (RHS only)
> 
>     distances_from_centroids = ...
> 
>     # Compute cluster assignments for each data point:
> 
>     # Fill in the blank (RHS only)
> 
>     cluster_assignment = ...
> 
>     return cluster_assignment
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_12:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_12 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_12 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_12:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_12.drop-target, .monaco-list.list_id_12 .monaco-list-rows.drop-target, .monaco-list.list_id_12 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> which is simply generalization of what we did above.
> 
> **Checkpoint**. For the last time, let us check if Step 1 was implemented correctly. With rows 0, 2, 4, and 6 of tf_idf as an initial set of centroids, we assign cluster labels to rows 0, 10, 20, ..., and 90 of tf_idf. The resulting cluster labels should be [0, 1, 1, 0, 0, 2, 0, 2, 2, 1].
> 
>  `1
> 
> 2
> 
> 3
> 
> 4
> 
> if np.allclose(assign_clusters(tf_idf[0:100:10], tf_idf[0:8:2]), np.array([0, 1, 1, 0, 0, 2, 0, 2, 2, 1])):
> 
>     print('Pass')
> 
> else:
> 
>     print('Check your code again.')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_13:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_13 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_13 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_13:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_13.drop-target, .monaco-list.list_id_13 .monaco-list-rows.drop-target, .monaco-list.list_id_13 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Revising clusters
> 
> Let's turn to Step 2, where we compute the new centroids given the cluster assignments.
> 
> SciPy and NumPy arrays allow for filtering via Boolean masks. For instance, we filter all data points that are assigned to cluster 0 by writing "data[cluster_assignment==0,:]".
> 
> To develop intuition about filtering, let's look at a toy example consisting of 3 data points and 2 clusters.
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
> data = np.array([[1., 2., 0.],
> 
>                  [0., 0., 0.],
> 
>                  [2., 2., 0.]])
> 
> centroids = np.array([[0.5, 0.5, 0.],
> 
>                       [0., -0.5, 0.]])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_14:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_14 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_14 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_14:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_14.drop-target, .monaco-list.list_id_14 .monaco-list-rows.drop-target, .monaco-list.list_id_14 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's assign these data points to the closest centroid.
> 
>  `1
> 
> 2
> 
> cluster_assignment = assign_clusters(data, centroids)
> 
> print cluster_assignment   # prints [0 1 0]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_15:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_15 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_15 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_15:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_15.drop-target, .monaco-list.list_id_15 .monaco-list-rows.drop-target, .monaco-list.list_id_15 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The expression "cluster_assignment==1" gives a list of Booleans that says whether each data point is assigned to cluster 1 or not. For cluster 0, the expression is "cluster_assignment==0". In lieu of indices, we can put in the list of Booleans to pick and choose rows. Only the rows that correspond to a True entry will be retained.
> 
> First, let's look at the data points (i.e., their values) assigned to cluster 1:
> 
>  `1
> 
> print data[cluster_assignment==1]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The output makes sense since [0 0 0] is closer to [0 -0.5 0] than to [0.5 0.5 0].
> 
> Now let's look at the data points assigned to cluster 0:
> 
>  `1
> 
> print data[cluster_assignment==0]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Again, this makes sense since these values are each closer to [0.5 0.5 0] than to [0 -0.5 0].
> 
> Given all the data points in a cluster, it only remains to compute the mean. Use [np.mean()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.mean.html). By default, the function averages all elements in a 2D array. To compute row-wise or column-wise means, add the axis argument. See the linked documentation for details.
> 
> Use this function to average the data points in cluster 0:
> 
>  `1
> 
> print data[cluster_assignment==0].mean(axis=0)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> We are now ready to complete this function:
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
> def revise_centroids(data, k, cluster_assignment):
> 
>     new_centroids = []
> 
>     for i in xrange(k):
> 
>         # Select all data points that belong to cluster i. Fill in the blank (RHS only)
> 
>         member_data_points = ...
> 
>         # Compute the mean of the data points. Fill in the blank (RHS only)
> 
>         centroid = ...
> 
>         # Convert numpy.matrix type to numpy.ndarray type
> 
>         centroid = centroid.A1
> 
>         new_centroids.append(centroid)
> 
>     new_centroids = np.array(new_centroids)
> 
>     return new_centroids
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint**. Let's check our Step 2 implementation. Letting rows 0, 10, ..., 90 of tf_idf as the data points and the cluster labels [0, 1, 1, 0, 0, 2, 0, 2, 2, 1], we compute the next set of centroids. Each centroid is given by the average of all member data points in corresponding cluster.
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
> result = revise_centroids(tf_idf[0:100:10], 3, np.array([0, 1, 1, 0, 0, 2, 0, 2, 2, 1]))
> 
> if np.allclose(result[0], np.mean(tf_idf[[0,30,40,60]].toarray(), axis=0)) and \
> 
>    np.allclose(result[1], np.mean(tf_idf[[10,20,90]].toarray(), axis=0))   and \
> 
>    np.allclose(result[2], np.mean(tf_idf[[50,70,80]].toarray(), axis=0)):
> 
>     print('Pass')
> 
> else:
> 
>     print('Check your code')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Assessing convergence
> 
> How can we tell if the k-means algorithm is converging? We can look at the cluster assignments and see if they stabilize over time. In fact, we'll be running the algorithm until the cluster assignments stop changing at all. To be extra safe, and to assess the clustering performance, we'll be looking at an additional criteria: the sum of all squared distances between data points and centroids. This is defined as
> 
> J(Z,μ)=∑j=1k∑i:zi=j∥xi−μj∥2.J(\mathcal{Z},\mu) = \sum_{j=1}^k \sum_{i:z_i = j} \|\mathbf{x}_i - \mu_j\|^2.J(Z,μ)=∑j=1k​∑i:zi​=j​∥xi​−μj​∥2.
> 
> The smaller the distances, the more homogeneous the clusters are. In other words, we'd like to have "tight" clusters.
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
> def compute_heterogeneity(data, k, centroids, cluster_assignment):
> 
>     heterogeneity = 0.0
> 
>     for i in xrange(k):
> 
>         # Select all data points that belong to cluster i. Fill in the blank (RHS only)
> 
>         member_data_points = data[cluster_assignment==i, :]
> 
>         if member_data_points.shape[0] > 0: # check if i-th cluster is non-empty
> 
>             # Compute distances from centroid to data points (RHS only)
> 
>             distances = pairwise_distances(member_data_points, [centroids[i]], metric='euclidean')
> 
>             squared_distances = distances**2
> 
>             heterogeneity += np.sum(squared_distances)
> 
>     return heterogeneity
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Combining into a single function
> 
> Once the two k-means steps have been implemented, as well as our heterogeneity metric we wish to monitor, it is only a matter of putting these functions together to write a k-means algorithm that
> 
> *   Repeatedly performs Steps 1 and 2
> 
> *   Tracks convergence metrics
> 
> *   Stops if either no assignment changed or we reach a certain number of iterations.
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
> # Fill in the blanks
> 
> def kmeans(data, k, initial_centroids, maxiter, record_heterogeneity=None, verbose=False):
> 
>     '''This function runs k-means on given data and initial set of centroids.
> 
>        maxiter: maximum number of iterations to run.
> 
>        record_heterogeneity: (optional) a list, to store the history of heterogeneity as function of iterations
> 
>                              if None, do not store the history.
> 
>        verbose: if True, print how many data points changed their cluster labels in each iteration'''
> 
>     centroids = initial_centroids[:]
> 
>     prev_cluster_assignment = None
> 
>     for itr in xrange(maxiter):        
> 
>         if verbose:
> 
>             print(itr)
> 
>         # 1. Make cluster assignments using nearest centroids
> 
>         # YOUR CODE HERE
> 
>         cluster_assignment = ...
> 
>         # 2. Compute a new centroid for each of the k clusters, averaging all data points assigned to that cluster.
> 
>         # YOUR CODE HERE
> 
>         centroids = ...
> 
>         # Check for convergence: if none of the assignments changed, stop
> 
>         if prev_cluster_assignment is not None and \
> 
>           (prev_cluster_assignment==cluster_assignment).all():
> 
>             break
> 
>         # Print number of new assignments 
> 
>         if prev_cluster_assignment is not None:
> 
>             num_changed = np.sum(prev_cluster_assignment!=cluster_assignment)
> 
>             if verbose:
> 
>                 print('    {0:5d} elements changed their cluster assignment.'.format(num_changed))   
> 
>         # Record heterogeneity convergence metric
> 
>         if record_heterogeneity is not None:
> 
>             # YOUR CODE HERE
> 
>             score = ...
> 
>             record_heterogeneity.append(score)
> 
>         prev_cluster_assignment = cluster_assignment[:]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_22:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_22 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_22 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_22:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_22.drop-target, .monaco-list.list_id_22 .monaco-list-rows.drop-target, .monaco-list.list_id_22 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Plotting convergence metric
> 
> We can use the above function to plot the convergence metric across iterations.
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
> def plot_heterogeneity(heterogeneity, k):
> 
>     plt.figure(figsize=(7,4))
> 
>     plt.plot(heterogeneity, linewidth=4)
> 
>     plt.xlabel('# Iterations')
> 
>     plt.ylabel('Heterogeneity')
> 
>     plt.title('Heterogeneity of clustering over time, K={0:d}'.format(k))
> 
>     plt.rcParams.update({'font.size': 16})
> 
>     plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_23:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_23 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_23 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_23:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_23.drop-target, .monaco-list.list_id_23 .monaco-list-rows.drop-target, .monaco-list.list_id_23 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's consider running k-means with K=3 clusters for a maximum of 400 iterations, recording cluster heterogeneity at every step. Then, let's plot the heterogeneity over iterations using the plotting function above.
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
> k = 3
> 
> heterogeneity = []
> 
> initial_centroids = get_initial_centroids(tf_idf, k, seed=0)
> 
> centroids, cluster_assignment = kmeans(tf_idf, k, initial_centroids, maxiter=400,
> 
>                                        record_heterogeneity=heterogeneity, verbose=True)
> 
> plot_heterogeneity(heterogeneity, k)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_24:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_24 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_24 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_24:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_24.drop-target, .monaco-list.list_id_24 .monaco-list-rows.drop-target, .monaco-list.list_id_24 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question.** (True/False) The clustering objective (heterogeneity) is non-increasing for this example.
> 
> **Quiz Question**. Let's step back from this particular example. If the clustering objective (heterogeneity) would ever increase when running k-means, that would indicate: (choose one)
> 
> 1.  k-means algorithm got stuck in a bad local minimum
> 
> 2.  There is a bug in the k-means code
> 
> 3.  All data points consist of exact duplicates
> 
> 4.  Nothing is wrong. The objective should generally go down sooner or later.
> 
> **Quiz Question.** Which of the cluster contains the greatest number of data points in the end? Hint: Use np.bincount() to count occurrences of each cluster label.
> 
> 1.  Cluster #0
> 
> 2.  Cluster #1
> 
> 3.  Cluster #2
> 
> ### Beware of local minima
> 
> One weakness of k-means is that it tends to get stuck in a local minimum. To see this, let us run k-means multiple times, with different initial centroids created using different random seeds.
> 
> **Note:** Again, in practice, you should set different seeds for every run. We give you a list of seeds for this assignment so that everyone gets the same answer.
> 
> This may take several minutes to run.
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
> k = 10
> 
> heterogeneity = {}
> 
> import time
> 
> start = time.time()
> 
> for seed in [0, 20000, 40000, 60000, 80000, 100000, 120000]:
> 
>     initial_centroids = get_initial_centroids(tf_idf, k, seed)
> 
>     centroids, cluster_assignment = kmeans(tf_idf, k, initial_centroids, maxiter=400,
> 
>                                            record_heterogeneity=None, verbose=False)
> 
>     # To save time, compute heterogeneity only once in the end
> 
>     heterogeneity[seed] = compute_heterogeneity(tf_idf, k, centroids, cluster_assignment)
> 
>     print('seed={0:06d}, heterogeneity={1:.5f}'.format(seed, heterogeneity[seed]))
> 
>     sys.stdout.flush()
> 
> end = time.time()
> 
> print(end-start)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_25:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_25 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_25 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_25:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_25.drop-target, .monaco-list.list_id_25 .monaco-list-rows.drop-target, .monaco-list.list_id_25 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Notice the variation in heterogeneity for different initializations. This indicates that k-means sometimes gets stuck at a bad local minimum.
> 
> **Quiz Question.** Another way to capture the effect of changing initialization is to look at the distribution of cluster assignments. Add a line to the code above to compute the size (# of member data points) of clusters for each run of k-means. Look at the size of the largest cluster (most # of member data points) across multiple runs, with seeds 0, 20000, ..., 120000\. How much does this measure vary across the runs? What is the minimum and maximum values this quantity takes?
> 
> One effective way to counter this tendency is to use **k-means++** to provide a smart initialization. This method tries to spread out the initial set of centroids so that they are not too close together. It is known to improve the quality of local optima and lower average runtime.
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
> def smart_initialize(data, k, seed=None):
> 
>     '''Use k-means++ to initialize a good set of centroids'''
> 
>     if seed is not None: # useful for obtaining consistent results
> 
>         np.random.seed(seed)
> 
>     centroids = np.zeros((k, data.shape[1]))
> 
>     # Randomly choose the first centroid.
> 
>     # Since we have no prior knowledge, choose uniformly at random
> 
>     idx = np.random.randint(data.shape[0])
> 
>     centroids[0] = data[idx,:].toarray()
> 
>     # Compute distances from the first centroid chosen to all the other data points
> 
>     squared_distances = pairwise_distances(data, centroids[0:1], metric='euclidean').flatten()**2
> 
>     for i in xrange(1, k):
> 
>         # Choose the next centroid randomly, so that the probability for each data point to be chosen
> 
>         # is directly proportional to its squared distance from the nearest centroid.
> 
>         # Roughtly speaking, a new centroid should be as far as from ohter centroids as possible.
> 
>         idx = np.random.choice(data.shape[0], 1, p=squared_distances/sum(squared_distances))
> 
>         centroids[i] = data[idx,:].toarray()
> 
>         # Now compute distances from the centroids to all data points
> 
>         squared_distances = np.min(pairwise_distances(data, centroids[0:i+1], metric='euclidean')**2,axis=1)
> 
>     return centroidsa fe
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_26:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_26 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_26 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_26:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_26.drop-target, .monaco-list.list_id_26 .monaco-list-rows.drop-target, .monaco-list.list_id_26 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's now rerun k-means with 10 clusters using the same set of seeds, but always using k-means++ to initialize the algorithm.
> 
> This may take several minutes to run.
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
> k = 10
> 
> heterogeneity_smart = {}
> 
> start = time.time()
> 
> for seed in [0, 20000, 40000, 60000, 80000, 100000, 120000]:
> 
>     initial_centroids = smart_initialize(tf_idf, k, seed)
> 
>     centroids, cluster_assignment = kmeans(tf_idf, k, initial_centroids, maxiter=400,
> 
>                                            record_heterogeneity=None, verbose=False)
> 
>     # To save time, compute heterogeneity only once in the end
> 
>     heterogeneity_smart[seed] = compute_heterogeneity(tf_idf, k, centroids, cluster_assignment)
> 
>     print('seed={0:06d}, heterogeneity={1:.5f}'.format(seed, heterogeneity_smart[seed]))
> 
>     sys.stdout.flush()
> 
> end = time.time()
> 
> print(end-start)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_27:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_27 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_27 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_27:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_27.drop-target, .monaco-list.list_id_27 .monaco-list-rows.drop-target, .monaco-list.list_id_27 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let's compare the set of cluster heterogeneities we got from our 7 restarts of k-means using random initialization compared to the 7 restarts of k-means using k-means++ as a smart initialization. The following code produces a [box plot](http://matplotlib.org/api/pyplot_api.html) for each of these methods, indicating the spread of values produced by each method.
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
> plt.figure(figsize=(8,5))
> 
> plt.boxplot([heterogeneity.values(), heterogeneity_smart.values()], vert=False)
> 
> plt.yticks([1, 2], ['k-means', 'k-means++'])
> 
> plt.rcParams.update({'font.size': 16})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_28:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_28 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_28 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_28:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_28.drop-target, .monaco-list.list_id_28 .monaco-list-rows.drop-target, .monaco-list.list_id_28 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Psb9mn-SEeaNlA6zo4Pi2Q_d9d83ef4802dcf7b602ce3a716845785_download-_19_.png?expiry=1657238400000&hmac=FcOPSC4SZdnWjMzGboURg3WJuloViGOeCfeKCHrqg3E)
> 
> A few things to notice from the box plot:
> 
> *   On average, k-means++ produces a better clustering than Random initialization.
> 
> *   Variation in clustering quality is smaller for k-means++.
> 
> In general, you should run k-means at least a few times with different initializations and then return the run resulting in the lowest heterogeneity. Let us write a function that runs k-means multiple times and picks the best run that minimizes heterogeneity. The function accepts an optional list of seed values to be used for the multiple runs; if no such list is provided, the current UTC time is used as seed values.
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
> def kmeans_multiple_runs(data, k, maxiter, num_runs, seed_list=None, verbose=False):
> 
>     heterogeneity = {}
> 
>     min_heterogeneity_achieved = float('inf')
> 
>     best_seed = None
> 
>     final_centroids = None
> 
>     final_cluster_assignment = None
> 
>     for i in xrange(num_runs):
> 
>         # Use UTC time if no seeds are provided 
> 
>         if seed_list is not None: 
> 
>             seed = seed_list[i]
> 
>             np.random.seed(seed)
> 
>         else: 
> 
>             seed = int(time.time())
> 
>             np.random.seed(seed)
> 
>         # Use k-means++ initialization
> 
>         # YOUR CODE HERE
> 
>         initial_centroids = ...
> 
>         # Run k-means
> 
>         # YOUR CODE HERE
> 
>         centroids, cluster_assignment = ...
> 
>         # To save time, compute heterogeneity only once in the end
> 
>         # YOUR CODE HERE
> 
>         heterogeneity[seed] = ...
> 
>         if verbose:
> 
>             print('seed={0:06d}, heterogeneity={1:.5f}'.format(seed, heterogeneity[seed]))
> 
>             sys.stdout.flush()
> 
>         # if current measurement of heterogeneity is lower than previously seen,
> 
>         # update the minimum record of heterogeneity.
> 
>         if heterogeneity[seed] < min_heterogeneity_achieved:
> 
>             min_heterogeneity_achieved = heterogeneity[seed]
> 
>             best_seed = seed
> 
>             final_centroids = centroids
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_29:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_29 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_29 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_29:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_29.drop-target, .monaco-list.list_id_29 .monaco-list-rows.drop-target, .monaco-list.list_id_29 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### How to choose K
> 
> Since we are measuring the tightness of the clusters, a higher value of K reduces the possible heterogeneity metric by definition. For example, if we have N data points and set K=N clusters, then we could have 0 cluster heterogeneity by setting the N centroids equal to the values of the N data points. (Note: Not all runs for larger K will result in lower heterogeneity than a single run with smaller K due to local optima.) Let's see explore this general trend for ourselves by performing the following analysis.
> 
> Use the kmeans_multiple_runs function to run k-means with five different values of K. For each K, use k-means++ and **multiple run**s to pick the best solution. In what follows, we consider K=2,10,25,50,100 and 7 restarts for each setting.
> 
> IMPORTANT: The code block below will take about one hour to finish. We highly suggest that you use the arrays that we have computed for you. Side note: In practice, a good implementation of k-means would utilize parallelism to run multiple runs of k-means at once. For an example, see [scikit-learn's KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html).
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
> #def plot_k_vs_heterogeneity(k_values, heterogeneity_values):
> 
> #    plt.figure(figsize=(7,4))
> 
> #    plt.plot(k_values, heterogeneity_values, linewidth=4)
> 
> #    plt.xlabel('K')
> 
> #    plt.ylabel('Heterogeneity')
> 
> #    plt.title('K vs. Heterogeneity')
> 
> #    plt.rcParams.update({'font.size': 16})
> 
> #    plt.tight_layout()
> 
> #start = time.time()
> 
> #centroids = {}
> 
> #cluster_assignment = {}
> 
> #heterogeneity_values = []
> 
> #k_list = [2, 10, 25, 50, 100]
> 
> #seed_list = [0, 20000, 40000, 60000, 80000, 100000, 120000]
> 
> #for k in k_list:
> 
> #    heterogeneity = []
> 
> #    centroids[k], cluster_assignment[k] = kmeans_multiple_runs(tf_idf, k, maxiter=400,
> 
> #                                                               num_runs=len(seed_list),
> 
> #                                                               seed_list=seed_list,
> 
> #                                                               verbose=True)
> 
> #    score = compute_heterogeneity(tf_idf, k, centroids[k], cluster_assignment[k])
> 
> #    heterogeneity_values.append(score)
> 
> #plot_k_vs_heterogeneity(k_list, heterogeneity_values)
> 
> #end = time.time()
> 
> #print(end-start)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_30:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_30 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_30 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_30:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_30.drop-target, .monaco-list.list_id_30 .monaco-list-rows.drop-target, .monaco-list.list_id_30 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> To use the pre-computed NumPy arrays, first download kmeans-arrays.npz as mentioned in the reading for this assignment and load them with the following code. Make sure the downloaded file is in the same directory as this notebook.
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
> def plot_k_vs_heterogeneity(k_values, heterogeneity_values):
> 
>     plt.figure(figsize=(7,4))
> 
>     plt.plot(k_values, heterogeneity_values, linewidth=4)
> 
>     plt.xlabel('K')
> 
>     plt.ylabel('Heterogeneity')
> 
>     plt.title('K vs. Heterogeneity')
> 
>     plt.rcParams.update({'font.size': 16})
> 
>     plt.tight_layout()
> 
> filename = 'kmeans-arrays.npz'
> 
> heterogeneity_values = []
> 
> k_list = [2, 10, 25, 50, 100]
> 
> if os.path.exists(filename):
> 
>     arrays = np.load(filename)
> 
>     centroids = {}
> 
>     cluster_assignment = {}
> 
>     for k in k_list:
> 
>         print k
> 
>         sys.stdout.flush()
> 
>         centroids[k] = arrays['centroids_{0:d}'.format(k)]
> 
>         cluster_assignment[k] = arrays['cluster_assignment_{0:d}'.format(k)]
> 
>         score = compute_heterogeneity(tf_idf, k, centroids[k], cluster_assignment[k])
> 
>         heterogeneity_values.append(score)
> 
>     plot_k_vs_heterogeneity(k_list, heterogeneity_values)
> 
> else:
> 
>     print('File not found. Skipping.')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_31:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_31:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_31:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_31:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_31:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_31:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_31:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_31 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_31 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_31 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_31 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_31:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_31.drop-target, .monaco-list.list_id_31 .monaco-list-rows.drop-target, .monaco-list.list_id_31 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Lb_lskBUEeai_BLpE3ZESw_f17d3d5b4a27e71b90b65bf55ec2d2e7_download-_3_.png?expiry=1657238400000&hmac=86UyvBmBexuMpMBSNsokNXH0-Hyall_Xu0EZ17LwcPU)
> 
> In the above plot we show that heterogeneity goes down as we increase the number of clusters. Does this mean we should always favor a higher K? **Not at all!** As we will see in the following section, setting K too high may end up separating data points that are actually pretty alike. At the extreme, we can set individual data points to be their own clusters (K=N) and achieve zero heterogeneity, but separating each data point into its own cluster is hardly a desirable outcome. In the following section, we will learn how to detect a K set "too large".
> 
> ### Visualize clusters of documents
> 
> Let's start visualizing some clustering results to see if we think the clustering makes sense. We can use such visualizations to help us assess whether we have set K too large or too small for a given application. Following the theme of this course, we will judge whether the clustering makes sense in the context of document analysis.
> 
> What are we looking for in a good clustering of documents?
> 
> *   Documents in the same cluster should be similar.
> 
> *   Documents from different clusters should be less similar.
> 
> So a bad clustering exhibits either of two symptoms:
> 
> *   Documents in a cluster have mixed content.
> 
> *   Documents with similar content are divided up and put into different clusters.
> 
> To help visualize the clustering, we do the following:
> 
> *   Fetch nearest neighbors of each centroid from the set of documents assigned to that cluster. We will consider these documents as being representative of the cluster.
> 
> *   Print titles and first sentences of those nearest neighbors.
> 
> *   Print top 5 words that have highest tf-idf weights in each centroid.
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
> def visualize_document_clusters(wiki, tf_idf, centroids, cluster_assignment, k, map_index_to_word, display_content=True):
> 
>     '''wiki: original dataframe
> 
>        tf_idf: data matrix, sparse matrix format
> 
>        map_index_to_word: SFrame specifying the mapping betweeen words and column indices
> 
>        display_content: if True, display 8 nearest neighbors of each centroid'''
> 
>     print('==========================================================')
> 
>     # Visualize each cluster c
> 
>     for c in xrange(k):
> 
>         # Cluster heading
> 
>         print('Cluster {0:d}    '.format(c)),
> 
>         # Print top 5 words with largest TF-IDF weights in the cluster
> 
>         idx = centroids[c].argsort()[::-1]
> 
>         for i in xrange(5): # Print each word along with the TF-IDF weight
> 
>             print('{0:s}:{1:.3f}'.format(map_index_to_word['category'][idx[i]], centroids[c,idx[i]])),
> 
>         print('')
> 
>         if display_content:
> 
>             # Compute distances from the centroid to all data points in the cluster,
> 
>             # and compute nearest neighbors of the centroids within the cluster.
> 
>             distances = pairwise_distances(tf_idf, [centroids[c]], metric='euclidean').flatten()
> 
>             distances[cluster_assignment!=c] = float('inf') # remove non-members from consideration
> 
>             nearest_neighbors = distances.argsort()
> 
>             # For 8 nearest neighbors, print the title as well as first 180 characters of text.
> 
>             # Wrap the text at 80-character mark.
> 
>             for i in xrange(8):
> 
>                 text = ' '.join(wiki[nearest_neighbors[i]]['text'].split(None, 25)[0:25])
> 
>                 print('\n* {0:50s} {1:.5f}\n  {2:s}\n  {3:s}'.format(wiki[nearest_neighbors[i]]['name'],
> 
>                     distances[nearest_neighbors[i]], text[:90], text[90:180] if len(text) > 90 else ''))
> 
>         print('==========================================================')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_32:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_32:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_32:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_32:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_32:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_32:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_32:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_32 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_32 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_32 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_32 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_32:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_32.drop-target, .monaco-list.list_id_32 .monaco-list-rows.drop-target, .monaco-list.list_id_32 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Let us first look at the 2 cluster case (K=2).
> 
>  `1
> 
> visualize_document_clusters(wiki, tf_idf, centroids[2], cluster_assignment[2], 2, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_33:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_33:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_33:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_33:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_33:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_33:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_33:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_33 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_33 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_33 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_33 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_33:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_33.drop-target, .monaco-list.list_id_33 .monaco-list-rows.drop-target, .monaco-list.list_id_33 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Both clusters have mixed content, although cluster 1 is much purer than cluster 0:
> 
> *   Cluster 0: artists, songwriters, professors, politicians, writers, etc.
> 
> *   Cluster 1: baseball players, hockey players, soccer (association football) players, etc.
> 
> Top words of cluster 1 are all related to sports, whereas top words of cluster 0 show no clear pattern.
> 
> Roughly speaking, the entire dataset was divided into athletes and non-athletes. It would be better if we sub-divided non-athletes into more categories. So let us use more clusters. How about K=10?
> 
>  `1
> 
> 2
> 
> k = 10
> 
> visualize_document_clusters(wiki, tf_idf, centroids[k], cluster_assignment[k], k, map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_34:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_34:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_34:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_34:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_34:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_34:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_34:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_34 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_34 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_34 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_34 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_34:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_34.drop-target, .monaco-list.list_id_34 .monaco-list-rows.drop-target, .monaco-list.list_id_34 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Clusters 0, 1, and 5 appear to be still mixed, but others are quite consistent in content.
> 
> *   Cluster 0: artists, actors, film directors, playwrights
> 
> *   Cluster 1: soccer (association football) players, rugby players
> 
> *   Cluster 2: track and field athletes
> 
> *   Cluster 3: baseball players
> 
> *   Cluster 4: professors, researchers, scholars
> 
> *   Cluster 5: Austrailian rules football players, American football players
> 
> *   Cluster 6: female figures from various fields
> 
> *   Cluster 7: composers, songwriters, singers, music producers
> 
> *   Cluster 8: ice hockey players
> 
> *   Cluster 9: politicians
> 
> Clusters are now more pure, but some are qualitatively "bigger" than others. For instance, the category of scholars is more general than the category of baseball players. Increasing the number of clusters may split larger clusters. Another way to look at the size of cluster is to count the number of articles in each cluster.
> 
>  `1
> 
> np.bincount(cluster_assignment[10])
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_35:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_35:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_35:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_35:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_35:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_35:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_35:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_35 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_35 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_35 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_35 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_35:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_35.drop-target, .monaco-list.list_id_35 .monaco-list-rows.drop-target, .monaco-list.list_id_35 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**. Which of the 10 clusters above contains the greatest number of articles?
> 
> **Quiz Question**. Which of the 10 clusters contains the least number of articles?
> 
> There appears to be at least some connection between the topical consistency of a cluster and the number of its member data points.
> 
> Let us visualize the case for K=25\. For the sake of brevity, we do not print the content of documents. It turns out that the top words with highest TF-IDF weights in each cluster are representative of the cluster.
> 
>  `1
> 
> 2
> 
> visualize_document_clusters(wiki, tf_idf, centroids[25], cluster_assignment[25], 25,
> 
>                             map_index_to_word, display_content=False) # turn off text for brevity
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_36:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_36:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_36:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_36:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_36:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_36:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_36:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_36 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_36 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_36 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_36 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_36:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_36.drop-target, .monaco-list.list_id_36 .monaco-list-rows.drop-target, .monaco-list.list_id_36 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Looking at the representative examples and top words, we classify each cluster as follows. Notice the bolded items, which indicate the appearance of a new theme.
> 
> *   Cluster 0: **lawyers, judges, legal scholars**
> 
> *   Cluster 1: **professors, researchers, scholars (natural and health sciences)**
> 
> *   Cluster 2: ice hockey players
> 
> *   Cluster 3: politicans
> 
> *   Cluster 4: **government officials**
> 
> *   Cluster 5: politicans
> 
> *   Cluster 6: **professors, researchers, scholars (social sciences and humanities)**
> 
> *   Cluster 7: Canadian politicians
> 
> *   Cluster 8: **car racers**
> 
> *   Cluster 9: **economists**
> 
> *   Cluster 10: track and field athletes
> 
> *   Cluster 11: females from various fields
> 
> *   Cluster 12: (mixed; no clear theme)
> 
> *   Cluster 13: baseball players
> 
> *   Cluster 14: **painters, sculptors, artists**
> 
> *   Cluster 15: Austrailian rules football players, American football players
> 
> *   Cluster 16: **musicians, composers**
> 
> *   Cluster 17: soccer (association football) players, rugby players
> 
> *   Cluster 18: **poets**
> 
> *   Cluster 19: **film directors, playwrights**
> 
> *   Cluster 20: **songwriters, singers, music producers**
> 
> *   Cluster 21: **generals of U.S. Air Force**
> 
> *   Cluster 22: **music directors, conductors**
> 
> *   Cluster 23: **basketball players**
> 
> *   Cluster 24: **golf players**
> 
> Indeed, increasing K achieved the desired effect of breaking up large clusters. Depending on the application, this may or may not be preferable to the K=10 analysis.
> 
> Let's take it to the extreme and set K=100\. We have a suspicion that this value is too large. Let us look at the top words from each cluster:
> 
>  `1
> 
> 2
> 
> 3
> 
> 4
> 
> k=100
> 
> visualize_document_clusters(wiki, tf_idf, centroids[k], cluster_assignment[k], k,
> 
>                             map_index_to_word, display_content=False)
> 
> # turn off text for brevity -- turn it on if you are curious ;)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_37:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_37:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_37:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_37:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_37:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_37:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_37:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_37 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_37 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_37 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_37 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_37:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_37.drop-target, .monaco-list.list_id_37 .monaco-list-rows.drop-target, .monaco-list.list_id_37 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The class of soccer (association football) players has been broken into two clusters (44 and 45). Same goes for Austrialian rules football players (clusters 26 and 48). The class of baseball players have been also broken into two clusters (16 and 91).
> 
> **A high value of K encourages pure clusters, but we cannot keep increasing K. For large enough K, related documents end up going to different clusters.**
> 
> That said, the result for K=100 is not entirely bad. After all, it gives us separate clusters for such categories as Brazil, wrestling, computer science and the Mormon Church. If we set K somewhere between 25 and 100, we should be able to avoid breaking up clusters while discovering new ones.
> 
> Also, we should ask ourselves how much **granularity** we want in our clustering. If we wanted a rough sketch of Wikipedia, we don't want too detailed clusters. On the other hand, having many clusters can be valuable when we are zooming into a certain part of Wikipedia.
> 
> **There is no golden rule for choosing K. It all depends on the particular application and domain we are in.**
> 
> Another heuristic people use that does not rely on so much visualization, which can be hard in many applications (including here!) is as follows. Track heterogeneity versus K and look for the "elbow" of the curve where the heterogeneity decrease rapidly before this value of K, but then only gradually for larger values of K. This naturally trades off between trying to minimize heterogeneity, but reduce model complexity. In the heterogeneity versus K plot made above, we did not yet really see a flattening out of the heterogeneity, which might indicate that indeed K=100 is "reasonable" and we only see real overfitting for larger values of K (which are even harder to visualize using the methods we attempted above.)
> 
> **Quiz Question.** Another sign of too large K is having lots of small clusters. Look at the distribution of cluster sizes (by number of member data points). How many of the 100 clusters have fewer than 236 articles, i.e. 0.4% of the dataset?
> 
> ### Takeaway
> 
> Keep in mind though that tiny clusters aren't necessarily bad. A tiny cluster of documents that really look like each others is definitely preferable to a medium-sized cluster of documents with mixed content. However, having too few articles in a cluster may cause overfitting by reading too much into limited pool of training data.
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/E26k9/clustering-text-data-with-k-means#main
