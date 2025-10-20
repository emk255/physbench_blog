import matplotlib.pyplot as plt
import numpy as np

# Set style to match your blog's clean aesthetic
plt.style.use("seaborn-v0_8-whitegrid")

# Data from the table - performance percentages
# Electromagnetism (245 questions)
electro_data = {
    "models": ["Gemini 2.5 Pro", "GPT-4.1 (CoT)", "GPT-4.1-mini (CoT)"],
    "no_tools": [46.94, 24.08, 24.90],
    "with_search": [42.86, 23.05, 12.13],  # Missing data for GPT-4.1-mini
}

# Optics (97 questions)
optics_data = {
    "models": ["Gemini 2.5 Pro", "GPT-4.1 (CoT)", "GPT-4.1-mini (CoT)"],
    "no_tools": [49.48, 18.56, 13.40],
    "with_search": [39.18, 13.68, 12.22],
}

# Thermodynamics (152 questions)
thermo_data = {
    "models": ["Gemini 2.5 Pro", "GPT-4.1 (CoT)", "GPT-4.1-mini (CoT)"],
    "no_tools": [48.68, 25.00, 23.68],
    "with_search": [46.05, 17.22, 12.00],
}

# Different colors for each subject
colors = {
    "Electromagnetism": "#E91E63",  # Pink
    "Optics": "#5C6BC0",  # Blue-purple
    "Thermodynamics": "#26A69A",  # Teal
}


def create_plot(data, subject, questions, filename):
    """Create a plot for a specific subject showing toolless vs web search performance"""

    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(data["models"]))
    width = 0.35

    # Get color for this subject
    main_color = colors[subject]

    # Create bars - toolless (solid)
    bars1 = ax.bar(
        x - width / 2,
        data["no_tools"],
        width,
        color=main_color,
        alpha=0.8,
        edgecolor="white",
        linewidth=1.5,
    )

    # Handle missing data for web search
    search_values = []
    for val in data["with_search"]:
        if val is None:
            search_values.append(0)  # Will be hidden
        else:
            search_values.append(val)

    # Create bars - web search (hatched pattern)
    bars2 = ax.bar(
        x + width / 2,
        search_values,
        width,
        color=main_color,
        alpha=0.8,
        edgecolor="white",
        linewidth=1.5,
        hatch="///",  # Add diagonal lines to distinguish from toolless
    )

    # Hide bars for missing data
    for i, val in enumerate(data["with_search"]):
        if val is None:
            bars2[i].set_visible(False)

    # Customize axes
    ax.set_ylabel(
        "Performance (%)",
        fontsize=13,
        fontweight="600",
        color="#424242",
        fontfamily="sans-serif",
    )
    ax.set_title(
        f"{subject} Performance: Toolless vs Web Search\n({questions} questions)",
        fontsize=14,
        fontweight="700",
        pad=20,
        color="#2C3E50",
        fontfamily="sans-serif",
    )

    # Set x-axis labels - centered between bars
    ax.set_xticks(x)
    ax.set_xticklabels(data["models"], fontsize=11, color="#424242", ha="center")

    # Add top margin for better spacing between bars and labels
    ax.set_ylim(
        bottom=0,
        top=max(
            max(data["no_tools"]),
            max([v for v in data["with_search"] if v is not None]),
        )
        + 8,
    )

    # Create simple legend
    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor=main_color, alpha=0.8, label="No Tools"),
        Patch(facecolor=main_color, alpha=0.8, hatch="///", label="With Web Search"),
    ]

    legend = ax.legend(
        handles=legend_elements,
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
            if val is not None:
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

    add_value_labels(bars1, data["no_tools"])
    add_value_labels(bars2, data["with_search"])

    # Set background color
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#FAFAFA")

    plt.tight_layout()
    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight",
        facecolor="white",
        edgecolor="none",
    )
    plt.show()


# Create the three plots
create_plot(electro_data, "Electromagnetism", 245, "electro_performance.png")
create_plot(optics_data, "Optics", 97, "optics_performance.png")
create_plot(thermo_data, "Thermodynamics", 152, "thermo_performance.png")
