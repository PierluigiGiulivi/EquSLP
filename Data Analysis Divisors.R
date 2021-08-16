#########################
# Data Analysis: Divisors
#########################
for (i in c(20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)){
  
  data = read.table(paste('divisors', i, '.csv', sep = ""), header=T, sep=',')
  
  # get the mean divisors amount for each bit range
  meandata = aggregate(divisors~bits, data, mean)
  
  if (i == 20) {
    total = meandata
  } else {
    total = rbind(total, meandata)
  }
}

# get the mean of all the means for the total mean
total = aggregate(divisors~bits, total, mean)

# Define the position of tick marks
v1 <- c(0,4,8,12,16,20,24,28,32)

# Define the labels of tick marks
v2 <- c("0","4","8","12","16","20","24","28","32")

x = c(1:33)
y = 1/x

jpeg(file = 'divisors.jpg', res = 600, width = 4800, height = 4800)

# create the plot 
plot(x = total$bits,
     y = total$divisors, 
     type="o",
     pch=15,
     xlim =c(0,33), 
     ylim =c(0,1),
     xaxt = "n",
     col="red",
     main = "Number of Bits of Divisor against the 
             Average Proability of Divisor in Range",
     sub = '1 to 2^(2^5)',
     xlab ="Number of Bits of Divisor", 
     ylab ="Average Proability of Divisor in Range")

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
     xlim =c(0,33), 
     ylim =c(0,1),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topright", legend = c("1/x","Probability = 0"),
       col = c("black", "green"), lty = 1:1, cex = 1)

dev.off()