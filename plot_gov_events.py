import matplotlib.pyplot as plt
import pandas as pd

def plot_government_events():
	# add vertical lines for important lockdown events
	# self isolation order
	self_iso = pd.to_datetime('2020-03-12')
	plt.axvline(x=self_iso, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=self_iso, y= -5, s='First self-isolation measures', alpha=0.7, color='black', rotation=90, fontsize= 9)
	# school closure announced
	school_close_announce = pd.to_datetime('2020-03-18')
	plt.axvline(x=school_close_announce, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=school_close_announce, y= -5, s='Schools close announcement', alpha=0.7, color='black', rotation=90, fontsize= 9)
	# schools closing
	school_close = pd.to_datetime('2020-03-20')
	plt.axvline(x=school_close, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=school_close, y= -5, s='Schools close', alpha=0.7, color='black', rotation=90, fontsize= 9)
	# stay at home order
	home = pd.to_datetime('2020-03-23')
	plt.axvline(x=home, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=home, y= -5, s='Lockdown starts', alpha=0.7, color='black', rotation=90, fontsize= 9)
	# 1st easing of lockdown measures: 
	ease_1 = pd.to_datetime('2020-05-13')
	plt.axvline(x=ease_1, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=ease_1, y= -5, s='1st easing of measures', alpha=0.7, color='black', rotation=90, fontsize= 9)     
	# 2nd easing of lockdown measures: 
	ease_2 = pd.to_datetime('2020-06-01')
	plt.axvline(x=ease_2, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=ease_2, y= -5, s='2nd easing of measures', alpha=0.7, color='black', rotation=90, fontsize= 9)  
	# new rules for entering UK
	rules_1 = pd.to_datetime('2020-06-08')
	plt.axvline(x=rules_1, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=rules_1, y= -5, s='Self-isolation rules for UK arrivals', alpha=0.7, color='black', rotation=90, fontsize= 9)  
	# 3rd easing of lockdown measures: 
	ease_3 = pd.to_datetime('2020-06-15')
	plt.axvline(x=ease_3, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=ease_3, y= -5, s='Reopening of shops', alpha=0.7, color='black', rotation=90, fontsize= 9)   
	# 4rd easing of lockdown measures, pubs to reopen in England: 
	ease_4 = pd.to_datetime('2020-07-04')
	plt.axvline(x=ease_4, color='black', linestyle='dotted', linewidth=0.8)
	plt.text(x=ease_4, y= -5, s='Reopening of pubs, meet up with 6', alpha=0.7, color='black', rotation=90, fontsize= 9) 