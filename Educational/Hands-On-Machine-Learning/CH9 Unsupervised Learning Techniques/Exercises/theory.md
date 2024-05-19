# CH9 Unsupervised Learning Techniques Exercises

1. How would you define clustering? Can you name a few clustering algorithms?

clustering is grouping data instances to a number of clusters (say k) based on their similarity to each other.
k-means, dbscan

<br>
<br>

2. What are some of the main applications of clustering algorithms?

clustering can be used on image segmentation (color, semantic, instance), semi-supervised learning, dimensionality reduction

<br>
<br>

3. Describe two techniques to select the right number of clusters when using
   k-means.

silhouette score or diagram which is the best, and inertia with elbow technique.

<br>
<br>

4. What is label propagation? Why would you implement it, and how?

label propagation is semi-supervised learning technique that after we apply clustering on data instances, we pick 'core' instances which are instances that represent the clusters and give them label manually, then `label propagation` come to give all cluster instances the same label of the core instance of it's cluster.

<br>
<br>

5. Can you name two clustering algorithms that can scale to large datasets? And two
   that look for regions of high density?

mini-batch k-means can scale very well to large datasets,
algorithms that looks for region of high density are gaussian mixture

<br>
<br>

6. Can you think of a use case where active learning would be useful? How would
   you implement it?

i think we could use it on critical applications such as medical diagnoses and military applications of detecting enemies
on military apps i can imagine there's learning algorithms that learned to detect enemies and we use active learning with it as if it receives picture of enemy and it isn't confident with it we pass it to human to label it and so on..

<br>
<br>
7. What is the difference between anomaly detection and novelty detection?

both used to detect outliers (anomalies) but the difference is in the data it self.
anomaly detection algorithm trained on data that have anomalies already (not clean dataset),
novelty detection algorithm trained on `clean` dataset that doesn't contain any outliers.

<br>
<br>

8. What is a Gaussian mixture? What tasks can you use it for?

gaussian mixture is an probabilistic model that used for clustering similar to k-means with a key difference:
it assumes that data come from k gaussian distributions with unknown parameters.
we can use it for clustering, anomaly detection.

<br>
<br>

9. Can you name two techniques to find the right number of clusters when using a
   Gaussian mixture model?

we can try to find model that minimized theoretical information criterion:
AIC
BIC
