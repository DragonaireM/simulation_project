import math
import numpy as np

class Exponential:
    """
    Represents an exponential distribution with a given rate parameter.
    """
    def __init__(self, rate: float=1.0):
        if rate <= 0:
            raise ValueError("Rate must be positive.")
        self.rate = rate

    def pdf(self, x: float) -> float:
        if x < 0:
            return 0
        return self.rate * (2.718281828459045 ** (-self.rate * x))

    def cdf(self, x: float) -> float:
        if x < 0:
            return 0
        return 1 - (2.718281828459045 ** (-self.rate * x))

    def mean(self) -> float:
        return 1 / self.rate

    def variance(self) -> float:
        return 1 / (self.rate ** 2)
    
    def sample(self, size: int=1, seed: int | None=None) -> np.ndarray:
        rng = np.random.default_rng(seed)
        return rng.exponential(scale=1.0 / self.rate, size=size)
    
class Lognormal:
    """
    Represents a lognormal distribution with given mu and sigma parameters.
    """
    def __init__(self, desired_mean: float, desired_std: float):
        if desired_mean <= 0 or desired_std <= 0:
            raise ValueError("Mean and standard deviation must be positive.")
        variance = desired_std ** 2
        self.mu = math.log((desired_mean ** 2) / math.sqrt(variance + desired_mean ** 2))
        self.sigma = math.sqrt(math.log(1 + (variance / (desired_mean ** 2))))

    def pdf(self, x: float) -> float:
        if x <= 0:
            return 0
        return (1 / (x * self.sigma * (2 * math.pi) ** 0.5)) * math.exp(-((math.log(x) - self.mu) ** 2) / (2 * self.sigma ** 2))
    
    def cdf(self, x: float) -> float:
        if x <= 0:
            return 0
        z = (math.log(x) - self.mu) / self.sigma
        return 0.5 * (1 + math.erf(z / math.sqrt(2)))
    
    def mean(self) -> float:
        return math.exp(self.mu + (self.sigma ** 2) / 2)
    
    def variance(self) -> float:
        return (math.exp(self.sigma ** 2) - 1) * math.exp(2 * self.mu + self.sigma ** 2)

    def sample(self, size: int=1, seed: int | None=None) -> np.ndarray:
        rng = np.random.default_rng(seed)
        return rng.lognormal(mean=self.mu, sigma=self.sigma, size=size)

class Triangular:
    """
    Represents a triangular distribution with given lower, upper, and mode parameters.
    """
    def __init__(self, lower: float=0.0, upper: float=1.0, mode: float=0.5):
        if not (lower <= mode <= upper):
            raise ValueError("Parameters must satisfy lower <= mode <= upper.")
        self.lower = lower
        self.upper = upper
        self.mode = mode

    def pdf(self, x: float) -> float:
        if x < self.lower or x > self.upper:
            return 0
        if x == self.mode:
            return 2 / (self.upper - self.lower)
        elif x < self.mode:
            return 2 * (x - self.lower) / ((self.upper - self.lower) * (self.mode - self.lower))
        else:
            return 2 * (self.upper - x) / ((self.upper - self.lower) * (self.upper - self.mode))

    def cdf(self, x: float) -> float:
        if x < self.lower:
            return 0
        elif x == self.mode:
            return (self.mode - self.lower) / (self.upper - self.lower)
        elif x < self.mode:
            return ((x - self.lower) ** 2) / ((self.upper - self.lower) * (self.mode - self.lower))
        elif x < self.upper:
            return 1 - ((self.upper - x) ** 2) / ((self.upper - self.lower) * (self.upper - self.mode))
        else:
            return 1

    def mean(self) -> float:
        return (self.lower + self.upper + self.mode) / 3

    def variance(self) -> float:
        return (self.lower**2 + self.upper**2 + self.mode**2 - (self.lower * self.upper) - (self.lower * self.mode) - (self.upper * self.mode)) / 18

    def sample(self, size: int=1, seed: int | None=None) -> list[float]:
        rng = np.random.default_rng(seed)
        return rng.triangular(left=self.lower, mode=self.mode, right=self.upper, size=size).tolist()