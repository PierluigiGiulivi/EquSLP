#####################################
# Data Analysis: 0+prime*prime^(2^64)
#####################################
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
       tck=-.02)
  
  # Add reference line
  abline(h=0.00,col="green")
  
  par(new=T) # superpose plots
  
  # Mean Data
  meandata = aggregate(proba~bits, data, mean)
  
  # Variance and Standard Deviation Data
  #vardata = aggregate(proba~bits, data, var)
  #sddata = aggregate(proba~bits, data, sd)
  
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
  
  if (i == "0+2*3^(2^64)") {
    total = meandata
  } else {
    total = rbind(total, meandata)
  }
}

# get the mean of all the means for the total mean
total = aggregate(proba~bits, total, mean)

# Define the position of tick marks
v1 <- c(8,12,16,20,24,28,32)

# Define the labels of tick marks
v2 <- c("8","12","16","20","24","28","32")

x = c(8:32)
y = 1/x

jpeg(file = 'all-0+prime*prime^(2^64).jpg', res = 600, 
     width = 4800, height = 4800)

# create the plot 
plot(x = total$bits,
     y = total$proba, 
     type="o",
     pch=15,
     xlim =c(8,32), 
     ylim =c(0,max(total$proba)),
     xaxt = "n",
     col="red",
     main = "Number of Bits of Random Component
             against the Mean Probability of Failure",
     sub = "0+prime*prime^(2^64)",
     xlab ="Number of Bits of Random Component", 
     ylab ="Mean Probability of Failure")

# Add an axis to the plot 
axis(side = 1, 
     at = v1, 
     labels = v2,
     tck=-.02)

# Add reference line
abline(h=0.00,col="green")

par(new=T) # superpose plots

# Create the plot
plot(x,
     y, 
     type="o",
     pch=15,
     xaxt = "n",
     yaxt = "n",
     xlim =c(8,32), 
     ylim =c(0,max(total$proba)),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topright", legend = c("1/x","Probability = 0"),
       col = c("black", "green"), lty = 1:1, cex = 1)

dev.off()