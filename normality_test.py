import seaborn as sns
from scipy.stats import shapiro
import matplotlib.pyplot as plt


def normality_test(data):
	sns.distplot(data)
	plt.xlabel('Actual Total Load [MW] - BZN|GB')
	plt.ylabel('Density')
	stat, p = shapiro(data)
	print('Statistics=%.3f, p=%.3f' % (stat, p))
	# interpret
	alpha = 0.05
	if p > alpha:
    		print('Sample looks Gaussian (fail to reject H0)')
	else:
    		print('Sample does not look Gaussian (reject H0)') 
