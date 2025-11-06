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
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Exponential):
            return NotImplemented
        return self.rate == other.rate
    
class Lognormal:
    """
    Represents a lognormal distribution with given mu and sigma parameters.
    """
    def __init__(self, desired_mean: float):
        if desired_mean <= 0:
            raise ValueError("Mean must be positive.")
        self.cv = 0.325  # Coefficient of variation
        # Calculate mu and sigma based on desired mean and CV
        self.sigma = math.sqrt(math.log(self.cv ** 2 + 1))
        self.mu = math.log(desired_mean) - (self.sigma ** 2) / 2

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
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Lognormal):
            return NotImplemented
        return (
            math.isclose(self.mu, other.mu, rel_tol=1e-9, abs_tol=1e-12)
            and math.isclose(self.sigma, other.sigma, rel_tol=1e-9, abs_tol=1e-12)
        )

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

class TruncatedNormal:
    """
    Represents a truncated normal distribution for patient unpunctuality.
    U(c) ~ N(μU, σU) truncated to [-30, 30] minutes.

    Parameters:
        mu: Mean unpunctuality in minutes (typically 0 or -15)
        sigma: Standard deviation in minutes (typically 10 or 20)

    The distribution is truncated to [-30, 30] minutes to prevent unrealistic values.
    """
    # Fixed truncation bounds (class constants)
    LOWER_BOUND = -30.0  # minutes (can't arrive more than 30 min early)
    UPPER_BOUND = 30.0   # minutes (can't arrive more than 30 min late)

    def __init__(self, mu: float = 0.0, sigma: float = 10.0):
        if sigma <= 0:
            raise ValueError("Standard deviation (sigma) must be positive.")
        self.mu = mu
        self.sigma = sigma

    def pdf(self, x: float) -> float:
        """Probability density function of truncated normal distribution."""
        if x < self.LOWER_BOUND or x > self.UPPER_BOUND:
            return 0.0

        # Standard normal PDF
        z = (x - self.mu) / self.sigma
        normal_pdf = (1 / (self.sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * z ** 2)

        # Normalization constant (CDF of untruncated normal at bounds)
        alpha = (self.LOWER_BOUND - self.mu) / self.sigma
        beta = (self.UPPER_BOUND - self.mu) / self.sigma
        Z = 0.5 * (math.erf(beta / math.sqrt(2)) - math.erf(alpha / math.sqrt(2)))

        return normal_pdf / Z if Z > 0 else 0.0

    def cdf(self, x: float) -> float:
        """Cumulative distribution function of truncated normal distribution."""
        if x < self.LOWER_BOUND:
            return 0.0
        if x > self.UPPER_BOUND:
            return 1.0

        alpha = (self.LOWER_BOUND - self.mu) / self.sigma
        beta = (self.UPPER_BOUND - self.mu) / self.sigma
        xi = (x - self.mu) / self.sigma

        numerator = 0.5 * (math.erf(xi / math.sqrt(2)) - math.erf(alpha / math.sqrt(2)))
        denominator = 0.5 * (math.erf(beta / math.sqrt(2)) - math.erf(alpha / math.sqrt(2)))

        return numerator / denominator if denominator > 0 else 0.0

    def mean(self) -> float:
        """Mean of the truncated normal distribution."""
        alpha = (self.LOWER_BOUND - self.mu) / self.sigma
        beta = (self.UPPER_BOUND - self.mu) / self.sigma

        phi_alpha = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * alpha ** 2)
        phi_beta = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * beta ** 2)

        Z = 0.5 * (math.erf(beta / math.sqrt(2)) - math.erf(alpha / math.sqrt(2)))

        if Z > 0:
            return self.mu + self.sigma * (phi_alpha - phi_beta) / Z
        return self.mu

    def variance(self) -> float:
        """Variance of the truncated normal distribution."""
        alpha = (self.LOWER_BOUND - self.mu) / self.sigma
        beta = (self.UPPER_BOUND - self.mu) / self.sigma

        phi_alpha = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * alpha ** 2)
        phi_beta = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * beta ** 2)

        Z = 0.5 * (math.erf(beta / math.sqrt(2)) - math.erf(alpha / math.sqrt(2)))

        if Z > 0:
            term1 = (alpha * phi_alpha - beta * phi_beta) / Z
            term2 = ((phi_alpha - phi_beta) / Z) ** 2
            return self.sigma ** 2 * (1 + term1 - term2)
        return self.sigma ** 2

    def sample(self, size: int = 1, seed: int | None = None) -> np.ndarray:
        """
        Generate samples from the truncated normal distribution.
        Uses numpy's clip to truncate values to [LOWER_BOUND, UPPER_BOUND].
        """
        rng = np.random.default_rng(seed)
        samples = rng.normal(loc=self.mu, scale=self.sigma, size=size)
        return np.clip(samples, self.LOWER_BOUND, self.UPPER_BOUND)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TruncatedNormal):
            return NotImplemented
        return self.mu == other.mu and self.sigma == other.sigma