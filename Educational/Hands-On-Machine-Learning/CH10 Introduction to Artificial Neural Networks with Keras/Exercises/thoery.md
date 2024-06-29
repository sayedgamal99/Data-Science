# Exercises: CH10 Introduction to Artificial Neural Networks with Keras

2. Draw an ANN using the original artificial neurons (like the ones in Figure 10-3)
   that computes A ⊕ B (where ⊕ represents the XOR operation). Hint: A ⊕ B =
   (A ∧ ¬ B) ∨ (¬ A ∧ B).

this problem cannot solve without idea of MLP (multi layer), cannot solve with one layer like in figure 10-3.

so, here's the solution:

![xor ann](https://raw.githubusercontent.com/ageron/handson-ml3/d2b4c73e9741fb5e28358c8b2932421c6ef89790//images/ann/exercise2.png)

---

3. Why is it generally preferable to use a logistic regression classifier rather than a
   classic perceptron (i.e., a single layer of threshold logic units trained using the
   perceptron training algorithm)? How can you tweak a perceptron to make it
   equivalent to a logistic regression classifier?

The answer in the word 'Logistic' which refers to the logistic/sigmoid activation function which is non-linear which allow the model to capture non-linearity property.<br>
the sigmoid is continuos function which can produce probability [0,1].
we can tweak it to logistic if we change the step function to be sigmoid.

4. Why was the sigmoid activation function a key ingredient in training the first MLPs?

The sigmoid activation function was a key ingredient in training the first MLPs because its derivative is always nonzero, so Gradient Descent can always roll down the slope. When the activation function is a step function, Gradient Descent cannot move, as there is no slope at all.

5. Name three popular activation functions. Can you draw them?

1- Sigmoid activation: used in logistic regression or any binary classification problem as output layer, range: [0,1]

$$\sigma(z) = {1\over{1+e^{-z}}}$$

2- tanh (hyperbolic tangent function): used in hidden layers as activation function, just like sigmoid but with wider range [-1,1]. this make layer outputs more or less centered about 0 at the beginning which speed up convergence.

$$tanh(z) = 2\sigma(2z) -1$$

3- Relu (rectified linear unit function): one is the common choices in hidden layers activations, known for it's speed of computation (reason it's simple), has no maximum

$$relu(z) = max(0,z)$$

<br>

6. Suppose you have an MLP composed of one input layer with 10 passthrough
   neurons, followed by one hidden layer with 50 artificial neurons, and finally
   one output layer with 3 artificial neurons. All artificial neurons use the ReLU
   activation function.<br>

a. What is the shape of the input matrix X?<br>
b. What are the shapes of the hidden layer’s weight matrix W and bias vector b?<br>
c. What are the shapes of the output layer’s weight matrix Wo and bias vector bo?<br>
d. What is the shape of the network’s output matrix Y?<br>
e. Write the equation that computes the network’s output matrix Y as a function of X, Wh, bh, Wo, and bo.<br>

X.shape = (m, 10), m is batch size, 10 is number of features<br>
W.shape = (10, 50), 50 is number of neurons in the layer, b.shape = (50,1)<br>
Wo.shape = (50,3), bo.shape = (3,1)<br>
Y.shape = (m,3)

$$Y = relu(relu(X.Wh + bh).Wo +bo)$$
<br>

7. How many neurons do you need in the output layer if you want to classify email
   into spam or ham? What activation function should you use in the output layer?
   If instead you want to tackle MNIST, how many neurons do you need in the
   output layer, and which activation function should you use? What about for
   getting your network to predict housing prices, as in Chapter 2?

We only need **one** layer with sigmoid activation function for email classification.<br>
In case of Mnist with 10 classes, we need **10** neurons with softmax activation function.<br>
Regression task like prediction of housing prices needs only **one** neuron to predict one value with Relu activation function (or use linear).

8. What is backpropagation and how does it work? What is the difference between
   backpropagation and reverse-mode autodiff?

Backpropagation is a technique used to train artificial neural networks. it use chain rule to compute gradients in reverse mode (traversing the network from output layer to input layer), computing gradients and then using it to update the weights. so in summary backpropagation computes gradient and do optimization as well.<br>

Reverse-mode autodiff performs a forward pass through a computation graph, computing every node's value for the current training batch, and then it performs a reverse pass, computing all the gradients at once.<br>

so backpropagation combines reverse-mode autodiff with optimization to train the NN.

9. Can you list all the hyperparameters you can tweak in a basic MLP? If the MLP
   overfits the training data, how could you tweak these hyperparameters to try to
   solve the problem?

Learning rate, batch size, # of epochs, # of hidden layers, # of neurons in each hidden layer, optimizer (adam, sgd,..), activation functions in hidden layers

if MLP overfits the tr data, we can using early stopping (# of epochs), down hidden layers, # of neurons.
