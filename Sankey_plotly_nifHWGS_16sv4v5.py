import plotly.graph_objects as go

labels = [
    "Isolates: 203 total, 15 nifH+",       # 0
    "Iso v4/v5: 156 total, 10 nifH+",  # 1
    "47 isolates excluded from seq",          # 2
    "WGS: 118 total, 12 nifH+",                  # 3
    "WGS--no v4/v5: 35 total, 4 nifH+",           # 4
    "v4/v5--no WGS: 73 total, 3 nifH+",           # 5
    "Both WGS & v4/v5: 83 total, 7 nifH+"        # 6
]

# Main data flows
source = [
    0,  # Total -> v4/v5
    0,  # Total -> no v4/v5
    1,  # v4/v5 -> both
    1,  # v4/v5 -> v4/v5 no WGS
    2,  # no v4/v5 -> WGS no v4/v5
    1,  # v4/v5 -> both (this is to get WGS part)
    2   # no v4/v5 -> WGS no v4/v5
]

target = [
    1,
    2,
    6,
    5,
    4,
    3,
    3
]

values = [
    156,  # Total -> v4/v5
    47,   # Total -> no v4/v5
    83,   # v4/v5 -> both
    73,   # v4/v5 -> no WGS
    35,   # no v4/v5 -> WGS no v4/v5
    83,   # v4/v5 -> WGS (via both)
    35    # no v4/v5 -> WGS
]

# nifH+ overlay flows (non-additive, just coloring subset)
source_nifH = [
    0,  # Total -> v4/v5
    0,  # Total -> no v4/v5 (0 with nifH+ assumed)
    1,  # v4/v5 -> both
    1,  # v4/v5 -> v4/v5 no WGS
    2,  # no v4/v5 -> WGS no v4/v5
    1,  # v4/v5 -> WGS (via both)
    2   # no v4/v5 -> WGS
]

target_nifH = [
    1,
    2,
    6,
    5,
    4,
    3,
    3
]

values_nifH = [
    10,  # Total -> v4/v5 (nifH+)
    0,   # Total -> no v4/v5
    7,   # v4/v5 -> both
    3,   # v4/v5 -> v4/v5 no WGS
    4,   # no v4/v5 -> WGS no v4/v5
    7,   # v4/v5 -> WGS (via both)
    4    # no v4/v5 -> WGS
]

# Combine flows
source_all = source + source_nifH
target_all = target + target_nifH
values_all = values + values_nifH
link_colors = ['rgba(0, 0, 255, 0.4)'] * len(source) + ['rgba(255, 0, 0, 0.7)'] * len(source_nifH)

# Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        label=labels,
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        color=['lightblue']*len(labels)
    ),
    link=dict(
        source=source_all,
        target=target_all,
        value=values_all,
        color=link_colors
    )
)])

fig.update_layout(title_text="Isolate Flow with nifH+ Subset Overlay", font_size=12)
fig.show()
fig.write_html("sankey_output.html", auto_open=True)
