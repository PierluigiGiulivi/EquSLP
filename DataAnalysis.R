###########################
# Data Analysis 0+1*2^(2^128).csv
##########################
data = read.table('0+1*2^(2^128).csv', header=T, sep=',') #reads data

cor(bits, colMeans(EquSLPData)[3:59], method = 'pearson') # get pearson correlation

# Define the position of tick marks
v1 <- c(8,12,16,20,24,28,32,36,40,44,48,52,56,60,64)

# Define the labels of tick marks
v2 <- c("8","12","16","20","24","28","32","36","40","44","48","52","56","60","64")

# plot bits vs. mean
bits = c(8:64)
plot(bits,
     colMeans(EquSLPData)[3:59],
     xaxt = "n",
     type="o",
     pch=20,
     xlim=c(8,64), 
     ylim=c(0,0.25),
     main = "Number of Bits of Random Component against Average Probability of Failure", 
     xlab="Number of Bits of Random Component", 
     ylab="Average Probability of Failure")

# Add an axis to the plot 
axis(side = 1, 
     at = v1, 
     labels = v2,
     tck=-.05)

# Add reference line
abline(h=0.00,col="green")

# Add Legend
legend("topright", legend=c("Probability = 0"), col=c("green"), lty=1, cex=1)



##################################
# Data Analysis: 0+1*2^(2^64).csv
##################################
for (i in c(2,3,5)){
        
        data = read.table(paste('0+1*', i, '^(2^64).csv', sep = ""), header=T, sep=',') # reads data
        
        # Define the position of tick marks
        v1 <- c(8,12,16,20,24,28,32)
        
        # Define the labels of tick marks
        v2 <- c("8","12","16","20","24","28","32")
        
        jpeg(file=paste('0+1*', i, '^(2^64).jpg', sep = ""), 
             res=600, width=4800, height=4800)
             #, pointsize=10, type="windows", antialias="cleartype")
        
        # Create the plot
        plot(x = data$bits,
             y = data$proba, 
             col = gray(.4, .4),
             pch = 16,
             xaxt = "n",
             xlim =c(8,32), 
             ylim =c(0,0.8),
             main = "Number of Bits of Random Component against the Probability of Failure",
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
        meandata = aggregate(data[, 4], list(data$bits), mean)
        
        # Create the plot
        plot(x = meandata[,1],
             y =  meandata[,2], 
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
        legend("topright", legend=c("Average Probability", "Probability = 0"), col=c("red", "green"), lty=1:1, cex=1)
        
        dev.off()
}
