import numpy, scipy.optimize

class SinusoidalRegression:
    def __init__ (self, domain, function):
        self.domain = domain
        self.function = function

    def fit_sin(self):
        '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
        currentDomain = numpy.array(self.domain)
        currentFunction = numpy.array(self.function)
        ff = numpy.fft.fftfreq(len(currentDomain), (currentDomain[1]-currentDomain[0]))   # assume uniform spacing
        Fyy = abs(numpy.fft.fft(currentFunction))
        guess_freq = abs(ff[numpy.argmax(Fyy[1:])+1])   # excluding the zero frequency "peak", which is related to offset
        guess_amp = numpy.std(currentFunction) * 2.**0.5 * 100
        guess_offset = numpy.mean(currentFunction)
        guess = numpy.array([guess_amp, 2.*numpy.pi*guess_freq, 0., guess_offset])

        def sinfunc(t, A, w, p, c):  return A * numpy.sin(w*t + p) + c
        popt, pcov = scipy.optimize.curve_fit(sinfunc, currentDomain, currentFunction, p0=guess, method='dogbox')
        A, w, p, c = popt
        f = w/(2.*numpy.pi) * 2
        fitfunc = lambda t: A * numpy.sin(w*t + p) + c
        return {
            "amp": A, 
            "omega": w, 
            "phase": p, 
            "offset": c, 
            "freq": f, 
            "period": 1./f, 
            "fitfunc": fitfunc, 
            "maxcov": numpy.max(pcov), 
            "rawres": (guess,popt,pcov)
        }