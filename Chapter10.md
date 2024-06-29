# K-nearest neighbors

You pick a data point in a dataset comparing two different things and based on what the closest neighbors to that thing is that's what we classify the object as.

Simple algorithm to implement but useful. 

## Usages 
### Building a recommendation system 
Suppose you're Netflix or some other streaming service. You want to build a movie recommendations system for your users. On a high level, this is similar to grapefruit problem.

Ratings and recommendations are based on user input (user ratings) on what they watch. This gives you a value system to be able to rate things by.

Pythagorean theorem is used to tell the distance between objects 

```
sqrt((x1-x2)^2+ (y1+y2)^2)
```
This formula can be expanded to have multiple points not just x and y 

This is also known as dimensions.

The more ratings you rate the more accurate Netflix or streaming service will be able to recommend movies for you.

## Regression 
Suppose you want to do more than just recommend a movie: you want to guess how the individual will rate this movie. Take the five people closest to her. 

In KNN - you do two things: 
1. Classification = categorization into a group 
2. Regression = predicting a response (like a number)


## Cosine Similarity 
Cosine Similarity doesn't measure the distance between two vectors. Instead, it compares the angles of the two vectors. It's better at dealing with cases like this. 

## Features

Keep in mind what you are trying to classify and account for biases. You want the features that you measure to be in line with what you are trying to introduce.

# Machine Learning 
KNN is a really useful algorithm, and it's your introduction to the magical world of machine learning! Machine learning is all about making your computer more intelligent. You already saw one example of machine learning: building a recommendation system.

## OCR 
OCR stands for optical character recognition. It means you can take a photo of a page of text and your computer will automatically read teh text for you. Google uses OCR to digitize books. 
1. Go thorugh a lot of images of numbers, and extract features of those numbers. 
2. When you get a new image, extract the features of that image, and see what it's nearest neighbors are! 

Complex ideas build upon KNN

You could use the same ideas for speech recognition or face recognition. When you uploada photo to Facebook, sometimes it's smart enough to tag people in the photo automatically. That's machine learning in action. 

The first step of OCR is called training. The next step involves spam filters, and it has a training step. 

## Building a SPAM filter 
Spam filters use another simple algorithm called the Naive Bayes Classifer. First you train your Naive Bayes classifier on some data. 

# RECAP: 

- KNN is used for classification and regression and involves looking at the k-nearest neighbors. 
- Classification = categorization into a group 
- Regression = predicting a response (like a number). 
- Feature extraction means converting an item (like a fruit or a user) into a list of numbers that can be compared. 
- Picking good features is an important part of successful KNN algorithm. 


