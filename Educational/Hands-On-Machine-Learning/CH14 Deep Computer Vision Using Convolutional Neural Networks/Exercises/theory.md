# CH14 Exercises: Loading and Preprocessing Data With Tensorflow

1. What are the advantages of a CNN over a fully connected DNN for image classification?

One of the advantages of cnn over regular dnn is computation cost and efficiency
and this help reducing overfitting and reducing parameters

other thing is the translation invariance ( means that the cnn learns shared parameters for the filters)
not the same for dnn each neuron is independent, once the pattern detected in some region of the image, it also
can be detected for sure ( because the parameters of the filter is shared for all image regions) in any other regions.

<br>
<br>

---

2.  Consider a CNN composed of three convolutional layers, each with 3 × 3 kernels,
    a stride of 2, and "same" padding. The lowest layer outputs 100 feature maps,
    the middle one outputs 200, and the top one outputs 400.
    The input images are RGB images of 200 × 300 pixels:

    a. What is the total number of parameters in the CNN?

    902,700 parameter (ignoring the biases parameters which are (100+200+400) params for the 3 layers respectively ), when not ignoring the biases, the result is **903,400**.
    explained in the picture below:

![CNN explained](https://github.com/sayedgamal99/Data-Science/raw/main/Educational/Hands-On-Machine-Learning/CH14%20Deep%20Computer%20Vision%20Using%20Convolutional%20Neural%20Networks/Exercises/Images/conv%20net.jpg)

    b. If we are using 32-bit floats, at least how much RAM will this network require
    when making a prediction for a single instance?

    first we calculate the size of the feature maps. Since the 32 bit is 4 bytes. **First layer** (100 feature maps) adds up to 100x150x100x4 = 6x10^6 bytes >> (6MB), **Second Layer** (200 feature maps) adds up to 75x50x200x4 = (3MB), **Third Layer** (400 FM) = 38x25x4x400 = (1.5MB).
    When Layer computed the memory occupied by the previous layers released.
    Plus the memory occupied by the parameters ( 903,400 x 4 >> 3.6 MB)

    total ram memory needed is about 14 MB if no more optimization and no releases in the memory after passing layers.

    c. What about when training on a mini-batch of 50 images?

During Training, when forward propagation, the size of input images is (4x200x300x50x3 >> 36MB), size of parameters computed (3.6 MB), size of feature map computed: (6+3+1.5 = 10.5MB )per instance, per batch ( >> 10.5 \*50 = 505 MB), so the total memory needed ( neglecting the backpropagation gradients ) is (505+3.6+36 = 564.6MB)

<br>
<br>

---

3.  If your GPU runs out of memory while training a CNN, what are five things you could try to solve the problem?

         1. I will reduce the batch-size.
         2. reduce the size of parameters with using lower precision data-type (e.g. float16 instead of float32).
         3. reducing the cnn size ( by removing some layers )
         4. reducing the dimensionality by using strides.
         5. distribute the cnn across multiple devices

<br>
<br>

---

4.  Why would you want to add a max pooling layer rather than a convolutional layer with the same stride?

             To let the convolution scan the whole input volume, with using strides in the Conv layer we might skip some information that could be useful.
             Plus the max-pooling layer is used to extract important information (by doing the max function) which is not the case for the convolution operation.

    <br>
    <br>

---

5.  When would you want to add a local response normalization layer?

             It is useful when we want to add more generalization, or avoid the overfitting issue.
             because if focuses on the important information and do normalization for all it's neighbors(including it), which signify this info.

    <br>
    <br>

---

6. Can you name the main innovations in AlexNet, as compared to LeNet-5?
   What about the main innovations in GoogLeNet, ResNet, SENet, Xception, and
   EfficientNet?

   1. The main innovations in AlexNet compared with LeNet are that is is much larger and deeper, and it stacks convolutional layers directly on top of each other, instead of using pooling after each one.
   2. **GoogleNet** :
      Inception modules: The most important innovation of GoogLeNet is the "inception module," which applies multiple filters of different sizes (1x1, 3x3, 5x5) in parallel and concatenates their outputs. This allows the network to capture features at multiple scales and avoids the problem of deciding on a single kernel size.
      1x1 convolutions: Used 1x1 convolutions for dimensionality reduction, which helped reduce the computational cost while keeping the network deep.
      Deeper network: GoogLeNet had 22 layers, deeper than previous models like AlexNet but more efficient in terms of the number of parameters, thanks to inception modules.

   3. **ResNet** :
      Residual block is the main block in this architecture, It is relies on skip connection and force the
      layers to learn identity function, avoiding vanishing gradients problem. build very deep ( more layers ) network
   4. **SeNet** :
      Using the SE block ( two layer dense network after the global average pooling ) after every inception module or residual unit. to recalibrate the relative important of feature maps.
   5. **Xception** :
      Using the _depth-wise-separable-convolution_ technique, which looks at spatial information and depthwise patterns separately. That reduces the number of parameters
   6. **EfficientNet** :
      The Compound scaling method, to efficiently scale a model to a larger compute budget
      <br>
      <br>

---

7. What is a fully convolutional network? How can you convert a dense layer into a
   convolutional layer?

   The FCN is architecture when not using the few dense layers on the top of the models. but The whole network is composed of convolution and pooling layers. The make the layer capable of processing images with any width and height.
   They are useful for object detection and sematic segmentation because it needs to see the image once, rather than run cnn multiple times on different parts of the images. Converting dense layer into a conv layer by using kernel size of the same size as input layer size. With one filter per neuron in the dense layer. and using 'valid' padding, strides of 1. using 1x1 conv is also possible.
   <br>
   <br>

---

8. What is the main technical difficulty of semantic segmentation?

   The main technical difficulty of semantic segmentation is the fact that the spatial information gets lost in the CNN as the signal flow through pooling layers and layers with strides more than 1, The spatial information needs to be restored somehow to accurately predict the class of each pixel.
