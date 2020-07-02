import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from functools import wraps

def _func_log(func):
	'''_func_log()
	made to log entry and exit of a decorated function
	for i/o clarity during executiin'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		print(f'[{func.__name__}] Entering')
		returned = func(*args, **kwargs)
		print(f'[{func.__name__}] Exiting')
		return returned
	return wrapper

class HouseKeep:
	'''HouseKeeping - class
	several methods designed to process and manipulate visualization
	metainformation, such as centroid identification and text'''
	def __init__(self):
		pass

	def centroid(self, x:np.array, y:np.array
			) -> 'tuple(np.array(x), np.array(x))':
	'''centroid()
	calculates the centroid of a 2d vector, with float x, float y'''
		x_c = np.median(x)
		y_c = np.median(y)
		return x_c,y_c

	def centroid_df(self, 
			df,  
			ptrn:str, 
			x='UMAP_1', 
			y='UMAP_2',
			clcol='new.annotations') -> tuple(np.array('x'), np.array('y')):
	'''centroid_df() 
	takes dataframe and calculates a centroid'''
	    df = df[df[clcol].str.contains(ptrn, case=False)]
	    x_c = np.median(df[x])
	    y_c = np.median(df[y])
	    return x_c,y_c

	def add_annotation(ax, anndic:dict):
		'''add_annotation()
		takes a dictionary that has the text for annotation as the key
		and the coordinates for the annotation as value for the key.
		Furthermore, requires axis parameter to plot'''
	    for k,v in zip(anndic.keys(), anndic.values()):
	        ax.text(s=k, x=v[0], y=v[1], fontsize=20, color='black')

if __name__ == '__main__':
	gs = HouseKeep()
