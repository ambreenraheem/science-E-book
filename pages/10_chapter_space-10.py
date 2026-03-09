import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 10 · Our Home in Space", layout="wide", initial_sidebar_state="expanded")

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
if "show_sun_fact"    not in st.session_state: st.session_state.show_sun_fact    = False
if "show_moon_fact"   not in st.session_state: st.session_state.show_moon_fact   = False
if "show_earth_fact"  not in st.session_state: st.session_state.show_earth_fact  = False
if "planet_picked"    not in st.session_state: st.session_state.planet_picked    = None
if "moon_phase_idx"   not in st.session_state: st.session_state.moon_phase_idx   = 0
if "quiz_answers"     not in st.session_state: st.session_state.quiz_answers     = {}
if "quiz_submitted"   not in st.session_state: st.session_state.quiz_submitted   = False

# ─── Helpers ─────────────────────────────────────────────────────────────────
def fun_card(emoji, title, body, bg="#fff8e1", border="#f9a825"):
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
    <div style="background:linear-gradient(135deg,#e3f0ff,#f0e6ff);
                border-radius:20px; padding:1rem 1.4rem; margin:0.8rem 0;
                border:2px dashed #4a90e2; text-align:center;">
        <span style="font-size:1.5rem;">🤔</span>
        <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;
                     font-size:0.97rem;">{question}</span>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#1a1a4e,#2d4a8c,#1a1a4e);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; position:relative; overflow:hidden;">
    <div style="font-size:1rem; color:#a0c4ff; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 10 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.3);">
        🚀 Our Home in Space 🌍
    </h1>
    <p style="color:#c8daff; font-size:1.05rem; margin:0.8rem 0 0;">
        A big adventure through the stars — just for YOU!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        🌟 ☀️ 🌙 🪐 🌎 🌟
    </div>
</div>
""", unsafe_allow_html=True)

# Learning goals
with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What is **outer space**
        - ✅ About the **Sun** — our giant star
        - ✅ About the **Earth** — our home
        - ✅ About the **Moon** and its shapes
        """)
    with col2:
        st.markdown("""
        - ✅ The **8 planets** of our Solar System
        - ✅ What makes each planet **special**
        - ✅ Fun **activities** along the way
        - ✅ A mini **quiz** at the end!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS OUTER SPACE?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌌", "What Is Outer Space?",
               "Everything beyond the sky above us!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Look up at the sky on a clear night. Do you see all those tiny lights? 
    Those are **stars** — and they are **very, very far away!** 🌟

    Everything beyond our sky — all the stars, moons, planets, and the huge 
    empty space between them — is called **Outer Space**.

    Outer space is incredibly big. It goes on and on **forever** in every direction!
    Scientists call this never-ending space the **Universe**.
    """)

    think_bubble("If you could travel in a rocket, what would you want to visit first?")

with col2:
    fun_card("🌌", "Space is HUGE!",
             "Our whole Earth looks like a tiny dot compared to the Sun. "
             "And the Sun looks like a tiny dot compared to outer space!",
             bg="#f0e6ff", border="#7c4dff")
    fun_card("🔇", "Space is Silent",
             "There is NO air in space, so sound cannot travel. "
             "It would be completely quiet — even if something exploded nearby!",
             bg="#e8f4fd", border="#4a90e2")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE SUN ☀️
# ═══════════════════════════════════════════════════════════════════════════════
section_header("☀️", "The Sun — Our Giant Star",
               "The brightest thing in our sky!")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    The **Sun** is a giant ball of hot, glowing gas. It sits in the middle of 
    our Solar System, and everything — including Earth — travels around it.

    The Sun gives us two very important things every single day:
    """)
    fun_card("🌡️", "Heat",
             "The Sun warms our land, our oceans, and the air we breathe. "
             "Without it, Earth would be frozen solid — colder than your freezer!",
             bg="#fff3e0", border="#ff8f00")
    fun_card("💡", "Light",
             "The Sun lights up our whole day! Plants use sunlight to make food, "
             "and we need daylight to see the world around us.",
             bg="#fffde7", border="#ffd600")

with col2:
    st.markdown("""
    ##### ⚡ Amazing Sun Facts
    """)
    sun_facts = [
        ("🔥", "Temperature", "The surface is about **5,500°C** — millions of times hotter than your oven!"),
        ("📏", "Size", "The Sun is so big that **1 million Earths** could fit inside it!"),
        ("🕐", "Distance", "Light from the Sun takes **8 minutes** to reach Earth, even though it travels super-fast!"),
        ("🌍", "Gravity", "The Sun's gravity is what keeps Earth and all the planets from flying away into space."),
        ("⭐", "It is a Star", "The Sun looks much bigger than other stars only because it is much **closer** to us."),
    ]
    for icon, label, fact in sun_facts:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fffbf0;">
            <span style="font-size:1.5rem;">{icon}</span>
            <div><strong style="color:#e67e00;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌞 Click to see a FUN Sun Fact!", use_container_width=True, key="sun_btn"):
        st.session_state.show_sun_fact = not st.session_state.show_sun_fact
    if st.session_state.show_sun_fact:
        st.success("🎉 The Sun is about 4.6 BILLION years old — that's older "
                   "than anything on Earth! It will keep shining for another "
                   "5 billion years. It's older than your great-great-great-great... "
                   "grandparents by a LOT! 😄")

think_bubble("Why do you think we should NEVER look directly at the Sun?")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — THE EARTH 🌍
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌍", "Earth — Our Beautiful Home",
               "The only planet we know has life!")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Earth** is the planet we live on. It is the third planet from the Sun —
    not too close, and not too far away. Scientists sometimes call this the 
    **"Goldilocks Zone"** — just right for life! 🐻

    Earth is very special because it has three things that living creatures need:
    """)
    for item in [
        ("💧", "Water", "Oceans, rivers, and rain keep plants and animals alive."),
        ("🌬️", "Air",   "Our atmosphere has oxygen — the gas we breathe every second."),
        ("🌡️", "Warmth","Earth is just the right temperature — not too hot, not too cold."),
    ]:
        fun_card(item[0], item[1], item[2], bg="#e8f5e9", border="#43a047")

with col2:
    st.markdown("##### 🌏 Cool Earth Facts")
    earth_facts = [
        ("🔵", "Mostly Water",  "About **71%** of Earth's surface is covered by oceans and water!"),
        ("🌀", "Earth Rotates", "Earth spins like a top every **24 hours** — that's what gives us day and night."),
        ("☀️", "Earth Orbits",  "Earth travels all the way around the Sun in **365 days** — one whole year!"),
        ("🏔️", "Layers",       "Earth has layers inside like an onion: crust, mantle, and a hot core in the middle."),
        ("🛡️", "Atmosphere",   "A layer of air called the **atmosphere** wraps around Earth like a giant blanket, keeping us safe."),
    ]
    for icon, label, fact in earth_facts:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f1f8f1;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#2e7d32;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌍 Discover a secret about Earth!", use_container_width=True, key="earth_btn"):
        st.session_state.show_earth_fact = not st.session_state.show_earth_fact
    if st.session_state.show_earth_fact:
        st.success("🎉 From space, Earth looks bright blue because of all its water! "
                   "Astronauts who have seen it from space say it looks like a "
                   "beautiful blue marble floating in black space. 🔵✨")

# ─── Interactive: Day & Night ────────────────────────────────────────────────
st.markdown("#### 🌗 Why Do We Have Day and Night?")
col1, col2, col3 = st.columns(3)
with col1:
    fun_card("🌍➡️☀️", "Facing the Sun",
             "When your side of Earth faces the Sun, it is **DAYTIME** ☀️ — bright and warm!",
             bg="#fff8e1", border="#ffd600")
with col2:
    fun_card("🌍↩️", "Spinning Around",
             "Earth keeps slowly spinning — like you spinning in a slow circle. It takes **24 hours** to spin all the way around.",
             bg="#e8f4fd", border="#4a90e2")
with col3:
    fun_card("🌍⬅️🌑", "Away from the Sun",
             "When your side of Earth faces **away** from the Sun, it is **NIGHTTIME** 🌙 — dark and cool!",
             bg="#f3e5f5", border="#8e24aa")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — THE MOON 🌙
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌙", "The Moon — Our Night-Sky Friend",
               "Earth's only natural moon!")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    The **Moon** is our closest neighbour in space. It travels around Earth 
    in a big circle — just like Earth travels around the Sun.

    The Moon does **not** make its own light. It shines because **sunlight 
    bounces off it** — like a mirror reflecting the Sun! 🪞

    The Moon is much smaller than Earth. It has no air, no water, and 
    no living things. It is covered with rocks, hills, and craters 
    (bowl-shaped holes made by space rocks hitting it long ago).
    """)
    fun_card("👨‍🚀", "Humans on the Moon!",
             "In 1969, astronaut Neil Armstrong became the first human to walk on the Moon. "
             "He said: 'That's one small step for man, one giant leap for mankind!' 🦶🌕",
             bg="#f3e5f5", border="#8e24aa")

with col2:
    st.markdown("##### 🌕 Moon Facts")
    moon_facts = [
        ("📏", "Distance",   "The Moon is about **384,000 km** away — if you drove a car there, it would take 5 months!"),
        ("⏱️", "Orbit",     "The Moon travels around Earth once every **28 days** — about one month!"),
        ("🌊", "Tides",     "The Moon's gravity pulls on Earth's oceans, causing **high tides** and **low tides** every day."),
        ("🌡️", "Temperature","The Moon gets very hot during the day (127°C!) and extremely cold at night (−173°C!)."),
    ]
    for icon, label, fact in moon_facts:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f8f4ff;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#6a1b9a;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌕 Tap to reveal a Moon secret!", use_container_width=True, key="moon_btn"):
        st.session_state.show_moon_fact = not st.session_state.show_moon_fact
    if st.session_state.show_moon_fact:
        st.success("🎉 On the Moon, you would weigh SIX times less than on Earth! "
                   "If you weigh 30 kg here, you'd only weigh 5 kg on the Moon. "
                   "You could jump super high! 🦘🌕")

# ─── Moon Phases Explorer ────────────────────────────────────────────────────
st.markdown("#### 🌑 The Moon's Changing Shapes — Moon Phases!")
st.markdown("The Moon seems to change shape each night because we can only see the "
            "part that is lit by the Sun. Press the button to explore each phase! 👇")

moon_phases = [
    ("🌑", "New Moon",        "The Moon is between Earth and the Sun. We cannot see it at all — the sky looks dark!"),
    ("🌒", "Waxing Crescent", "A tiny sliver of the Moon appears on the right side. It grows a little each night!"),
    ("🌓", "First Quarter",   "We can see exactly half the Moon lit up — like a half-circle!"),
    ("🌔", "Waxing Gibbous",  "More than half is now lit. The lit part is growing bigger and bigger!"),
    ("🌕", "Full Moon",       "The whole face of the Moon is lit up! This is the brightest night of the month."),
    ("🌖", "Waning Gibbous",  "The Moon starts getting smaller on the right side — it is shrinking now."),
    ("🌗", "Last Quarter",    "Again we see half — but now the LEFT side is lit. It's getting smaller!"),
    ("🌘", "Waning Crescent", "Just a tiny sliver is left. Soon it will disappear and start all over again! 🔄"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Previous", use_container_width=True, key="moon_prev"):
        st.session_state.moon_phase_idx = (st.session_state.moon_phase_idx - 1) % len(moon_phases)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="moon_next"):
        st.session_state.moon_phase_idx = (st.session_state.moon_phase_idx + 1) % len(moon_phases)

idx   = st.session_state.moon_phase_idx
phase = moon_phases[idx]
with col2:
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#1a1a4e,#2a2a6e);
                border-radius:20px; padding:2rem; text-align:center; color:#fff;">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{phase[0]}</div>
        <div style="font-size:1.3rem; font-weight:700; margin-bottom:0.5rem;">
            Phase {idx+1} of 8 · {phase[1]}
        </div>
        <div style="font-size:0.97rem; color:#c8daff; line-height:1.6;">{phase[2]}</div>
        <div style="margin-top:1rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.3}">●</span>'
                      for i in range(len(moon_phases))])}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — THE 8 PLANETS 🪐
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🪐", "The 8 Planets of Our Solar System",
               "Click any planet to learn about it!")

planets = {
    "☿ Mercury": {
        "emoji": "☿", "color": "#b0b0b0", "bg": "#f5f5f5",
        "order": "1st from the Sun · Smallest Planet",
        "body": (
            "Mercury is the **smallest planet** and the closest to the Sun. "
            "It races around the Sun faster than any other planet — one year on Mercury "
            "is only **88 Earth days!** ⚡\n\n"
            "Even though it's closest to the Sun, it's not the hottest planet. "
            "It has no thick air to hold warmth, so nights are freezing cold.\n\n"
            "🔘 **No moons** · 🌡️ Day: 430°C, Night: −180°C · 📏 Size: a little bigger than our Moon"
        )
    },
    "♀ Venus": {
        "emoji": "♀", "color": "#ff8f00", "bg": "#fff3e0",
        "order": "2nd from the Sun · Hottest Planet",
        "body": (
            "Venus is the **hottest planet** in our Solar System — even hotter than Mercury! "
            "It has thick clouds that trap heat like a giant blanket. 🔥\n\n"
            "Venus is the **brightest object in our sky** after the Sun and Moon. "
            "You can sometimes see it just before sunrise or just after sunset — "
            "people call it the **Morning Star or Evening Star!** ⭐\n\n"
            "🔘 **No moons** · 🌡️ Surface: 465°C · ⏪ It spins backwards compared to most planets!"
        )
    },
    "🌍 Earth": {
        "emoji": "🌍", "color": "#1565c0", "bg": "#e3f2fd",
        "order": "3rd from the Sun · Our Home!",
        "body": (
            "You already know Earth — it's where WE live! 🏡\n\n"
            "Earth is the **only planet we know of** that has life on it. "
            "It has liquid water, breathable air, and just the right temperature "
            "for plants, animals, and people to survive.\n\n"
            "Earth has **one moon** that we simply call 'the Moon.' "
            "It is covered with beautiful blue oceans, green forests, "
            "sandy deserts, and snowy mountains.\n\n"
            "🌙 **1 moon** · 🌡️ Average: 15°C · 💧 71% of surface is water"
        )
    },
    "♂ Mars": {
        "emoji": "♂", "color": "#c62828", "bg": "#ffebee",
        "order": "4th from the Sun · The Red Planet",
        "body": (
            "Mars is called the **Red Planet** because its soil is full of rusty red dust. "
            "The whole planet looks orange-red from space! 🔴\n\n"
            "Mars has the **tallest volcano in the Solar System** — Olympus Mons. "
            "It is 3 times taller than Mount Everest!\n\n"
            "Scientists send robot explorers called **rovers** to drive around Mars and "
            "take photos and collect rocks. One day, humans might visit Mars! 🤖🚀\n\n"
            "🌙 **2 moons** (Phobos & Deimos) · 🌡️ Average: −60°C · ❄️ Has polar ice caps!"
        )
    },
    "♃ Jupiter": {
        "emoji": "♃", "color": "#e65100", "bg": "#fff3e0",
        "order": "5th from the Sun · Biggest Planet",
        "body": (
            "Jupiter is a **giant!** It is the biggest planet — so big that all the other "
            "7 planets could fit inside it at the same time! 🌐🌐🌐\n\n"
            "Jupiter is made mostly of gas and liquid — there is no solid ground to stand on. "
            "It has a giant swirling storm called the **Great Red Spot** that has been "
            "going for over **350 years!** 🌪️\n\n"
            "Jupiter has **95 moons** — more than any other planet!\n\n"
            "🌙 **95 moons** · ⚡ Has powerful lightning storms · 🔴 Great Red Spot = a storm bigger than Earth!"
        )
    },
    "♄ Saturn": {
        "emoji": "♄", "color": "#f9a825", "bg": "#fffde7",
        "order": "6th from the Sun · The Ringed Planet",
        "body": (
            "Saturn is famous for its beautiful **rings** — flat circles of ice and rock "
            "that go all the way around the planet. They look like a giant hula hoop! 💍\n\n"
            "Saturn is a gas giant like Jupiter. It is so light that it could **float in water** "
            "— if there were an ocean big enough! 🛁\n\n"
            "Saturn has **146 moons** — the most of any planet! Its biggest moon, Titan, "
            "has a thick atmosphere and lakes of liquid gas.\n\n"
            "🌙 **146 moons** · 💍 Rings made of ice & rock · 🪶 Lightest planet for its size"
        )
    },
    "♅ Uranus": {
        "emoji": "♅", "color": "#00838f", "bg": "#e0f7fa",
        "order": "7th from the Sun · The Tilted Planet",
        "body": (
            "Uranus is a beautiful **blue-green** colour! It looks that way because of a "
            "gas in its atmosphere called methane that absorbs red light. 🩵\n\n"
            "The most unique thing about Uranus is that it **spins on its side** — "
            "like a rolling ball! Scientists think a giant space rock crashed into it "
            "long ago and knocked it over.\n\n"
            "This means Uranus has very unusual seasons — one summer on Uranus lasts "
            "**42 Earth years!** ☀️ And so does winter! 🥶\n\n"
            "🌙 **27 moons** · 🩵 Blue-green colour · ↔️ Spins on its side!"
        )
    },
    "♆ Neptune": {
        "emoji": "♆", "color": "#1565c0", "bg": "#e8eaf6",
        "order": "8th from the Sun · Windiest Planet",
        "body": (
            "Neptune is the **furthest planet** from the Sun and the **windiest** place in "
            "the Solar System! Its winds blow at over **2,000 km per hour** — faster than "
            "any storm on Earth! 🌬️💨\n\n"
            "Neptune is a deep, dark **blue** — even bluer than Uranus — and is also a gas planet. "
            "It takes **165 Earth years** to travel once around the Sun. "
            "That means one Neptune year is longer than a human lifetime!\n\n"
            "🌙 **16 moons** · 💨 Fastest winds in the Solar System · 🔵 Deepest blue colour"
        )
    },
}

# Planet selector
planet_cols = st.columns(8)
planet_names = list(planets.keys())
for i, (pname, pdata) in enumerate(planets.items()):
    with planet_cols[i]:
        short = pname.split(" ")[1]
        if st.button(pdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"planet_{i}"):
            st.session_state.planet_picked = pname

# Planet detail card
if st.session_state.planet_picked:
    pname = st.session_state.planet_picked
    pdata = planets[pname]
    st.markdown(f"""
    <div style="background:{pdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {pdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{pdata['emoji']}</span>
            <div>
                <div style="font-size:1.4rem; font-weight:700; color:#2c3e50;">
                    {pname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{pdata['color']}; font-weight:600;">
                    {pdata['order']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(pdata["body"])

else:
    st.info("👆 Tap any planet button above to explore it!")

# Planet order helper
st.markdown("#### 🧠 How to Remember the Planet Order!")
st.markdown("""
<div style="background:linear-gradient(135deg,#1a1a4e,#2d4a8c); color:#fff;
            border-radius:16px; padding:1.4rem 1.8rem; margin:0.5rem 0;">
    <div style="font-size:1.05rem; font-weight:600; margin-bottom:0.5rem;">
        🌟 Use this fun sentence to remember all 8 planets in order:
    </div>
    <div style="font-size:1.5rem; font-weight:700; color:#ffd700; letter-spacing:0.03em;
                margin-bottom:0.5rem;">
        "My Very Excited Monkey Jumps Swiftly Under Neptune"
    </div>
    <div style="display:flex; gap:1.5rem; flex-wrap:wrap; font-size:0.93rem; color:#c8daff;">
        <span>☿ <b>M</b>ercury</span>
        <span>♀ <b>V</b>enus</span>
        <span>🌍 <b>E</b>arth</span>
        <span>♂ <b>M</b>ars</span>
        <span>♃ <b>J</b>upiter</span>
        <span>♄ <b>S</b>aturn</span>
        <span>♅ <b>U</b>ranus</span>
        <span>♆ <b>N</b>eptune</span>
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — MINI QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Let's Test What You Know!",
               "Answer all 6 questions, then press Check My Answers! 🎯")

questions = [
    {
        "q":  "Q1 ☀️ — What does the Sun give us every day?",
        "opts": ["Ice and Snow", "Heat and Light", "Rain and Thunder", "Wind and Clouds"],
        "ans": "Heat and Light",
        "explain": "The Sun gives us heat to keep us warm and light to brighten our day! 🌞"
    },
    {
        "q":  "Q2 🌍 — Which planet do WE live on?",
        "opts": ["Mars", "Venus", "Earth", "Jupiter"],
        "ans": "Earth",
        "explain": "We live on Earth — the third planet from the Sun, and the only one with life! 🌍"
    },
    {
        "q":  "Q3 🌙 — Does the Moon make its own light?",
        "opts": ["Yes, it glows!", "No — it reflects sunlight", "Yes, from fire inside it", "No, it uses batteries"],
        "ans": "No — it reflects sunlight",
        "explain": "The Moon works like a mirror — it reflects the Sun's light towards us! 🪞"
    },
    {
        "q":  "Q4 🔴 — Which planet is called the Red Planet?",
        "opts": ["Venus", "Jupiter", "Mars", "Mercury"],
        "ans": "Mars",
        "explain": "Mars looks red because it is covered with rusty red dust! 🔴"
    },
    {
        "q":  "Q5 🪐 — Which planet has beautiful rings around it?",
        "opts": ["Jupiter", "Saturn", "Neptune", "Earth"],
        "ans": "Saturn",
        "explain": "Saturn has famous flat rings made of ice and rocks — like a giant hula hoop! 💍"
    },
    {
        "q":  "Q6 🌌 — How many planets are in our Solar System?",
        "opts": ["6", "10", "8", "12"],
        "ans": "8",
        "explain": "There are exactly 8 planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune!"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="quiz_submit"):
        st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    score = 0
    for i, q in enumerate(questions):
        ans = st.session_state.quiz_answers.get(i)
        if ans == q["ans"]:
            score += 1
            st.success(f"✅ **{q['q'].split('—')[1].strip()}** → Correct! 🎉 {q['explain']}")
        elif ans is None:
            st.warning(f"⚠️ **{q['q'].split('—')[1].strip()}** → You didn't answer this one!")
        else:
            st.error(f"❌ **{q['q'].split('—')[1].strip()}** → Not quite! "
                     f"The answer is **{q['ans']}**. {q['explain']}")

    # Score badge
    badge_data = [
        (6, "🏆", "SPACE SUPERSTAR!", "#ffd700", "#fffde7"),
        (5, "🥇", "Amazing Explorer!", "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Space Cadet!", "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good Job, Stargazer!", "#4a90e2", "#e8f4fd"),
        (0, "🚀", "Keep Exploring! You'll get there!", "#8e24aa", "#f3e5f5"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — WHAT DID WE LEARN?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?", "A quick summary for you!")

summary_items = [
    ("🌌", "Outer Space", "Everything beyond Earth's sky — full of stars, planets, and moons!"),
    ("☀️", "The Sun",    "A giant glowing star that gives Earth heat and light. Life needs it!"),
    ("🌍", "Earth",      "Our home planet — the only one with air, water, and living things."),
    ("🌙", "The Moon",   "Earth's companion that reflects sunlight and changes shape each month."),
    ("🪐", "8 Planets",  "Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune — all orbiting the Sun."),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)


# ─── Grand Finale Footer ─────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:2.5rem 2rem;
            background:linear-gradient(135deg,#003300,#1b5e20,#0d47a1,#003300);
            border-radius:24px; color:#fff;">
    <div style="font-size:3rem; margin-bottom:0.5rem;">🌍🎓🌟</div>
    <div style="font-size:1.8rem; font-weight:700; margin-bottom:0.8rem; color:#ffffff;">
        Congratulations, Little Scientist! 🏆
    </div>
    <div style="font-size:1.1rem; color:#c8e6c9; margin-bottom:1rem; line-height:1.8;">
        You have completed all <strong style="color:#ffffff;">10 Chapters</strong>
        of <em>Science for Little Stars</em>! 🌟<br>
        From the stars above to the magnets on your fridge, from the weather in the sky
        to the blood in your veins, from the electricity in your home
        to the magnificent planet beneath your feet —
        <strong style="color:#a5d6a7;">you now understand the world in a way most adults never will.</strong>
    </div>
    <div style="background:rgba(255,255,255,0.12); border-radius:16px;
                padding:1rem 1.5rem; margin:1rem 0; display:inline-block;">
        <div style="font-size:1rem; color:#fff9c4; font-weight:700; margin-bottom:0.5rem;">
            🎒 The 10 Chapters You Conquered:
        </div>
        <div style="font-size:0.95rem; color:#e8f5e9; line-height:2;">
            🦴 Chapter 01: Our Amazing Body &nbsp;|&nbsp;
            👁️ Chapter 02: The Five Senses &nbsp;|&nbsp;
            🌱 Chapter 03: Plants and Growth &nbsp;|&nbsp;
            🐾 Chapter 04: Animals and Habitats<br>
            🧲 Chapter 05: Magnets &nbsp;|&nbsp;
            ☁️ Chapter 06: Water and Weather<br>
            🛠️ Chapter 07: Simple Machines &nbsp;|&nbsp;
            🌍 Chapter 08: Saving Our Planet
            ⚡ Chapter 09: Energy and Electricity<br>
            🌌 Chapter 10: The Solar System &nbsp;|&nbsp;
        </div>
    </div>
    <div style="font-size:1.05rem; color:#a5d6a7; margin-top:1rem;">
        Now go outside, look up at the sky, feel the wind, touch a leaf —
        and remember: <strong style="color:#ffffff;">you are a scientist!</strong> 🔬✨
    </div>
    <div style="margin-top:1.2rem; font-size:1.8rem; letter-spacing:0.4rem;">
        🌍 ♻️ 💧 🌳 🌡️ 🌊 🦋 💚 🌟 🎓
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
