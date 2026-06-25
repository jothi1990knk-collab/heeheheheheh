import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="IceCreamVerse 3D",
    page_icon="🍦",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main{
    background: linear-gradient(
    135deg,
    #0B1026,
    #161B3D,
    #0B1026
    );
}

h1,h2,h3{
    color:white;
}

.flavor-card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    backdrop-filter: blur(10px);
    margin:10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar Menu

selected = option_menu(
    menu_title="🍦 IceCreamVerse",
    options=[
        "Home",
        "3D View",
        "Flavors",
        "About Ice Cream",
        "Nutrition",
        "AI Recommender"
    ],
    icons=[
        "house",
        "badge-3d",
        "stars",
        "book",
        "activity",
        "robot"
    ],
    default_index=0
)

# HOME

if selected == "Home":

    st.title("🍦 ICECREAMVERSE")
    st.subheader("Future of Ice Cream Experience")

    col1,col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ### Welcome to IceCreamVerse

        Explore premium ice creams in a futuristic
        3D environment.

        Features:
        - Interactive 3D Models
        - Flavor Explorer
        - Nutrition Insights
        - AI Recommendations
        - Beautiful Animations
        """)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1563805042-7684c019e1cb",
            use_container_width=True
        )

# 3D VIEW

elif selected == "3D View":

    st.title("🍦 Interactive 3D Ice Cream")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter3d(
            x=[0],
            y=[0],
            z=[0],
            mode='markers',
            marker=dict(
                size=60,
                color='pink'
            )
        )
    )

    fig.update_layout(
        scene=dict(
            bgcolor="black"
        ),
        paper_bgcolor="#0B1026",
        font_color="white",
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)

# FLAVORS

elif selected == "Flavors":

    st.title("🌈 Ice Cream Flavors")

    flavors = [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Mango",
        "Blueberry",
        "Butterscotch",
        "Cookies & Cream",
        "Pistachio"
    ]

    cols = st.columns(4)

    for i, flavor in enumerate(flavors):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div class='flavor-card'>
                <h3>{flavor}</h3>
                Premium flavor experience.
                </div>
                """,
                unsafe_allow_html=True
            )

# ABOUT

elif selected == "About Ice Cream":

    st.title("📖 About Ice Cream")

    st.header("History")
    st.write("""
    Ice cream has origins tracing back thousands of years.
    Ancient civilizations enjoyed frozen desserts before
    modern ice cream evolved into the treat we know today.
    """)

    st.header("How Ice Cream Is Made")

    st.markdown("""
    1. Milk Collection
    2. Cream Blending
    3. Sugar Mixing
    4. Pasteurization
    5. Homogenization
    6. Flavor Addition
    7. Freezing
    8. Packaging
    """)

    st.header("Types")

    st.markdown("""
    - Gelato
    - Sorbet
    - Frozen Yogurt
    - Kulfi
    - Soft Serve
    - Sundae
    - Mochi Ice Cream
    """)

    st.header("Fun Facts")

    st.markdown("""
    - Vanilla is the most popular flavor.
    - Ice cream contains air for smooth texture.
    - July is celebrated as Ice Cream Month in several places.
    """)

# NUTRITION

elif selected == "Nutrition":

    st.title("📊 Nutrition Dashboard")

    nutrition = pd.DataFrame({
        "Nutrient":[
            "Calories",
            "Protein",
            "Carbs",
            "Fat",
            "Sugar"
        ],
        "Value":[210,4,24,11,20]
    })

    st.dataframe(nutrition)

    chart = go.Figure(
        data=[
            go.Bar(
                x=nutrition["Nutrient"],
                y=nutrition["Value"],
                marker_color="cyan"
            )
        ]
    )

    chart.update_layout(
        paper_bgcolor="#0B1026",
        plot_bgcolor="#0B1026",
        font_color="white"
    )

    st.plotly_chart(chart)

# AI RECOMMENDER

elif selected == "AI Recommender":

    st.title("🤖 AI Flavor Recommender")

    sweetness = st.slider(
        "Sweetness Level",
        1,
        10,
        5
    )

    fruit = st.checkbox("Fruit Lover")

    chocolate = st.checkbox("Chocolate Lover")

    if st.button("Recommend"):

        if chocolate:
            st.success(
                "🍫 Recommended: Chocolate Supreme"
            )

        elif fruit:
            st.success(
                "🥭 Recommended: Tropical Mango Blast"
            )

        else:
            st.success(
                "🍦 Recommended: Classic Vanilla Dream"
            )