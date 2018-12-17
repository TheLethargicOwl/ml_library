#linear regression using classes

import numpy as np
import matplotlib.pyplot as plt


class optimize(object):
 
  def __init__(self,X_f,y):                           #x_f is matrix of n features.

    self.X_f = X_f
    self.y = y
    X_norm = self.normalise()
	
    m = np.shape(y)[0]
    X = np.hstack([np.ones((m,1)),X_norm])
    self.X = X
	
  def gettheta(self,alpha,iterations=100,lambda_=0):
  
    self.alpha = alpha
    self.iterations = iterations
    self.lambda_ = lambda_
	
    self.theta = self.gradDescent()
    
    return self.theta

  def costfunc(self,theta):
    
    m = np.shape(self.X)[0]
    predit = np.dot(self.X,theta)
    sq_error = np.power((predit-self.y),2)
    J = (1.0/(2*m))*np.sum(sq_error)
    regular=(self.lambda_/(2*m))*(np.sum(np.multiply(theta,theta))- (theta[0,0]**2))
    J = J + regular
    return J

  def gradDescent(self):

    n=np.shape(self.X)[1]-1
    m= np.shape(self.X)[0]
    
    theta = np.random.random((n+1,1))
    print np.shape(theta)
    J_vec = np.ones(self.iterations)

    for i in range(0,self.iterations):
    
      a = np.dot(self.X,theta)
      b = self.y
      predt = np.subtract(a,b)
      grad = np.dot((self.X).T,predt)
      theta = np.subtract(theta*(1 - (self.lambda_*self.alpha)/m),grad*((self.alpha*1.0)/m))
      J_vec[i]=self.costfunc(theta)
    
    self.J_vec = J_vec
    return theta

  def normalise(self):
      
    mean= np.mean(self.X_f,0)
    self.mean = mean
    stddev = np.std(self.X_f,0)
    self.stddev = stddev
    X_norm = np.true_divide((self.X_f - mean),stddev)
    return X_norm
	
  def plotJvsno(self,alpha,iterations,lambda_=0):
    
    self.alpha = alpha
    self.iterations = iterations
    self.lambda_ = lambda_
	
    self.gradDescent()
	
    plt.plot(np.arange(0,iterations),self.J_vec)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Cost vs Iterations')
    plt.show()
    
  def predict(self,x):                             # X is a vector of n features
      
    x_norm = np.true_divide((x - self.mean),self.stddev)
    x_new = np.hstack([np.ones((np.shape(x_norm)[0],1)),x_norm])
    print ('.........',np.shape(x_new))
    return np.dot(x_new,self.theta)

  def accuracy(self,x,y):                              # x is a vector of n features
      y_predt = self.predict(x)
      error  = (100*(y_predt - y))/y
      error_mean= np.mean(error)
      
      return (100 - error_mean)