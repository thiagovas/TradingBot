library(quantmod)
collect_currency <- function(symbol, output_filename) {
  userInput=symbol
  eurusd<-as.data.frame(getSymbols(Symbols = userInput, 
            src = "yahoo", from = "2007-01-01", to = "2016-01-01", env = NULL))
  write.table(eurusd, file = output_filename, sep = ",", col.names = NA,
                      qmethod = "double")
}

# Collecting the Euro/Dollar.
collect_currency("EURUSD=X",  "currency/originals/eurusd-2007-2015.csv");

# Collecting the Chinese Yuan/Dollar.
collect_currency("CNY=X",     "currency/originals/cny-2007-2015.csv");

# Collecting the S&P 500
collect_currency("^GSPC",     "currency/originals/gspc-2007-2015.csv");

# Collecting the SPDR Gold Shares.
collect_currency("GLD",       "currency/originals/gld-2007-2015.csv");
