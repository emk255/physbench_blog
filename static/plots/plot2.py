import matplotlib.pyplot as plt
import numpy as np

# Set style to match your blog's clean aesthetic
plt.style.use("seaborn-v0_8-whitegrid")

# Data from the table - performance percentages
models = ["GPT-4.1\n(CoT)", "GPT-5\n(Minimal Reasoning)", "Gemini 2.5 Pro"]
olympiad_bench = [44.06, 50.76, 65.01]
physics_bench = [23.84, 29.18, 49.23]

# Color scheme
olympiad_color = "#E91E63"  # Pink accent from your blog
physics_color = "#5C6BC0"  # Blue-purple

fig, ax = plt.subplots(figsize=(12, 8))

x = np.arange(len(models))
width = 0.35

# Create bars
bars1 = ax.bar(
    x - width / 2,
    olympiad_bench,
    width,
    label="OlympiadBench (463 questions)",
    color=olympiad_color,
    alpha=0.8,
    edgecolor="white",
    linewidth=1.5,
)

bars2 = ax.bar(
    x + width / 2,
    physics_bench,
    width,
    label="PhysBench (843 questions)",
    color=physics_color,
    alpha=0.8,
    edgecolor="white",
    linewidth=1.5,
)

# Customize axes
ax.set_ylabel(
    "Overall Accuracy (%)",
    fontsize=13,
    fontweight="600",
    color="#424242",
    fontfamily="sans-serif",
)
ax.set_title(
    "Model Performance Comparison: OlympiadBench vs PhysBench",
    fontsize=16,
    fontweight="700",
    pad=20,
    color="#2C3E50",
    fontfamily="sans-serif",
)

# Set x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=11, color="#424242", ha="center")

# Style the legend
legend = ax.legend(
    loc="upper right",
    framealpha=0.95,
    fontsize=11,
    edgecolor="#E0E0E0",
    fancybox=True,
    shadow=True,
)
legend.get_frame().set_facecolor("white")

# Grid styling
ax.grid(axis="y", alpha=0.2, linestyle="-", linewidth=0.8, color="#BDBDBD")
ax.set_axisbelow(True)

# Spine styling
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#BDBDBD")
ax.spines["bottom"].set_color("#BDBDBD")
ax.spines["left"].set_linewidth(1.5)
ax.spines["bottom"].set_linewidth(1.5)

# Tick styling
ax.tick_params(axis="both", colors="#757575", labelsize=10)


# Add value labels on bars
def add_value_labels(bars, values):
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 0.5,
            f"{val:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="600",
            color="#424242",
        )


add_value_labels(bars1, olympiad_bench)
add_value_labels(bars2, physics_bench)

# Set background color
fig.patch.set_facecolor("white")
ax.set_facecolor("#FAFAFA")

# Set y-axis limits with some padding
ax.set_ylim(0, max(max(olympiad_bench), max(physics_bench)) + 8)

plt.tight_layout()
plt.savefig(
    "model_performance_comparison.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
plt.show()
