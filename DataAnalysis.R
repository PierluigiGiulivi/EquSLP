#####################################
# Data Analysis: 0+1*prime^(2^64).csv
#####################################
for (i in c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)){
        
        data = read.table(paste('0+1*', i, '^(2^64).csv', sep = ""),
                          header=T, sep=',')
        
        # Define the position of tick marks
        v1 <- c(8,12,16,20,24,28,32)
        
        # Define the labels of tick marks
        v2 <- c("8","12","16","20","24","28","32")
        
        jpeg(file = paste('0+1*', i, '^(2^64).jpg', sep = ""), 
             res = 600, width = 4800, height = 4800)
        
        # Create the plot
        plot(x = data$bits,
             y = data$proba, 
             col = gray(.4, .4),
             pch = 16,
             xaxt = "n",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "Number of Bits of Random Component 
                        against the Probability of Failure",
             sub = paste('0+1*', i, '^(2^64)', sep = ""),
             xlab ="Number of Bits of Random Component", 
             ylab ="Probability of Failure")
        
        # Add an axis to the plot 
        axis(side = 1, 
             at = v1, 
             labels = v2,
             tck=-.05)
        
        # Add reference line
        abline(h=0.00,col="green")
        
        par(new=T) # superpose plots
        
        # Mean Data
        meandata = aggregate(proba~bits, data, mean)
        
        # Variance and Standard Deviation Data
        vardata = aggregate(proba~bits, data, var)
        sddata = aggregate(proba~bits, data, sd)
        
        # Create the plot
        plot(x = meandata$bits,
             y =  meandata$proba, 
             type="o",
             pch=15,
             xaxt = "n",
             yaxt = "n",
             col="red",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "", 
             xlab ="", 
             ylab ="")
        
        # Add Legend
        legend("topright", legend = c("Average Probability","Probability = 0"),
               col = c("red", "green"), lty = 1:1, cex = 1)
        
        dev.off()
}



#########################################
# Data Analysis: 0+prime*prime^(2^64).csv
#########################################
for (i in c("0+2*3^(2^64)","0+2*5^(2^64)","0+2*7^(2^64)","0+2*11^(2^64)",
            "0+3*2^(2^64)","0+3*5^(2^64)","0+3*7^(2^64)","0+3*11^(2^64)",
            "0+5*2^(2^64)","0+5*3^(2^64)","0+5*7^(2^64)","0+5*11^(2^64)",
            "0+7*2^(2^64)","0+7*3^(2^64)","0+7*5^(2^64)","0+7*11^(2^64)",
            "0+11*2^(2^64)","0+11*3^(2^64)","0+11*5^(2^64)","0+11*7^(2^64)")){
        
        data = read.table(paste(i, '.csv', sep = ""), header=T, sep=',')
        
        # Define the position of tick marks
        v1 <- c(8,12,16,20,24,28,32)
        
        # Define the labels of tick marks
        v2 <- c("8","12","16","20","24","28","32")
        
        jpeg(file = paste(i, '.jpg', sep = ""), 
             res = 600, width = 4800, height = 4800)
        
        # Create the plot
        plot(x = data$bits,
             y = data$proba, 
             col = gray(.4, .4),
             pch = 16,
             xaxt = "n",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "Number of Bits of Random Component 
                        against the Probability of Failure",
             sub = i,
             xlab ="Number of Bits of Random Component", 
             ylab ="Probability of Failure")
        
        # Add an axis to the plot 
        axis(side = 1, 
             at = v1, 
             labels = v2,
             tck=-.05)
        
        # Add reference line
        abline(h=0.00,col="green")
        
        par(new=T) # superpose plots
        
        # Mean Data
        meandata = aggregate(proba~bits, data, mean)
        
        # Variance and Standard Deviation Data
        vardata = aggregate(proba~bits, data, var)
        sddata = aggregate(proba~bits, data, sd)
        
        # Create the plot
        plot(x = meandata$bits,
             y =  meandata$proba, 
             type="o",
             pch=15,
             xaxt = "n",
             yaxt = "n",
             col="red",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "", 
             xlab ="", 
             ylab ="")
        
        # Add Legend
        legend("topright", legend=c("Average Probability", "Probability = 0"),
               col = c("red", "green"), lty = 1:1, cex = 1)
        
        dev.off()
}



#########################################
# Data Analysis: x+1*2^(2^64).csv
#########################################
for (i in c("1+1*2^(2^64)","2+1*2^(2^64)","3+1*2^(2^64)","4+1*2^(2^64)",
            "5+1*2^(2^64)","6+1*2^(2^64)","7+1*2^(2^64)","8+1*2^(2^64)",
            "9+1*2^(2^64)")){
        
        data = read.table(paste(i, '.csv', sep = ""), header=T, sep=',')
        
        # Define the position of tick marks
        v1 <- c(8,12,16,20,24,28,32)
        
        # Define the labels of tick marks
        v2 <- c("8","12","16","20","24","28","32")
        
        jpeg(file = paste(i, '.jpg', sep = ""), 
             res = 600, width = 4800, height = 4800)
        
        # Create the plot
        plot(x = data$bits,
             y = data$proba, 
             col = gray(.4, .4),
             pch = 16,
             xaxt = "n",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "Number of Bits of Random Component 
                        against the Probability of Failure",
             sub = i,
             xlab ="Number of Bits of Random Component", 
             ylab ="Probability of Failure")
        
        # Add an axis to the plot 
        axis(side = 1, 
             at = v1, 
             labels = v2,
             tck=-.05)
        
        # Add reference line
        abline(h=0.00,col="green")
        
        par(new=T) # superpose plots
        
        # Mean Data
        meandata = aggregate(proba~bits, data, mean)
        
        # Variance and Standard Deviation Data
        vardata = aggregate(proba~bits, data, var)
        sddata = aggregate(proba~bits, data, sd)
        
        # Create the plot
        plot(x = meandata$bits,
             y =  meandata$proba, 
             type="o",
             pch=15,
             xaxt = "n",
             yaxt = "n",
             col="red",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "", 
             xlab ="", 
             ylab ="")
        
        # Add Legend
        legend("topright", legend=c("Average Probability", "Probability = 0"),
               col = c("red", "green"), lty = 1:1, cex = 1)
        
        dev.off()
}



##########################################################
# Data Analysis: 0+1*prime^(2^64) vs. 0+1*prime^(2^64).csv
##########################################################
for (i in c('0+1*2^(2^64) vs. 0+1*3^(2^64)', '0+1*2^(2^64) vs. 0+1*5^(2^64)',
            '0+1*2^(2^64) vs. 0+1*7^(2^64)', '0+1*2^(2^64) vs. 0+1*11^(2^64)',
            '0+1*3^(2^64) vs. 0+1*5^(2^64)', '0+1*3^(2^64) vs. 0+1*7^(2^64)',
            '0+1*3^(2^64) vs. 0+1*11^(2^64)', '0+1*5^(2^64) vs. 0+1*7^(2^64)',
            '0+1*5^(2^64) vs. 0+1*11^(2^64)', '0+1*7^(2^64) vs. 0+1*11^(2^64)')){
        
        data = read.table(paste(i,'.csv', sep = ""),
                          header=T, sep=',')
        
        # Define the position of tick marks
        v1 <- c(8,12,16,20,24,28,32)
        
        # Define the labels of tick marks
        v2 <- c("8","12","16","20","24","28","32")
        
        jpeg(file = paste(i,'.jpg', sep = ""), 
             res = 600, width = 4800, height = 4800)
        
        # Create the plot
        plot(x = data$bits,
             y = data$proba, 
             col = gray(.4, .4),
             pch = 16,
             xaxt = "n",
             xlim =c(8,32), 
             ylim =c(0,0.1),
             main = "Number of Bits of Random Component 
                        against the Probability of Failure",
             sub = i,
             xlab ="Number of Bits of Random Component", 
             ylab ="Probability of Failure")
        
        # Add an axis to the plot 
        axis(side = 1, 
             at = v1, 
             labels = v2,
             tck=-.05)
        
        # Add reference line
        abline(h=0.00,col="green")
        
        par(new=T) # superpose plots
        
        # Mean Data
        meandata = aggregate(proba~bits, data, mean)
        
        # Variance and Standard Deviation Data
        vardata = aggregate(proba~bits, data, var)
        sddata = aggregate(proba~bits, data, sd)
        
        # Create the plot
        plot(x = meandata$bits,
             y =  meandata$proba, 
             type="o",
             pch=15,
             xaxt = "n",
             yaxt = "n",
             col="red",
             xlim =c(8,32), 
             ylim =c(0,0.1),
             main = "", 
             xlab ="", 
             ylab ="")
        
        # Add Legend
        legend("topright", legend = c("Average Probability","Probability = 0"),
               col = c("red", "green"), lty = 1:1, cex = 1)
        
        dev.off()
}



####################
# Data Analysis: All
####################
globalData = data.frame(Group.1 = integer(), x = integer())

for (i in c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)){
        
        data = read.table(paste('0+1*', i, '^(2^64).csv', sep = ""),
                          header=T, sep=',')
        globalData = rbind(globalData, 
                           aggregate(data[, 4], list(data$bits), mean))
}

jpeg(file = 'all.jpg', res = 600, width = 4800, height = 4800)

# Define the position of tick marks
v1 <- c(8,12,16,20,24,28,32)

# Define the labels of tick marks
v2 <- c("8","12","16","20","24","28","32")

# Mean Data
meandata = aggregate(globalData[, 2], list(globalData$Group.1), mean)

# Create the plot
plot(x = meandata[,1],
     y =  meandata[,2], 
     type="o",
     pch=15,
     xaxt = "n",
     xlim =c(8,32), 
     ylim =c(0,0.8),
     main = "Number of Bits of Random Component 
                against the Global Probability of Failure",
     xlab ="Number of Bits of Random Component", 
     ylab ="Global Probability of Failure")

# Add an axis to the plot 
axis(side = 1, 
     at = v1, 
     labels = v2,
     tck=-.05)

# Add reference line
abline(h=0.00,col="green")

# Add Legend
legend("topright", legend = "Probability = 0",
       col = "green", lty = 1:1, cex = 1)

dev.off()



###########################################
# Worse Case Scenario: 0+1*prime^(2^64).csv
###########################################
data0 = read.table(paste('0+1*', 2, '^(2^64).csv', sep = ""),
                   header=T, sep=',')

# Select the max probability for each bit value
maxproba = aggregate(proba~bits, data0, max)
data = data0[data0$proba == maxproba$proba,]
data = data[order(data$proba),] 

# Add possible bounding functions
data$"6.5/b" = 6.5/data$bits 
data$"0.384/b" = 0.384/data$bits

data

# Mean Data
meandata = aggregate(proba~bits, data0, mean)

meandata$"coeff/b" = mean(meandata$bits * meandata$proba) / meandata$bits

meandata$"1/exp(b)" = meandata$bits / exp(meandata$bits)

meandata

# Variance and Standard Deviation Data
vardata = aggregate(proba~bits, data0, var)
sddata = aggregate(proba~bits, data0, sd)


###############
data0 = read.table(paste('0+1*', 3, '^(2^64).csv', sep = ""),
                   header=T, sep=',')

data = data0[data0$bits == 16,]
x = data$proba
y = dnorm(x, mean(data$proba), sd(data$proba))
plot(x,y)
abline(v = mean(data$proba))
abline(v = mean(data$proba) + sd(data$proba))
abline(v = mean(data$proba) - sd(data$proba))

hist(x)
#################








cor(data$bits, data$proba, method = 'pearson')

model = lm(data$proba ~ data$bits)
summary(model)

model = lm(data$proba ~ data$bits + I(data$bits^2))
summary(model)