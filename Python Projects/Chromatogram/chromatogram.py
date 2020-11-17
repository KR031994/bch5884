#Programming Project#2
#Link to repository:https://github.com/KR031994/bch5884

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

FILE_NAME = "superose6_50.asc" #name of the file

def load_data():
    data = np.loadtxt(FILE_NAME,skiprows=3) #loading the data table skipping the 1st 3 rows as they are headings
    time,miliabs = np.hsplit(data,2) #splitting the data columns to separate the data
    return np.reshape(time,(len(time))),np.reshape(miliabs,(len(miliabs))) #reshaping data to correct dimensions

def get_peaks(time,miliabs, relative_height, width):
    index, props = find_peaks(miliabs, prominence=1, rel_height=relative_height, width=width) #finding the peaks with fine tuned parameters
    return (time[index],miliabs[index], index, props) 

def plot_height_width(x, y, peaks, properties):
    start = []
    end = []
    for i in range(len(peaks)):
        start.append(x[int(properties["left_ips"][i])])
        end.append(x[int(properties["right_ips"][i])])
        
    plt.plot(x, y)
    plt.plot(x[peaks], y[peaks], "x")
 
if __name__ == '__main__':
    t,m = load_data()
    peak_t,peak_m, peaks, properties = get_peaks(t,m, relative_height=1, width=0)
    plot_height_width(t, m, peaks, properties)
    
    #finding the start and end time points, maximum absorbance and exact time point of 7 peaks detected
    for i in range(len(peaks)):
        chromatogram=("The starting and ending points of peak with maximum absorbance {a_max} are at {start} and {end} mins respectively, with exact peak time point at {tm} mins")
        print(chromatogram.format(a_max=m[peaks[i]],start=t[int(properties["left_ips"][i])], end=t[int(properties["right_ips"][i])], tm=peak_t[i]))
    
    #setting the limits for the axes
    plt.xlim(0,180)
    plt.ylim(0,1200)
    plt.show()