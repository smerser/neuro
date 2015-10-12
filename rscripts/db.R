##########################################################################################################################
## MySQL
## Be sure to START local Mac MySQL server: mysql_start
#con <- dbConnect(MySQL(), host='localhost', dbname='NeuroRH', user='root')

##########################################################################################################################
## REMOTE MYSQL:: statcom.dk
##
## Be sure to STOP local Mac MySQL server: mysql_stop
## Connect to statcom.dk MySQL-server
## ssh -L 3306:localhost:3306 statcom.dk
#require(RMySQL)
#con <- dbConnect(MySQL(), host='127.0.0.1', dbname='NeuroRH', user='root', password='merser')


#########################################################################################################################
## REMOTE POSTGRES::STATCOM_II::77.66.12.57
##
##  ssh -f soren@77.66.12.57 -L 5439:localhost:5432 -N
## BE SURE TO UNLOAD PACKAGE::RMySQL AND CLOSE THE LOCAL PostgreSQL SERVER !!!!
require(RPostgreSQL)
con <- dbConnect(PostgreSQL(), host='localhost', port=5439, user="postgres", dbname="NeuroRH", password="neW6R@BGeCMMBL)Z3guA")

# ## 
# library(dplyr)
# db <- src_postgres(host='localhost', port=5439, user="postgres", dbname="NeuroRH", password="neW6R@BGeCMMBL)Z3guA")
# x <- tbl(db, 'main_patienter')
# df <- as.data.frame(x)

