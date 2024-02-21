# Implementing EM for Gaussian mixtures
> 
> In this assignment you will
> 
> *   implement the EM algorithm for a Gaussian mixture model
> 
> *   apply your implementation to cluster images
> 
> *   explore clustering results and interpret the output of the EM algorithm
> 
> ## If you are using Turi Create
> 
> An IPython Notebook has been provided below to you for this assignment. This notebook contains the instructions, quiz questions and partially-completed code for you to use as well as some cells to test your code.
> 
> *   Download the image dataset in SFrame format:
> 
>  [ZIP File
> 
> images.sf
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/i5pPo94bEemHAgogVwzP7g_3428f1f81e4b46f7b0043df9e496de29_images.sf.zip?Expires=1657756800&Signature=BGaOgqEIzU0M8RQ0rnuDBPV5RTrBrrMvaPpveGW1RO6Mt8JmzW7how0CUEK6lhrrYZ4V47ndDRm-NhMes8SYhrbb22Q6q9WyzH9dEeurn0-y5SIC9EJmrgc7X4dBvlDINP0nOkg4vx~VvHccSUgoa316UskBGbbnF80QfJa2DBA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the companion IPython notebook:
> 
>  [ZIP File
> 
> CLU04-NB01.ipynb
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/EXiRLuI8Eemm5A4ynZyB2A_02d835d967234a7abc91cf61451f8ff0_CLU04-NB01.ipynb.zip?Expires=1657756800&Signature=KzxznYY-dY0EbsBUloP3sh~hATEnekA7YpAXID9rPWGPdMejpO9mSFXZ2gqL6FkJb8T-DwwFoeZMNAb8Zq3eIcY-~-HTg1NSIKRc5ca~m3-l-HzQd2Z6NLb5-wgXZhzBu-~vIgP5aaBiyVfLdhHdKUDRGjiLYO1om82UmkYcOZc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> *   Download the sample picture: (Choose "Save Link As..." from the context menu)
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/v8uaOt4dEemhaQ6bnADF5g_a53cdcf49d1346dc91d0a7aa2f1fe4bd_chosen_images.png?expiry=1657756800000&hmac=9HjTjTTu2_PdSP2OzH2folqcLK_vHVEp2-MPuqF0ggc)
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
> *   Download the image dataset in SFrame format:
> 
>  [ZIP File
> 
> images.sf
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_a20552cf806c54b71b3b87cb593b9968_images.sf.zip?Expires=1657756800&Signature=WNiBsbet4opUKbqbIOVA1R1jeojiTA3JnAajFt8ca1Sil3hwAvDGrFgb2~6zebR5H4U0rBjLET83yq~eOQWdJyC51F1DfjkFOIiOU9Tg-61FvbDhJkwep4gL7CJeMSAlW19jdr5YGU4yktWPu~ogpIDsL07RFvkVxj04jza1Ixc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
> 
> For those experimenting with other tools:
> 
>  [ZIP File
> 
> images
> 
> ZIP File](https://d3c33hcgiwev3.cloudfront.net/_8a352ed8c119f98f079305de3bd46e26_images.zip?Expires=1657756800&Signature=YXCqD8OrXbuzV1iTYMbLvTMQ5h8x-yfA4uoMpTQ8SWRpLLBl~h0yjIjgyB1t0IK95x~BENxZ2-NXRtWOFS7je49FluDMHpY7EiNsOerzllvs0EjORyFZXf7hfzPvKKUPDty7ewYQL0x9O2npjKQkZMrMJVxApPv4C7X8WJZm7sA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) 
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
> 10
> 
> 11
> 
> import sframe                                                  # see below for install instruction
> 
> import numpy as np                                             # dense matrices
> 
> import matplotlib.pyplot as plt                                # plotting
> 
> from scipy.stats import multivariate_normal                    # multivariate Gaussian distribution
> 
> import copy                                                    # deep copies
> 
> # image handling library
> 
> from PIL import Image
> 
> from io import BytesIO
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
> ### Implementing the EM algorithm for Gaussian mixture models
> 
> In this section, you will implement the EM algorithm. We will take the following steps:
> 
> *   Create some synthetic data.
> 
> *   Provide a log likelihood function for this model.
> 
> *   Implement the EM algorithm.
> 
> *   Visualize the progress of the parameters during the course of running EM.
> 
> *   Visualize the convergence of the model.
> 
> **Log likelihood.** We provide a function to calculate log likelihood for mixture of Gaussians. The log likelihood quantifies the probability of observing a given set of data under a particular setting of the parameters in our model. We will use this to assess convergence of our EM algorithm; specifically, we will keep looping through EM update steps until the log likelihood ceases to increase at a certain rate.
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
> def log_sum_exp(Z):
> 
>     """ Compute log(\sum_i exp(Z_i)) for some array Z."""
> 
>     return np.max(Z) + np.log(np.sum(np.exp(Z - np.max(Z))))
> 
> def loglikelihood(data, weights, means, covs):
> 
>     """ Compute the loglikelihood of the data for a Gaussian mixture model with the given parameters. """
> 
>     num_clusters = len(means)
> 
>     num_dim = len(data[0])
> 
>     ll = 0
> 
>     for d in data:
> 
>         Z = np.zeros(num_clusters)
> 
>         for k in range(num_clusters):
> 
>             # Compute (x-mu)^T * Sigma^{-1} * (x-mu)
> 
>             delta = np.array(d) - means[k]
> 
>             exponent_term = np.dot(delta.T, np.dot(np.linalg.inv(covs[k]), delta))
> 
>             # Compute loglikelihood contribution for this data point and this cluster
> 
>             Z[k] += np.log(weights[k])
> 
>             Z[k] -= 1/2. * (num_dim * np.log(2*np.pi) + np.log(np.linalg.det(covs[k])) + exponent_term)
> 
>         # Increment loglikelihood contribution of this data point across all clusters
> 
>         ll += log_sum_exp(Z)
> 
>     return ll
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_3:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_3:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_3:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_3 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_3 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_3 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_3:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_3.drop-target, .monaco-list.list_id_3 .monaco-list-rows.drop-target, .monaco-list.list_id_3 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **E-step: assign cluster responsibilities, given current parameters**. The first step in the EM algorithm is to compute cluster responsibilities. Let rikr_{ik}rik​ denote the responsibility of cluster kkk for data point iii. Note that cluster responsibilities are fractional parts: Cluster responsibilities for a single data point iii should sum to 1.
> 
> ri1+ri2+…+riK=1r_{i1} + r_{i2} + \ldots + r_{iK} = 1ri1​+ri2​+…+riK​=1
> 
> To figure how much a cluster is responsible for a given data point, we compute the likelihood of the data point under the particular cluster assignment, multiplied by the weight of the cluster. For data point iii and cluster kkk, this quantity is
> 
> rik∝πkN(xi∣μk,Σk)r_{ik} \propto \pi_k N(x_i | \mu_k, \Sigma_k)rik​∝πk​N(xi​∣μk​,Σk​)
> 
> where N(xi∣μk,Σk)N(x_i | \mu_k, \Sigma_k)N(xi​∣μk​,Σk​) is the Gaussian distribution for cluster kkk (with mean μk\mu_kμk​ and covariance Σk\Sigma_kΣk​).
> 
> We used ∝\propto∝ because the quantity N(xi∣μk,Σk)N(x_i | \mu_k, \Sigma_k)N(xi​∣μk​,Σk​) is not yet the responsibility we want. To ensure that all responsibilities over each data point add up to 1, we add the normalization constant in the denominator:
> 
> rik=πkN(xi∣μk,Σk)∑k=1KπkN(xi∣μk,Σk).r_{ik} = \dfrac{\pi_k N(x_i | \mu_k, \Sigma_k)}{\sum_{k=1}^{K} \pi_k N(x_i | \mu_k, \Sigma_k)}.rik​=∑k=1K​πk​N(xi​∣μk​,Σk​)πk​N(xi​∣μk​,Σk​)​.
> 
> Complete the following function that computes rikr_{ik}rik​ for all data points iii and clusters kkk.
> 
> **Drawing from a Gaussian distribution**. SciPy provides a convenient function [multivariate_normal.pdf](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.multivariate_normal.html) that computes the likelihood of seeing a data point in a multivariate Gaussian distribution. The usage is
> 
> multivariate_normal.pdf([data point], mean=[mean vector], cov=[covariance matrix])
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
> def compute_responsibilities(data, weights, means, covariances):
> 
>     '''E-step: compute responsibilities, given the current parameters'''
> 
>     num_data = len(data)
> 
>     num_clusters = len(means)
> 
>     resp = np.zeros((num_data, num_clusters))
> 
>     # Update resp matrix so that resp[i,k] is the responsibility of cluster k for data point i.
> 
>     # Hint: To compute likelihood of seeing data point i given cluster k, use multivariate_normal.pdf.
> 
>     for i in range(num_data):
> 
>         for k in range(num_clusters):
> 
>             # YOUR CODE HERE
> 
>             resp[i, k] = ...
> 
>     # Add up responsibilities over each data point and normalize
> 
>     row_sums = resp.sum(axis=1)[:, np.newaxis]
> 
>     resp = resp / row_sums
> 
>     return resp
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_4:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_4:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_4:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_4 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_4 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_4 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_4:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_4.drop-target, .monaco-list.list_id_4 .monaco-list-rows.drop-target, .monaco-list.list_id_4 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint.**
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
> resp = compute_responsibilities(data=np.array([[1.,2.],[-1.,-2.]]), weights=np.array([0.3, 0.7]),
> 
>                                 means=[np.array([0.,0.]), np.array([1.,1.])],
> 
>                                 covariances=[np.array([[1.5, 0.],[0.,2.5]]), np.array([[1.,1.],[1.,2.]])])
> 
> if resp.shape==(2,2) and np.allclose(resp, np.array([[0.10512733, 0.89487267], [0.46468164, 0.53531836]])):
> 
>     print 'Checkpoint passed!'
> 
> else:
> 
>     print 'Check your code again.'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_5:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_5:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_5:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_5 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_5 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_5 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_5:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_5.drop-target, .monaco-list.list_id_5 .monaco-list-rows.drop-target, .monaco-list.list_id_5 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **M-step: Update parameters, given current cluster responsibilities.**
> 
> Once the cluster responsibilities are computed, we update the parameters (weights, means, and covariances) associated with the clusters.
> 
> **Computing soft counts**. Before updating the parameters, we first compute what is known as "soft counts". The soft count of a cluster is the sum of all cluster responsibilities for that cluster:
> 
> Nksoft=r1k+r2k+…+rNk=∑i=1NrikN^{\text{soft}}_k = r_{1k} + r_{2k} + \ldots + r_{Nk} = \sum_{i=1}^{N} r_{ik}Nksoft​=r1k​+r2k​+…+rNk​=∑i=1N​rik​
> 
> where we loop over data points. Note that, unlike k-means, we must loop over every single data point in the dataset. This is because all clusters are represented in all data points, to a varying degree.
> 
> We provide the function for computing the soft counts:
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
> def compute_soft_counts(resp):
> 
>     # Compute the total responsibility assigned to each cluster, which will be useful when 
> 
>     # implementing M-steps below. In the lectures this is called N^{soft}
> 
>     counts = np.sum(resp, axis=0)
> 
>     return counts
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_6:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_6:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_6:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_6 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_6 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_6 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_6:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_6.drop-target, .monaco-list.list_id_6 .monaco-list-rows.drop-target, .monaco-list.list_id_6 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Updating weights**. The cluster weights show us how much each cluster is represented over all data points. The weight of cluster kkk is given by the ratio of the soft count NksoftN^{\text{soft}}_{k}Nksoft​ to the total number of data points NNN:
> 
> π^k=NksoftN\hat{\pi}_k = \dfrac{N^{\text{soft}}_{k}}{N}π^k​=NNksoft​​
> 
> Notice that NNN is equal to the sum over the soft counts NksoftN^{\text{soft}}_{k}Nksoft​ of all clusters.
> 
> Complete the following function:
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
> def compute_weights(counts):
> 
>     num_clusters = len(counts)
> 
>     weights = [0.] * num_clusters
> 
>     for k in range(num_clusters):
> 
>         # Update the weight for cluster k using the M-step update rule for the cluster weight, \hat{\pi}_k.
> 
>         # HINT: compute # of data points by summing soft counts.
> 
>         # YOUR CODE HERE
> 
>         weights[k] = ...
> 
>     return weights
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_7:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_7:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_7:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_7 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_7 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_7 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_7:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_7.drop-target, .monaco-list.list_id_7 .monaco-list-rows.drop-target, .monaco-list.list_id_7 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint.**
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
> resp = compute_responsibilities(data=np.array([[1.,2.],[-1.,-2.],[0,0]]), weights=np.array([0.3, 0.7]),
> 
>                                 means=[np.array([0.,0.]), np.array([1.,1.])],
> 
>                                 covariances=[np.array([[1.5, 0.],[0.,2.5]]), np.array([[1.,1.],[1.,2.]])])
> 
> counts = compute_soft_counts(resp)
> 
> weights = compute_weights(counts)
> 
> print counts
> 
> print weights
> 
> if np.allclose(weights, [0.27904865942515705, 0.720951340574843]):
> 
>     print 'Checkpoint passed!'
> 
> else:
> 
>     print 'Check your code again.'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_8:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_8:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_8:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_8 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_8 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_8 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_8:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_8.drop-target, .monaco-list.list_id_8 .monaco-list-rows.drop-target, .monaco-list.list_id_8 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Updating means**. The mean of each cluster is set to the weighted average of all data points, weighted by the cluster responsibilities:
> 
> μ^k=1Nksoft∑i=1Nrikxi\hat{\mu}_k = \dfrac{1}{N_k^{\text{soft}}} \sum_{i=1}^N r_{ik}x_iμ^​k​=Nksoft​1​∑i=1N​rik​xi​
> 
> Complete the following function:
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
> def compute_means(data, resp, counts):
> 
>     num_clusters = len(counts)
> 
>     num_data = len(data)
> 
>     means = [np.zeros(len(data[0]))] * num_clusters
> 
>     for k in range(num_clusters):
> 
>         # Update means for cluster k using the M-step update rule for the mean variables.
> 
>         # This will assign the variable means[k] to be our estimate for \hat{\mu}_k.
> 
>         weighted_sum = 0.
> 
>         for i in range(num_data):
> 
>             # YOUR CODE HERE
> 
>             weighted_sum += ...
> 
>         # YOUR CODE HERE
> 
>         means[k] = ...
> 
>     return means
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_9:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_9:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_9:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_9 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_9 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_9 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_9:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_9.drop-target, .monaco-list.list_id_9 .monaco-list-rows.drop-target, .monaco-list.list_id_9 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint.**
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
> data_tmp = np.array([[1.,2.],[-1.,-2.]])
> 
> resp = compute_responsibilities(data=data_tmp, weights=np.array([0.3, 0.7]),
> 
>                                 means=[np.array([0.,0.]), np.array([1.,1.])],
> 
>                                 covariances=[np.array([[1.5, 0.],[0.,2.5]]), np.array([[1.,1.],[1.,2.]])])
> 
> counts = compute_soft_counts(resp)
> 
> means = compute_means(data_tmp, resp, counts)
> 
> if np.allclose(means, np.array([[-0.6310085, -1.262017], [0.25140299, 0.50280599]])):
> 
>     print 'Checkpoint passed!'
> 
> else:
> 
>     print 'Check your code again.'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_10:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_10:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_10:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_10 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_10 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_10 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_10:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_10.drop-target, .monaco-list.list_id_10 .monaco-list-rows.drop-target, .monaco-list.list_id_10 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Updating covariances**. The covariance of each cluster is set to the weighted average of all [outer products](https://people.duke.edu/~ccc14/sta-663/LinearAlgebraReview.html), weighted by the cluster responsibilities:
> 
> Σ^k=1Nksoft∑i=1Nrik(xi−μ^k)(xi−μ^k)T\hat{\Sigma}_k = \dfrac{1}{N^{\text{soft}}_k}\sum_{i=1}^N r_{ik} (x_i - \hat{\mu}_k)(x_i - \hat{\mu}_k)^TΣ^k​=Nksoft​1​∑i=1N​rik​(xi​−μ^​k​)(xi​−μ^​k​)T
> 
> The "outer product" in this context refers to the matrix product
> 
> (xi−μ^k)(xi−μ^k)T.(x_i - \hat{\mu}_k)(x_i - \hat{\mu}_k)^T.(xi​−μ^​k​)(xi​−μ^​k​)T.
> 
> Letting (xi−μ^k)(x_i - \hat{\mu}_k)(xi​−μ^​k​) to be d×1d \times 1d×1 column vector, this product is a d×dd \times dd×d matrix. Taking the weighted average of all outer products gives us the covariance matrix, which is also d×dd \times dd×d.
> 
> Complete the following function:
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
> def compute_covariances(data, resp, counts, means):
> 
>     num_clusters = len(counts)
> 
>     num_dim = len(data[0])
> 
>     num_data = len(data)
> 
>     covariances = [np.zeros((num_dim,num_dim))] * num_clusters
> 
>     for k in range(num_clusters):
> 
>         # Update covariances for cluster k using the M-step update rule for covariance variables.
> 
>         # This will assign the variable covariances[k] to be the estimate for \hat{\Sigma}_k.
> 
>         weighted_sum = np.zeros((num_dim, num_dim))
> 
>         for i in range(num_data):
> 
>             # YOUR CODE HERE (Hint: Use np.outer on the data[i] and this cluster's mean)
> 
>             weighted_sum += ...
> 
>         # YOUR CODE HERE
> 
>         covariances[k] = ...
> 
>     return covariances
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_11:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_11:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_11:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_11 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_11 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_11 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_11:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_11.drop-target, .monaco-list.list_id_11 .monaco-list-rows.drop-target, .monaco-list.list_id_11 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Checkpoint.**
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
> data_tmp = np.array([[1.,2.],[-1.,-2.]])
> 
> resp = compute_responsibilities(data=data_tmp, weights=np.array([0.3, 0.7]),
> 
>                                 means=[np.array([0.,0.]), np.array([1.,1.])],
> 
>                                 covariances=[np.array([[1.5, 0.],[0.,2.5]]), np.array([[1.,1.],[1.,2.]])])
> 
> counts = compute_soft_counts(resp)
> 
> means = compute_means(data_tmp, resp, counts)
> 
> covariances = compute_covariances(data_tmp, resp, counts, means)
> 
> if np.allclose(covariances[0], np.array([[0.60182827, 1.20365655], [1.20365655, 2.4073131]])) and \
> 
>     np.allclose(covariances[1], np.array([[ 0.93679654, 1.87359307], [1.87359307, 3.74718614]])):
> 
>     print 'Checkpoint passed!'
> 
> else:
> 
>     print 'Check your code again.'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_12:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_12:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_12:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_12 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_12 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_12 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_12:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_12.drop-target, .monaco-list.list_id_12 .monaco-list-rows.drop-target, .monaco-list.list_id_12 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **The EM algorithm.** We are almost done. Let us write a function that takes initial parameter estimates and runs EM. You should complete each line that says # YOUR CODE HERE.
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
> def EM(data, init_means, init_covariances, init_weights, maxiter=1000, thresh=1e-4):
> 
>     # Make copies of initial parameters, which we will update during each iteration
> 
>     means = init_means[:]
> 
>     covariances = init_covariances[:]
> 
>     weights = init_weights[:]
> 
>     # Infer dimensions of dataset and the number of clusters
> 
>     num_data = len(data)
> 
>     num_dim = len(data[0])
> 
>     num_clusters = len(means)
> 
>     # Initialize some useful variables
> 
>     resp = np.zeros((num_data, num_clusters))
> 
>     ll = loglikelihood(data, weights, means, covariances)
> 
>     ll_trace = [ll]
> 
>     for it in range(maxiter):
> 
>         if it % 5 == 0:
> 
>             print("Iteration %s" % it)
> 
>         # E-step: compute responsibilities
> 
>         resp = compute_responsibilities(data, weights, means, covariances)
> 
>         # M-step
> 
>         # Compute the total responsibility assigned to each cluster, which will be useful when 
> 
>         # implementing M-steps below. In the lectures this is called N^{soft}
> 
>         counts = compute_soft_counts(resp)
> 
>         # Update the weight for cluster k using the M-step update rule for the cluster weight, \hat{\pi}_k.
> 
>         # YOUR CODE HERE
> 
>         weights = ...
> 
>         # Update means for cluster k using the M-step update rule for the mean variables.
> 
>         # This will assign the variable means[k] to be our estimate for \hat{\mu}_k.
> 
>         # YOUR CODE HERE
> 
>         means = ...
> 
>         # Update covariances for cluster k using the M-step update rule for covariance variables.
> 
>         # This will assign the variable covariances[k] to be the estimate for \hat{\Sigma}_k.
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_13:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_13:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_13:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_13 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_13 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_13 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_13:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_13.drop-target, .monaco-list.list_id_13 .monaco-list-rows.drop-target, .monaco-list.list_id_13 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Testing the implementation on the simulated data
> 
> To help us develop and test our implementation, we will generate some observations from a mixture of Gaussians and then run our EM algorithm to discover the mixture components. We'll begin with a function to generate the data, and a quick plot to visualize its output for a 2-dimensional mixture of three Gaussians.
> 
> Now we will create a function to generate data from a mixture of Gaussians model.
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
> def generate_MoG_data(num_data, means, covariances, weights):
> 
>     """ Creates a list of data points """
> 
>     num_clusters = len(weights)
> 
>     data = []
> 
>     for i in range(num_data):
> 
>         #  Use np.random.choice and weights to pick a cluster id greater than or equal to 0 and less than num_clusters.
> 
>         k = np.random.choice(len(weights), 1, p=weights)[0]
> 
>         # Use np.random.multivariate_normal to create data from this cluster
> 
>         x = np.random.multivariate_normal(means[k], covariances[k])
> 
>         data.append(x)
> 
>     return data
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_14:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_14:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_14:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_14 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_14 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_14 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_14:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_14.drop-target, .monaco-list.list_id_14 .monaco-list-rows.drop-target, .monaco-list.list_id_14 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> After specifying a particular set of clusters (so that the results are reproducible across assignments), we use the above function to generate a dataset.
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
> # Model parameters
> 
> init_means = [
> 
>     [5, 0], # mean of cluster 1
> 
>     [1, 1], # mean of cluster 2
> 
>     [0, 5]  # mean of cluster 3
> 
> ]
> 
> init_covariances = [
> 
>     [[.5, 0.], [0, .5]], # covariance of cluster 1
> 
>     [[.92, .38], [.38, .91]], # covariance of cluster 2
> 
>     [[.5, 0.], [0, .5]]  # covariance of cluster 3
> 
> ]
> 
> init_weights = [1/4., 1/2., 1/4.]  # weights of each cluster
> 
> # Generate data
> 
> np.random.seed(4)
> 
> data = generate_MoG_data(100, init_means, init_covariances, init_weights)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_15:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_15:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_15:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_15 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_15 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_15 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_15:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_15.drop-target, .monaco-list.list_id_15 .monaco-list-rows.drop-target, .monaco-list.list_id_15 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Now plot the data you created above. The plot should be a scatterplot with 100 points that appear to roughly fall into three clusters.
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
> plt.figure()
> 
> d = np.vstack(data)
> 
> plt.plot(d[:,0], d[:,1],'ko')
> 
> plt.rcParams.update({'font.size':16})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_16:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_16:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_16:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_16 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_16 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_16 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_16:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_16.drop-target, .monaco-list.list_id_16 .monaco-list-rows.drop-target, .monaco-list.list_id_16 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/QE7kU3-XEead-BJkoDOYOw_7d5572541e14dfa28d8e24fbecc0610f_download-_20_.png?expiry=1657756800000&hmac=-wSheB_ZlRxF3DoQDdu0IOoqiLrrQnu8XXX8Jb1VDkI)
> 
> Now we'll fit a mixture of Gaussians to this data using our implementation of the EM algorithm. As with k-means, it is important to ask how we obtain an initial configuration of mixing weights and component parameters. In this simple case, we'll take three random points to be the initial cluster means, use the empirical covariance of the data to be the initial covariance in each cluster (a clear overestimate), and set the initial mixing weights to be uniform across clusters.
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
> np.random.seed(4)
> 
> # Initialization of parameters
> 
> chosen = np.random.choice(len(data), 3, replace=False)
> 
> initial_means = [data[x] for x in chosen]
> 
> initial_covs = [np.cov(data, rowvar=0)] * 3
> 
> initial_weights = [1/3.] * 3
> 
> # Run EM 
> 
> results = EM(data, initial_means, initial_covs, initial_weights)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_17:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_17:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_17:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_17 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_17 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_17 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_17:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_17.drop-target, .monaco-list.list_id_17 .monaco-list-rows.drop-target, .monaco-list.list_id_17 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Note**. Like k-means, EM is prone to converging to a local optimum. In practice, you may want to run EM multiple times with different random initialization. We have omitted multiple restarts to keep the assignment reasonably short. For the purpose of this assignment, we assign a particular random seed (seed=4) to ensure consistent results among the students.
> 
> **Checkpoint.** For this particular example, the EM algorithm is expected to terminate in 23 iterations. That is, the last line of the log should say "Iteration 22". If your function stopped too early or too late, you should re-visit your code.
> 
> Our algorithm returns a dictionary with five elements:
> 
> *   'loglik': a record of the log likelihood at each iteration
> 
> *   'resp': the final responsibility matrix
> 
> *   'means': a list of K means
> 
> *   'covs': a list of K covariance matrices
> 
> *   'weights': the weights corresponding to each model component
> 
> **Quiz Question:** What is the weight that EM assigns to the first component after running the above code block?
> 
> **Quiz Question**: Using the same set of results, obtain the mean that EM assigns the second component. What is the mean in the first dimension?
> 
> **Quiz Question**: Using the same set of results, obtain the covariance that EM assigns the third component. What is the variance in the first dimension?
> 
> **Plot progress of parameters.** One useful feature of testing our implementation on low-dimensional simulated data is that we can easily visualize the results.
> 
> We will use the following plot_contours function to visualize the Gaussian components over the data at three different points in the algorithm's execution:
> 
> 1.  At initialization (using initial_mu, initial_cov, and initial_weights)
> 
> 2.  After running the algorithm to completion
> 
> 3.  After just 12 iterations (using parameters estimates returned when setting maxiter=12)
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
> import matplotlib.mlab as mlab
> 
> def plot_contours(data, means, covs, title):
> 
>     plt.figure()
> 
>     plt.plot([x[0] for x in data], [y[1] for y in data],'ko') # data
> 
>     delta = 0.025
> 
>     k = len(means)
> 
>     x = np.arange(-2.0, 7.0, delta)
> 
>     y = np.arange(-2.0, 7.0, delta)
> 
>     X, Y = np.meshgrid(x, y)
> 
>     col = ['green', 'red', 'indigo']
> 
>     for i in range(k):
> 
>         mean = means[i]
> 
>         cov = covs[i]
> 
>         sigmax = np.sqrt(cov[0][0])
> 
>         sigmay = np.sqrt(cov[1][1])
> 
>         sigmaxy = cov[0][1]/(sigmax*sigmay)
> 
>         Z = mlab.bivariate_normal(X, Y, sigmax, sigmay, mean[0], mean[1], sigmaxy)
> 
>         plt.contour(X, Y, Z, colors = col[i])
> 
>         plt.title(title)
> 
>     plt.rcParams.update({'font.size':16})
> 
>     plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_18:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_18:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_18:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_18 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_18 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_18 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_18:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_18.drop-target, .monaco-list.list_id_18 .monaco-list-rows.drop-target, .monaco-list.list_id_18 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> If you are using other tools, look for library functions to visualize 2D Gaussian distributions.
> 
> Run the following code block to visualize the progress of EM at initialization, after 12 iterations, and after convergence.
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
> # Parameters after initialization
> 
> plot_contours(data, initial_means, initial_covs, 'Initial clusters')
> 
> # Parameters after 12 iterations
> 
> results = ... # YOUR CODE HERE
> 
> plot_contours(data, results['means'], results['covs'], 'Clusters after 12 iterations')
> 
> # Parameters after running EM to convergence
> 
> results = EM(data, initial_means, initial_covs, initial_weights)
> 
> plot_contours(data, results['means'], results['covs'], 'Final clusters')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_19:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_19:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_19:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_19 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_19 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_19 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_19:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_19.drop-target, .monaco-list.list_id_19 .monaco-list-rows.drop-target, .monaco-list.list_id_19 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Quiz Question**: Plot the loglikelihood that is observed at each iteration. Is the loglikelihood plot monotonically increasing, monotonically decreasing, or neither [multiple choice]? Complete the following code block to answer the question.
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
> results = EM(data, initial_means, initial_covs, initial_weights)
> 
> # YOUR CODE HERE
> 
> loglikelihoods = ...
> 
> plt.plot(range(len(loglikelihoods)), loglikelihoods, linewidth=4)
> 
> plt.xlabel('Iteration')
> 
> plt.ylabel('Log-likelihood')
> 
> plt.rcParams.update({'font.size':16})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_20:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_20:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_20:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_20 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_20 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_20 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_20:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_20.drop-target, .monaco-list.list_id_20 .monaco-list-rows.drop-target, .monaco-list.list_id_20 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> ### Fitting a Gaussian mixture model for image data
> 
> Now that we're confident in our implementation of the EM algorithm, we'll apply it to cluster some more interesting data. In particular, we have a set of images that come from four categories: sunsets, rivers, trees and forests, and cloudy skies. For each image we are given the average intensity of its red, green, and blue pixels, so we have a 3-dimensional representation of our data. Our goal is to find a good clustering of these images using our EM implementation; ideally our algorithm would find clusters that roughly correspond to the four image categories.
> 
> To begin with, we'll take a look at the data and get it in a form suitable for input to our algorithm. The data are provided in SFrame format:
> 
>  `1
> 
> 2
> 
> images = sframe.SFrame('images.sf/')
> 
> images['rgb'] = images.pack_columns(['red', 'green', 'blue'])['X4']
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_21:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_21:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_21:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_21 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_21 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_21 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_21:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_21.drop-target, .monaco-list.list_id_21 .monaco-list-rows.drop-target, .monaco-list.list_id_21 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> _(Optional) Generating dataset from original images_. You are free to experiment with other tools to generate 3-dimensional representation of images yourself. For each images, you should compute the average pixel value of each color channel and then divide the average by 256:
> 
>  `1
> 
> 2
> 
> 3
> 
> # arr = 3D array of pixels, with dimensions (width, height, 3)
> 
> r, g, b = np.mean(arr[:,:,0]/256.0), np.mean(arr[:,:,1]/256.0), np.mean(arr[:,:,2]/256.0)IniIni
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_22:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_22:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_22:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_22 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_22 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_22 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_22:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_22.drop-target, .monaco-list.list_id_22 .monaco-list-rows.drop-target, .monaco-list.list_id_22 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Initialization**. We need to come up with initial estimates for the mixture weights and component parameters. Let's take three images to be our initial cluster centers, and let's initialize the covariance matrix of each cluster to be diagonal with each element equal to the sample variance from the full data. As in our test on simulated data, we'll start by assuming each mixture component has equal weight.
> 
> This may take a few minutes to run.
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
> np.random.seed(1)
> 
> # Initalize parameters
> 
> init_means = [images['rgb'][x] for x in np.random.choice(len(images), 4, replace=False)]
> 
> cov = np.diag([images['red'].var(), images['green'].var(), images['blue'].var()])
> 
> init_covariances = [cov, cov, cov, cov]
> 
> init_weights = [1/4., 1/4., 1/4., 1/4.]
> 
> # Convert rgb data to numpy arrays
> 
> img_data = [np.array(i) for i in images['rgb']]  
> 
> # Run our EM algorithm on the image data using the above initializations. 
> 
> # This should converge in about 125 iterations
> 
> out = EM(img_data, init_means, init_covariances, init_weights)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_23:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_23:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_23:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_23 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_23 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_23 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_23:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_23.drop-target, .monaco-list.list_id_23 .monaco-list-rows.drop-target, .monaco-list.list_id_23 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The following sections will evaluate the results by asking the following questions:
> 
> *   **Convergence**: How did the log likelihood change across iterations? Did the algorithm achieve convergence?
> 
> *   **Uncertainty**: How did cluster assignment and uncertainty evolve?
> 
> *   **Interpretability**: Can we view some example images from each cluster? Do these clusters correspond to known image categories?
> 
> **Evaluating convergence.** Let's start by plotting the log likelihood at each iteration - we know that the EM algorithm guarantees that the log likelihood can only increase (or stay the same) after each iteration, so if our implementation is correct then we should see an increasing function.
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
> ll = out['loglik']
> 
> plt.plot(range(len(ll)),ll,linewidth=4)
> 
> plt.xlabel('Iteration')
> 
> plt.ylabel('Log-likelihood')
> 
> plt.rcParams.update({'font.size':16})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_24:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_24:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_24:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_24 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_24 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_24 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_24:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_24.drop-target, .monaco-list.list_id_24 .monaco-list-rows.drop-target, .monaco-list.list_id_24 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> The log likelihood increases so quickly on the first few iterations that we can barely see the plotted line. Let's plot the log likelihood after the first three iterations to get a clearer view of what's going on:
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
> plt.figure()
> 
> plt.plot(range(3,len(ll)),ll[3:],linewidth=4)
> 
> plt.xlabel('Iteration')
> 
> plt.ylabel('Log-likelihood')
> 
> plt.rcParams.update({'font.size':16})
> 
> plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_25:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_25:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_25:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_25 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_25 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_25 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_25:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_25.drop-target, .monaco-list.list_id_25 .monaco-list-rows.drop-target, .monaco-list.list_id_25 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> **Evaluating uncertainty**. Next we'll explore the evolution of cluster assignment and uncertainty. Remember that the EM algorithm represents uncertainty about the cluster assignment of each data point through the responsibility matrix. Rather than making a 'hard' assignment of each data point to a single cluster, the algorithm computes the responsibility of each cluster for each data point, where the responsibility corresponds to our certainty that the observation came from that cluster.
> 
> We can track the evolution of the responsibilities across iterations to see how these 'soft' cluster assignments change as the algorithm fits the Gaussian mixture model to the data; one good way to do this is to plot the data and color each point according to its cluster responsibilities. Our data are three-dimensional, which can make visualization difficult, so to make things easier we will plot the data using only two dimensions, taking just the [R G], [G B] or [R B] values instead of the full [R G B] measurement for each observation.
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
> import colorsys
> 
> def plot_responsibilities_in_RB(img, resp, title):
> 
>     N, K = resp.shape
> 
>     HSV_tuples = [(x*1.0/K, 0.5, 0.9) for x in range(K)]
> 
>     RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
> 
>     R = img['red']
> 
>     B = img['blue']
> 
>     resp_by_img_int = [[resp[n][k] for k in range(K)] for n in range(N)]
> 
>     cols = [tuple(np.dot(resp_by_img_int[n], np.array(RGB_tuples))) for n in range(N)]
> 
>     plt.figure()
> 
>     for n in range(len(R)):
> 
>         plt.plot(R[n], B[n], 'o', c=cols[n])
> 
>     plt.title(title)
> 
>     plt.xlabel('R value')
> 
>     plt.ylabel('B value')
> 
>     plt.rcParams.update({'font.size':16})
> 
>     plt.tight_layout()
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_26:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_26:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_26:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_26 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_26 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_26 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_26:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_26.drop-target, .monaco-list.list_id_26 .monaco-list-rows.drop-target, .monaco-list.list_id_26 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> To begin, we will visualize what happens when each data has random responsibilities.
> 
>  `1
> 
> 2
> 
> 3
> 
> N, K = out['resp'].shape
> 
> random_resp = np.random.dirichlet(np.ones(K), N)
> 
> plot_responsibilities_in_RB(images, random_resp, 'Random responsibilities')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_27:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_27:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_27:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_27 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_27 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_27 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_27:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_27.drop-target, .monaco-list.list_id_27 .monaco-list-rows.drop-target, .monaco-list.list_id_27 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Fzqik0CHEeai_BLpE3ZESw_4d0bbbe565b208650cd3113aa470fc7a_download-_5_.png?expiry=1657756800000&hmac=xBRmCaFiuIITmfO7YNpKiXV6yX3HqOKjvPQV8dWcVOs)
> 
> We now use the above plotting function to visualize the responsibilities after 1 iteration.
> 
>  `1
> 
> 2
> 
> out = EM(img_data, init_means, init_covariances, init_weights, maxiter=1)
> 
> plot_responsibilities_in_RB(images, out['resp'], 'After 1 iteration')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_28:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_28:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_28:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_28 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_28 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_28 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_28:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_28.drop-target, .monaco-list.list_id_28 .monaco-list-rows.drop-target, .monaco-list.list_id_28 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/s5silkCHEeaBig4GYhAaLQ_83ef0fa19cbbbf28cea8486a6b54c171_download-_6_.png?expiry=1657756800000&hmac=7WRy_cbHLrYnhJvqpRrvQr_RMTGcT9dbr5dQpC8pH-c)
> 
> We now use the above plotting function to visualize the responsibilities after 20 iterations. We will see there are fewer unique colors; this indicates that there is more certainty that each point belongs to one of the four components in the model.
> 
>  `1
> 
> 2
> 
> out = EM(img_data, init_means, init_covariances, init_weights, maxiter=20)
> 
> plot_responsibilities_in_RB(images, out['resp'], 'After 20 iterations')
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_29:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_29:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_29:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_29 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_29 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_29 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_29:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_29.drop-target, .monaco-list.list_id_29 .monaco-list-rows.drop-target, .monaco-list.list_id_29 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/u7gpyECHEeaCKhKaSMZqmQ_e1d81c0833968d731fc37c4002869c72_download-_7_.png?expiry=1657756800000&hmac=lZ0Zs00wMZoK6IVJQQoYrWVnhPsAmhFYhny0Kbw8jmE)
> 
> Plotting the responsibilities over time in [R B] space shows a meaningful change in cluster assignments over the course of the algorithm's execution. While the clusters look significantly better organized at the end of the algorithm than they did at the start, it appears from our plot that they are still not very well separated. We note that this is due in part our decision to plot 3D data in a 2D space; everything that was separated along the G axis is now "squashed" down onto the flat [R B] plane. If we were to plot the data in full [R G B] space, then we would expect to see further separation of the final clusters. We'll explore the cluster interpretability more in the next section.
> 
> ### Interpreting each cluster
> 
> Let's dig into the clusters obtained from our EM implementation. Recall that our goal in this section is to cluster images based on their RGB values. We can evaluate the quality of our clustering by taking a look at a few images that 'belong' to each cluster. We hope to find that the clusters discovered by our EM algorithm correspond to different image categories - in this case, we know that our images came from four categories ('cloudy sky', 'rivers', 'sunsets', and 'trees and forests'), so we would expect to find that each component of our fitted mixture model roughly corresponds to one of these categories.
> 
> If we want to examine some example images from each cluster, we first need to consider how we can determine cluster assignments of the images from our algorithm output. This was easy with k-means - every data point had a 'hard' assignment to a single cluster, and all we had to do was find the cluster center closest to the data point of interest. Here, our clusters are described by probability distributions (specifically, Gaussians) rather than single points, and our model maintains some uncertainty about the cluster assignment of each observation.
> 
> One way to phrase the question of cluster assignment for mixture models is as follows: how do we calculate the distance of a point from a distribution? Note that simple Euclidean distance might not be appropriate since (non-scaled) Euclidean distance doesn't take direction into account. For example, if a Gaussian mixture component is very stretched in one direction but narrow in another, then a data point one unit away along the 'stretched' dimension has much higher probability (and so would be thought of as closer) than a data point one unit away along the 'narrow' dimension.
> 
> In fact, the correct distance metric to use in this case is known as [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance). For a Gaussian distribution, this distance is proportional to the square root of the negative log likelihood. This makes sense intuitively - reducing the Mahalanobis distance of an observation from a cluster is equivalent to increasing that observation's probability according to the Gaussian that is used to represent the cluster. This also means that we can find the cluster assignment of an observation by taking the Gaussian component for which that observation scores highest. We'll use this fact to find the top examples that are 'closest' to each cluster.
> 
> **Quiz Question:** Calculate the likelihood (score) of the first image in our data set (images[0]) under each Gaussian component through a call to multivariate_normal.pdf. Given these values, what cluster assignment should we make for this image? Hint: don't forget to use the cluster weights.
> 
> Now we calculate cluster assignments for the entire image dataset using the result of running EM for 20 iterations above:
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
> weights = out['weights']
> 
> means = out['means']
> 
> covariances = out['covs']
> 
> rgb = images['rgb']
> 
> N = len(images) # number of images
> 
> K = len(means) # number of clusters
> 
> assignments = [0]*N
> 
> probs = [0]*N
> 
> for i in range(N):
> 
>     # Compute the score of data point i under each Gaussian component:
> 
>     p = np.zeros(K)
> 
>     for k in range(K):
> 
>         p[k] = weights[k]*multivariate_normal.pdf(rgb[i], mean=means[k], cov=covariances[k])
> 
>     # Compute assignments of each data point to a given cluster based on the above scores:
> 
>     assignments[i] = np.argmax(p)
> 
>     # For data point i, store the corresponding score under this cluster assignment:
> 
>     probs[i] = np.max(p)
> 
> assignments = sframe.SFrame({'assignments':assignments, 'probs':probs, 'image': images['image']})
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_30:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_30:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_30:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_30 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_30 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_30 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_30:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_30.drop-target, .monaco-list.list_id_30 .monaco-list-rows.drop-target, .monaco-list.list_id_30 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> We'll use the 'assignments' SFrame to find the top images from each cluster by sorting the datapoints within each cluster by their score under that cluster (stored in probs). We can plot the corresponding images in the original data using show().
> 
> Create a function that returns the top 5 images assigned to a given category in our data (HINT: use the SFrame function topk(column, k) to find the k top values according to specified column in an SFrame).
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
> def get_top_images(assignments, cluster, k=5):
> 
>     # YOUR CODE HERE
> 
>     images_in_cluster = ...
> 
>     top_images = images_in_cluster.topk('probs', k)
> 
>     return top_images['image']
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_31:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_31:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_31:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_31:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_31:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_31:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_31:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_31 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_31 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_31 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_31 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_31:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_31.drop-target, .monaco-list.list_id_31 .monaco-list-rows.drop-target, .monaco-list.list_id_31 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Here are some utility function to display the top images.
> 
> *   IPython notebook users: use display_images().
> 
> *   Others: use save_images(). This will save the images instead of displaying them on the screen.
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
> def display_images(images):
> 
>     from IPython.display import display
> 
>     for image in images:
> 
>         display(Image.open(BytesIO(image._image_data)))
> 
> def save_images(images, prefix):
> 
>     for i, image in enumerate(images):
> 
>         Image.open(BytesIO(image._image_data)).save(prefix % i)
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_32:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_32:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_32:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_32:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_32:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_32:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_32:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_32 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_32 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_32 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_32 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_32:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_32.drop-target, .monaco-list.list_id_32 .monaco-list-rows.drop-target, .monaco-list.list_id_32 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> Run the following to display the top images.
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
> for component_id in range(4):
> 
>     print 'Component {0:d}'.format(component_id)
> 
>     images = get_top_images(assignments, component_id)
> 
>     display_images(images)
> 
>     #save_images(images, 'component_{0:d}_%d.jpg'.format(component_id))
> 
>     print '\n'
> 
> Enter to Rename, Shift+Enter to Preview
> 
> .monaco-list.list_id_33:focus .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_33:focus .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_33:focus .monaco-list-row.selected { background-color: #0069d1; } .monaco-list.list_id_33:focus .monaco-list-row.selected:hover { background-color: #0069d1; } .monaco-list.list_id_33:focus .monaco-list-row.selected { color: #ffffff; } .monaco-drag-image, .monaco-list.list_id_33:focus .monaco-list-row.selected.focused { background-color: #0074e8; } .monaco-drag-image, .monaco-list.list_id_33:focus .monaco-list-row.selected.focused { color: #ffffff; } .monaco-list.list_id_33 .monaco-list-row.focused { background-color: #d6ebff; } .monaco-list.list_id_33 .monaco-list-row.focused:hover { background-color: #d6ebff; } .monaco-list.list_id_33 .monaco-list-row.selected { background-color: #e4e6f1; } .monaco-list.list_id_33 .monaco-list-row.selected:hover { background-color: #e4e6f1; } .monaco-list.list_id_33:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color: #f0f0f0; } .monaco-list.list_id_33.drop-target, .monaco-list.list_id_33 .monaco-list-rows.drop-target, .monaco-list.list_id_33 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; } .monaco-list-type-filter { background-color: #efc1ad } .monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); } .monaco-list-type-filter.no-matches { border: 1px solid #be1100; } .monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }` 
> 
> These look pretty good! Our algorithm seems to have done a good job overall at 'discovering' the four categories that from which our image data was drawn. It seems to have had the most difficulty in distinguishing between rivers and cloudy skies, probably due to the similar color profiles of images in these categories; if we wanted to achieve better performance on distinguishing between these categories, we might need a richer representation of our data than simply the average [R G B] values for each image.
> 
> **Quiz Question:** Which of the following images are _not_ in the list of top 5 images in the first cluster?
> 
> ![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/pRKEFkCJEeai_BLpE3ZESw_05c31c4e5639c6ef5b7021b11006a900_chosen_images.png?expiry=1657756800000&hmac=vSyVIhtmWmfgOxo9ByOrD4bqjfOB2CDlhXOLHk-TCHc)
>
> -- https://www.coursera.org/learn/ml-clustering-and-retrieval/supplement/XbP9U/implementing-em-for-gaussian-mixtures#main
