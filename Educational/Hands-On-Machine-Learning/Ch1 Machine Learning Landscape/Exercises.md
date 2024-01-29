# Ch1 Exercises: Machine Learning Landscape

1. How would you define machine learning?

```
ML is to make computer learn from data ( Experience ) to do some ( Task )
and having some (Performance) then be able to generalize it's output for unseen data( new situation )
and that happened without explicitly programming
```

2. Can you name four types of applications where it shines?

```
NLP ( Chatgpt ),
ComputerVision (facial recognition),
recommender search engine ( google ),
object detection and tracking ( football automated camera that track the ball where's gone)
```

3. What is a labeled training set?

```
That is the data that has label for each record of it ( or image ),
and the label mean that this image belongs to specific category,
which there is n category in the data
```

4. What are the two most common supervised tasks?

```
classification task ( Image classification)
Regression task ( prediction for houses prices or stock market)
```

5. Can you name four common unsupervised tasks?

```
Recommendation ( movies recommender system ),
Anomaly Detection ( manufacturing failure detector in industry),
Clustering ( group and divide the data into clusters),
association rule learning ( discover interesting information in the data provided)
```

6. What type of algorithm would you use to allow a robot to walk in various unknown terrains?

```
Reinforcement learning as it capable of learn the robot to do such complex things to do
```

7. What type of algorithm would you use to segment your customers into multiple groups?

```
Clustering ( unsupervised learning ) that would segment that data based on similarity
```

8. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem

```
Supervised learning because we learn the machine to know it spam or not by specifying some emails at first( labeling )
then train on it.
```

9. What is an online learning system?

```
The online learning is that the system is able to learn inclemently as new data is available,
either learn from data individually or divide it into mini-batches.
each learning step is cheap and fast so the system can learn on the fly or as new data point arrives.
```

10. What is out-of-core learning?

```
Is used to train the machine on huge amounts of data, that cannot be fit in memory, so it uses online learning techniques to
divide the data into batches and do training on.
```

11. What type of algorithm relies on a similarity measure to make predictions?

```
Clustering algorithms ( k-means )
instance based learning, when it given new instance it uses similarity measures to make predictions
```

12. What is the difference between a model parameter and a model hyperparameter?

```
the model parameter is that the model learned during the training process, like ( slope, bias)
and the hyperparameter that not being learned but user specify it from beginning of training. like ( learning rate, number of clusters)
```

13. What do model-based algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?

```
model based algorithms search for something like equation parameters for measure how well is that model perform on the data,
is called loss measure, and it tries to minimize it all time. This is opposite from instance-based learning that based on similarity measure
it's common strategy is to find best parameters for that equation and then once it takes new instance it feed it into the model ( equation for simplicity) and do math then get the output ( prediction ).
```

14. Can you name four of the main challenges in machine learning?

```
Non-representative dataset
model over-fitting
model under-fitting
insufficient quantity of training data
```

15. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?

```
This is called over-fitting challenge for the model, there is possible solutions:
- Simplify your model
- Use regularization ( increase the hyperparameter lambda )
- decrease number of used feature in feature selection step
- Gather more data
- Reducing noise on training set
```

16. What is a test set, and why would you want to use it?

```
the test set is set that used for final evaluation of the model performance just before deployment,
unseen data from the model and give indication about model performance or it's problems like generalization.
```

17. What is the purpose of a validation set?

```
The validation data set is used to measure how the model is doing outside the training set,
whether it has fitting well or not, to include in the loop of training process ( Train, validate,Changes( model, hyperparameter),Train ..)

```

18. What is the train-dev set, when do you need it, and how do you use it?

```
Train-dev set is subset from training set ( the model not trained on), that we use it when our model is being prepared to be used on mobile devices or do inference in another environments, it give indicates about model performance.

if the model:
- doing well on training set and poorly predict train-dev set: it has over-fitting
- doing well on both train, train-dev but poorly on validation: there is dis-match between the train examples and validation + test set
we need to make the train data just like validation or test ( example if we train the models on images taken by camera, and our task is to make
model classify images taken by mobile phone, there is a little difference here that mey cause dis-match on some cases)
```

19. What can go wrong if you tune hyperparameters using the test set?

```
It may generalize poorly on unseen data on the real world.
```

---
