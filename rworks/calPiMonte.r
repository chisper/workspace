calPiMonte<-function(n){
    library("Rmpfr")
    set.seed(as.numeric(Sys.time()))
    sum<-0
    x<-mpfr(runif(n,-1,1),17)
    y<-mpfr(runif(n,-1,1),17)
    distt<-sqrt(x^2+y^2)
    for (i in distt)
    {   
      if(i<1)
        sum <- sum + 1
    }
    print(sum/n*4)
    print(pi)
    print((sum/n*4/-pi)/pi)
    return (sum/n*4)
}