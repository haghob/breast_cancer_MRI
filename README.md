## Part 1

The code reference I have used
https://github.com/sayakpaul/Breast-Cancer-Detection-using-Deep-Learning 

In fact, I am testing the **Fastai** library : 
https://dejanbatanjac.github.io/2019/03/15/ImageDataBunch.html 

**vision.data** contains the definition of **ImageDataBunch** and **DataBunch** 


It wasn't work.
*************************************************************************************

## Part 2

The code reference I'm using 
https://pyimagesearch.com/2019/02/18/breast-cancer-classification-with-keras-and-deep-learning/  

The model is CancerNet : https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-022-04783-y 
The optimizer that I tested : Adagrad, Adam 


**CancerNet** is a convolutional neural network (CNN) model that has been proposed for the classification of breast cancer histology images.

**CancerNet** is a deep learning model that utilizes several convolutional and pooling layers to learn features from the input images. The architecture of the model consists of multiple convolutional layers, followed by max pooling layers and then fully connected layers. The final layer is a softmax layer, which outputs the predicted probability distribution over the different classes of cancer.

**The CancerNet** model was designed to classify breast cancer histology images into four different classes: normal tissue, benign lesions, in situ carcinoma, and invasive carcinoma. It was trained on a large dataset of breast cancer images and achieved high accuracy in classification.

It's worth noting that there may be multiple versions of the CancerNet model, as deep learning researchers often make modifications to existing architectures to improve their performance on specific tasks or datasets.


## The architecture of our model 

(3x3) SepConv, 32
MaxPool (2,2)
(3x3) SepConv, 64
(3x3) SepConv, 64
MaxPool (2,2)
(3x3) SepConv, 128
(3x3) SepConv, 128
(3x3) SepConv, 128
MaxPool (2,2)
FC (256)
FC (2)
Softmax

********************************************************************
### Why ***SepConv  (Separable Convolution)*** ? 


More effective

Requires less memory

Requires fewer calculations

May perform better in some situations than normal convolution


### Why ***softmax*** ? 

Multi-class classification problem

The predictive model returns:

The predicted class (identified by a number for example).

The list of the probabilities of belonging to each class. 

The model then returns a probability vector, that is a vector of numbers between 0 and 1, the sum of which is 1.


### Precision:

Very accurate for benign tumors (95%) but much less for malignancies (about 70%).

This can be explained by the fact that benign tumors are probably more similar than malignant tumors that can be of different types therefore more complicated to detect because very specific depending on the cas

### Max-pooling : 

It selects maximum element from the feature map. The resulting max-pooled layer holds important features of feature map.

It is the most common approach as it gives better results.

ReLU sets all negative values to zero and all other values remains constant. It is mathematically represented as

![Diagram](Diagramme.png)



