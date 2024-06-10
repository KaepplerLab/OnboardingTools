import numpy as np
import matplotlib.pyplot as plt

def convertiq(filename,dtype=np.float32,offset=0,count=-1):
    
    dtype = np.dtype([('re',dtype),('im',dtype)])
    data_out = np.fromfile(filename,dtype,offset,count)

    return data_out



def convertiqbatch(datadir,dtype=np.float32):

    dtype = np.dtype([('re',dtype),('im',dtype)])

    inith5stuff = 1

    # Find all binary/IQ files in the data directory.
    filelist = datadir

    # Loop over all files and store.
    for i in len(filelist):
        np.fromfile(filelist,dtype=dtype)
        # add to h5 file

    return allh5filecontents


def quickplotfromiq(filename,sample_frequency,dtype=np.float32,offset=0,count=-1,center_frequency=0):
    
    # Run conversion
    data = convertiq(filename,dtype,offset,count)
    
    # Basic diagnostic plot
    fig, (ax0,ax1) = plt.subplots(2,1,figsize=[20,10])
    fig.subplots_adjust(hspace=0.6)
    ax0.specgram(data,NFFT=256,Fs=sample_frequency,Fc=center_frequency)
    ax0.set_title("Spectrogram")
    ax0.set_xlabel("Time (in seconds)")
    ax0.set_ylabel("Frequency")
    ax1.set_title("Power Spectral Density")
    ax1.psd(data)
    plt.savefig(filename+'_qp.png')
    plt.show()
