######################
# Data Analysis: Speed
######################

######## BitSpeed

data = read.table('BitSpeed2.csv', header=T, sep=',')

lm(data$seconds~data$bits)
x = seq(min(data$bits),max(data$bits),10)
y = 6.617e-05 + 5.034e-07 * x

jpeg(file = 'BitSpeed2.jpg', res = 600, width = 4800, height = 4800)

# create the plot 
plot(x = data$bits,
     y = data$seconds,  
     type="o",
     pch=20,
     col="black",
     xlim =c(min(data$bits),max(data$bits)), 
     ylim =c(min(data$seconds),max(data$seconds)),
     main = "Number of Bits of Random Component against 
                EquSLP algorithm runtime in seconds",
     sub = '2^(2^100) vs. 2^(2^100)',
     xlab ="Number of Bits of Random Component", 
     ylab ="EquSLP algorithm runtime in seconds")

par(new=T) # superpose plots

# Create the plot
plot(x,
     y, 
     type="o",
     pch=20,
     xaxt = "n",
     yaxt = "n",
     col="salmon",
     xlim =c(min(data$bits),max(data$bits)), 
     ylim =c(min(data$seconds),max(data$seconds)),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topleft", legend = c("y = 6.617e-05 + 5.034e-07 * x"),
       col = c("salmon"), lty = 1:1, cex = 1)

dev.off()



######## SLPSpeed

data = read.table('SLPSpeed1.csv', header=T, sep=',')

lm(data$seconds~data$len)
x = seq(min(data$len),max(data$len),10)
y = 3.625e-06 + 3.217e-07 * x

jpeg(file = 'SLPSpeed1.jpg', res = 600, width = 4800, height = 4800)

# create the plot 
plot(x = data$len,
     y = data$seconds,  
     type="o",
     pch=20,
     col="black",
     main = "Total size of input against 
                EquSLP algorithm runtime in seconds",
     sub = 'From 2^(2^0) to 2^(2^500)',
     xlab ="Total size of input", 
     ylab ="EquSLP algorithm runtime in seconds")

par(new=T) # superpose plots

# Create the plot
plot(x,
     y, 
     type="o",
     pch=20,
     xaxt = "n",
     yaxt = "n",
     col="salmon",
     xlim =c(min(data$len),max(data$len)), 
     ylim =c(min(data$seconds),max(data$seconds)),
     main = "", 
     xlab ="", 
     ylab ="")

# Add Legend
legend("topleft", legend = c("y = 3.625e-06 + 3.217e-07 * x"),
       col = c("salmon"), lty = 1:1, cex = 1)

dev.off()