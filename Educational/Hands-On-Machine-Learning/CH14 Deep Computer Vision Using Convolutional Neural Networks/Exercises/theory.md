# CH14 Exercises: Loading and Preprocessing Data With Tensorflow

1. What are the advantages of a CNN over a fully connected DNN for image classification?

The advantage of cnn over regular dnn is computation cost, for example if we has 3*3 filter cnn with 10 feature maps (filters), then 
we have now (3*3*10 = 90 parameter), on the other hand for dnn there's a lot. and this help reducing overfitting when reducing parameters

other thing is the transition invariance ( means that the cnn learns to share parameters for the filters) not the same for dnn each neuron is independent.


<br>
<br>

---

2.  Consider a CNN composed of three convolutional layers, each with 3 × 3 kernels, a stride of 2, and "same" padding. The lowest layer outputs 100 feature maps, the middle one outputs 200, and the top one outputs 400. The input images are RGB images of 200 × 300 pixels:

    a. What is the total number of parameters in the CNN?

    902,700 parameter

    b. If we are using 32-bit floats, at least how much RAM will this network require
    when making a prediction for a single instance?

    number of params * size of each param takes : 902,700 * 32 bit = 6.8 megabytes

    c. What about when training on a mini-batch of 50 images?

    *50?

<br>
<br>

---

3. If your GPU runs out of memory while training a CNN, what are five things you could try to solve the problem?

<br>
<br>

---

4. Why would you want to add a max pooling layer rather than a convolutional layer with the same stride?

<br>
<br>

---

5. When would you want to add a local response normalization layer?

<br>
<br>

---

6. Can you name the main innovations in AlexNet, as compared to LeNet-5?
   What about the main innovations in GoogLeNet, ResNet, SENet, Xception, and
   EfficientNet?

<br>
<br>

---

7. What is a fully convolutional network? How can you convert a dense layer into a
   convolutional layer?

<br>
<br>

---

8. What is the main technical difficulty of semantic segmentation?
