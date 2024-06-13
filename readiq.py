import numpy as np
import matplotlib.pyplot as plt
import h5py

def convertiq(filename,dtype=np.float32,offset=0,count=-1):
    
    dtype = np.dtype([('re',dtype),('im',dtype)])
    data_out = np.fromfile(filename,dtype=dtype,offset=offset,count=count)
    data_out = data_out.view(np.complex64)
    return data_out



def convertiqbatch(datadir,dtype=np.float32,offset=0,count=31250*10):

    dtype = np.dtype([('re',dtype),('im',dtype)])

    inith5stuff = 1

    # Find all binary/IQ files in the data directory.
    filelist = datadir
    h5savefile = h5py.File(datadir+'convertediq.h5',"w")
    data_array = np.empty([count,len(filelist)])
    # Loop over all files and store.
    for i in len(filelist):
         data_array[:,i]= np.fromfile(filelist,dtype=dtype,offset=offset,count=count)
        # add to h5 file
    h5savefile["data_array"] = data_array
    h5savefile.close()

    return h5savefile


def quickplotfromiq(filename,sample_frequency,dtype=np.float32,offset=0,count=-1,center_frequency=0):
    
    # Run conversion
    dtype = np.dtype([('re',dtype),('im',dtype)])
    data = np.fromfile(filename,dtype=dtype,offset=offset,count=count)
    data = data.view(np.complex64)
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

    return