# Simple Linear Regression

# Importing the dataset
setwd("E:/academia.Kineret/2018-2019/2nd/R and Python/Lectures/09- 05.06.2019")
dataset = read.csv('students.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$FinalMark, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Simple Linear Regression to the Training set
regressor = lm(formula = FinalMark ~ Lectures+WatchTv, data = training_set)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Visualising the Training set results
# install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$Lectures, y = training_set$FinalMark),
             colour = 'red') +
  geom_line(aes(x = training_set$Lectures, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('FinalMark vs Experience (Training set)') +
  xlab('# Simple Linear Regression

# Importing the dataset
setwd("E:/academia.Kineret/2018-2019/2nd/R and Python/Lectures/09- 05.06.2019")
dataset = read.csv('students.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$FinalMark, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting Simple Linear Regression to the Training set
regressor = lm(formula = FinalMark ~ Lectures,
               data = training_set)

# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

# Visualising the Training set results
# install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$Lectures, y = training_set$FinalMark),
             colour = 'red') +
  geom_line(aes(x = training_set$Lectures, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('FinalMark vs Experience (Training set)') +
  xlab('Lectures and TV watch') +
  ylab('FinalMark')

# Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$Lectures, y = test_set$FinalMark),
             colour = 'red') +
  geom_line(aes(x = training_set$Lectures, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('FinalMark vs Experience (Test set)') +
  xlab('Lectures and TV watch') +
  ylab('FinalMark')')
  
# Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$Lectures, y = test_set$FinalMark),
             colour = 'red') +
  geom_line(aes(x = training_set$Lectures, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('FinalMark vs Experience (Test set)') +
  xlab('Lectures and TV watch') +
  ylab('FinalMark')