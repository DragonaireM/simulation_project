"""
Script to verify that inter-arrival times follow: Fixed Schedule + Normal Distribution

This script will:
1. Generate inter-arrival times using your simulation parameters
2. Visualize the distribution to verify it's fixed_value + normal_distribution
3. Perform statistical tests to confirm the distribution properties
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from distribution import TruncatedNormal, Triangular
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 10)

def verify_interarrival_distribution(
    scheduled_arrival: float = 17.0,
    mu: float = 0.0,
    sigma: float = 10.0,
    sample_size: int = 1000,
    seed: int = 42
):
    """
    Verify that inter-arrival times = scheduled_arrival + TruncatedNormal(mu, sigma)

    Parameters:
        scheduled_arrival: Fixed appointment slot spacing (minutes)
        mu: Mean of the deviation (patient unpunctuality)
        sigma: Standard deviation of the deviation
        sample_size: Number of samples to generate for verification
        seed: Random seed for reproducibility
    """

    print("="*70)
    print("INTER-ARRIVAL TIME DISTRIBUTION VERIFICATION")
    print("="*70)

    # Create distribution
    iat_distribution = TruncatedNormal(mu=mu, sigma=sigma)

    # Generate deviations
    deviations = iat_distribution.sample(size=sample_size, seed=seed)

    # Generate inter-arrival times (same as in simulation.py line 54)
    interarrival_times = np.array([scheduled_arrival + dev for dev in deviations])

    # Print statistics
    print(f"\n1. CONFIGURATION:")
    print(f"   - Scheduled Arrival (fixed): {scheduled_arrival:.2f} minutes")
    print(f"   - Deviation Mean (mu): {mu:.2f} minutes")
    print(f"   - Deviation Std Dev (sigma): {sigma:.2f} minutes")
    print(f"   - Truncation bounds: [{iat_distribution.LOWER_BOUND}, {iat_distribution.UPPER_BOUND}]")
    print(f"   - Sample size: {sample_size}")

    print(f"\n2. DEVIATION STATISTICS (should follow N({mu}, {sigma}²) truncated):")
    print(f"   - Mean: {np.mean(deviations):.2f} minutes (expected: ~{mu:.2f})")
    print(f"   - Std Dev: {np.std(deviations):.2f} minutes (expected: ~{sigma:.2f})")
    print(f"   - Min: {np.min(deviations):.2f} minutes (>= {iat_distribution.LOWER_BOUND})")
    print(f"   - Max: {np.max(deviations):.2f} minutes (<= {iat_distribution.UPPER_BOUND})")

    print(f"\n3. INTER-ARRIVAL TIME STATISTICS:")
    print(f"   - Mean: {np.mean(interarrival_times):.2f} minutes")
    print(f"   - Expected Mean: {scheduled_arrival + iat_distribution.mean():.2f} minutes")
    print(f"   - Std Dev: {np.std(interarrival_times):.2f} minutes")
    print(f"   - Min: {np.min(interarrival_times):.2f} minutes")
    print(f"   - Max: {np.max(interarrival_times):.2f} minutes")

    # Normality test on deviations (should be approximately normal)
    _, p_value = stats.shapiro(deviations[:5000] if len(deviations) > 5000 else deviations)
    print(f"\n4. NORMALITY TEST (Shapiro-Wilk on deviations):")
    print(f"   - p-value: {p_value:.4f}")
    print(f"   - Result: {'PASS - Deviations are approximately normal' if p_value > 0.05 else 'Note: p < 0.05, but truncation may affect test'}")

    # Create visualizations
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Inter-Arrival Time Distribution Verification\n' +
                 f'IAT = {scheduled_arrival} (fixed) + TruncatedNormal({mu}, {sigma}²)',
                 fontsize=16, fontweight='bold')

    # Plot 1: Histogram of deviations
    ax1 = axes[0, 0]
    ax1.hist(deviations, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black')

    # Overlay theoretical truncated normal PDF
    x_range = np.linspace(iat_distribution.LOWER_BOUND, iat_distribution.UPPER_BOUND, 1000)
    theoretical_pdf = [iat_distribution.pdf(x) for x in x_range]
    ax1.plot(x_range, theoretical_pdf, 'r-', linewidth=2, label='Theoretical PDF')

    ax1.axvline(mu, color='green', linestyle='--', linewidth=2, label=f'Mean = {mu}')
    ax1.axvline(iat_distribution.LOWER_BOUND, color='orange', linestyle='--', alpha=0.7, label='Truncation bounds')
    ax1.axvline(iat_distribution.UPPER_BOUND, color='orange', linestyle='--', alpha=0.7)

    ax1.set_xlabel('Deviation (minutes)', fontsize=11)
    ax1.set_ylabel('Density', fontsize=11)
    ax1.set_title('Deviations from Schedule\n(Should be Truncated Normal)', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Histogram of inter-arrival times
    ax2 = axes[0, 1]
    ax2.hist(interarrival_times, bins=50, density=True, alpha=0.7, color='lightcoral', edgecolor='black')
    ax2.axvline(scheduled_arrival, color='green', linestyle='--', linewidth=2,
                label=f'Scheduled = {scheduled_arrival} min')
    ax2.axvline(np.mean(interarrival_times), color='blue', linestyle='--', linewidth=2,
                label=f'Actual Mean = {np.mean(interarrival_times):.1f} min')

    ax2.set_xlabel('Inter-Arrival Time (minutes)', fontsize=11)
    ax2.set_ylabel('Density', fontsize=11)
    ax2.set_title('Inter-Arrival Times\n(Fixed Schedule + Deviation)', fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Plot 3: Q-Q plot for deviations (check normality)
    ax3 = axes[0, 2]
    stats.probplot(deviations, dist="norm", plot=ax3)
    ax3.set_title('Q-Q Plot of Deviations\n(Should be linear if normal)', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)

    # Plot 4: Cumulative distribution of deviations
    ax4 = axes[1, 0]
    sorted_deviations = np.sort(deviations)
    empirical_cdf = np.arange(1, len(sorted_deviations) + 1) / len(sorted_deviations)
    theoretical_cdf = [iat_distribution.cdf(x) for x in sorted_deviations]

    ax4.plot(sorted_deviations, empirical_cdf, 'b-', linewidth=2, label='Empirical CDF', alpha=0.7)
    ax4.plot(sorted_deviations, theoretical_cdf, 'r--', linewidth=2, label='Theoretical CDF')
    ax4.set_xlabel('Deviation (minutes)', fontsize=11)
    ax4.set_ylabel('Cumulative Probability', fontsize=11)
    ax4.set_title('CDF Comparison\n(Empirical vs Theoretical)', fontsize=12, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Plot 5: Time series of inter-arrival times
    ax5 = axes[1, 1]
    sample_indices = np.arange(min(100, sample_size))
    ax5.plot(sample_indices, interarrival_times[:len(sample_indices)], 'o-',
             alpha=0.6, markersize=4, label='IAT samples')
    ax5.axhline(scheduled_arrival, color='green', linestyle='--', linewidth=2,
                label=f'Fixed schedule = {scheduled_arrival}')
    ax5.axhline(np.mean(interarrival_times), color='blue', linestyle='--', linewidth=2,
                label=f'Mean = {np.mean(interarrival_times):.1f}')

    # Add confidence interval band
    ax5.fill_between(sample_indices,
                     scheduled_arrival - 2*sigma,
                     scheduled_arrival + 2*sigma,
                     alpha=0.2, color='green', label='±2σ band')

    ax5.set_xlabel('Patient Index', fontsize=11)
    ax5.set_ylabel('Inter-Arrival Time (minutes)', fontsize=11)
    ax5.set_title(f'First {min(100, sample_size)} Inter-Arrival Times\n(Showing fixed + random pattern)',
                  fontsize=12, fontweight='bold')
    ax5.legend()
    ax5.grid(True, alpha=0.3)

    # Plot 6: Box plot comparison
    ax6 = axes[1, 2]
    bp = ax6.boxplot([deviations, interarrival_times],
                      tick_labels=['Deviations', 'Inter-Arrival Times'],
                      patch_artist=True)
    bp['boxes'][0].set_facecolor('skyblue')
    bp['boxes'][1].set_facecolor('lightcoral')

    ax6.axhline(0, color='gray', linestyle='--', alpha=0.5)
    ax6.axhline(scheduled_arrival, color='green', linestyle='--', linewidth=2,
                label=f'Fixed schedule = {scheduled_arrival}')
    ax6.set_ylabel('Time (minutes)', fontsize=11)
    ax6.set_title('Distribution Comparison\n(Box Plots)', fontsize=12, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    # Save the figure
    output_path = 'c:\\Users\\jingh\\MH4702 project\\others\\project\\interarrival_verification.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n5. VISUALIZATION SAVED:")
    print(f"   - File: {output_path}")
    print(f"\n{'='*70}")
    print("VERIFICATION COMPLETE!")
    print("="*70)
    print("\nInterpretation Guide:")
    print("- Top-left plot: Deviations should follow the red theoretical curve")
    print("- Top-middle plot: IAT distribution centered around scheduled_arrival")
    print("- Top-right plot: Points should follow diagonal line (indicates normality)")
    print("- Bottom-left plot: Blue and red lines should overlap closely")
    print("- Bottom-middle plot: IAT should fluctuate around the green line")
    print("- Bottom-right plot: Shows the shift from deviations to IAT")

    plt.close('all')  # Close instead of show for non-interactive mode

    return deviations, interarrival_times


if __name__ == "__main__":
    # Test with default parameters from main.py
    print("\nTest 1: Default parameters (scheduled_arrival=17, mu=0, sigma=10)")
    print("-" * 70)
    deviations1, iat1 = verify_interarrival_distribution(
        scheduled_arrival=17.0,
        mu=0.0,
        sigma=10.0,
        sample_size=1000,
        seed=42
    )

    # Optionally test with different parameters (commented out for non-interactive mode)
    # print("\n\n")
    # input("Press Enter to test with different parameters (scheduled_arrival=20, mu=-5, sigma=15)...")
    # print("\nTest 2: Different parameters")
    # print("-" * 70)
    # deviations2, iat2 = verify_interarrival_distribution(
    #     scheduled_arrival=20.0,
    #     mu=-5.0,
    #     sigma=15.0,
    #     sample_size=1000,
    #     seed=123
    # )
