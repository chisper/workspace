
findruns <- function(x,k){
	n <- length(x)
	runs <-NULL
	if(k>3)
		stop("k must less than 5!")
	for (i in 1:(n-k+1)){
		if (all(x[i:(i+k-1)]==1))
			runs <-c(runs ,i)
	}
	return (runs)
}