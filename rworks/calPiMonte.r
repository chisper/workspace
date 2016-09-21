calPiMonte<-function(n){
    sum<-0
    x<-runif(n,-1,1)
    y<-runif(n,-1,1)
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