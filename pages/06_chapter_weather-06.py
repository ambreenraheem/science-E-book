import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 06 · Water and Weather", layout="wide", initial_sidebar_state="expanded")

# ─── Global CSS (Applied early to prevent flicker) ───────────────────────────
st.markdown("""
<style>
    /* Hide default Streamlit MainMenu and Footer */
    #MainMenu, footer {display: none;}

    /* Hide default sidebar navigation list */
    div[data-testid="stSidebarNav"] {display: none;}

    /* Smooth font */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d2b5e 0%, #1565c0 50%, #0d47a1 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #e3f2fd !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    /* Button hover glow */
    div.stButton > button {
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:0.5rem 0;">
        <div style="font-size:2.5rem;">🔬</div>
        <div style="font-weight:700; font-size:1.1rem; color:#fff;">Science for Little Stars</div>
        <div style="font-size:0.8rem; color:#90caf9;">Grades 1–3 · Ages 5–8</div>
    </div>
    <hr style="border:2px solid lightblue;">
    """, unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Navigation")
    st.page_link("Home.py", label="🏠 Home", icon="🏠")
    st.page_link("pages/01_chapter_our_body-01.py", label="Ch 01 · Our Amazing Body", icon="🦴")
    st.page_link("pages/02_chapter_senses-02.py", label="Ch 02 · The Five Senses", icon="👁️")
    st.page_link("pages/03_chapter_plants-03.py", label="Ch 03 · Plants and Growth", icon="🌱")
    st.page_link("pages/04_chapter_animals-04.py", label="Ch 04 · Animals and Habitats", icon="🐾")
    st.page_link("pages/05_chapter_magnets-05.py", label="Ch 05 · Marvelous Magnets", icon="🧲")
    st.page_link("pages/06_chapter_weather-06.py", label="Ch 06 · Water and Weather", icon="☁️")
    st.page_link("pages/07_chapter_simple_machines-07.py", label="Ch 07 · Simple Machines", icon="🛠️")
    st.page_link("pages/08_chapter_saving_our_planet-08.py", label="Ch 08 · Saving Our Planet", icon="🌍")
    st.page_link("pages/09_chapter_energy_electricity-09.py", label="Ch 09 · Energy and Electricity", icon="🔋")
    st.page_link("pages/10_chapter_space-10.py", label="Ch 10 · The Solar System", icon="🌌")
    st.page_link("pages/science_quiz.py",label="Science Game",icon="🎯")
    st.page_link("pages/video_library.py",label="Science Cinema",icon="🎬")
    
    st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

with st.sidebar:st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)

# ─── Session State Defaults ──────────────────────────────────────────────────
for key in [
    "show_rain_fact", "show_snow_fact",
    "show_wind_fact", "show_rainbow_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "weather_picked"  not in st.session_state: st.session_state.weather_picked  = None
if "animal_picked"   not in st.session_state: st.session_state.animal_picked   = None
if "cycle_step"      not in st.session_state: st.session_state.cycle_step      = 0
if "quiz_answers"    not in st.session_state: st.session_state.quiz_answers    = {}

# ─── Helpers ─────────────────────────────────────────────────────────────────
def fun_card(emoji, title, body, bg="#e8f4fd", border="#4a90e2"):
    st.markdown(f"""
    <div style="background:{bg}; border-left:5px solid {border};
                border-radius:16px; padding:1.2rem 1.4rem; margin:0.6rem 0;
                box-shadow:0 3px 10px rgba(0,0,0,0.07);">
        <div style="font-size:2rem; margin-bottom:0.3rem;">{emoji}</div>
        <div style="font-weight:700; font-size:1.1rem; color:#2c3e50;
                    margin-bottom:0.4rem;">{title}</div>
        <div style="font-size:0.97rem; color:#444; line-height:1.7;">{body}</div>
    </div>""", unsafe_allow_html=True)

def section_header(emoji, title, subtitle=""):
    st.markdown(f"""
    <div style="text-align:center; margin: 2rem 0 1rem;">
        <div style="font-size:3.5rem; margin-bottom:0.3rem;">{emoji}</div>
        <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">{title}</h2>
        {"<p style='color:#6b7c93; font-size:1rem; margin-top:0.3rem;'>" + subtitle + "</p>" if subtitle else ""}
    </div>""", unsafe_allow_html=True)

def think_bubble(question):
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f3e5f5);
                border-radius:20px; padding:1rem 1.4rem; margin:0.8rem 0;
                border:2px dashed #7b1fa2; text-align:center;">
        <span style="font-size:1.5rem;">🤔</span>
        <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;
                     font-size:0.97rem;">{question}</span>
    </div>""", unsafe_allow_html=True)

def fact_row(icon, label, fact, bg="#f5f5f5", color="#333"):
    st.markdown(f"""
    <div style="display:flex; align-items:flex-start; gap:0.7rem;
                padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                background:{bg};">
        <span style="font-size:1.4rem; flex-shrink:0;">{icon}</span>
        <div><strong style="color:{color};">{label}:</strong>
        <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#0d2b5e,#1565c0,#00838f,#0d2b5e);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#90caf9; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 06 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        ☁️ Water and Weather! 🌈
    </h1>
    <p style="color:#b3e5fc; font-size:1.05rem; margin:0.8rem 0 0;">
        Why does it rain? Where does snow come from? What makes a rainbow?
        Let's discover all the amazing secrets of weather!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        ☀️ 🌧️ ❄️ 🌬️ 🌈 ⛅ 🌩️ 🌊
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What **weather** is and why it changes every day
        - ✅ How the **water cycle** works — evaporation to rain
        - ✅ Why it **rains** and how clouds are made
        - ✅ How **snow, hail, and frost** form
        """)
    with col2:
        st.markdown("""
        - ✅ What **wind** is and what makes it blow
        - ✅ How **rainbows** are made from sunlight
        - ✅ Different types of **clouds** in the sky
        - ✅ How animals predict weather + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS WEATHER?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌤️", "What Is Weather?",
               "Everything happening in the air outside your window right now!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Look outside right now — is it sunny? Rainy? Cloudy? Windy? Cold?
    Whatever is happening out there is called **WEATHER**! 🌍

    **Weather** is what the air around us is doing each day.
    It can be hot or cold, wet or dry, still or windy — and it changes all the time!
    No two days are exactly the same, and that is what makes weather so fascinating. ☁️

    Weather is made by just **three things** working together:
    the **Sun** (heat energy), **Water** (liquid, ice, and vapour), and **Air** (moving around).
    When these three mix, they create every type of weather on Earth!
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#e1f5fe,#e8f5e9);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #0288d1;">
        <div style="font-weight:700; color:#01579b; font-size:1.05rem; margin-bottom:0.8rem;">
            ☀️💧💨 The Three Ingredients of ALL Weather:
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.7rem; text-align:center;">
                <div style="font-size:1.8rem;">☀️</div>
                <div style="font-weight:700; color:#f57f17;">The Sun</div>
                <div style="font-size:0.82rem; color:#666;">Heats the air and water, giving weather its energy!</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.7rem; text-align:center;">
                <div style="font-size:1.8rem;">💧</div>
                <div style="font-weight:700; color:#0288d1;">Water</div>
                <div style="font-size:0.82rem; color:#666;">Moves from oceans to clouds to rain and back again!</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.7rem; text-align:center;">
                <div style="font-size:1.8rem;">💨</div>
                <div style="font-weight:700; color:#546e7a;">Air</div>
                <div style="font-size:0.82rem; color:#666;">Carries heat and moisture around the whole planet!</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("What is the weather like outside right now? Can you describe it using weather words? ☀️🌧️❄️")

with col2:
    fun_card("🌡️", "Hot and Cold Air",
             "Warm air is lighter and floats <strong>UP</strong>. "
             "Cold air is heavier and sinks <strong>DOWN</strong>. "
             "This up-and-down movement of air is what creates "
             "winds, storms, and weather patterns all over the world! 🔄",
             bg="#fff8e1", border="#f9a825")
    fun_card("📅", "Weather Changes Every Day!",
             "The same place can have completely different weather "
             "day after day — sunny on Monday, rainy on Tuesday, "
             "snowy on Wednesday! This is because the air, water, "
             "and heat from the Sun are always moving and changing. ♻️",
             bg="#e8f5e9", border="#43a047")
    fun_card("🌍", "Weather Happens Everywhere",
             "Every planet with an atmosphere has weather! "
             "On Jupiter, there is a storm bigger than Earth that "
             "has been going for 400 years! On Mars, there are "
             "enormous dust storms that cover the whole planet. 🪐",
             bg="#f3e5f5", border="#8e24aa")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE WATER CYCLE (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔄", "The Amazing Water Cycle!",
               "The same water has been going round and round on Earth for billions of years — step through how it works! 💧")

cycle_steps = [
    ("☀️", "Step 1: Evaporation — Water Becomes Invisible!",
     "The Sun shines on oceans, lakes, rivers, and puddles. Its heat warms the water until tiny "
     "water particles escape into the air as an invisible gas called **WATER VAPOUR**. 💨\n\n"
     "This is called **EVAPORATION** — and it happens every single day, all over the world! "
     "The oceans lose billions of litres of water this way every hour. "
     "You cannot see water vapour — it is completely invisible! "
     "But you can see it when you breathe on a cold day — that little cloud of mist is water vapour cooling down! 🌫️",
     "#fff8e1", "#f9a825"),
    ("🌬️", "Step 2: Rising Up — The Great Lift!",
     "Warm air is lighter than cold air, so it floats upward — and it carries the water vapour with it! 🎈\n\n"
     "The higher you go above Earth, the colder it gets. "
     "As the warm, wet air rises up into the sky, it starts to cool down. "
     "Cool air cannot hold as much water vapour as warm air — "
     "so the water vapour starts to change back into tiny liquid water droplets. "
     "This is called **CONDENSATION** — the opposite of evaporation! 🔄",
     "#e3f2fd", "#1565c0"),
    ("☁️", "Step 3: Cloud Formation — Billions of Tiny Droplets!",
     "Those billions and billions of tiny water droplets group together in the sky — "
     "and that is exactly what a **CLOUD** is! ☁️\n\n"
     "A single cloud can contain hundreds of millions of water droplets — "
     "yet they are so tiny and light that they float! "
     "Each droplet forms around a microscopic speck of dust or pollen — "
     "dust from the ground actually helps clouds form! 🌫️ "
     "The water droplets keep joining together, growing bigger and heavier, "
     "until they are too heavy to stay up in the sky...",
     "#eceff1", "#546e7a"),
    ("🌧️", "Step 4: Precipitation — Falling Back Down!",
     "When the water droplets in a cloud join together and grow heavy enough, "
     "gravity pulls them back down to Earth. This is called **PRECIPITATION**! 🌧️\n\n"
     "Precipitation can fall as many different things depending on how cold the air is:\n\n"
     "- 🌧️ **Rain** — liquid water droplets (air is above 0°C)\n"
     "- ❄️ **Snow** — frozen water crystals (air is below 0°C all the way down)\n"
     "- 🧊 **Sleet** — rain that partly freezes on the way down\n"
     "- 🪨 **Hail** — ice balls bounced up and down by strong winds inside storm clouds!\n"
     "- 🌫️ **Fog** — cloud that forms right at ground level!",
     "#e8f5e9", "#2e7d32"),
    ("🌊", "Step 5: Collection — Back to the Beginning!",
     "The rain, snow, and hail fall onto the land and into the sea. "
     "Water flows downhill in streams and rivers, back into lakes and oceans. ⛰️🏞️\n\n"
     "Some water soaks deep into the ground, where it is stored in underground rivers "
     "called **AQUIFERS** — and slowly flows back to the sea. "
     "Some water is absorbed by trees and plants, which release water vapour through "
     "their leaves — this is called **TRANSPIRATION**! 🌳💧\n\n"
     "And then the Sun shines again — and the whole cycle starts all over again! "
     "The same water on Earth has been cycling around for over **4 BILLION YEARS!** 🌍✨",
     "#e0f2f1", "#00695c"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="cycle_prev"):
        st.session_state.cycle_step = max(0, st.session_state.cycle_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="cycle_next"):
        st.session_state.cycle_step = min(len(cycle_steps)-1, st.session_state.cycle_step + 1)

idx   = st.session_state.cycle_step
cstep = cycle_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{cstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {cstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{cstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {cstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {cstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{cstep[4]}">●</span>'
                for i in range(len(cycle_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Step {idx+1} of {len(cycle_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

think_bubble("When you see a puddle disappear on a sunny day, what is happening to that water? Where is it going? ☀️💧")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — RAIN AND CLOUDS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌧️", "Rain and Clouds — In Detail!",
               "From fluffy white puffs to dark thunderclouds — let's explore! ☁️")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### ☁️ Types of Clouds")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Clouds are not all the same! Scientists have named different cloud types
    based on their **shape** and **how high up** they are. Here are the main ones:
    """)
    cloud_types = [
        ("🌥️", "Cumulus",   "#e3f2fd", "#1565c0",
         "Big, fluffy, white clouds that look like cotton wool or cauliflower! "
         "They float in the middle of the sky on sunny days. If they grow very tall and dark — watch out for a storm! ⛈️"),
        ("🌫️", "Stratus",   "#eceff1", "#546e7a",
         "Flat, grey blanket clouds that cover the whole sky like a sheet. "
         "They often bring light drizzle or grey, misty weather. Fog is stratus cloud at ground level! 🌁"),
        ("🌩️", "Cumulonimbus", "#e8eaf6", "#3949ab",
         "The GIANT storm cloud — a towering monster that can reach 15 km high! "
         "It brings heavy rain, hail, lightning, and thunder. The most powerful cloud of all! ⚡"),
        ("🌤️", "Cirrus",    "#e1f5fe", "#0288d1",
         "Thin, wispy, feathery clouds very high up in the sky. "
         "They are made of ICE CRYSTALS because it is so cold up there. "
         "They often appear before rain is on the way. 🧊"),
        ("⛅", "Altocumulus", "#f3e5f5", "#7b1fa2",
         "Mid-level clouds that look like rows of fluffy puffs or fish scales. "
         "They often appear in the morning before a thunderstorm later in the day. 🐟"),
    ]
    for icon, name, bg, color, desc in cloud_types:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.8rem;
                    padding:0.6rem 0.9rem; border-radius:12px; margin-bottom:0.4rem;
                    background:{bg}; border-left:4px solid {color};">
            <span style="font-size:1.5rem; flex-shrink:0;">{icon}</span>
            <div>
                <strong style="color:{color};">{name}:</strong>
                <span style="font-size:0.93rem; color:#444;"> {desc}</span>
            </div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Look at the sky today — which type of cloud can you see? What does it tell you about tomorrow's weather? ☁️")

with col2:
    st.markdown("##### 🌧️ Amazing Rain Facts")
    for icon, label, fact in [
        ("💧", "Raindrop size",    "A typical raindrop is only 1–5mm wide — about the size of a sesame seed! But it falls at up to 30 km per hour! 💨"),
        ("🌍", "How much rain",    "About 505,000 cubic kilometres of rain falls on Earth every single year — enough to fill every swimming pool on Earth many times over! 🏊"),
        ("🌡️", "Warm rain",        "In tropical countries near the equator, rain can feel WARM — like a warm shower! In cold countries, rain is icy cold and can even freeze on the ground. 🥶"),
        ("🌧️", "Acid rain",        "Pollution from factories and cars can mix with rainwater and make it slightly acidic — called ACID RAIN. It can damage trees, lakes, and buildings. 🏭⚠️"),
        ("🌵", "Driest place",     "The Atacama Desert in Chile went 400 YEARS without a single drop of rain — the driest place on Earth! 🏜️"),
        ("🌧️", "Wettest place",    "Mawsynram in India gets over 11,800mm of rain per year — the wettest inhabited place on Earth! That is over 11 metres of rain! 😱"),
    ]:
        fact_row(icon, label, fact, "#e1f5fe", "#0288d1")

    if st.button("🌧️ Reveal a Rain Secret!", use_container_width=True, key="rain_btn"):
        st.session_state.show_rain_fact = not st.session_state.show_rain_fact
    if st.session_state.show_rain_fact:
        st.success("🎉 Raindrops are NOT shaped like teardrops! "
                   "In cartoons they look pointy at the top — but real raindrops are "
                   "shaped like a tiny hamburger bun — flat on the bottom, round on top! 🍔 "
                   "As they fall, air pressure pushes up on the bottom and flattens them. "
                   "Only very small drops are perfectly round. 💧")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### ❄️ Snow, Hail, and Frost")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    When the temperature is cold enough, water does not fall as rain —
    it falls as something much more exciting! ❄️

    **How does snow form — step by step?**
    """)
    for step, icon, title, desc in [
        (1, "💧", "Water droplets rise",      "Water vapour rises high into cold clouds where temperatures drop below 0°C — the freezing point of water."),
        (2, "🧊", "Ice crystal forms",        "Each tiny water droplet freezes around a dust particle into a microscopic ice crystal with six flat sides — a hexagon! ⬡"),
        (3, "✨", "Crystal grows bigger",     "More water vapour freezes onto the crystal, building beautiful branching arms. Every arm grows differently depending on temperature and humidity."),
        (4, "❄️", "Snowflake is born",        "The finished snowflake has SIX sides and SIX arms — always! This six-fold pattern comes from how water molecules lock together when they freeze."),
        (5, "🌨️", "Snowflakes fall",          "When the snowflake is heavy enough, it drifts gently down. If the air stays cold all the way to the ground — it lands as beautiful snow! ⛄"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e1f5fe;">
            <span style="background:#0277bd; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#0277bd;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("🪨", "Hail — Ice Balls From the Sky!",
             "Hail forms inside huge storm clouds with powerful updrafts — upward blasts of air. "
             "A tiny ice pellet gets blown UP, grows a layer of ice, falls DOWN, gets blown UP again — "
             "and each trip adds another ice layer like an onion! 🧅 "
             "Larger hailstones mean the updraft was stronger. "
             "The biggest hailstone ever recorded was the size of a volleyball! 🏐",
             bg="#e8eaf6", border="#3949ab")

with col2:
    st.markdown("##### ❄️ Snow and Ice Facts")
    for icon, label, fact in [
        ("❄️", "Unique snowflakes", "Every snowflake truly IS unique — scientists have never found two identical ones in over 100 years of looking! Each one grows in slightly different conditions. 🔬"),
        ("🌨️", "Types of snow",     "Not all snow is the same! Powder snow (cold and dry), wet snow (warm and heavy), and blizzard snow (blown by fierce winds) all feel and behave completely differently. 🏔️"),
        ("⚪", "Snow is white",     "Snow looks white because the ice crystals scatter all colours of light equally — white is all colours together! Actual ice in a thick glacier looks blue. 💙"),
        ("🔇", "Snow is quiet",     "Fresh snow absorbs sound — a thick layer of snow makes the world go eerily quiet! The snowflakes trap air between them, which dampens sound waves. 🤫"),
        ("🥶", "Frost",            "Frost forms when water vapour in the air freezes directly onto cold surfaces overnight — skipping the liquid stage entirely! This is called DEPOSITION. 🌿"),
        ("🗻", "Most snow",        "Mount Rainier in Washington USA receives an average of 17.4 metres of snow per year — enough to bury a five-storey building! 🏔️"),
    ]:
        fact_row(icon, label, fact, "#e1f5fe", "#0277bd")

    if st.button("❄️ Tap for a Snow Secret!", use_container_width=True, key="snow_btn"):
        st.session_state.show_snow_fact = not st.session_state.show_snow_fact
    if st.session_state.show_snow_fact:
        st.success("🎉 It is possible for it to snow when the temperature is ABOVE freezing! "
                   "If the air is very dry, snowflakes can evaporate as they fall and cool the air "
                   "around them enough to reach the ground still frozen — even when it is 2°C or 3°C! "
                   "This is called VIRGA when the precipitation evaporates before landing. ☁️✨")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — WIND
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌬️", "What Is Wind?",
               "Moving air that shapes our weather and powers our world! 💨")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Wind is simply **moving air** — and air moves because of differences in **temperature**! 🌡️

    You cannot see wind, but you can feel it on your skin, hear it in the trees,
    and watch it push clouds across the sky. 🍃

    **How does wind form — step by step?**
    """)
    for step, icon, title, desc in [
        (1, "☀️", "Sun heats the ground",       "The Sun heats some parts of Earth more than others — land heats up faster than sea, and dark surfaces heat faster than light ones."),
        (2, "⬆️", "Warm air rises",              "Warm air above hot ground becomes lighter and rises upward — like a hot air balloon! This creates an area of LOW PRESSURE at the ground."),
        (3, "❄️", "Cool air moves in",           "Cool air from nearby areas (which is heavier) rushes in to fill the low pressure gap left by the rising warm air — and this rushing air IS the wind! 💨"),
        (4, "🔄", "Air keeps circulating",       "The warm air rises, cools at height, spreads sideways, sinks somewhere else, and then gets warmed again — creating a constant circulation loop."),
        (5, "🌍", "Global wind patterns",        "On a global scale, these circulations create permanent wind patterns — like the TRADE WINDS that blow toward the equator, and the WESTERLIES that push weather systems across continents. 🗺️"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e0f7fa;">
            <span style="background:#00838f; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#00838f;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Stand near a window or go outside — can you feel any wind? Which direction is it coming from? 🌬️")

with col2:
    st.markdown("##### 🌬️ Wonderful Wind Facts")
    for icon, label, fact in [
        ("📏", "Measuring wind",   "Scientists measure wind speed using an ANEMOMETER — a spinning wheel with cups that catches the wind. The faster it spins, the faster the wind! 🌀"),
        ("🌪️", "Tornado",         "The fastest winds on Earth are inside tornadoes — spinning funnels of air that can reach 480 km/h! Strong enough to lift houses and cars. 🏠"),
        ("🌀", "Hurricane",       "A HURRICANE is a massive spinning storm hundreds of kilometres wide, powered by warm ocean water. It can last for weeks and devastate entire cities. 🌊"),
        ("💨", "Jet stream",      "High in the atmosphere, there is a river of fast-moving air called the JET STREAM that travels at up to 400 km/h — it steers weather systems around the world! ✈️"),
        ("🏭", "Wind energy",     "Wind turbines convert wind energy into electricity — completely clean and renewable! Wind power supplies electricity to millions of homes worldwide. ⚡"),
        ("🌵", "Saharan dust",    "The Sahara Desert wind (HARMATTAN) blows dust all the way across the Atlantic Ocean to South America — fertilising the Amazon rainforest! 🌱🤯"),
    ]:
        fact_row(icon, label, fact, "#e0f7fa", "#00838f")

    if st.button("🌬️ Reveal a Wind Secret!", use_container_width=True, key="wind_btn"):
        st.session_state.show_wind_fact = not st.session_state.show_wind_fact
    if st.session_state.show_wind_fact:
        st.success("🎉 The wind on other planets is even more extreme! "
                   "On Neptune, the farthest planet, winds reach 2,100 km/h — "
                   "almost supersonic speed! A hurricane on Neptune would make "
                   "Earth's strongest tornadoes look like a gentle breeze. 🪐💨 "
                   "And on Venus, thick clouds race around the whole planet in just 4 days! ☁️")

    fun_card("🍃", "The Beaufort Scale",
             "In 1805, Admiral Francis Beaufort invented a scale from 0 to 12 "
             "to describe wind strength! "
             "0 = dead calm (smoke goes straight up). "
             "6 = strong breeze (umbrellas hard to hold). "
             "12 = hurricane force (catastrophic damage)! "
             "Sailors still use this scale today. ⛵📊",
             bg="#e0f7fa", border="#00838f")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — RAINBOWS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌈", "Rainbows — Magic Made by Light!",
               "One of the most beautiful things in nature — and it's all pure science! ✨")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    A **rainbow** is one of the most magical things you can see in the sky —
    and it is made entirely by sunlight and water droplets working together! 🌧️☀️

    **How is a rainbow made — step by step?**
    """)
    for step, icon, title, desc in [
        (1, "☀️", "White sunlight enters a raindrop",  "Sunlight looks white, but it is actually made of ALL the colours mixed together! When sunlight enters a raindrop, something incredible happens."),
        (2, "🔀", "Light bends — refraction!",         "As light enters the raindrop, it SLOWS DOWN and BENDS — this is called REFRACTION. Different colours of light bend at slightly different angles."),
        (3, "🪞", "Light bounces off the back",        "The light bounces off the inside back of the raindrop like a mirror — this is called REFLECTION."),
        (4, "🔀", "Light bends again leaving",         "As the light exits the raindrop, it bends AGAIN — and this second bending separates the colours even further apart."),
        (5, "🌈", "Colours fan out!",                  "Each colour exits at a slightly different angle — red at 42°, violet at 40°. With millions of raindrops doing this at once, you see a full arc of colours! 🎨"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fff9c4;">
            <span style="background:#f9a825; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#f57f17;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### 🌈 The Seven Colours — In Order, Always!")
    rainbow_colours = [
        ("🔴", "Red",    "#ffebee", "#c62828", "Always on the OUTSIDE top of the rainbow — the biggest arc!"),
        ("🟠", "Orange", "#fff3e0", "#e65100", "Just inside the red — a warm, glowing band."),
        ("🟡", "Yellow", "#fffde7", "#f9a825", "Bright and cheerful in the middle section."),
        ("🟢", "Green",  "#e8f5e9", "#2e7d32", "The lush green band right in the centre."),
        ("🔵", "Blue",   "#e3f2fd", "#1565c0", "Cool blue — starting to move toward the inside."),
        ("🟣", "Indigo", "#ede7f6", "#4527a0", "A deep blue-violet, hard to spot but it is there!"),
        ("🔵", "Violet", "#f3e5f5", "#7b1fa2", "Always on the INSIDE of the rainbow — the smallest arc!"),
    ]
    for icon, colour, bg, color, desc in rainbow_colours:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:8px; padding:0.4rem 0.8rem;
                    margin-bottom:0.25rem; border-left:4px solid {color};
                    display:flex; align-items:center; gap:0.5rem;">
            <span style="font-size:1.1rem;">{icon}</span>
            <strong style="color:{color}; min-width:55px;">{colour}</strong>
            <span style="font-size:0.87rem; color:#555;">{desc}</span>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### 🌈 Rainbow Wonders")
    for icon, label, fact in [
        ("⭕", "Full circle",    "A rainbow is actually a FULL CIRCLE — but from the ground we only see the top half! From an aeroplane, you can sometimes see the complete circle! ✈️🌈"),
        ("👥", "No two same",    "No two people ever see the exact same rainbow! Each person sees light bouncing from different raindrops at a slightly different angle. Your rainbow is uniquely yours! 🤩"),
        ("🌙", "Moonbow",        "On very bright full-moon nights, moonlight can create a rainbow too — called a MOONBOW! They are much rarer and look almost white because moonlight is dimmer. 🌕"),
        ("🌡️", "Fire rainbow",   "On hot days, sunlight through ice crystals in high clouds can make a FIRE RAINBOW — a colourful arc that looks like a rainbow on fire! 🔥 It is one of the rarest optical phenomena. 🤯"),
        ("🔴", "Red rainbow",    "At sunrise and sunset, the light travels through much more atmosphere and only red wavelengths survive — creating a stunning RED RAINBOW! 🌅"),
        ("🌈", "Double rainbow", "Sometimes you can see TWO rainbows! The outer one has its colours in REVERSE order — red on the inside, violet on the outside — because the light bounces twice inside the drops! 🔄"),
    ]:
        fact_row(icon, label, fact, "#fffde7", "#f57f17")

    if st.button("🌈 Reveal a Rainbow Secret!", use_container_width=True, key="rainbow_btn"):
        st.session_state.show_rainbow_fact = not st.session_state.show_rainbow_fact
    if st.session_state.show_rainbow_fact:
        st.success("🎉 You can NEVER reach the end of a rainbow! "
                   "A rainbow is not a physical object — it is an optical effect that moves "
                   "as YOU move! No matter how far or fast you walk toward it, "
                   "the rainbow always appears the same distance away. "
                   "It is like chasing your own shadow — forever just out of reach! 🏃🌈")

    think_bubble("Make your own rainbow! Stand with your back to the Sun and spray water from a hose — can you see a rainbow in the mist? 🌊☀️")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — TYPES OF WEATHER (Topic selector)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("⛅", "Explore All Types of Weather!",
               "Tap each weather type to discover everything about it! 🌍")

weather_types = {
    "☀️ Sunny": {
        "emoji": "☀️", "color": "#f57f17", "bg": "#fffde7",
        "tagline": "☀️ The most energetic weather of all!",
        "body": (
            "Sunny weather happens when the sky is clear and no clouds block the Sun's rays! ☀️\n\n"
            "- 🌡️ **Why it is warm**: The Sun sends energy as light and heat across 150 million km of space to reach us — in just 8 minutes! That heat warms the ground, the air, and everything on Earth.\n"
            "- 🕶️ **UV rays**: Sunlight contains invisible ultraviolet (UV) rays that give you a suntan — but too much can burn your skin! Always wear sunscreen. 🧴\n"
            "- 🌱 **Plants love it**: Plants use sunlight to make their own food through PHOTOSYNTHESIS — every bite of food you eat started as sunlight energy! 🌿\n"
            "- ☀️ **Solar energy**: Solar panels on rooftops capture sunlight and convert it directly into electricity — clean energy from our nearest star! ⚡\n"
            "- 🌡️ **Record heat**: The hottest temperature ever recorded on Earth was 56.7°C in Death Valley, USA — hot enough to fry an egg on the pavement! 🍳"
        )
    },
    "🌧️ Rainy": {
        "emoji": "🌧️", "color": "#0288d1", "bg": "#e1f5fe",
        "tagline": "🌧️ The life-giving weather!",
        "body": (
            "Rain is one of the most essential types of weather — without it, no life could exist on land! 🌱\n\n"
            "- 💧 **Fresh water supply**: Almost all fresh water on Earth comes from rain — filling rivers, lakes, and underground aquifers that supply our drinking water and farms. 🏡\n"
            "- 🌡️ **Types of rain**: Light drizzle (tiny droplets), moderate rain, heavy rain, and MONSOON rain (months of continuous heavy downpours in tropical countries). 🌏\n"
            "- 🌈 **After the rain**: Rain washes dust from the air, making everything look brighter — and sets up perfect conditions for rainbows! 🌈\n"
            "- 🌧️ **Petrichor**: That gorgeous earthy smell after rain has a name — PETRICHOR! It comes from bacteria in the soil releasing a chemical when raindrops hit. 🌿\n"
            "- 🌊 **Flooding**: Too much rain too quickly can cause dangerous floods — water cannot soak in fast enough and fills streets and buildings. ⚠️"
        )
    },
    "❄️ Snowy": {
        "emoji": "❄️", "color": "#0277bd", "bg": "#e1f5fe",
        "tagline": "❄️ The frozen wonder!",
        "body": (
            "Snow transforms the world into a beautiful white landscape — and it is all pure science! ❄️\n\n"
            "- 🧊 **Pure water**: Snow is made of incredibly pure water — far purer than rainwater, which picks up dust and pollution on the way down. 💎\n"
            "- ⛄ **Insulator**: A thick blanket of snow actually INSULATES the ground beneath it — keeping soil and plant roots warm! Animals like bears sleep under snow for warmth. 🐻\n"
            "- 🔊 **Sound absorber**: Snow absorbs sound waves — a world covered in fresh snow is eerily, beautifully quiet. 🤫\n"
            "- 💧 **Spring water**: Mountain snowfall melts in spring, filling rivers — providing fresh water for cities and farms throughout the summer. Many cities depend entirely on mountain snow! 🏔️\n"
            "- 🏂 **Record snow**: In 1972, Mount Rainier in Washington USA recorded 31.1 metres of snow in a single season — almost as tall as a 10-storey building! 😱"
        )
    },
    "🌩️ Stormy": {
        "emoji": "🌩️", "color": "#4527a0", "bg": "#ede7f6",
        "tagline": "🌩️ Nature's most powerful weather!",
        "body": (
            "Storms are the most dramatic and powerful type of weather — formed when huge amounts of energy build up in the atmosphere! ⚡\n\n"
            "- ⚡ **Lightning**: A lightning bolt is 5 times hotter than the surface of the Sun — reaching 30,000°C in an instant! It is caused by static electricity building up between clouds. 🌡️\n"
            "- 🥁 **Thunder**: The huge heat of lightning instantly expands the air around it — creating a massive shockwave we hear as THUNDER! Light travels faster than sound, which is why we see lightning first. 👁️👂\n"
            "- 🌩️ **Count the distance**: Count the seconds between lightning and thunder, then divide by 3 — that gives the distance in kilometres! (Divide by 5 for miles.) 🧮\n"
            "- 🌪️ **Tornado formation**: The most powerful storms can create tornadoes — spinning columns of air with winds up to 480 km/h that touch down on the ground! 🌀\n"
            "- ⚡ **Lightning strikes**: Earth is struck by lightning about 100 times every SECOND — that is 8.6 million lightning bolts per day! 🤯"
        )
    },
    "🌫️ Foggy": {
        "emoji": "🌫️", "color": "#546e7a", "bg": "#eceff1",
        "tagline": "🌫️ Cloud on the ground!",
        "body": (
            "Fog is simply a cloud that forms at ground level — exactly the same thing, just in a different place! 🌁\n\n"
            "- 🌡️ **How fog forms**: On clear, calm nights the ground cools rapidly, cooling the air just above it. If the air cools enough, water vapour condenses into tiny droplets — forming fog by morning! 🌅\n"
            "- 🌊 **Sea fog**: When warm, moist air blows over cold ocean water, it rapidly cools and forms thick sea fog — very dangerous for ships! ⛵\n"
            "- 🏙️ **Famous fogs**: London was once famous for its thick, yellowish SMOG — fog mixed with coal smoke pollution. The Great Smog of 1952 was so thick people could not see their own hands! 😷\n"
            "- 👁️ **Visibility**: Thick fog can reduce visibility to just a few metres — airports close, motorways slow down, and ships drop anchor when fog is very dense. ✈️\n"
            "- 🌵 **Fog collecting**: In the Atacama Desert, people collect fresh water from fog using special nets — the tiny fog droplets collect on the net and drip down into containers! 💧🤯"
        )
    },
    "🌈 Rainbow": {
        "emoji": "🌈", "color": "#7b1fa2", "bg": "#f3e5f5",
        "tagline": "🌈 The most beautiful weather gift!",
        "body": (
            "Rainbows appear when sunlight and rain happen at the same time — a perfect combination of two weathers! 🌧️☀️\n\n"
            "- 🎨 **Seven colours**: Red, Orange, Yellow, Green, Blue, Indigo, Violet — always in the same order, always! A handy way to remember: Richard Of York Gave Battle In Vain (ROY G BIV)! 🎭\n"
            "- 👁️ **How to find one**: Stand with your BACK to the Sun and look toward rain — the rainbow will always be opposite the Sun at about 40-42 degrees above the horizon. 🧭\n"
            "- ⭕ **Full circle**: A rainbow is actually a full circle — but we only see the top arc because the ground is in the way. From a plane, you can sometimes see the full ring! ✈️\n"
            "- 🌈 **Double rainbow**: The second, fainter rainbow outside the first has colours in REVERSE order — caused by double reflection inside the raindrops! 🔄\n"
            "- 🌕 **Moonbow**: On a bright full-moon night, the Moon can create a rainbow too — called a MOONBOW! Much rarer and usually looks white or very pale. 🌕"
        )
    },
}

w_cols = st.columns(len(weather_types))
for i, (wname, wdata) in enumerate(weather_types.items()):
    with w_cols[i]:
        short = wname.split(" ", 1)[1]
        if st.button(wdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"wtype_{i}"):
            st.session_state.weather_picked = wname

if st.session_state.weather_picked and st.session_state.weather_picked in weather_types:
    wname = st.session_state.weather_picked
    wdata = weather_types[wname]
    st.markdown(f"""
    <div style="background:{wdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {wdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{wdata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {wname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{wdata['color']}; font-weight:700;">
                    {wdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(wdata["body"])
else:
    st.info("👆 Tap any weather type above to discover everything about it!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — ANIMALS AND WEATHER
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🐾", "Animals and Weather — Nature's Forecasters!",
               "Animals often know when weather is changing before we do! Tap to discover! 🌍")

animal_weather = {
    "🐄 Cows": {
        "emoji": "🐄", "color": "#795548", "bg": "#efebe9",
        "tagline": "🌧️ The original weather forecasters!",
        "body": (
            "People have watched cows to predict weather for centuries! 🐄\n\n"
            "- 🛋️ **Lying down**: The old saying 'cows lie down before rain' may have some truth! Before rain, air pressure drops and humidity rises — cows may lie down to keep a dry patch under them.\n"
            "- 🌡️ **Bunching together**: When cows gather closely together, it may indicate cold weather is coming — body heat shared between animals! 🔥\n"
            "- 🌬️ **Facing the wind**: Some farmers believe cows turn their backs to oncoming storms — giving them natural weather-sensing abilities.\n"
            "- 🧠 **Actually accurate?**: Modern scientists have found mixed evidence — cows ARE sensitive to air pressure and humidity changes, but it is not a reliable forecast! 😄\n"
            "- 🏡 **Heading home**: Cows returning early to the barn before dark is a more reliable sign — they feel atmospheric changes hours before storms arrive. ⛈️"
        )
    },
    "🐸 Frogs": {
        "emoji": "🐸", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🌧️ Nature's humidity detectors!",
        "body": (
            "Frogs are extraordinarily sensitive to changes in weather — their whole body feels it! 🐸\n\n"
            "- 🌧️ **Singing before rain**: Frogs become much louder and more active before rain — they sense the rising humidity and falling air pressure. Rain means puddles for breeding! 🎶\n"
            "- 🩺 **Skin sensors**: Frogs breathe partly through their thin, moist skin — which makes them incredibly sensitive to humidity, temperature, and air pressure changes. They are living barometers! 📊\n"
            "- 🌡️ **Temperature tells**: Frogs are cold-blooded — they become sluggish in cold and lively in warmth. Watching their activity level tells you a lot about the temperature! 🌡️\n"
            "- 🧪 **Scientific use**: Scientists actually monitor frog populations to study climate change — frogs are so sensitive that they are among the first animals to be affected by climate shifts. ⚠️\n"
            "- 🌧️ **Rain frogs**: Some desert frogs can survive underground for YEARS waiting for rain — then emerge, breed rapidly in temporary pools, and disappear again before it dries up! 🏜️"
        )
    },
    "🐦 Birds": {
        "emoji": "🐦", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "💨 Built-in weather instruments!",
        "body": (
            "Birds are remarkably sophisticated weather observers — using multiple senses we do not have! 🐦\n\n"
            "- 👂 **Infrasound hearing**: Birds can hear INFRASOUND — sound waves far too low for humans to detect. Storms generate infrasound hundreds of kilometres away. Birds hear storms coming long before they arrive! 🌩️\n"
            "- 📊 **Ear pressure detectors**: Birds have baroreceptors in their ears that detect tiny changes in air pressure — dropping pressure means a storm is approaching, so they fly lower or take shelter. 🌬️\n"
            "- 🐦 **Flying low**: Birds fly lower before storms because the lower air pressure at altitude makes it harder to fly. Also, insects (their food) also fly lower before storms. 🦟\n"
            "- 🧹 **Preening**: Birds preen their feathers more intensely before rain — waterproofing their feathers with oil from their preen gland in preparation for wet weather. 🌧️\n"
            "- 🌅 **Migration timing**: Long-distance migrating birds read weather patterns across entire continents — timing their journeys to ride on favourable winds for thousands of kilometres! 🌍"
        )
    },
    "🐝 Bees": {
        "emoji": "🐝", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "⛈️ The hive knows first!",
        "body": (
            "Honeybee colonies respond to weather changes with impressive precision — the whole hive acts as one weather station! 🍯\n\n"
            "- 🏠 **Staying in**: On days before storms, foraging bees return to the hive early and fewer leave — the colony senses the approaching bad weather hours in advance! 🌩️\n"
            "- 📊 **Pressure sensors**: Bees detect tiny changes in air pressure through sensory hairs on their bodies — dropping pressure signals a storm is building. 🌬️\n"
            "- 🌡️ **Fanning in heat**: In hot weather, special worker bees stand at the hive entrance and fan their wings to cool the hive — like a living air conditioning system! ❄️\n"
            "- 🌸 **Sunshine and flowers**: Bees need dry, calm, sunny weather to collect nectar efficiently — they are most active between 10am and 2pm on sunny days. ☀️\n"
            "- 🌡️ **Winter cluster**: When it turns cold, all the bees in the hive form a tight ball — constantly vibrating their flight muscles to generate heat and keep the queen warm all winter! 🐝💕"
        )
    },
    "🦔 Hedgehogs": {
        "emoji": "🦔", "color": "#6d4c41", "bg": "#efebe9",
        "tagline": "❄️ The hibernation weather expert!",
        "body": (
            "Hedgehogs have one of the most dramatic responses to seasonal weather of any animal! 🦔\n\n"
            "- 😴 **Hibernation**: When autumn temperatures consistently drop below 10°C, hedgehogs enter HIBERNATION — slowing their heartbeat from 190 to just 20 beats per minute! 💓\n"
            "- 🌡️ **Weather trigger**: Hedgehogs do not simply follow a calendar — they respond directly to air temperature. A warm spell in December can wake them up; a cold snap in October puts them to sleep. 🌡️\n"
            "- 🍂 **Nest building**: Weeks before hibernation, hedgehogs gather enormous amounts of dry leaves to build an insulating nest — they know cold weather is coming! 🌿\n"
            "- 🌡️ **Body temperature**: During hibernation, a hedgehog's body temperature drops to match the surrounding air — sometimes as low as 1°C! They are essentially frozen little spiky balls. 🥶\n"
            "- ☀️ **Spring waking**: Rising temperatures in spring trigger hedgehogs to wake — they emerge hungry after 5-6 months of no eating! One of nature's most reliable seasonal clocks. ⏰"
        )
    },
    "🦈 Sharks": {
        "emoji": "🦈", "color": "#0277bd", "bg": "#e1f5fe",
        "tagline": "🌊 The ocean's storm predictor!",
        "body": (
            "Sharks can sense approaching hurricanes and storms far better than any human instrument! 🦈\n\n"
            "- 📊 **Barometric pressure**: Sharks have sensory systems that detect subtle changes in water pressure — they can feel a drop in barometric pressure before a hurricane, even when the sea looks perfectly calm! ⚡\n"
            "- 🏊 **Diving deep**: Before major hurricanes, sharks and other large marine animals have been tracked diving to much deeper water — getting below the storm-driven surface turbulence. 🌊\n"
            "- 🌡️ **Temperature detection**: Sharks use the AMPULLAE OF LORENZINI to detect temperature differences — they track warm and cold currents to find prey, and notice when storms mix up ocean layers. 🔌\n"
            "- 🔬 **Scientific tracking**: Scientists tracking sharks with GPS found they dove to 400+ metres hours before Hurricane Gabrielle in 2001 — before any official storm warnings were issued! 🤯\n"
            "- 🌊 **After storms**: Storms actually bring nutrients up from the deep ocean floor — so after a storm passes, sharks often find excellent hunting in the churned-up waters! 🐟"
        )
    },
}

a_cols = st.columns(len(animal_weather))
for i, (aname, adata) in enumerate(animal_weather.items()):
    with a_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"anim_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in animal_weather:
    aname = st.session_state.animal_picked
    adata = animal_weather[aname]
    st.markdown(f"""
    <div style="background:{adata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {adata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{adata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {aname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{adata['color']}; font-weight:700;">
                    {adata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(adata["body"])
else:
    st.info("👆 Tap any animal above to discover how it senses and responds to weather!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — STAYING SAFE IN DIFFERENT WEATHER
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Staying Safe in All Weathers!",
               "Different weather needs different care — here is how to stay safe! 🌟")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("☀️", "Sunny and Hot Weather",
     "Drink lots of water — your body loses water quickly in heat! "
     "Wear sunscreen to protect your skin from UV rays. "
     "Wear a hat and light-coloured clothes. "
     "Take breaks in the shade. Never sit in a parked car — temperatures inside can become deadly! 🌡️🧴",
     "#fffde7", "#f9a825"),
    ("🌧️", "Rainy Weather",
     "Wear a waterproof coat and wellingtons to keep dry and warm. "
     "Be careful on wet roads and paths — they are very slippery! "
     "Never shelter under a tall tree in a thunderstorm — lightning strikes the tallest objects. "
     "Indoors is the safest place during heavy rain and storms. ⚡🌧️",
     "#e1f5fe", "#0288d1"),
    ("❄️", "Cold and Snowy Weather",
     "Wear lots of layers — trapped air between layers keeps you warm. "
     "Keep extremities (fingers, toes, nose, ears) covered — frostbite can happen in minutes! "
     "Eat warm food and hot drinks to maintain body temperature. "
     "Watch for ice on roads and footpaths — it is nearly invisible and extremely slippery! 🧤🧣",
     "#e3f2fd", "#0277bd"),
    ("🌩️", "Storms and Thunder",
     "Stay indoors during a thunderstorm — it is the safest place! "
     "Stay away from windows, tall trees, and metal objects. "
     "If caught outside, crouch low with feet together and do not lie flat. "
     "Count seconds between lightning and thunder — 3 seconds = 1 km away. "
     "Wait 30 minutes after the last thunder before going back outside. ⚡🏠",
     "#ede7f6", "#4527a0"),
    ("🌬️", "Very Windy Weather",
     "Hold on to things in very strong wind — it can knock you off your feet! "
     "Watch for falling branches and debris blown by wind. "
     "Stay away from cliffs, riversides, and open hilltops in gale force winds. "
     "Tie down or bring inside garden furniture and trampolines before a storm. 🌳💨",
     "#e0f7fa", "#00838f"),
    ("🌫️", "Foggy Weather",
     "Wear bright or reflective clothing so drivers can see you. "
     "Slow down and be extra careful on roads — fog makes it hard to see other people and vehicles. "
     "Never run in fog near roads. "
     "Use a torch if walking in thick fog at night. "
     "Ships use foghorns and radar to navigate safely through sea fog! 🔦🌫️",
     "#eceff1", "#546e7a"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("What weather do you love the most and what weather do you find hardest? Why? ☀️❄️🌧️")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Weather Quiz — Test What You Know!",
               "6 wonderful weather questions — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 💧 — What is it called when water turns into invisible gas and rises into the sky?",
        "opts": ["Condensation", "Precipitation", "Evaporation", "Transpiration"],
        "ans":  "Evaporation",
        "explain": "EVAPORATION happens when the Sun heats water and it turns into invisible water vapour that floats up into the sky — the first step of the water cycle! ☀️💧"
    },
    {
        "q":    "Q2 ❄️ — Why does every snowflake have a different shape?",
        "opts": ["Because of gravity", "Because of wind", "Because each one grows in slightly different conditions", "Because snow is coloured"],
        "ans":  "Because each one grows in slightly different conditions",
        "explain": "Every snowflake grows in unique temperature and humidity conditions as it falls — so no two snowflakes in history have ever been exactly the same! ❄️🔬"
    },
    {
        "q":    "Q3 🌬️ — What causes wind to blow?",
        "opts": ["The Moon pulling air", "Differences in air temperature making air move", "Clouds spinning", "The sea moving"],
        "ans":  "Differences in air temperature making air move",
        "explain": "Wind is caused by warm air rising and cool air rushing in to fill its place — it is all about temperature differences between places! ☀️❄️💨"
    },
    {
        "q":    "Q4 🌈 — What two things are needed to make a rainbow?",
        "opts": ["Moon and clouds", "Ice and wind", "Sunlight and raindrops", "Blue sky and snow"],
        "ans":  "Sunlight and raindrops",
        "explain": "Sunlight enters raindrops and bends — splitting into all its colours! You need both sun AND rain at the same time, which is why rainbows often appear just after a shower! 🌧️☀️🌈"
    },
    {
        "q":    "Q5 ⛅ — What is a cumulonimbus cloud?",
        "opts": ["A flat grey cloud that brings drizzle", "A giant towering storm cloud with lightning and hail", "A thin wispy cloud made of ice", "A small fluffy fair-weather cloud"],
        "ans":  "A giant towering storm cloud with lightning and hail",
        "explain": "CUMULONIMBUS is the giant storm cloud — it can tower 15 km high and brings heavy rain, hail, lightning, and thunder! The most powerful and dramatic cloud in the sky! ⛈️🌩️"
    },
    {
        "q":    "Q6 🐸 — How do frogs help predict the weather?",
        "opts": ["They read the newspaper", "They feel changes in humidity and air pressure through their skin", "They look at the clouds", "They check the temperature with their tongue"],
        "ans":  "They feel changes in humidity and air pressure through their skin",
        "explain": "Frogs breathe partly through their moist skin — making them living barometers that are incredibly sensitive to humidity and pressure changes before rain! They start croaking loudly before storms. 🐸🌧️"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"wx_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="wx_quiz_submit"):
        st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    score = 0
    for i, q in enumerate(questions):
        ans = st.session_state.quiz_answers.get(i)
        if ans == q["ans"]:
            score += 1
            st.success(f"✅ **{q['q'].split('—')[1].strip()}** → Correct! 🎉 {q['explain']}")
        elif ans is None:
            st.warning(f"⚠️ **{q['q'].split('—')[1].strip()}** → You did not answer this one!")
        else:
            st.error(f"❌ **{q['q'].split('—')[1].strip()}** → Not quite! "
                     f"The answer is **{q['ans']}**. {q['explain']}")

    badge_data = [
        (6, "🏆", "WEATHER WIZARD! ☀️🌧️❄️",           "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Cloud Scientist! ⛅",      "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Weather Explorer! 🌈",         "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Weather Detective! 🌬️",   "#7b1fa2", "#f3e5f5"),
        (0, "✨", "Keep Exploring — You Can Do It! 💪", "#1565c0", "#e3f2fd"),
    ]
    for threshold, icon, label, border, bg in badge_data:
        if score >= threshold:
            st.markdown(f"""
            <div style="background:{bg}; border:3px solid {border};
                        border-radius:20px; padding:1.5rem; text-align:center; margin-top:1rem;">
                <div style="font-size:4rem;">{icon}</div>
                <div style="font-size:1.5rem; font-weight:700; color:#2c3e50;">
                    You scored {score}/6!
                </div>
                <div style="font-size:1.1rem; color:{border}; font-weight:600;">{label}</div>
            </div>""", unsafe_allow_html=True)
            break

    if st.button("🔄 Try Again!", use_container_width=False, key="wx_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 10 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?",
               "Water and Weather — your quick recap! 🎉")

summary_items = [
    ("☀️💧💨", "Weather",      "Made by the Sun, water, and air working together!"),
    ("🔄",     "Water Cycle",  "Evaporation → Clouds → Rain → Repeat — forever!"),
    ("🌧️",     "Rain",         "Water droplets in clouds grow heavy and fall back down!"),
    ("❄️",     "Snow",         "Frozen water crystals — every one uniquely shaped!"),
    ("🌬️",     "Wind",         "Moving air caused by temperature differences!"),
    ("🌈",     "Rainbow",      "Sunlight split into 7 colours by raindrops!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #0288d1;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#0d2b5e,#1565c0,#00838f,#0d2b5e);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Amazing work, little scientist! You are a Weather Wizard! ✨
    </div>
    <div style="color:#b3e5fc; font-size:0.95rem;">
        Every raindrop, snowflake, gust of wind, and rainbow is your amazing planet telling its story!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        ☀️ 🌧️ ❄️ 🌬️ 🌈 ⛅ 🌩️ 🌊
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# Footer
st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)