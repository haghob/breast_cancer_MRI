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

3x3 sepconv, 32
pool 2,2
3x3 sepconv, 64
3x3 sepconv, 64
pool 2,2
3x3 sepconv, 128
3x3 sepconv, 128
3x3 sepconv, 128
pool 2,2
FC1
FC2
FC3
Softmax
