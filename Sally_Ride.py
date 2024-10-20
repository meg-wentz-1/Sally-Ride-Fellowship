import plotly.graph_objects as go
import random
import math

# Define key moments and assign random coordinates
key_moments = [
    {"label": "First time seeing NASA logo", "description": "My dad had the logo on a document in his office, that's when it all began"},
    {'label': 'Learning to Code', 'description': 'Finally feeling like I found something I was good at.'},
    {"label": "Joining the robotics team", "description": "Discovered my love for engineering and problem-solving."},
    {"label": "Winning the robotics competition", "description": "Realized I could turn my passion into a career."},
    {"label": "Applying to Purdue University", "description": "Taking the first step to get closer to my future."},
    {"label": "Learning about Small Satellite Systems", "description": "Discovered my calling within aerospace engineering."},
    {"label": "Getting accepted to Purdue University", "description": "Taking my next giant leap."},
    {"label": "First day of classes", "description": "Embarking on my journey that was harder than I thought."},
    {'label': 'Seeing my First Rocket Launch', "description": 'I knew I was on the right path and I could not give up just yet.'},
    {"label": "Learning to fail", "description": "Realizing that failure is part of the process through my classes."},
    {"label": "XGAnalytics internship", "description": "Falling in love with data science and analytics."},
    {"label": "Caterpillar internship", "description": "Gained exposure to engineering that fuels my passion."},
    {"label": "Aerospace Design Course", "description": "Found my calling in systems engineering."},
    {"label": "Joining Purdue SEDS", "description": "Found a community to nurture my aspirations and allow me to learn."},
    {"label": "Boiler Bus Project", "description": "Helping to pave the way for student friendly and affordable CubeSats."},
    {'label': 'STEM Outreach', 'description': 'Inspiring the next generation of engineers and scientists and giving me a sense of hope.'},
    {'label': 'Meeting Wendy Lawerence', 'description': 'Inspired me to keep pushing forward and never give up.'},
    {'label': 'Graduating from Purdue University', 'description': 'I will be ready to take on the world.'},
    {'label': 'Joining NASA', 'description': 'I will get to become part of the team that inspired me.'},
    {'label': 'Using CubeSats for good', 'description': 'I will use my knowledge to help our environment and society.'},
    {'label': 'Inspiring the next generation', 'description': 'I will help others reach for the stars.'},
]

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate random coordinates for stars with minimum distance check
stars = []
min_distance = 0.1  # Increased minimum distance between stars
top_margin = 0.4 # Define a top margin to avoid placing stars too close to the top

for moment in key_moments:
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1 - top_margin)  # Ensure y is within the allowed range
        if all(distance(x, y, star["x"], star["y"]) >= min_distance for star in stars):
            stars.append({
                "x": x,
                "y": y,
                "label": moment["label"],
                "description": moment["description"]
            })
            break

# Create star map figure
fig = go.Figure()

# Add stars with labels and descriptions on hover
for star in stars:
    fig.add_trace(go.Scatter(
        x=[star["x"]],
        y=[star["y"]],
        mode='text',  # Only text mode for the star emoji
        text="⭐ " + star["label"],  # Combine star emoji and label
        hovertext=star["description"],  # Description on hover
        hoverinfo='text',
        textposition="top right",  # Position label near the star
        showlegend=False  # Hide from legend
    ))

# Set chart layout to look like a starry night
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    xaxis=dict(showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False),
    title={
        "text": "How the Stars Aligned: My Journey to Aerospace<br><span style='font-size: 14px;'>Hover over each star to discover the moments that shaped my path and what I hope to do.</span><br><span style='font-size: 12px;'>Use the pan function at the top right to move around and see all the stars.</span><br><span style='font-size: 10px;'>Created using Python</span>",
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"
    },
    font=dict(color='white'),
    showlegend=False  # Remove legend entirely
)

# Show the star map
fig.show()

# Optional: Save the star map as an interactive HTML file
fig.write_html("Meg_Wentz_Star_Map.html")
