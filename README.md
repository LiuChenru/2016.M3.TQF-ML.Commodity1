# 2016.M3.TQF-ML.Commodity1
this project is designed to predict commodity that user may buy

* Proposal: (https://github.com/LiuChenru/2016.M3.TQF-ML.Commodity1/blob/master/Chenru%20Liu_Proposal.pdf)
* PPT: (https://github.com/LiuChenru/2016.M3.TQF-ML.Commodity1/blob/master/ML%20PRE.pptx)


Description:

  We have a dataset which contain information about people's basic attribution and productions' basic attribution and people's interaction with product such as clicking and purchasing. We want to use the information we have to predict which commodity the user will buy in next five days.
  
Data source:

  Our data come from the a well-known shopping website in China. The data can be divided into 3 parts. First, the information about the user such as age, sex, class-level. Second, the production's attribute such as brand. Finally and most importantly, the actions of user with respect to specific product.
  
Method:

  We first turn our problem into a classification problem. Our final result's key is (user_id, product_id). We will get result 1 or 0 for this key, which means that if we get 1 we will predict that that user will buy that specific product in later 5 days.
  We will use a bunch of classfication methods we have learned in the ML class to solve problem.

Result:

  We have tried many ML algorithms. But many algorithms such as the Logistic Regression, SVM, K-NN. I think that these methods do not work well  because the data is highly unbalanced data which means that our data for class 1 is too sparse compared with class 0. What is more, our problem is not a linear problem.
  Our final model is Decision Tree model.
 
 
