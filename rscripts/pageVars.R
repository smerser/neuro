## SETUP R DATA VARIABLES
dr <- 'dr_var'
dg <- 'dg_var'
dl <- 'dl_var'

## CALL SWEAVE
Sweave('rapport.Rnw', syntax='SweaveSyntaxNoweb')

## COMPILE PDF
system("pdflatex --interaction=nonstopmode rapport.tex")
system("pdflatex --interaction=nonstopmode rapport.tex")
