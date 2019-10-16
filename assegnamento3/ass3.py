import logging
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.stats import norm
from scipy.integrate import simps
from matplotlib import pyplot as plt


class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    '''Pdf class child of InterpolatedUnivariateSpline'''

    def __init__(self, x, y, order=3):

        distr_int = simps(y, x)  # Compute distribution integral
        res = abs(1. - simps(y, x))  # Difference of distr integral from 1

        if(res < 1e-3):  # is your distribution normalized? It is not.
            y = y / distr_int

        super().__init__(x, y, k=order, ext=2)  # Call to parent constructor
        self.y_cdf = np.array([self.integral(0, x_cdf) for x_cdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, self.y_cdf, k=order, ext=2)
        self.ppf = InterpolatedUnivariateSpline(self.y_cdf, x, k=order, ext=2)

    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2."""

        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size=1000):
        """Return an array of random values from the pdf.
        """
        return self.ppf(np.random.uniform(size=size))


if __name__ == '__main__':
    # x = np.array([0., 1., 2., 3., 4., 5., 6., 8.])
    # y = np.array([0.125, 0.125, 0, 0, 0., 0.250, 0.250, 0.250])
    x = np.linspace(0, 10, 100)
    y = norm.pdf(x, loc=5, scale=1)
    pdf = ProbabilityDensityFunction(x, y)

    # xx=np.linspace(0, 8, 100)

    a = np.array([0.2, 0.6])
    print(pdf(a))

    plt.figure('pdf')
    plt.title('pdf')
    plt.plot(x, pdf(x))
    plt.scatter(x, y, marker=".")
    plt.xlabel('x')
    plt.ylabel('pdf(x)')

    plt.figure('cdf')
    plt.title('cdf')
    plt.plot(x, pdf.cdf(x))
    plt.scatter(x, pdf.y_cdf, marker=".")
    plt.xlabel('x')
    plt.ylabel('cdf(x)')

    plt.figure('ppf')
    plt.title('ppf')
    plt.scatter(pdf.y_cdf, x, marker=".")
    plt.plot(pdf.y_cdf, pdf.ppf(pdf.y_cdf))
    plt.xlabel('x')
    plt.ylabel('ppf(x)')

    plt.show()
