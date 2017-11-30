---
layout: post
title: Derivation of FWHM and Height for Peak Fitting Functions
tag: Learning
category: Science

excerpt: Gaussian (Normal distribution), Lorentzian, Voigt, Pseudo Voigt, Moffat, Pearson 7, Students T, Breit-Wigner-Fano, Lognormal, Damped Oscillator, Exponential Gaussian, Skewed Gaussian, Donaich Sunjic (photo-emission),
---



* TOC
{:toc}

## Gaussian (Normal distribution)

A = amplitude, $$\mu$$ = center, and $$\sigma$$ = sigma
(see [Wikipedia](http://en.wikipedia.org/wiki/Normal_distribution) for more info)

$$f(x;A,\mu,\sigma)=\frac{A}{\sigma\sqrt{2\pi}}\exp\left[\frac{-(x-\mu)^2}{2\sigma^2}\right]$$

### Gaussian Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma)=\frac{A}{\sigma\sqrt{2\pi}}\exp\left[\frac{-(\mu-\mu)^2}{2\sigma^2}\right]$$

$$\operatorname{height} = \frac{A}{\sigma\sqrt{2\pi}}$$

### Gaussian FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.


$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\exp\left[\frac{-x_0^2}{2\sigma^2}\right] = 2^{-1}$$

$$x_0 = \pm\sigma\sqrt{2\ln 2}$$

$$\operatorname{FWHM}=2\sigma\sqrt{2\ln{2}}\approx 2.3548\sigma$$

* * *
## Lorentzian

A = amplitude, $$\mu$$ = center, and $$\sigma$$ = sigma
(see [Wikipedia](http://en.wikipedia.org/wiki/Cauchy_distribution) for more info)

$$f(x;A,\mu,\sigma)=\frac{A}{\pi}\left[\frac{\sigma}{(x-\mu)^2+\sigma^2}\right]$$

### Lorentzian Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma)=\frac{A}{\pi}\left[\frac{\sigma}{(\mu-\mu)^2+\sigma^2}\right]$$

$$\operatorname{height} = \frac{A}{\sigma\pi}$$

### Lorentzian FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{\sigma}{x_0^2+\sigma^2}=\frac{1}{2\sigma}$$

$$2\sigma^2=x_0^2+\sigma^2$$

$$x_0=\pm\sigma$$

$$\operatorname{FWHM}=2\sigma$$

* * *
## Voigt

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\gamma$$ = gamma
(see [Wikipedia](http://en.wikipedia.org/wiki/Voigt_profile) for more info)

$$f(x;A,\mu,\sigma,\gamma)=\frac{A\textrm{Re}[w(z)]}{\sigma\sqrt{2\pi}}$$

where

$$z=\frac{x-\mu +i\gamma}{\sigma\sqrt{2}}$$

$$w(z)=e^{-z^2}{\operatorname{erfc}}(-iz)$$

`erfc` is the complimentary error function.  As above,

### Voigt Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$z(\mu;\mu,\sigma,\gamma)=\frac{i\gamma}{\sigma\sqrt{2}}$$

$$f(\mu;A,\mu,\sigma,\gamma)=\frac{A\textrm{Re}[w(z)]}{\sigma\sqrt{2\pi}}$$

$$\operatorname{height}=\frac{A}{\sigma\sqrt{2\pi}}\textrm{Re}\left[w\left(\frac{i\gamma}{\sigma\sqrt{2}}\right)\right]$$

### Voigt FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A}{\sigma\sqrt{2\pi}}\textrm{Re}\left[w\left(\frac{x_0+i\gamma}{\sigma\sqrt{2}}\right)\right]=
\frac{1}{2}\frac{A}{\sigma\sqrt{2\pi}}\textrm{Re}\left[w\left(\frac{i\gamma}{\sigma\sqrt{2}}\right)\right]$$


$$e^{-\left(\frac{x_0+i\gamma}{\sigma\sqrt{2}}\right)^2}{\operatorname{erfc}}(-i\left(\frac{x_0+i\gamma}{\sigma\sqrt{2}}\right))=
e^{-\left(\frac{i\gamma}{\sigma\sqrt{2}}\right)^2}{\operatorname{erfc}}(-i\left(\frac{i\gamma}{\sigma\sqrt{2}}\right))$$


$$e^{-\left(\frac{x_0+i\gamma}{\sigma\sqrt{2}}\right)^2}{\operatorname{erfc}}(-i\left(\frac{x_0+i\gamma}{\sigma\sqrt{2}}\right))=
e^{-\left(\frac{i\gamma}{\sigma\sqrt{2}}\right)^2}{\operatorname{erfc}}(-i\left(\frac{i\gamma}{\sigma\sqrt{2}}\right))$$

Hmmm   IDK where to go from here.

$$\operatorname{FWHM}\approx 3.6013\sigma$$

* * *
## Pseudo Voigt

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\alpha$$ = fraction
(see [Wikipedia](http://en.wikipedia.org/wiki/Voigt_profile#Pseudo-Voigt_Approximation) for more info)


$$f(x;A,\mu,\sigma,\alpha)=
\frac{(1-\alpha)A}{\sigma_g\sqrt{2\pi}} e^{[{-{(x-\mu)^2}/{2\sigma_g^2}}]}
+\frac{\alpha A}{\pi} \big[\frac{\sigma}{(x - \mu)^2 + \sigma^2}\big]$$

where $$\sigma_g = {\sigma}/{\sqrt{2\ln{2}}}$$ so that the full width
at half maximum of each component and of the sum is $$2\sigma$$

### Pseudo Voigt Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma,\alpha)=
\frac{(1-\alpha)A}{\sigma_g\sqrt{2\pi}}
+\frac{\alpha A}{\pi\sigma}$$

$$\operatorname{height}=\frac{(1-\alpha)A}{\sigma\sqrt{\pi/\ln(2)}}
+\frac{\alpha A}{\pi\sigma}$$

### Pseudo Voigt FWHM
{:.no_toc}

The definition of the function depends on FWHM=2$$\sigma$$.

Please see derivations of [Gaussian](#gaussian-normal-distribution) and [Lorentzian](#lorentzian).


$$\operatorname{FWHM}=2\sigma$$

* * *
## Moffat

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\beta$$ = beta
(see [Wikipedia](https://en.wikipedia.org/wiki/Moffat_distribution) for more info)

$$f(x; A, \mu, \sigma, \beta) = A \big[\left(\frac{x-\mu}{\sigma}\right)^2+1\big]^{-\beta}$$

### Moffat Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu; A, \mu, \sigma, \beta) = A \big[1\big]^{-\beta}$$

$$\operatorname{height}=A$$

### Moffat FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\big[\left(\frac{x}{\sigma}\right)^2+1\big]^{-\beta}=2^{-1}$$

$$\left(\frac{x}{\sigma}\right)^2=2^{1/\beta}-1$$

$$x=\pm\sigma\sqrt{2^{1/\beta}-1}$$

$$\operatorname{FWHM}=2\sigma\sqrt{2^{1/\beta}-1}$$

* * *
## Pearson 7

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$m$$ = exponent
(see [wikipedia](http://en.wikipedia.org/wiki/Pearson_distribution#The_Pearson_type_VII_distribution) for more info)

$$f(x;A,\mu,\sigma,m)=\frac{A}{\sigma{\beta(m-\frac{1}{2},\frac{1}{2})}}\left[1+\frac{(x-\mu)^2}{\sigma^2}\right]^{-m}$$

where $$\beta$$ is the beta function

### Pearson 7 Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma,m)=\frac{A}{\sigma{\beta(m-\frac{1}{2},\frac{1}{2})}}\left[1+\frac{(\mu-\mu)^2}{\sigma^2}\right]^{-m}$$

$$\operatorname{height}=\frac{A}{\sigma{\beta(m-\frac{1}{2},\frac{1}{2})}}$$

### Pearson 7 FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\left[1+\frac{(x_0)^2}{\sigma^2}\right]^{-m}=\frac{1}{2}$$

$$x_0=\pm\sigma\sqrt{\left(\frac{1}{2}\right)^{-1/m}-1}$$

$$\operatorname{FWHM}=2\sigma\sqrt{2^{1/m}-1}$$



* * *
## Students T

A = amplitude, $$\mu$$ = center, and $$\sigma$$ = sigma
(see [Wikipedia](http://en.wikipedia.org/wiki/Student%27s_t-distribution) for more info)


$$f(x;A,\mu,\sigma)=\frac{A\Gamma(\frac{\sigma+1}{2})}{\sqrt{\sigma\pi}\,\Gamma(\frac{\sigma}{2})}
\Bigl[1+\frac{(x-\mu)^2}{\sigma}\Bigr]^{-\frac{\sigma+1}{2}}$$

where $$\Gamma(x)$$ is the gamma function.

### Students T Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma,m)=
\frac{A\Gamma(\frac{\sigma+1}{2})}{\sqrt{\sigma\pi}\,\Gamma(\frac{\sigma}{2})}
\Bigl[1+\frac{(\mu-\mu)^2}{\sigma}\Bigr]^{-\frac{\sigma+1}{2}}$$

$$\operatorname{height}=
\frac{A\Gamma(\frac{\sigma+1}{2})}{\sqrt{\sigma\pi}\,\Gamma(\frac{\sigma}{2})}$$

### Students T FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A\Gamma(\frac{\sigma+1}{2})}{\sqrt{\sigma\pi}\,\Gamma(\frac{\sigma}{2})}
\Bigl[1+\frac{(x_0)^2}{\sigma}\Bigr]^{-\frac{\sigma+1}{2}}=
\frac{1}{2}\frac{A\Gamma(\frac{\sigma+1}{2})}{\sqrt{\sigma\pi}\,\Gamma(\frac{\sigma}{2})}$$

$$\Bigl[1+\frac{(x_0)^2}{\sigma}\Bigr]^{-\frac{\sigma+1}{2}}=2^{-1}$$

$$x_0^2=\sigma(2^{\frac{2}{\sigma+1}}-1)$$

$$x_0=\pm\sqrt{2^{\frac{2}{\sigma+1}}\sigma-\sigma}$$

$$\operatorname{FWHM}=2\sqrt{2^{\frac{2}{\sigma+1}}\sigma-\sigma}$$

* * *
## Breit-Wigner-Fano

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$q$$ = exponent
(see [Wikipedia](http://en.wikipedia.org/wiki/Fano_resonance) for more info)

$$f(x;A,\mu,\sigma,q)=\frac{A(q\sigma/2+x-\mu)^2}{(\sigma/2)^2+(x-\mu)^2}$$

### Breit-Wigner-Fano Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma,m)=\frac{A(q\sigma/2+\mu-\mu)^2}{(\sigma/2)^2+(\mu-\mu)^2}$$

$$=\frac{A(q\sigma/2)^2}{(\sigma/2)^2}$$

$$\operatorname{height}=A(q)^2$$

### Breit-Wigner-Fano FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A(q\sigma/2+x_0)^2}{(\sigma/2)^2+(x_0)^2}=\frac{1}{2}A(q)^2$$

$$2(q\sigma/2+x_0)^2=q^2\left((\sigma/2)^2+(x_0)^2\right)$$

$$\frac{q^2\sigma^2}{2}+2q\sigma x_0+2x_0^2=\frac{q^2\sigma^2}{4}+x_0^2q^2$$

$$x_0^2(2-q^2)+2q\sigma x_0+\frac{q^2\sigma^2}{4}=0$$

$$x_0^2(q^2-2)-2q\sigma x_0-\frac{q^2\sigma^2}{4}=0$$

$$x = 2q\sigma \pm \frac{\sqrt{4q^2\sigma^2 + (q^2-2)(q^2\sigma^2)}}{2(q^2-2)}=0$$

$$\operatorname{FWHM}=2\frac{\sqrt{q^2\sigma^2(q^2+2)}}{2(q^2-2)}$$

* * *
## Lognormal

A = amplitude, $$\mu$$ = center, and $$\sigma$$ = sigma
(see [Wikipedia](http://en.wikipedia.org/wiki/Lognormal) for more info)

$$f(x; A, \mu, \sigma) = \frac{A}{\sigma\sqrt{2\pi}}\frac{e^{-(\ln(x) - \mu)^2/ 2\sigma^2}}{x}$$

### Lognormal Height
{:.no_toc}

Max height occurs at x = $$e^{\mu-\sigma^2}$$

$$f(e^{\mu-\sigma^2};A,\mu,\sigma)=\frac{A}{\sigma\sqrt{2\pi}}
\frac{e^{-(\ln(e^{\mu-\sigma^2})-\mu)^2/(2\sigma^2)}}{e^{\mu-\sigma^2}}$$

$$=\frac{A}{\sigma\sqrt{2\pi}}\frac{e^{\sigma^2/2}}{e^{\mu-\sigma^2}}$$

$$\operatorname{height}=\frac{A}{\sigma\sqrt{2\pi}}e^{\frac{\sigma^2}{2}-\mu}$$


### Lognormal FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height.


$$f(x_0;A,\mu,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A}{\sigma\sqrt{2\pi}}\frac{e^{-(\ln(x_0) - \mu)^2/ 2\sigma^2}}{x_0}=
\frac{A}{2\sigma\sqrt{2\pi}}e^{\frac{\sigma^2}{2}-\mu}$$

$$\frac{e^{-(\ln(x_0) - \mu)^2/ 2\sigma^2}}{x_0}=
\frac{1}{2}e^{\frac{\sigma^2}{2}-\mu}$$

$$\frac{x_0}{2}=e^{\frac{-(\ln(x_0) - \mu)^2}{2\sigma^2}-(\frac{\sigma^2}{2}-\mu)}$$

$$2\sigma^2\ln{x_0}+(\ln(x_0) - \mu)^2=2\sigma^2\left(\mu-\frac{\sigma^2}{2}+\ln{2}\right)$$

$$2\sigma^2\ln{x_0}+\ln(x_0)^2 - 2\mu\ln(x_0)+\mu^2=2\sigma^2\ln{2}-\sigma^4+2\sigma^2\mu-\mu^2$$

$$\ln(x_0)^2 + 2(\sigma^2-\mu)\ln(x_0)+(\sigma^2-\mu)^2=2\sigma^2\ln{2}-(\sigma^2-\mu)^2+(\sigma^2-\mu)^2$$

$$(\ln(x_0)+(\sigma^2-\mu))^2=2\sigma^2\ln{2}$$

$$\ln(x_0)=(\mu-\sigma^2)\pm\sqrt{2\sigma^2\ln{2}}$$

$$\operatorname{FWHM}=e^{(\mu-\sigma^2)+\sqrt{2\sigma^2\ln{2}}}-e^{(\mu-\sigma^2)-\sqrt{2\sigma^2\ln{2}}}$$


* * *
## Damped Oscillator

A = amplitude, $$\mu$$ = center, and $$\sigma$$ = sigma
(see [Wikipedia](http://en.wikipedia.org/wiki/Harmonic_oscillator#Amplitude_part) for more info)

$$f(x;A,\mu,\sigma)=\frac{A}{\sqrt{[1-(x/\mu)^2]^2+(2\sigma x/\mu)^2}}$$

### Damped Oscillator Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu;A,\mu,\sigma)=\frac{A}{\sqrt{[1-(\mu/\mu)^2]^2+(2\sigma \mu/\mu)^2}}$$

$$\operatorname{height}=\frac{A}{2\sigma}$$

### Damped Oscillator FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height.

$$f(x_0;A,\mu,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A}{\sqrt{[1-(x_0/\mu)^2]^2+(2\sigma x_0/\mu)^2}}=\frac{1}{2}\frac{A}{2\sigma}$$

$$(4\sigma)^2 = [1-(x_0/\mu)^2]^2+(2\sigma x_0/\mu)^2$$

$$1-2\frac{x_0^2}{\mu^2}+\frac{x_0^4}{\mu^4}+\frac{4\sigma^2 x_0^2}{\mu^2}-16\sigma^2=0$$

$$\frac{x_0^4}{\mu^4}+x_0^2\left(\frac{4\sigma^2-2}{\mu^2}\right)+1-16\sigma^2=0$$

$$x_0^4+x_0^2\mu^2(4\sigma^2-2)+\mu^2-16\mu^2\sigma^2=0$$

Substitute $$y=x_0^2$$

$$y^2+y\mu^2(4\sigma^2-2)+\mu^2-16\mu^2\sigma^2=0$$

$$y=\frac{-\mu^2(4\sigma^2-2)\pm\sqrt{(2\mu^2(2\sigma^2-1))^2-4(\mu^2-16\mu^2\sigma^2)}}{2}$$

$$y=\frac{\mu^2(2-4\sigma^2)\pm \sqrt{4\mu^4((4\sigma^4-4\sigma^2+1)-(1-16\sigma^2))}}{2}$$

$$y=\frac{\mu^2(2-4\sigma^2)\pm \sqrt{4\mu^4(4\sigma^4+12\sigma^2)}}{2}$$

$$y=\mu^2(1-2\sigma^2)\pm 2\sqrt{\mu^4(\sigma^4+3\sigma^2)}$$

Substitute back $$y=x_0^2$$

$$x_0=\pm\sqrt{\mu^2(1-2\sigma^2)\pm 2\sqrt{\mu^4\sigma^2(\sigma^2+3)}}$$

$$\operatorname{FWHM}=\sqrt{\mu^2(1-2\sigma^2)+ 2\sqrt{\mu^4\sigma^2(\sigma^2+3)}}
-\sqrt{\mu^2(1-2\sigma^2)- 2\sqrt{\mu^4\sigma^2(\sigma^2+3)}}$$



* * *
## Damped Harmonic Oscillator

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\gamma$$ = gamma
(see [Wikipedia](http://en.wikipedia.org/wiki/Harmonic_oscillator) and
[DAVE/PAN](https://www.ncnr.nist.gov/dave/) for more info)

$$f(x;A,\mu,\sigma,\gamma)=\frac{A\sigma}{\pi [1 - \exp(-x/\gamma)]}
\Big[ \frac{1}{(x-\mu)^2 + \sigma^2} - \frac{1}{(x+\mu)^2 + \sigma^2} \Big]$$

### DHO Height
{:.no_toc}

Max height occurs at x = $$\mu$$.

$$f(\mu;A,\mu,\sigma,\gamma)=\frac{A\sigma}{\pi [1 - \exp(-\mu/\gamma)]}
\Big[ \frac{1}{(\mu-\mu)^2 + \sigma^2} - \frac{1}{(\mu+\mu)^2 + \sigma^2} \Big]$$

$$\operatorname{height}=\frac{A\sigma}{\pi [1 - \exp(-\mu/\gamma)]}
\Big[\frac{1}{\sigma^2} - \frac{1}{4\mu^2 + \sigma^2} \Big]$$


### DHO FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height.

$$f(x_0;A,\mu,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{1}{1 - \exp(-x_0/\gamma)}
\Big[ \frac{1}{(x_0-\mu)^2 + \sigma^2} - \frac{1}{(x_0+\mu)^2 + \sigma^2} \Big]
=\frac{1}{1 - \exp(-\mu/\gamma)}
\Big[\frac{1}{\sigma^2} - \frac{1}{4\mu^2 + \sigma^2} \Big]$$

$$(1 - \exp(-\mu/\gamma))
\Big[ \frac{1}{(x_0-\mu)^2 + \sigma^2} - \frac{1}{(x_0+\mu)^2 + \sigma^2} \Big]
=(1 - \exp(-x_0/\gamma))
\Big[\frac{1}{\sigma^2} - \frac{1}{4\mu^2 + \sigma^2} \Big]$$

Hmmm   IDK where to go from here.

But as defined in DAVE/PAN:

$$\operatorname{FWHM}\approx 2\sigma$$

* * *
## Exponential Gaussian

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\gamma$$ = gamma
(see [Wikipedia(http://en.wikipedia.org/wiki/Exponentially_modified_Gaussian_distribution)

$$f(x; A, \mu, \sigma, \gamma) = \frac{A\gamma}{2}
\exp\left[\gamma(\mu - x  + \gamma\sigma^2/2)\right]
\operatorname{erfc}\left(\frac{\mu + \gamma\sigma^2 - x}{\sqrt{2}\sigma}\right)$$


where :func:`erfc` is the complimentary error function.

### Exponential Gaussian Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu; A, \mu, \sigma, \gamma) = \frac{A\gamma}{2}
\exp\left[\gamma(\mu - \mu  + \gamma\sigma^2/2)\right]
\operatorname{erfc}\left(\frac{\mu + \gamma\sigma^2 - \mu}{\sqrt{2}\sigma}\right)$$

$$\operatorname{height}=\frac{A\gamma}{2}
\exp\left[\frac{\gamma^2\sigma^2}{2}\right]
\operatorname{erfc}\left(\frac{\gamma\sigma}{\sqrt{2}}\right)$$


### Exponential Gaussian FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A\gamma}{2}
\exp\left[\gamma(x_0  + \gamma\sigma^2/2)\right]
\operatorname{erfc}\left(\frac{\gamma\sigma^2 - x_0}{\sqrt{2}\sigma}\right)
=\frac{A\gamma}{2}
\exp\left[\frac{\gamma^2\sigma^2}{2}\right]
\operatorname{erfc}\left(\frac{\gamma\sigma}{\sqrt{2}}\right)$$

$$\exp\left[\gamma(x_0  + \gamma\sigma^2/2)\right]
\operatorname{erfc}\left(\frac{\gamma\sigma^2 - x_0}{\sqrt{2}\sigma}\right)
=\exp\left[\frac{\gamma^2\sigma^2}{2}\right]
\operatorname{erfc}\left(\frac{\gamma\sigma}{\sqrt{2}}\right)$$

Hmmm   IDK where to go from here.

But by observation:

$$\operatorname{FWHM}\approx2\sigma\sqrt{2\ln{2}}\approx 2.3548\sigma$$

* * *
## Skewed Gaussian

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\gamma$$ = gamma
(see [Wikipedia](http://en.wikipedia.org/wiki/Skew_normal_distribution) for more info)

$$f(x; A, \mu, \sigma, \gamma) = \frac{A}{\sigma\sqrt{2\pi}}
e^{[{-{(x-\mu)^2}/{2\sigma^2}}]} \Bigl\{ 1 +
{\operatorname{erf}}\bigl[ \frac{\gamma(x-\mu)}{\sigma\sqrt{2}} \bigr] \Bigr\}$$

where :func:`erf` is the error function.

### Skewed Gaussian Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu; A, \mu, \sigma, \gamma) = \frac{A}{\sigma\sqrt{2\pi}}
e^{[{-{(\mu-\mu)^2}/{2\sigma^2}}]} \Bigl\{ 1 +
{\operatorname{erf}}\bigl[ \frac{\gamma(\mu-\mu)}{\sigma\sqrt{2}} \bigr] \Bigr\}$$

$$\operatorname{height}=\frac{A}{\sigma\sqrt{2\pi}}$$

### Skewed Gaussian FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{A}{\sigma\sqrt{2\pi}}
e^{[{-{(x_0)^2}/{2\sigma^2}}]} \bigl\{ 1 +
{\operatorname{erf}}\bigl[ \frac{\gamma(x_0)}{\sigma\sqrt{2}} \bigr] \bigr\}
=\frac{A}{\sigma\sqrt{2\pi}}$$

$$e^{[{-{(x_0)^2}/{2\sigma^2}}]} \bigl\{ 1 +
{\operatorname{erf}}\bigl[ \frac{\gamma(x_0)}{\sigma\sqrt{2}} \bigr] \bigr\}=0$$

Hmmm   IDK where to go from here.

But by observation:

$$\operatorname{FWHM}\approx2\sigma\sqrt{2\ln{2}}\approx 2.3548\sigma$$


* * *
## Donaich Sunjic (photo-emission)

A = amplitude, $$\mu$$ = center, $$\sigma$$ = sigma, and $$\gamma$$ = gamma
(see [Casaxps](http://www.casaxps.com/help_manual/line_shapes.htm) for more info)

$$f(x; A, \mu, \sigma, \gamma) = \frac{A}{\sigma^{1-\gamma}}\frac{\cos\left[\pi\gamma/2 + (1-\gamma)
\arctan{((x - \mu)/\sigma)}\right]} {\left[1 + (x-\mu)/\sigma\right]^{(1-\gamma)/2}}$$

###  Donaich Sunjic Height
{:.no_toc}

Max height occurs at x = $$\mu$$

$$f(\mu; A, \mu, \sigma, \gamma) = \frac{A}{\sigma^{1-\gamma}}\frac{\cos\left[\pi\gamma/2 + (1-\gamma)
\arctan{((\mu - \mu)}/\sigma)\right]} {\left[1 + (\mu-\mu)/\sigma\right]^{(1-\gamma)/2}}$$

$$=\frac{A}{\sigma^{1-\gamma}}\frac{\cos\left[\pi\gamma/2\right]} {\left[1\right]^{(1-\gamma)/2}}$$

$$\operatorname{height}=\frac{A}{\sigma^{1-\gamma}}\cos(\pi\gamma/2)$$


###  Donaich Sunjic FWHM
{:.no_toc}

FWHM is found by finding the values of x at 1/2 the max height. For simplicity $$\mu$$ can be set to 0.

$$f(x_0;A,0,\sigma,m)=\frac{1}{2}f(\mu;A,\mu,\sigma,m)$$

$$\frac{\cos\left[\pi\gamma/2 + (1-\gamma)
\arctan{((x_0)}/\sigma)\right]} {\left[1 + (x_0)/\sigma\right]^{(1-\gamma)/2}}
=\cos(\pi\gamma/2)$$

Hmmm   IDK where to go from here.

$$\operatorname{FWHM}=$$
