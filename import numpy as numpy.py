import numpy as np

f= open(r"C:\Users\R I B\Desktop\Loan_prediction_dataset.csv", "r")
Loans=np.genfromtxt(f, delimiter=",", skip_header=1, usecols=8)
f.close()

print("Mean:",np.nanmean(Loans))
print("Median:",np.nanmedian(Loans))
print("std:", np.nanstd(Loans))