titanic <- read.csv("train.csv") #https://www.kaggle.com/c/3136/download/train.csv

#Exercises
#1  What's the average age from survival men
#2. How many people survived
#3. How many people died
#4. How many people were on board the Titanic
#5. What's the ratio of people from first and third class
#6. Select columns Age and Sex for first class passengers
#7. Calculate the mask to select the survivors from 3rd class or the men from 1st class that passed away.
#8. Correlation between Age and Fare for each sex
#9. Create a new column on "titanic" named "riesgo" with the following values for each group:
 #            Female    Male
 # 1st class   1        2
 # 2nd class   2        3
 # 3rd class   3        4
# 10. Create another column named desviationFare with the diference between Fare and the Fare mean
 # Calculate min and max from this new variable for each combination of sex and class.
# 11. Check out the documentation for xtabs and get the mins from the previous exercises with this function

#1.
mean(titanic[titanic$Sex == "male" & titanic$Survived == 1, "Age"], na.rm= T)

#2.
sum(titanic$Survived)

#3.
sum(!titanic$Survived)

#4.
sum(titanic$Embarked != "") #need to account for not embarked passengers

#5.
sum(titanic$Pclass == 1) / sum(titanic$Pclass == 3) #start reading backwards, for each 3rd class there's 0.43 1st

#6.
titanic %>%
  filter(Pclass == 1) %>%
  select(Age, Sex)
titanic[titanic["Pclass"] == 1, c("Age", "Sex")]

#7.
titanic_mask <- (titanic$Survived == 1 & titanic$Pclass == 3) | (titanic$Sex == "male" & titanic$Pclass == 1 & titanic$Survived == 0)

#8.
cor(titanic$Age, titanic$Fare, use="comple")

#9
titanic$riesgo = 0
titanic$riesgo[titanic$Pclass == 1 & titanic$Sex == "female"] = 1
titanic$riesgo[titanic$Pclass == 1 & titanic$Sex == "male"] = 2
titanic$riesgo[titanic$Pclass == 2 & titanic$Sex == "female"] = 2
titanic$riesgo[titanic$Pclass == 2 & titanic$Sex == "male"] = 3
titanic$riesgo[titanic$Pclass == 3 & titanic$Sex == "female"] = 3
titanic$riesgo[titanic$Pclass == 3 & titanic$Sex == "male"] = 3


#10.
titanic$DesviationFare = titanic$Fare - mean(titanic$Fare)
aggregate(DesviationFare~Sex+Pclass,titanic,FUN=function(x) c(min = min(x),max = max(x)))

#11.
xtabs(DesviationFare~Sex+Pclass, aggregate(DesviationFare~Sex+Pclass,titanic,FUN=min)
