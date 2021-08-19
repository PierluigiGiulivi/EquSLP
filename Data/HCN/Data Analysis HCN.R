####################
# Data Analysis: HCN
####################
data = read.table('HCN.csv', header=T, sep=',')
  
# get the mean divisors amount for each bit range
meandata = aggregate(divisors~bits, data, mean)

x = c(1:136)
y = 1/x

jpeg(file = 'HCN.jpg', res = 600, width = 4800, height = 4800)

# Create the plot
plot(x = data$bits,
     y = data$divisors, 
     col = gray(.4, .4),
     pch = 16,
     xaxt = "n",
     yaxt = "n",
     xlim =c(0,136), 
     ylim =c(0,1),
     main = "", 
     xlab ="", 
     ylab ="")

par(new=T) # superpose plots

# create the plot 
plot(x = meandata$bits,
     y = meandata$divisors, 
     type="o",
     pch=20,
     xlim =c(0,136), 
     ylim =c(0,1),
     col="red",
     main = "Number of Bits of Divisor against the 
             Average Proability of Divisor in Range",
     sub = 'First 39 SHCN',
     xlab ="Number of Bits of Divisor", 
     ylab ="Average Proability of Divisor in Range")

# Add reference line
abline(h=0.00,col="green")

par(new=T) # superpose plots

# Create the plot
plot(x,
     y, 
     type="o",
     pch=20,
     xaxt = "n",
     yaxt = "n",
     col="orchid4",
     xlim =c(0,136), 
     ylim =c(0,1),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topright", legend = c("Mean Probability","1/x","Probability = 0"),
       col = c("red","orchid4", "green"), lty = 1:1, cex = 1)

dev.off()



jpeg(file = 'HCN2.jpg', res = 600, width = 4800, height = 4800)

# Create the plot
plot(x = data$bits,
     y = data$divisors, 
     col = gray(.4, .4),
     pch = 16,
     xaxt = "n",
     yaxt = "n",
     xlim =c(0,136), 
     ylim =c(0,0.2),
     main = "", 
     xlab ="", 
     ylab ="")

par(new=T) # superpose plots

# create the plot 
plot(x = meandata$bits,
     y = meandata$divisors, 
     type="o",
     pch=20,
     xlim =c(0,136), 
     ylim =c(0,0.2),
     col="red",
     main = "Number of Bits of Divisor against the 
             Average Proability of Divisor in Range",
     sub = 'First 39 SHCN',
     xlab ="Number of Bits of Divisor", 
     ylab ="Average Proability of Divisor in Range")

# Add reference line
abline(h=0.00,col="green")

par(new=T) # superpose plots

# Create the plot
plot(x,
     y, 
     type="o",
     pch=20,
     xaxt = "n",
     yaxt = "n",
     col="orchid4",
     xlim =c(0,136), 
     ylim =c(0,0.2),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topright", legend = c("Mean Probability","1/x","Probability = 0"),
       col = c("red","orchid4", "green"), lty = 1:1, cex = 1)

dev.off()