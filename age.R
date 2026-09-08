
# Create a sample dataset set.seed(123)
data <- data.frame( ID = 1:10,
                    Age = sample(18:60, 10, replace = TRUE),
                    Gender = sample(c("Male", "Female"), 10, replace = TRUE), Score = sample(1:100, 10)
)
# Print the sample data 
print(data)
filtered_data <- data[data$Age > 30, ]
filtered_data <- data[data$Age > 30 & data$Gender == "Male", ]
cleaned_data <- unique(data[, c("ID", "Age", "Gender")])
cleaned_data <- na.omit(data)
# Load the ggplot2 package
library(ggplot2)
# Create a scatterplot of Age vs. Score with points colored by Gender ggplot(data = cleaned_data, aes(x = Age, y = Score, color = Gender)) + geom_point() +
labs(title = "Scatterplot of Age vs. Score", x = "Age",
     y = "Score")
# Create a histogram of Age
ggplot(data = cleaned_data, aes(x = Age)) + geom_histogram(binwidth = 5, fill = "blue", alpha = 0.5) + labs(title = "Histogram of Age",
                                                                                                            x = "Age",
                                                                                                            y = "Frequency")
# Create a bar chart of Gender distribution 
ggplot(data = cleaned_data, aes(x = Gender)) + geom_bar(fill = "green", alpha = 0.7) + labs(title = "Gender Distribution",
x = "Gender", y = "Count")

