import numpy as np
import pylab as pl




def load_cltf(fname):

    F=open(fname, 'rb')

    tt_size= np.fromfile(F, dtype=np.intc, count=1)[0]
    l_size = np.fromfile(F, dtype=np.intc, count=1)[0]
    q_size = np.fromfile(F, dtype=np.intc, count=1)[0]

    l = np.fromfile(F, dtype=np.intc, count=l_size)
    q = np.fromfile(F, dtype=np.float64, count=q_size)

    data=np.fromfile(F, dtype=np.float64).reshape(tt_size, l_size, q_size)

    return l, q, data




if __name__=='__main__':
    #
    root='/home/xwang/workspace/code/dcmode/workspace/'

    # scalar #
    folder='output/'
    fname=['decay_scalar/cltransfer_ad.dat', 'decay_scalar/cltransfer_addcs.dat']

    # tesnor #
    #folder='output_tensor/'
    #fname=['decay_tensor/cltransfer_ad.dat', 'decay_tensor/cltransfer_ten.dat', \
    #       'decay_tensor/cltransfer_addct.dat']



    # for scalar, the first few common outputs are [t2, e, t0, t1, b ...]
    # for tensor, the common outputs are [t2, e, b ]


    l, q, tf=load_cltf(root+folder+fname[0])
    print tf.shape
    print 'l=', l
    print 'q=', q
    

    #tt_idx = -1
    llist=[0, 1, 2, 3, 4, 5, 10, 20, 50]   # range(len(l))
    
    
    for li in llist:
        pl.semilogx(q, tf[0,li,:]+tf[2,li,:]+tf[3,li,:])   # t0, t1, t2
        #pl.semilogx(q, tf[0,li,:])
    
    
    pl.xlim([5e-6, 0.5])
    pl.show()
