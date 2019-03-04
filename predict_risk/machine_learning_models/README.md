# Heart-Disease-Prediction

Cardiovascular diseases are the leading cause of death globally, resulted in 17.9 million deaths (32.1%) in 2015, up from 12.3 million (25.8%) in 1990. It is estimated that 90% of CVD is preventable. There are many risk factors for heart diseases that we will take a closer look at.

The main objective of this study is to build a model that can predict the heart disease occurrence, based on a combination of features (risk factors) describing the disease. Different machine learning classification techniques will be implemented and compared upon standard performance metric such as accuracy.

The dataset used for this study was taken from UCI machine learning repository

Description:

This data set currently contains 303 instances, some of which aren't complete (some features may be missing for a certain instance). In the case that this happens, the instance has been removed. There are 14 relevant features which have been extracted, from a maximum of 76 in the total dataset.

Features information:

1.age - age in years

2.sex - sex(1 = male; 0 = female)

3.chest_pain - chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 4 = asymptomatic)

4.blood_pressure - resting blood pressure (in mm Hg on admission to the hospital)

5.serum_cholestoral - serum cholestoral in mg/dl

6.fasting_blood_sugar - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

7.electrocardiographic - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)

8.max_heart_rate - maximum heart rate achieved

9.induced_angina - exercise induced angina (1 = yes; 0 = no)

10.ST_depression - ST depression induced by exercise relative to rest

11.slope - the slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)

12.no_of_vessels - number of major vessels (0-3) colored by flourosopy

13.thal - 3 = normal; 6 = fixed defect; 7 = reversable defect

14.num:diagnosis - the predicted attribute - diagnosis of heart disease (angiographic disease status) (Value 0 = < 50% diameter narrowing; Value 1 = > 50% diameter narrowing)


Types of features:

A. Categorical features (Has two or more categories and each value in that feature can be categorised by them): sex, chest_pain


B. Ordinal features (Variable having relative ordering or sorting between the values): fasting_blood_sugar, electrocardiographic, induced_angina, slope, no_of_vessels, thal, diagnosis


C. Continuous features (Variable taking values between any two points or between the minimum or maximum values in the feature column): age, blood_pressure, serum_cholestoral, max_heart_rate, ST_depression

The main goal  is to predict heart disease occurrence with the highest accuracy. In order to achieve this, several classification algorithms are tested. 

1.LOGISTIC REGRESSION
2.NAIVE BAYES
3.DECISION TREE
4.SVC
