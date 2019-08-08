# copyright (c) 2019 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )

if(!"ggplot2" %in% rownames(installed.packages())){
             install.packages("ggplot2",repos="https://cran.ism.ac.jp/")
}

library(ggplot2)
arg1 = commandArgs(trailingOnly=TRUE)[1]
arg2 = commandArgs(trailingOnly=TRUE)[2]

d=read.table(paste(arg1,".txt",sep=""),header=T)

g=ggplot2::ggplot(d,aes(x=position,y=mean_qual,group=filename,color=FR))
g=g+theme_bw()+theme_bw()+theme(panel.background = element_rect(fill = "transparent",color = NA),plot.background = element_rect(fill = "transparent",color = NA))
g=g+geom_line(alpha=0.6, size=0.3)
ggsave(file=paste(arg1,".pdf",sep=""), plot=g, height=4,width=as.numeric(arg2))



