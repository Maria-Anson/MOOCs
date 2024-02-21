# Clustering text data with Gaussian mixtures
> 
> In a previous assignment, we explored K-means clustering for a high-dimensional Wikipedia dataset. We can also model this data with a mixture of Gaussians, though with increasing dimension we run into several important problems associated with using a full covariance matrix for each component.
> 
> In this section, we will use an EM implementation to fit a Gaussian mixture model with **diagonal** covariances to a subset of the Wikipedia dataset.
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
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5zBDt4bEemhxxJUtZcQoA_7fb43aab245846f09a8c48977883f0b6_people_wiki.sframe.zip?Expires=1657843200&Signature=AROISpL10VQhe8u9YiYdYCtuKupAPHVFZD1K8JOgAkKv9edTv9eG27P~YIlzNwcv6lI2Gp9zG2NRObwFYpeU0il1CGzO~NlpjBVWz3i5NRHsfoEH98QEcSC0TGiSIIPITCtK3jdQzEDm1nnM53NuzBNbpgVR9JLrfwU1lOdAv6o_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython notebook:
> 
>  [ZIP File
> 
> CLU04-NB02.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/EXa8L-I8EemELQpo9cj5Ig_47f889d69bf74016adb595f66fad3bec_CLU04-NB02.ipynb.zip?Expires=1657843200&Signature=JBDLtMEh5YOLEYG1cngx1aS5d1FimzqcfEzeSjG5CVKLGw~xH~j11ohAuvVBZ~25QFvl2pVuFKm6HQWQlD1DErf84gzqkYawNt9nM9YIbM0uI1ufcdREVp-XodJj2Ie1Ut1be~1OckCL9t2SgqQOie9vH0r2OabT7mM~sUcph7Q_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download a collection of helper functions:
> 
>  [ZIP File
> 
> em_utilities.py
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/DCphrd4eEemzYQ60aJAwVA_fc87f6033fa34a2ab644e47ef86539cc_em_utilities.py.zip?Expires=1657843200&Signature=WRqMdb7MGIuoGm3KYMMCswfJma~cg3D3zCENPSwfFLPiJwiAhYHHXDEA1dyNjgsj4VB-hbjfl2VcIB3ZLXf2DbvmY4RhLkhz60G7xKwAEisl-H2LysLhtXPqOH5FayIfdMrHG6t4g6uPFkA-qs6Pwi9kUvIToE7VYiXvMbTpbWg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
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
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_a20552cf806c54b71b3b87cb593b9968_people_wiki.gl.zip?Expires=1657843200&Signature=ef9Jmdht68jIaE3BAmcfObloPnMdKI8Bl5Y3uqQP0sUnYw-eAtLTd-wS3A1HmcmaNOaeSNKBBya91rRMFIFi2K35dejf01eTfhTTN4G6c3Jy5MJ~ah81OWsKgHC-gkbvffDCBcCpUyRzF0rW19w9N0V6jBEiAzkg5-IfRJp~7Bs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> people_wiki.csv
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_167fc84b78dc145609e919983b475aaa_people_wiki.csv.zip?Expires=1657843200&Signature=jpwF0kcAZTaDUg3qWz1Fct26g4b6zKegL0FmHkMm0dmrLrabB9Bc7gBInPgIel4roAzERL3jMzwpIwTENDVqpWPPqI6yHPZUsQU~UDyjIxcaiXiPcM5vfTlh7cddg1TPsXx-8g2kegugfYnnkMRnRuT7HtmEpc~9Bu34-EU3lho_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the mapping between words and integer indices (note the prefix **4_**):
> 
>  [ZIP File
> 
> 4_map_index_to_word.gl
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_8022d9156b93197ae8878c79eba9767b_4_map_index_to_word.gl.zip?Expires=1657843200&Signature=Qev7g0A64w8TwJR8IhfZIRM7EVyxQVAQbR~L8EoVRzI7ni5wM28xfbNqOseIzSWi052Q4pKUX7vllJANkuZgt8Cu6iFOKUnjkI5FoYc-HUBBPwpWpxc6aVsGNL3iqdivu-2bw2RLvbd34OUOmBQHFZQFx7yRS7NvQuG8Dcpq-EI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> 4_map_index_to_word.json
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_8022d9156b93197ae8878c79eba9767b_4_map_index_to_word.json.zip?Expires=1657843200&Signature=STrePmJD2X8CGAcKSCGMzgiva6MUer5QAhyHfaEgp0fRu6dpF0Wb~NlKljZ0crpsyH1uejxnRX84JsOZofpz1u54NRNXQO9vkmajW4e74nbIWGl~C7Km6B2lF7CWbhtV2OwM6CgKR3MT6wOUTGGI-CdyljcPKB5M4TNolIp-kZg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the pre-processed set of TF-IDF scores (note the prefix **4_**):
> 
>  [ZIP File
> 
> 4_tf_idf.npz
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_af95de312b911daa1d7142fd60ae12e1_4_tf_idf.npz.zip?Expires=1657843200&Signature=MFy~JiFLmkBc5ViMPBBZIM7a6RPUHv3elCq2dvscKsmq7CHzTfqHtjJWWxohYHYpAbt~pbCbPxVOtL-3X9J0rbQ44ETr1yRdEjthGZePU40tYhk~XGSH4i7kj75WBY-YH-wL-guS7nwqqWv77VcVRg~K8uDIFgm~d1KxWo8KJJE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> ### Overview
> 
> In a previous assignment, we explored k-means clustering for a high-dimensional Wikipedia dataset. We can also model this data with a mixture of Gaussians, though with increasing dimension we run into two important issues associated with using a full covariance matrix for each component.
> 
> *   Computational cost becomes prohibitive in high dimensions: score calculations have complexity cubic in the number of dimensions M if the Gaussian has a full covariance matrix.
> 
> *   A model with many parameters require more data: bserve that a full covariance matrix for an M-dimensional Gaussian will have M(M+1)/2 parameters to fit. With the number of parameters growing roughly as the square of the dimension, it may quickly become impossible to find a sufficient amount of data to make good inferences.
> 
> Both of these issues are avoided if we require the covariance matrix of each component to be diagonal, as then it has only M parameters to fit and the score computation decomposes into M univariate score calculations. Recall from the lecture that the M-step for the full covariance is:
> 
> Σ^k=1Nksoft∑i=1Nrik(xi−μ^k)(xi−μ^k)T\displaystyle \hat{\Sigma}_k = \frac{1}{N_k^{soft}} \sum_{i=1}^N r_{ik} (x_i-\hat{\mu}_k)(x_i - \hat{\mu}_k)^TΣ^k​=Nksoft​1​i=1∑N​rik​(xi​−μ^​k​)(xi​−μ^​k​)T
> 
> Note that this is a square matrix with M rows and M columns, and the above equation implies that the (v, w) element is computed by
> 
> Σ^k,v,w=1Nksoft∑i=1Nrik(xiv−μ^kv)(xiw−μ^kw)\displaystyle \hat{\Sigma}_{k, v, w} = \frac{1}{N_k^{soft}} \sum_{i=1}^N r_{ik} (x_{iv}-\hat{\mu}_{kv})(x_{iw} - \hat{\mu}_{kw})Σ^k,v,w​=Nksoft​1​i=1∑N​rik​(xiv​−μ^​kv​)(xiw​−μ^​kw​)
> 
> When we assume that this is a diagonal matrix, then non-diagonal elements are assumed to be zero and we only need to compute each of the M elements along the diagonal independently using the following equation.
> 
> σ^k,v2=Σ^k,v,v=1Nksoft∑i=1Nrik(xiv−μ^kv)2\displaystyle \hat{\sigma}^2_{k, v} = \hat{\Sigma}_{k, v, v} = \frac{1}{N_k^{soft}} \sum_{i=1}^N r_{ik} (x_{iv}-\hat{\mu}_{kv})^2σ^k,v2​=Σ^k,v,v​=Nksoft​1​i=1∑N​rik​(xiv​−μ^​kv​)2
> 
> In this section, we will use an EM implementation to fit a Gaussian mixture model with **diagonal** covariances to a subset of the Wikipedia dataset. The implementation uses the above equation to compute each variance term.
> 
> We'll begin by importing the dataset and coming up with a useful representation for each article. After running our algorithm on the data, we will explore the output to see whether we can give a meaningful interpretation to the fitted parameters in our model.
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
> import sframe                                            # see below for install instruction
> 
> import numpy as np
> 
> from scipy.sparse import csr_matrix
> 
> from scipy.sparse import spdiags
> 
> from scipy.stats import multivariate_normal
> 
> from copy import deepcopy
> 
> from sklearn.metrics import pairwise_distances
> 
> from sklearn.preprocessing import normalize
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_43:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_43:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_43:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_43:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_43:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_43:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_43:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_43 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_43 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_43 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_43 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_43:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_43.drop-target, .monaco-list.list_id_43 .monaco-list-rows.drop-target, .monaco-list.list_id_43 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **About SFrame**. SFrame is a dataframe library Turi has released free-of-charge. Its source code is available [here](https://github.com/turi-code/SFrame). You may install SFrame via pip:
> 
>  `1
> 
> pip install --upgrade sframe
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_44:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_44:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_44:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_44:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_44:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_44:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_44:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_44 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_44 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_44 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_44 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_44:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_44.drop-target, .monaco-list.list_id_44 .monaco-list-rows.drop-target, .monaco-list.list_id_44 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Load Wikipedia data and extract TF-IDF features
> 
> Load Wikipedia data and transform each of the first 5000 document into a TF-IDF representation.
> 
>  `1
> 
> wiki = sframe.SFrame('people_wiki.gl/').head(5000)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_45:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_45:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_45:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_45:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_45:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_45:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_45:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_45 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_45 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_45 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_45 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_45:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_45.drop-target, .monaco-list.list_id_45 .monaco-list-rows.drop-target, .monaco-list.list_id_45 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
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
> tf_idf = load_sparse_csr('4_tf_idf.npz')  # NOT people_wiki_tf_idf.npz
> 
> map_index_to_word = sframe.SFrame('4_map_index_to_word.gl/')  # NOT people_wiki_map_index_to_word.gl
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_46:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_46:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_46:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_46:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_46:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_46:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_46:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_46 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_46 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_46 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_46 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_46:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_46.drop-target, .monaco-list.list_id_46 .monaco-list-rows.drop-target, .monaco-list.list_id_46 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> As in the previous assignment, we will normalize each document's TF-IDF vector to be a unit vector.
> 
>  `1
> 
> tf_idf = normalize(tf_idf)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_47:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_47:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_47:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_47:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_47:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_47:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_47:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_47 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_47 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_47 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_47 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_47:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_47.drop-target, .monaco-list.list_id_47 .monaco-list-rows.drop-target, .monaco-list.list_id_47 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> _(Optional) Extracting TF-IDF vectors yourself_. We provide the pre-computed TF-IDF vectors to minimize potential compatibility issues. You are free to experiment with other tools to compute the TF-IDF vectors yourself. A good place to start is [sklearn.TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). Note. Due to variations in [tokenization](https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis)) and other factors, your TF-IDF vectors may differ from the ones we provide. For the purpose the assessment, we ask you to use the vectors from 4_tf_idf.npz.
> 
> ### EM in high dimensions
> 
> EM for high-dimensional data requires some special treatment:
> 
> *   E step and M step must be vectorized as much as possible, as explicit loops are dreadfully slow in Python.
> 
> *   All operations must be cast in terms of sparse matrix operations, to take advantage of computational savings enabled by sparsity of data.
> 
> *   Initially, some words may be entirely absent from a cluster, causing the M step to produce zero mean and variance for those words. This means any data point with one of those words will have 0 probability of being assigned to that cluster since the cluster allows for no variability (0 variance) around that count being 0 (0 mean). Since there is a small chance for those words to later appear in the cluster, we instead assign a small positive variance (~1e-10). Doing so also prevents numerical overflow.
> 
> Due to complexity in implementation, we provide the complete implementation here. You are expected to answer some quiz questions using the results of clustering.
> 
> **Log probability function for diagonal covariance Gaussian**.
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
> def diag(array):
> 
>     n = len(array)
> 
>     return spdiags(array, 0, n, n)
> 
> def logpdf_diagonal_gaussian(x, mean, cov):
> 
>     '''
> 
>     Compute logpdf of a multivariate Gaussian distribution with diagonal covariance at a given point x.
> 
>     A multivariate Gaussian distribution with a diagonal covariance is equivalent
> 
>     to a collection of independent Gaussian random variables.
> 
>     x should be a sparse matrix. The logpdf will be computed for each row of x.
> 
>     mean and cov should be given as 1D numpy arrays
> 
>     mean[i] : mean of i-th variable
> 
>     cov[i] : variance of i-th variable'''
> 
>     n = x.shape[0]
> 
>     dim = x.shape[1]
> 
>     assert(dim == len(mean) and dim == len(cov))
> 
>     # multiply each i-th column of x by (1/(2*sigma_i)), where sigma_i is sqrt of variance of i-th variable.
> 
>     scaled_x = x.dot( diag(1./(2*np.sqrt(cov))) )
> 
>     # multiply each i-th entry of mean by (1/(2*sigma_i))
> 
>     scaled_mean = mean/(2*np.sqrt(cov))
> 
>     # sum of pairwise squared Eulidean distances gives SUM[(x_i - mean_i)^2/(2*sigma_i^2)]
> 
>     return -np.sum(np.log(np.sqrt(2*np.pi*cov))) - pairwise_distances(scaled_x, [scaled_mean], 'euclidean').flatten()**2
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_48:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_48:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_48:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_48:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_48:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_48:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_48:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_48 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_48 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_48 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_48 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_48:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_48.drop-target, .monaco-list.list_id_48 .monaco-list-rows.drop-target, .monaco-list.list_id_48 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **EM algorithm for sparse data**.
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
> def log_sum_exp(x, axis):
> 
>     '''Compute the log of a sum of exponentials'''
> 
>     x_max = np.max(x, axis=axis)
> 
>     if axis == 1:
> 
>         return x_max + np.log( np.sum(np.exp(x-x_max[:,np.newaxis]), axis=1) )
> 
>     else:
> 
>         return x_max + np.log( np.sum(np.exp(x-x_max), axis=0) )
> 
> def EM_for_high_dimension(data, means, covs, weights, cov_smoothing=1e-5, maxiter=int(1e3), thresh=1e-4, verbose=False):
> 
>     # cov_smoothing: specifies the default variance assigned to absent features in a cluster.
> 
>     #                If we were to assign zero variances to absent features, we would be overconfient,
> 
>     #                as we hastily conclude that those featurese would NEVER appear in the cluster.
> 
>     #                We'd like to leave a little bit of possibility for absent features to show up later.
> 
>     n = data.shape[0]
> 
>     dim = data.shape[1]
> 
>     mu = deepcopy(means)
> 
>     Sigma = deepcopy(covs)
> 
>     K = len(mu)
> 
>     weights = np.array(weights)
> 
>     ll = None
> 
>     ll_trace = []
> 
>     for i in range(maxiter):
> 
>         # E-step: compute responsibilities
> 
>         logresp = np.zeros((n,K))
> 
>         for k in xrange(K):
> 
>             logresp[:,k] = np.log(weights[k]) + logpdf_diagonal_gaussian(data, mu[k], Sigma[k])
> 
>         ll_new = np.sum(log_sum_exp(logresp, axis=1))
> 
>         if verbose:
> 
>             print(ll_new)
> 
>         logresp -= np.vstack(log_sum_exp(logresp, axis=1))
> 
>         resp = np.exp(logresp)
> 
>         counts = np.sum(resp, axis=0)
> 
>         # M-step: update weights, means, covariances
> 
>         weights = counts / np.sum(counts)
> 
>         for k in range(K):
> 
>             mu[k] = (diag(resp[:,k]).dot(data)).sum(axis=0)/counts[k]
> 
>             mu[k] = mu[k].A1
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_49:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_49:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_49:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_49:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_49:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_49:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_49:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_49 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_49 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_49 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_49 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_49:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_49.drop-target, .monaco-list.list_id_49 .monaco-list-rows.drop-target, .monaco-list.list_id_49 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Initializing mean parameters using k-means.** Recall from the lectures that EM for Gaussian mixtures is very sensitive to the choice of initial means. With a bad initial set of means, EM may produce clusters that span a large area and are mostly overlapping. To eliminate such bad outcomes, we first produce a suitable set of initial means by using the cluster centers from running k-means. That is, we first run k-means and then take the final set of means from the converged solution as the initial means in our EM algorithm.
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
> from sklearn.cluster import KMeans
> 
> np.random.seed(5)
> 
> num_clusters = 25
> 
> # Use scikit-learn's k-means to simplify workflow
> 
> kmeans_model = KMeans(n_clusters=num_clusters, n_init=5, max_iter=400, random_state=1, n_jobs=-1)
> 
> kmeans_model.fit(tf_idf)
> 
> centroids, cluster_assignment = kmeans_model.cluster_centers_, kmeans_model.labels_
> 
> means = [centroid for centroid in centroids]
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_50:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_50:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_50:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_50:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_50:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_50:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_50:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_50 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_50 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_50 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_50 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_50:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_50.drop-target, .monaco-list.list_id_50 .monaco-list-rows.drop-target, .monaco-list.list_id_50 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Initializing cluster weights.** We will initialize each cluster weight to be the proportion of documents assigned to that cluster by k-means above.
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
> num_docs = tf_idf.shape[0]
> 
> weights = []
> 
> for i in xrange(num_clusters):
> 
>     # Compute the number of data points assigned to cluster i:
> 
>     num_assigned = ... # YOUR CODE HERE
> 
>     w = float(num_assigned) / num_docs
> 
>     weights.append(w)**Initializing covariances.** To initialize our covariance parameters, we compute $\hat{\sigma}_{k, j}^2 = \sum_{i=1}^{N}(x_{i,j} - \hat{\mu}_{k, j})^2$ for each feature $j$.  For features with really tiny variances, we assign 1e-8 instead to prevent numerical instability. We do this computation in a vectorized fashion in the following code block.
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_51:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_51:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_51:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_51:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_51:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_51:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_51:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_51 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_51 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_51 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_51 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_51:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_51.drop-target, .monaco-list.list_id_51 .monaco-list-rows.drop-target, .monaco-list.list_id_51 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Initializing covariances.** To initialize our covariance parameters, we compute σ^k,j2=∑i=1N(xi,j−μ^k,j)2\hat{\sigma}_{k, j}^2 = \sum_{i=1}^{N}(x_{i,j} - \hat{\mu}_{k, j})^2σ^k,j2​=∑i=1N​(xi,j​−μ^​k,j​)2 for each feature jjj. For features with really tiny variances, we assign 1e-8 instead to prevent numerical instability. We do this computation in a vectorized fashion in the following code block.
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
> covs = []
> 
> for i in xrange(num_clusters):
> 
>     member_rows = tf_idf[cluster_assignment==i]
> 
>     cov = (member_rows.multiply(member_rows) - 2*member_rows.dot(diag(means[i]))).sum(axis=0).A1 / member_rows.shape[0] \
> 
>           + means[i]**2
> 
>     cov[cov < 1e-8] = 1e-8
> 
>     covs.append(cov)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_52:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_52:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_52:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_52:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_52:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_52:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_52:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_52 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_52 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_52 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_52 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_52:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_52.drop-target, .monaco-list.list_id_52 .monaco-list-rows.drop-target, .monaco-list.list_id_52 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Running EM.** Now that we have initialized all of our parameters, run EM.
> 
>  `1
> 
> 2
> 
> out = EM_for_high_dimension(tf_idf, means, covs, weights, cov_smoothing=1e-10)
> 
> print out['loglik'] # print history of log-likelihood over time
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_53:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_53:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_53:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_53:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_53:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_53:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_53:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_53 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_53 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_53 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_53 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_53:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_53.drop-target, .monaco-list.list_id_53 .monaco-list-rows.drop-target, .monaco-list.list_id_53 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Interpret clusters
> 
> In contrast to k-means, EM is able to explicitly model clusters of varying sizes and proportions. The relative magnitude of variances in the word dimensions tell us much about the nature of the clusters.
> 
> Write yourself a cluster visualizer as follows. Examining each cluster's mean vector, list the 5 words with the largest mean values (5 most common words in the cluster). For each word, also include the associated variance parameter (diagonal element of the covariance matrix).
> 
> A sample output may be:
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
> ==========================================================
> 
> Cluster 0: Largest mean parameters in cluster 
> 
> Word        Mean        Variance    
> 
> football    1.08e-01    8.64e-03
> 
> season      5.80e-02    2.93e-03
> 
> club        4.48e-02    1.99e-03
> 
> league      3.94e-02    1.08e-03
> 
> played      3.83e-02    8.45e-04
> 
> ...
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_54:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_54:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_54:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_54:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_54:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_54:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_54:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_54 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_54 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_54 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_54 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_54:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_54.drop-target, .monaco-list.list_id_54 .monaco-list-rows.drop-target, .monaco-list.list_id_54 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }`  `1
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
> # Fill in the blanks
> 
> def visualize_EM_clusters(tf_idf, means, covs, map_index_to_word):
> 
>     print('')
> 
>     print('==========================================================')
> 
>     num_clusters = len(means)
> 
>     for c in xrange(num_clusters):
> 
>         print('Cluster {0:d}: Largest mean parameters in cluster '.format(c))
> 
>         print('\n{0: <12}{1: <12}{2: <12}'.format('Word', 'Mean', 'Variance'))
> 
>         # The k'th element of sorted_word_ids should be the index of the word 
> 
>         # that has the k'th-largest value in the cluster mean. Hint: Use np.argsort().
> 
>         sorted_word_ids = ...  # YOUR CODE HERE
> 
>         for i in sorted_word_ids[:5]:
> 
>             print '{0: <12}{1:<10.2e}{2:10.2e}'.format(map_index_to_word['category'][i], 
> 
>                                                        means[c][i],
> 
>                                                        covs[c][i])
> 
>         print '\n=====================================================Quiz Question. Select all the topics that have a cluster in the model created above. [multiple choice]===='
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_55:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_55:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_55:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_55:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_55:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_55:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_55:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_55 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_55 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_55 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_55 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_55:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_55.drop-target, .monaco-list.list_id_55 .monaco-list-rows.drop-target, .monaco-list.list_id_55 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**. Select all the topics that have a cluster in the model created above. [multiple choice]
> 
>  `1
> 
> 2
> 
> '''By EM'''
> 
> visualize_EM_clusters(tf_idf, out['means'], out['covs'], map_index_to_word)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_56:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_56:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_56:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_56:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_56:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_56:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_56:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_56 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_56 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_56 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_56 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_56:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_56.drop-target, .monaco-list.list_id_56 .monaco-list-rows.drop-target, .monaco-list.list_id_56 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Comparing to random initialization
> 
> Create variables for randomly initializing the EM algorithm. Complete the following code block.
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
> np.random.seed(5)
> 
> num_clusters = len(means)
> 
> num_docs, num_words = tf_idf.shape
> 
> random_means = []
> 
> random_covs = []
> 
> random_weights = []
> 
> for k in range(num_clusters):
> 
>     # Create a numpy array of length num_words with random normally distributed values.
> 
>     # Use the standard univariate normal distribution (mean 0, variance 1).
> 
>     # YOUR CODE HERE
> 
>     mean = ...
> 
>     # Create a numpy array of length num_words with random values uniformly distributed between 1 and 5.
> 
>     # YOUR CODE HERE
> 
>     cov = ...
> 
>     # Initially give each cluster equal weight.
> 
>     # YOUR CODE HERE
> 
>     weight = ...
> 
>     random_means.append(mean)
> 
>     random_covs.append(cov)
> 
>     random_weights.append(weight)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_57:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_57:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_57:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_57:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_57:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_57:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_57:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_57 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_57 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_57 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_57 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_57:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_57.drop-target, .monaco-list.list_id_57 .monaco-list-rows.drop-target, .monaco-list.list_id_57 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**: Try fitting EM with the random initial parameters you created above. (Use cov_smoothing=1e-5.) Store the result to out_random_init. What is the final loglikelihood that the algorithm converges to?
> 
> **Quiz Question:** Is the final loglikelihood larger or smaller than the final loglikelihood we obtained above when initializing EM with the results from running k-means?
> 
> **Quiz Question**: For the above model, out_random_init, use the visualize_EM_clustersmethod you created above. Are the clusters more or less interpretable than the ones found after initializing using k-means?
> 
> ### Takeaway
> 
> In this assignment we were able to apply the EM algorithm to a mixture of Gaussians model of text data. This was made possible by modifying the model to assume a diagonal covariance for each cluster, and by modifying the implementation to use a sparse matrix representation. In the second part you explored the role of k-means initialization on the convergence of the model as well as the interpretability of the clusters.
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/XGgeJ/clustering-text-data-with-gaussian-mixtures#main
