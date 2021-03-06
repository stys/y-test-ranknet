"""
Linear algebra functions
========================

Notation
--------
Integers: i, j, k, m, n, q
Scalars: a, b, c, d, e, g, h
Vectors: s, t, u, v, w, x, y, z
Matrices: A, B, C, D, G, H 

Column-wise matrix representation
---------------------------------
Matrix are stored column-wise, i.e A[j] gets the j-th column of the matrix. 


"""
from sqlite3 import collections
from _ctypes import Array

def unit(n, k):
    """
    Create a unit vector  
    """
    return [ 0 if j!=k else 1 for j in xrange(n) ]

def vsum(x, y):
    """
    Compute element-wise sum of two vectors
    """
    
    assert len(x) == len(y), "Vectors must be of the same size"
    
    result = [0] * len(x)           # preallocate result
    
    for j in xrange(0, len(x)):     
        result[j] =  x[j] + y[j]    # sum of corresponding elements
        
    return result
  
def vmul(x, y): 
    """
    Compute element-wise multiplication of two vectors
    """
    
    assert len(x) == len(y), "Vectors must be of the same size"
    
    result = [0] * len(x)           # preallocate result
    
    for j in xrange(0, len(x)):     
        result[j] =  x[j] * y[j]    # product of corresponding elements
        
    return result 

def inner(x, y):
    """
    Inner product of two vectors
    
    Returns
    -------
    Scalar value
    
    """
    
    assert len(x) == len(y), "Vectors must be of the same size"
    
    result = 0
    
    for j in xrange(0, len(x)):
        result += x[j]*y[j]
        
    return result

def sax(a, x):
    """ 
    Multiply vector by scalar. The name is derived from `saxpy`:
    "Scalar `a` multiplied by vector `x` plus vector `y`"
    """
    
    # multiply each element of vector by scalar
    return map( lambda element: element*a, x )
    

def outer(x, y):
    """
    Outer product of two vectors
    
    Returns
    -------
    Column-wise matrix 
    
    """
    
    # Multiply x by elements of y
    return map(lambda e: sax(e, x), y)

def gax(A, x):
    """
    Multiply matrix A by vector x. The name is derived from `gaxpy`:
    "General matrix `A` by vector `x` plus vector `y`"
    """
        
    assert len(A) == len(x), "Matrix dimensions must agree"             
    
    z = [0] * len(A[0])                 # initial result is zero vector
    
    for j in xrange(0, len(A)):
        z = vsum(z, sax(x[j], A[j]))
    
    return z

def lgax(x, A):
    """
    Left side version of gax
    """
    
    assert len(x) == len(A[0])

    z = [0] * len(A)
    
    for j in xrange(0, len(A)):
        z[j] = inner(x, A[j])
        
    return z
    
class idxview(collections.Sequence):
    """
    View of list indexed by another list
    """
    def __init__(self, arr, idx):
        self.arr = arr
        self.idx = idx
    
    def __getitem__(self, index):
        return self.arr[self.idx[index]]    
    
    def __len__(self):
        return len(self.idx) 
    
    def __iter__(self):   
        self.current = -1
        return self
    
    def next(self):
        if self.current >= len(self.idx)-1:
            raise StopIteration
        else:
            self.current += 1
            return self.arr[self.idx[self.current]]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

