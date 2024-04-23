# CH8 Dimensionality Reduction Exercises


1. What are the main motivations for reducing a dataset’s dimensionality? What are
the main drawbacks?

    - Do optimization (saving time and recourses)when running ml models on this dataset ( assuming any unimportant features exist)
    - compressing data will save space.
    - reduce dimensionality to be Able to `Visualize` the data (2d or 3d) gaining insights about the data.

    - **DrawBacks** : Losing information.. we can easily loosing information that maybe help improving performance
    - It can be computationally intensive.
    - It adds some complexity to your Machine Learning pipelines.
    Transformed features are often hard to interpret.

2. What is the curse of dimensionality?

    - Presence of many **unimportant** features causing Slower and harder Training process

3. Once a dataset’s dimensionality has been reduced, is it possible to reverse the
operation? If so, how? If not, why?

    - we can reverse the operation successfully but can't restore dropped features. (the example of images: recompressed images are similar to origin but has noise resulting from losing information when compressing)

4. Can PCA be used to reduce the dimensionality of a highly nonlinear dataset?

    - PCA can be used to significantly reduce the dimensionality of most datasets, even if they are highly nonlinear, **because it can at least get rid of useless dimensions**. However, if there are no useless dimensions—as in the Swiss roll dataset—then reducing dimensionality with **PCA will lose too much information**. You want to unroll the Swiss roll, not squash it.


5. Suppose you perform PCA on a 1,000-dimensional dataset, setting the explained
variance ratio to 95%. How many dimensions will the resulting dataset have?

    - we can't tell how many dimensions will produced after PCA. It depends on the data itself.
    -  Plotting the explained variance as a function of the number of dimensions is one way to get a rough idea of the dataset's intrinsic dimensionality.


6. In what cases would you use regular PCA, incremental PCA, randomized PCA,
or random projection?

    - **Regular PCA**: we can use it when data can fit in the memory, else we use **Incremental PCA** but it is slower than regular PCA and incremental is useful for online tasks, when you need to apply PCA every time a new instance arrives. **Randomized PCA** is useful when you want to considerably reduce dimensionality and the dataset fits in memory; in this case, it is much faster than regular PCA. Finally, **Random Projection** is great for very `high-dimensional datasets`.



7. How can you evaluate the performance of a dimensionality reduction algorithm
on your dataset?

    - DimRed Algorithm works well when if it eliminates a lot of dimensions without loosing too much information.
    - we can decompress the data again (reverse the DR Process) and see the reconstruction error(not all dimensionality reduction algorithms provide a reverse transformation).
    - if we use it as preprocessing step before another machine learning algorithm, we can measure the performance of second algorithm, if dimensionality reduction did not lose too much information, then the algorithm should perform just as well as when using the original dataset.

8. Does it make any sense to chain two different dimensionality reduction
algorithms?

    - YES, example: using pca or random projection to get rid of large numbers of useless dimensions, then applying a much slower algorithm such LLE, these two steps can be approached using LLE in one step but differ greatly in time.
