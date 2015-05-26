import numpy as np
import scipy
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins=150)
    plt.suptitle('Residual histogram')
    plt.xlabel('Residuals')
    plt.ylabel('Frequency')
    return plt
    
      
if __name__ == '__main__':


    print "Linear regression predictions via gradient descent:"
    predicted, plot = predictions(df)
    print plot
    compute_r_squared(df['ENTRIESn_hourly'], predicted)
    print "Plotting the residuals:"
    plot_residuals(df, predicted)
    plt.show()
