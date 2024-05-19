# CH9 Unsupervised Learning Techniques Exercises

1. How would you define clustering? Can you name a few clustering algorithms?

clustering is grouping data instances to a number of clusters (say k) based on their similarity to each other.
Popular clustering algorithms include K-Means, DBSCAN, agglomerative clustering, BIRCH, Mean-Shift, affinity propagation, and spectral

<br>
<br>

2. What are some of the main applications of clustering algorithms?

main applications clustering used on are data analysis, customer segmentation, recommender systems, search engines
clustering can be also used for image segmentation (color, semantic, instance), semi-supervised learning, dimensionality reduction and anomaly & novelty detection.

<br>
<br>

3. Describe two techniques to select the right number of clusters when using
   k-means.

The elbow rule is a simple technique to select the number of clusters when using K-Means: just plot the inertia (the mean squared distance from each instance to its nearest centroid) as a function of the number of clusters, and find the point in the curve where the inertia stops dropping fast (the "elbow"). This is generally close to the optimal number of clusters. Another approach is to plot the silhouette score as a function of the number of clusters. There will often be a peak, and the optimal number of clusters is generally nearby. The silhouette score is the mean silhouette coefficient over all instances. This coefficient varies from +1 for instances that are well inside their cluster and far from other clusters, to –1 for instances that are very close to another cluster. You may also plot the silhouette diagrams and perform a more thorough analysis.

<br>
<br>

4. What is label propagation? Why would you implement it, and how?

label propagation is semi-supervised learning technique that after we apply clustering on data instances, we pick 'core' instances which are instances that represent the clusters and give them label manually, then `label propagation` come to give all cluster instances the same label of the core instance of it's cluster.
this is an easy approach versus labeling all instances which often costly and time-consuming.
This can greatly extend the number of labeled instances, and thereby allow a supervised algorithm to reach better performance

<br>
<br>

5. Can you name two clustering algorithms that can scale to large datasets? And two that look for regions of high density?

K-Means and BIRCH scale well to large datasets. DBSCAN and Mean-Shift look for regions of high density.

<br>
<br>

6. Can you think of a use case where active learning would be useful? How would
   you implement it?

Active learning is useful whenever you have plenty of unlabeled instances but labeling is costly. In this case (which is very common), rather than randomly selecting instances to label, it is often preferable to perform active learning, where human experts interact with the learning algorithm, providing labels for specific instances when the algorithm requests them. A common approach is uncertainty sampling

<br>
<br>

7. What is the difference between anomaly detection and novelty detection?

both used to detect outliers (anomalies) but the difference is in the data it self.
anomaly detection algorithm trained on data that have anomalies already (not clean dataset),
novelty detection algorithm trained on `clean` dataset that doesn't contain any outliers.

Some algorithms work best for anomaly detection (e.g., Isolation Forest), while others are better suited for novelty detection (e.g., one-class SVM).

<br>
<br>

8. What is a Gaussian mixture? What tasks can you use it for?

A Gaussian mixture model (GMM) is a probabilistic model that assumes that the instances were generated from a mixture of several Gaussian distributions whose parameters are unknown. In other words, the assumption is that the data is grouped into a finite number of clusters, each with an ellipsoidal shape (but the clusters may have different ellipsoidal shapes, sizes, orientations, and densities), and we don't know which cluster each instance belongs to. This model is useful for density estimation, clustering, and anomaly detection.

<br>
<br>

9. Can you name two techniques to find the right number of clusters when using a
   Gaussian mixture model?

One way to find the right number of clusters when using a Gaussian mixture model is to plot the Bayesian information criterion (BIC) or the Akaike information criterion (AIC) as a function of the number of clusters, then choose the number of clusters that minimizes the BIC or AIC. Another technique is to use a Bayesian Gaussian mixture model, which automatically selects the number of clusters.

----
