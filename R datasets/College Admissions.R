rm(list = ls())
# Step 1 - Import the data and set up the working directory and environment.	

Aptitute = read.csv("Project 1_Dataset.csv")
# Data snapshot
View(Aptitute)

 # Step 2 - Convert the rank variable into factor and run logistic model.

Aptitute$rank = as.factor(Aptitute$rank)

AptGLM = glm(admit~.,Aptitute,family="binomial")
summary(AptGLM)

# Step 3 - Drop insignificant variables.

AptGLM = glm(admit~gre+gpa+rank,Aptitute,family="binomial")
summary(AptGLM)

# Now, all the variables are significant. This is final mode with GRE, 
# GPA, rank2, rank3, and rank4 as final variables. Rank1 is reference 
# level in logistic regression.

# Step 4 - Test model accuracy.

Predictions = predict(AptGLM, Aptitute, type="response")
Predictions

Predicted_Aptitute = cbind(Aptitute, Predictions)

head(Predicted_Aptitute)

Predicted_Aptitute_Categorized = transform(Predicted_Aptitute,
                                           Predicted_Admission = ifelse(Predictions<.5,0,1))
head(Predicted_Aptitute_Categorized)

log_accuracy = mean(Predicted_Aptitute_Categorized$admit == Predicted_Aptitute_Categorized$Predicted_Admission)
log_accuracy

# confusionMatrix(table(Predicted_Aptitute_Categorized$admit,
#                       Predicted_Aptitute_Categorized$Predicted_Admission))

# library(caret)
# library(e1071)

# Step 5 - Try to fit the Decision Tree model.
# Trying Decision Tree model

library(tree)

tree_Apt = tree(admit ~ . , Aptitute)

Predictions = predict(tree_Apt, Aptitute)
Predictions

Predicted_Aptitute = cbind(Aptitute,Predictions)
head(Predicted_Aptitute)
Predicted_Aptitute_Categorized = transform(Predicted_Aptitute,
                                           Predicted_Admission = ifelse(Predictions<.5,0,1))
head(Predicted_Aptitute_Categorized)

dt_accuracy = mean(Predicted_Aptitute_Categorized$admit == Predicted_Aptitute_Categorized$Predicted_Admission)
dt_accuracy

# confusionMatrix(table(Predicted_Aptitute_Categorized$admit,
#                       Predicted_Aptitute_Categorized$Predicted_Admission))

# Accuracy is 73%

# bag.boston=randomForest(medv~., data=Boston, subset=train, 
#                         mtry=13, importance=TRUE)

## Random Forest
library(randomForest)
dim(Aptitute)
class(Aptitute$admit)
Aptitute$admit = as.factor(Aptitute$admit)

tree_Apt = randomForest(admit ~ . , Aptitute, mtry = sqrt(7), importance=TRUE)

Predictions = predict(tree_Apt, Aptitute, type = "response")
Predictions
# Predicted_Aptitute = cbind(Aptitute, Predictions)
# head(Predicted_Aptitute)
# Predicted_Aptitute_Categorized = transform(Predicted_Aptitute,
#                                            Predicted_Admission = ifelse(Predictions<.5,0,1))
# head(Predicted_Aptitute_Categorized)

rf_accuracy = mean(Aptitute$admit == Predictions)

# rf_accuracy = mean(Predicted_Aptitute_Categorized$admit == Predicted_Aptitute_Categorized$Predicted_Admission)

rf_accuracy

# confusionMatrix(table(Predicted_Aptitute_Categorized$admit,
#                       Predicted_Aptitute_Categorized$Predicted_Admission))

# Step 6 - Selecting champion model

models_ = c('log_accuracy', 'dt_accuracy', 'rf_accuracy')
accuracy_ = c(log_accuracy, dt_accuracy, rf_accuracy)

tbl = cbind(models_, accuracy_)

tbl

# Since logistic has the accuracy rate of 71% and tree has 
# accuracy rate of 69%, logistic is the champion model.


# # Descriptive
# # Step 1 - Categorize the grade point average into High or Medium and plot it on point chart.
# 
# Aptitute_Descriptive = transform(Aptitute,
#                                  GreLevels=ifelse(gre<439,"Low",ifelse(gre<579,"Medium","High")))
# # View(Aptitute_Descriptive)
# Sum_Apt=aggregate(admit~GreLevels,Aptitute_Descriptive,FUN=sum)
# length_Apt=aggregate(admit~GreLevels,Aptitute_Descriptive,FUN=length)
# Probability_Table = cbind(Sum_Apt,Recs=length_Apt[,2])
# Probability_Table_final = transform(Probability_Table,Probability_Admission = admit/Recs)
# Probability_Table_final
# ggplot(Probability_Table_final,aes(x=GreLevels,y=Probability_Admission))+geom_point()
# 
# # Step 2: Cross grid for admission variable with GRE categorized
# 
# table(Aptitute_Descriptive$admit,Aptitute_Descriptive$GreLevels)

tbl
