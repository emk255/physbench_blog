import matplotlib.pyplot as plt
import numpy as np

# Set style to match your blog's clean aesthetic
plt.style.use("seaborn-v0_8-whitegrid")

# Data
categories = [
    "Electromagnetism\n(245)",
    "Mechanics\n(321)",
    "Optics\n(97)",
    "Relativity\n(24)",
    "Thermodynamics\n(152)",
]
x = np.arange(len(categories))
width = 0.25

# Performance drops from baseline
gemini_drop = [-4.08, -3.69, -10.30, +4.17, -2.63]
gpt4_drop = [-1.03, +3.11, -4.88, -8.33, -7.78]
gpt4_mini_drop = [-12.77, -8.34, -1.18, -29.16, -11.68]

fig, ax = plt.subplots(figsize=(14, 7))

# Colors matching your blog theme (pink accent + complementary colors)
color_gemini = "#E91E63"  # Pink accent from your blog
color_gpt4 = "#5C6BC0"  # Complementary blue-purple
color_mini = "#26A69A"  # Complementary teal

# Create bars
bars1 = ax.bar(
    x - width,
    gemini_drop,
    width,
    label="Gemini 2.5 Pro",
    color=color_gemini,
    alpha=0.85,
    edgecolor="white",
    linewidth=1.5,
)
bars2 = ax.bar(
    x,
    gpt4_drop,
    width,
    label="GPT-4.1 (CoT)",
    color=color_gpt4,
    alpha=0.85,
    edgecolor="white",
    linewidth=1.5,
)
bars3 = ax.bar(
    x + width,
    gpt4_mini_drop,
    width,
    label="GPT-4.1-mini (CoT)",
    color=color_mini,
    alpha=0.85,
    edgecolor="white",
    linewidth=1.5,
)

# Add horizontal line at y=0
ax.axhline(y=0, color="#424242", linestyle="-", linewidth=2, alpha=0.7)

# Customize axes
ax.set_ylabel(
    "Performance Change (%)",
    fontsize=13,
    fontweight="600",
    color="#424242",
    fontfamily="sans-serif",
)
ax.set_xlabel(
    "Subject Area (Number of Questions)",
    fontsize=13,
    fontweight="600",
    color="#424242",
    fontfamily="sans-serif",
)
ax.set_title(
    "Impact of Augmenting Built-in Web Search Tools on Model Performance on PhysBench",
    fontsize=16,
    fontweight="700",
    pad=20,
    color="#2C3E50",
    fontfamily="sans-serif",
)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11, color="#424242")

# Style the legend to match your blog
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
def add_value_labels(bars, color):
    for bar in bars:
        height = bar.get_height()
        label_y = height + (0.5 if height > 0 else -0.5)
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            label_y,
            f"{height:+.1f}%",
            ha="center",
            va="bottom" if height > 0 else "top",
            fontsize=9,
            fontweight="600",
            color=color,
        )


add_value_labels(bars1, color_gemini)
add_value_labels(bars2, color_gpt4)
add_value_labels(bars3, color_mini)

# Set background color to match your blog
fig.patch.set_facecolor("white")
ax.set_facecolor("#FAFAFA")

plt.tight_layout()
plt.savefig(
    "web_search_impact.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
)
plt.show()
