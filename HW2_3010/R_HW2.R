cell<-read.csv("/Users/justinnguyen/Downloads/Cancer Risk.csv")
attach(cell)
head(cell)
summary(cell)

#Number 4
#A-Frequency Table
cell$AgeCat[Age < 40] <-"Age < 40"
cell$AgeCat[Age >= 40 & Age <= 50] <- "40 <= Age < 50"
cell$AgeCat[Age > 50 & Age <= 60 ] <-"50 <= Age < 60"
cell$AgeCat[Age > 60] <-"Age > 60"

attach(cell)
head(cell)
table(cell$AgeCat) 

#B-Pie Chart
AgeCat_labels<- round (tables(AgeCat)/sum(table(AgeCat))*100,1)
AgeCat_labels<- pasts (AgeCat_labelsm "%", sep="")
colors<- c("White","Grey","Black","Blue")
pie(table(AgeCat), main="Figure 1: Pie Chart of Age")

#C-Bar Plot
barplot(table(AgeCat), main="Figure 2: BarChart of Age")
barplot(table(ordered(AgeCat,c("Age < 40","40 <= Age < 50","50 <= Age < 60","Age > 60"))), main = "Figure 2: Bar Chart of Age", xlab = "Number of Employees")  


#Number 5
#A-Table
summary(Calories, Gender)

#B-Boxplot
boxplot(Calories~Gender, data=cell,
	main= "Figure 3: Side by Side Boxplots of Texts Sent By Gender",
	ylab= "No. of Calories Eaten", xlab= "Gender")
		
	
#Number 6 
#A-Frequency Table
table(SmokeStat,AgeCat)

#B-Rel. Freq. Table
prop.table(table(SmokeStat,AgeCat))

#C-Row Freq. Table
prop.table(table(SmokeStat,AgeCat),1)

#D-Column Rel. Freq
prop.table(table(SmokeStat,AgeCat),2)



#F-100% Stacked Bar Chart
barplot(prop.table(table(SmokeStat,AgeCat),2)*100, col=c("green","orange","red"),main = "Figure 4: 100% Stacked Bar Chart of Smokers Vs Age", xlab="Age of Smoker",ylab="Percent", legend=NULL)
legend("topright", fill=c("green","orange","red"), c("Never","Former","Current"))

#Number 7
#Scatter Plot
plot(Fat,Calories, main= "Figure 5:Scatterplot of Caloric Intake to Fat", xlab="Fat", ylab="Calories")

abline(lm(Calories~Fat), col="black", lty=5,lwd=2) #regression Line

#Number 8
#Random Number Generator
#A
set.seed(1143)
sam1<-cell[sample(1:nrow(cell),75,replace=FALSE),] 
sam1
#Confidence Interval
n<- sum(!is.na(Calories))
m<- mean(Calories,na.rm=TRUE)
se<- sd(Calories,na.rm=TRUE)/sqrt(n)
ci<- m+c(-1,1)*qt(p=0.95,df=n-1)*se
out<- cbind(n,m,se,ci)
out

#C-Rel. Freq. 
prop.table(table(sam1$SmokeStat))


