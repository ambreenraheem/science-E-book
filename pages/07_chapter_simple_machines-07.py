import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 07 · Simple Machines", layout="wide", initial_sidebar_state="expanded")

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
    "show_lever_fact", "show_wheel_fact",
    "show_pulley_fact", "show_ramp_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "machine_picked"  not in st.session_state: st.session_state.machine_picked  = None
if "animal_picked"   not in st.session_state: st.session_state.animal_picked   = None
if "machine_step"    not in st.session_state: st.session_state.machine_step    = 0
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
<div style="background:linear-gradient(135deg,#1b2631,#784212,#1a5276,#1b2631);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#f0b27a; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 07 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🛠️ Simple Machines! ⚙️
    </h1>
    <p style="color:#fad7a0; font-size:1.05rem; margin:0.8rem 0 0;">
        Discover the six incredible tools that have helped humans build, lift,
        and move things for thousands of years — all around you right now!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        ⚖️ 🎡 🪜 ⚙️ 🔪 🪝
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What a **simple machine** is and why it helps us
        - ✅ How a **lever** multiplies our pushing force
        - ✅ How **wheels and axles** make movement easy
        - ✅ How a **pulley** helps us lift heavy things high
        """)
    with col2:
        st.markdown("""
        - ✅ How an **inclined plane (ramp)** reduces effort
        - ✅ How a **wedge** splits and cuts things apart
        - ✅ How a **screw** is really a ramp wrapped in a spiral
        - ✅ Simple machines hidden in everyday life + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS A SIMPLE MACHINE?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🛠️", "What Is a Simple Machine?",
               "Tools that make every job easier — with no engine, no electricity, just clever science!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Have you ever used a door handle? Ridden a bicycle? Opened a tin with a can opener?
    All of these use **simple machines**! 🤩

    A **simple machine** is a basic tool that makes doing a job **easier**.
    It does not have an engine or use electricity — it just uses the clever science of
    **forces** to multiply your effort, change direction, or help you move things
    that would be impossible to move with your bare hands alone. 💪

    Scientists have identified **six types** of simple machines.
    Together, these six have built every pyramid, every cathedral, every skyscraper,
    and every bridge on Earth! All the complicated machines you see — cars,
    cranes, clocks, scissors — are combinations of these same six simple machines. ⚙️
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#fdf2e9,#eaf2ff);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #784212;">
        <div style="font-weight:700; color:#784212; font-size:1.05rem; margin-bottom:0.8rem;">
            ⚙️ The Six Simple Machines — Know Them All!
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">⚖️</div>
                <div style="font-weight:700; color:#c0392b;">Lever</div>
                <div style="font-size:0.8rem; color:#666;">A bar that pivots on a point</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🎡</div>
                <div style="font-weight:700; color:#1a5276;">Wheel &amp; Axle</div>
                <div style="font-size:0.8rem; color:#666;">A wheel on a spinning rod</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🪝</div>
                <div style="font-weight:700; color:#1e8449;">Pulley</div>
                <div style="font-size:0.8rem; color:#666;">A wheel with a rope over it</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🪜</div>
                <div style="font-weight:700; color:#7d6608;">Inclined Plane</div>
                <div style="font-size:0.8rem; color:#666;">A flat sloping surface (ramp)</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🔪</div>
                <div style="font-weight:700; color:#6c3483;">Wedge</div>
                <div style="font-size:0.8rem; color:#666;">Two ramps joined at a point</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🔩</div>
                <div style="font-weight:700; color:#117a65;">Screw</div>
                <div style="font-size:0.8rem; color:#666;">A ramp wrapped in a spiral</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("Look around the room right now — can you spot any simple machines? Hint: check the door, your pencil, and your chair! 🔍")

with col2:
    fun_card("💪", "What is FORCE?",
             "A <strong>force</strong> is a push or a pull — it is what makes things move, stop, "
             "or change shape! Simple machines do not create new force — "
             "they just change HOW you use the force you already have. "
             "A small force over a long distance can equal a big force over a short distance! 🔄",
             bg="#fdf2e9", border="#e67e22")
    fun_card("🏛️", "Thousands of Years Old!",
             "Ancient Egyptians used levers, ramps, and sledges to build the pyramids "
             "over 4,500 years ago — without any machinery! "
             "The ancient Greeks identified and named the simple machines. "
             "These ideas are still the foundation of all engineering today. 🌍⛏️",
             bg="#eaf2ff", border="#1a5276")
    fun_card("⚙️", "Compound Machines",
             "When you put two or more simple machines together, you get a "
             "<strong>compound machine</strong>! A bicycle uses a wheel and axle, "
             "a lever (brakes), and sometimes a pulley (gear chain). "
             "A pair of scissors is two levers with two wedges! ✂️",
             bg="#e9f7ef", border="#1e8449")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE SIX SIMPLE MACHINES IN DETAIL
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔬", "Let's Explore Each Simple Machine!",
               "Dive deep into how every one works — they are more amazing than you think! ⚙️")

# ─── LEVER ───────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### ⚖️ Machine 1 — The Lever")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    A **lever** is one of the oldest and most useful simple machines!
    It is simply a **rigid bar** that rests on a turning point called a **FULCRUM**. ⚖️

    A lever lets a small force in one place create a much bigger force somewhere else —
    like magic! The further you push from the fulcrum, the less effort you need.

    **How a lever works — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "📏", "The bar (lever)",       "A stiff rod, plank, or bar that does not bend under pressure — it can be wood, metal, or any rigid material."),
        (2, "🔵", "The fulcrum",           "The FULCRUM is the pivot point — the place the lever balances and rotates around. Move the fulcrum and you change how easy or hard the lever is to use!"),
        (3, "💪", "The effort",            "The EFFORT is the force YOU apply — where you push or pull down on the lever. The further the effort from the fulcrum, the less force you need!"),
        (4, "📦", "The load",             "The LOAD is the heavy thing you are trying to move. The closer the load is to the fulcrum, the easier it is to lift! ⬆️"),
        (5, "✨", "Mechanical advantage", "A lever multiplies your effort! A long lever can let a child lift a car — if the fulcrum is in the right place! This multiplying effect is called MECHANICAL ADVANTAGE. 💡"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fdedec;">
            <span style="background:#c0392b; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#c0392b;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### ⚖️ The Three Classes of Lever")
    classes = [
        ("1️⃣", "First Class",  "#fdedec", "#c0392b",
         "Fulcrum is IN THE MIDDLE — effort and load on opposite ends.",
         "Seesaw, scissors, crowbar, pliers, balance scales ⚖️"),
        ("2️⃣", "Second Class", "#fef9e7", "#d4ac0d",
         "Load is IN THE MIDDLE — fulcrum at one end, effort at the other.",
         "Wheelbarrow, nutcracker, bottle opener, stapler 🔧"),
        ("3️⃣", "Third Class",  "#e9f7ef", "#1e8449",
         "Effort is IN THE MIDDLE — fulcrum at one end, load at the other.",
         "Tweezers, fishing rod, your own arm! Forearm is the lever, elbow is fulcrum 💪"),
    ]
    for icon, name, bg, color, rule, eg in classes:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:12px; padding:0.6rem 1rem;
                    border-left:4px solid {color}; margin-bottom:0.4rem;">
            <span style="font-size:1.2rem;">{icon}</span>
            <strong style="color:{color};"> {name}:</strong>
            <span style="font-size:0.88rem; color:#555;"> {rule}</span>
            <div style="font-size:0.83rem; color:#777; margin-top:0.2rem; padding-left:1.6rem;">
                📍 Examples: {eg}
            </div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Your arm is a lever! Your elbow is the fulcrum. Can you work out — is your arm a first, second, or third class lever? 💪")

with col2:
    st.markdown("##### ⚖️ Lever Facts")
    for icon, label, fact in [
        ("🏛️", "Ancient Greece",    "Archimedes, the great Greek scientist, said: 'Give me a lever long enough and a fulcrum on which to place it, and I shall move the world!' He was right — in theory! 🌍"),
        ("✂️", "Scissors",         "A pair of scissors is actually TWO levers joined at the fulcrum (the central bolt)! Each blade is a lever, and the bolt is the shared fulcrum. ✂️"),
        ("🦷", "Tooth extraction",  "Dentists use a lever-like tool to loosen teeth before pulling them — the gum acts as the fulcrum and the tooth is the load! 😬"),
        ("🏗️", "Crowbar",          "A steel crowbar is an incredibly powerful first-class lever — builders use them to lift floorboards and pry apart heavy timber with very little effort. 💪"),
        ("⚖️", "Balance scales",   "Weighing scales are first-class levers! When both sides are balanced, the weights must be equal — used for thousands of years in markets! 🛒"),
        ("🎪", "See-saw",          "A playground see-saw is a perfect first-class lever — the fulcrum is in the middle, and two children are the effort and load on either side! 🎢"),
    ]:
        fact_row(icon, label, fact, "#fdedec", "#c0392b")

    if st.button("⚖️ Reveal a Lever Secret!", use_container_width=True, key="lever_btn"):
        st.session_state.show_lever_fact = not st.session_state.show_lever_fact
    if st.session_state.show_lever_fact:
        st.success("🎉 Your entire skeleton is a system of levers! "
                   "Every bone in your body acts as a lever, every joint is a fulcrum, "
                   "and every muscle provides the effort force. "
                   "When you kick a football, your leg bones are third-class levers "
                   "with your hip joint as the fulcrum! ⚽🦴")

# ─── WHEEL AND AXLE ──────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🎡 Machine 2 — Wheel and Axle")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    The **wheel and axle** is one of the greatest inventions in human history —
    it transformed how people travel, work, and live! 🎡

    A wheel and axle is simply a **large wheel** attached to a **smaller cylinder (axle)**.
    When the wheel turns, the axle turns too — and vice versa!

    **How a wheel and axle works:**
    """)
    for step, icon, title, desc in [
        (1, "🎡", "The wheel",           "The large outer circle — the part you turn or that rolls along the ground. The bigger the wheel, the more mechanical advantage!"),
        (2, "🔩", "The axle",            "The small cylinder in the centre that the wheel is attached to. It spins whenever the wheel spins, and the wheel spins whenever the axle turns."),
        (3, "💪", "Small force, big spin","Turning the large wheel with a small force creates a LARGE FORCE at the small axle — this is mechanical advantage at work! 🔄"),
        (4, "🚀", "Reduces friction",    "A wheel rolling along the ground has far less friction than sliding — this is why wheels made carts and chariots so much faster than dragging things! 🏎️"),
        (5, "🔄", "Two directions",      "A wheel and axle can work both ways — turn the wheel to spin the axle (like a screwdriver), OR turn the axle to spin the wheel (like a motor driving a car)! 🚗"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#eaf2ff;">
            <span style="background:#1a5276; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1a5276;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("🚲", "The Bicycle — Wheel and Axle Champion!",
             "A bicycle uses wheel and axle in two brilliant ways! "
             "The pedals turn a gear (axle), which drives the chain, which turns the rear wheel. "
             "Each gear change moves the fulcrum point — making it easier to go uphill "
             "or faster on the flat. A bicycle is a compound machine masterpiece! 🏆",
             bg="#eaf2ff", border="#1a5276")

with col2:
    st.markdown("##### 🎡 Wheel and Axle Facts")
    for icon, label, fact in [
        ("📅", "Invented",          "The wheel was invented around 3,500 BC in Mesopotamia (modern Iraq) — first used for pottery, then for carts about 300 years later! 🏺"),
        ("🚗", "In every car",      "Every car has at least 4 wheels and axles for driving — plus many more inside the engine, steering column, and gearbox! A car has hundreds of wheel-and-axle systems. 🔧"),
        ("🚪", "Door handles",      "A door handle is a wheel and axle! The handle (wheel) turns a short axle that retracts the latch. Try turning a door lock with just the axle — nearly impossible! 🔒"),
        ("🪛", "Screwdriver",       "A screwdriver is a wheel and axle — the handle is the wheel (larger diameter) and the shaft is the axle. A fat handle gives more turning force! 💪"),
        ("⚙️", "Gears",            "Interlocking gears are wheel-and-axle systems! Large gears turning small gears creates speed. Small gears turning large gears creates force. Clocks use dozens of gears! ⏰"),
        ("🎡", "Ferris wheel",      "A Ferris wheel is an enormous wheel-and-axle — an electric motor turns the central axle which spins the giant passenger wheel! 🎪"),
    ]:
        fact_row(icon, label, fact, "#eaf2ff", "#1a5276")

    if st.button("🎡 Reveal a Wheel Secret!", use_container_width=True, key="wheel_btn"):
        st.session_state.show_wheel_fact = not st.session_state.show_wheel_fact
    if st.session_state.show_wheel_fact:
        st.success("🎉 The wheel was NOT the first great invention — "
                   "humans used boats, spears, and needles for thousands of years before the wheel! "
                   "But once invented, the wheel changed everything. "
                   "Today, a world without wheels is impossible to imagine — "
                   "your food, your clothes, everything you own was transported by wheels! 🌍🎡")

# ─── PULLEY ──────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🪝 Machine 3 — The Pulley")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    A **pulley** is a wheel with a groove around its edge — a rope sits in the groove.
    Pull one end of the rope and the other end lifts! 🪝

    Pulleys are how sailors raise sails, how builders lift steel beams, and how
    flagpoles raise flags high in the air!

    **How a pulley works:**
    """)
    for step, icon, title, desc in [
        (1, "🎡", "Grooved wheel",          "A pulley is a wheel with a groove — it is fixed to a support above the load you want to lift. The groove guides the rope so it does not slip off."),
        (2, "🪢", "Rope or cable",          "A rope (or strong cable) sits in the groove. One end is attached to the load, the other end you pull. The pulley changes the DIRECTION of force. 🔄"),
        (3, "⬆️", "Single pulley",          "A single FIXED pulley does not reduce effort — it just lets you pull DOWN to lift something UP. Pulling down is much easier for humans than lifting straight up! 💪"),
        (4, "💡", "Moving pulley",          "A MOVING pulley (attached to the load) halves the force needed! You pull twice as much rope, but with half the effort. This is called a BLOCK AND TACKLE. 🏗️"),
        (5, "🔗", "More pulleys = easier",  "Chain multiple pulleys together (a block and tackle system) and you can lift incredibly heavy loads with very little force. Cranes use dozens! 🏙️"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e9f7ef;">
            <span style="background:#1e8449; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1e8449;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("When you pull down a rope on a flagpole to make the flag go UP — what simple machine is doing that work? 🚩")

with col2:
    st.markdown("##### 🪝 Pulley Facts")
    for icon, label, fact in [
        ("⚓", "Sailing ships",     "Ancient sailing ships used hundreds of pulley systems to control the sails — a single sailor could adjust enormous sails using ropes and pulleys! ⛵"),
        ("🏗️", "Tower cranes",     "The tower cranes on building sites use complex pulley systems to lift steel beams and concrete weighing many tonnes high into the sky! 🏙️"),
        ("🎭", "Theatre rigging",  "Theatre stages use elaborate pulley systems to lower and raise scenery, curtains, and even actors during performances! 🎪"),
        ("⛏️", "Mine lifts",       "Before electric motors, miners were raised and lowered into deep mine shafts in cages suspended from pulley systems — sometimes hundreds of metres deep! ⬇️"),
        ("🏋️", "Gym equipment",    "Many gym weight machines use pulley systems — you pull a handle and pulleys redirect your force to lift the weights from a safe direction. 💪"),
        ("🧲", "Elevators",        "The first elevators used pulley and counterweight systems — one heavy counterweight on the other side of a pulley made lifting the passenger car much easier! 🏢"),
    ]:
        fact_row(icon, label, fact, "#e9f7ef", "#1e8449")

    if st.button("🪝 Tap for a Pulley Surprise!", use_container_width=True, key="pulley_btn"):
        st.session_state.show_pulley_fact = not st.session_state.show_pulley_fact
    if st.session_state.show_pulley_fact:
        st.success("🎉 Archimedes (the ancient Greek genius) once built a giant pulley system "
                   "called a POLYSPASTOS that he claimed could allow one man to pull a fully "
                   "loaded warship out of the sea onto dry land — all by himself! "
                   "He reportedly demonstrated this to a stunned king. "
                   "The right pulley system truly can make the impossible possible! ⛵💪")

# ─── INCLINED PLANE ──────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🪜 Machine 4 — The Inclined Plane (Ramp)")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    An **inclined plane** is simply a flat surface that is tilted at an angle — a **ramp**! 🪜
    It is one of the simplest and most useful machines ever made.

    Instead of lifting something straight up (which needs a lot of force),
    you slide it up a ramp (which needs much less force — just more distance)!

    **How an inclined plane works:**
    """)
    for step, icon, title, desc in [
        (1, "📐", "A sloped surface",       "An inclined plane is just a flat, sloped surface connecting a low point to a high point. The angle of the slope changes how easy or hard it is to use."),
        (2, "📦", "Force vs distance",      "To lift a box straight up requires a BIG force over a SHORT distance. A ramp lets you use a SMALLER force over a LONGER distance — same work, less effort! ⚖️"),
        (3, "📉", "Gentle slope = easier",  "The GENTLER the slope, the less effort needed — but you must travel a longer distance. A very steep ramp takes more effort but a shorter path. 🔄"),
        (4, "📈", "Steep slope = harder",   "The steeper the ramp, the harder it is to push something up — but the shorter the distance! You always trade force for distance in simple machines."),
        (5, "🛝", "Everywhere around us!",  "Ramps are everywhere — roads zigzag up mountains, wheelchair ramps help people into buildings, loading docks help move heavy boxes into lorries! 🚛"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fef9e7;">
            <span style="background:#d4ac0d; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#d4ac0d;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("🏔️", "The Great Pyramid — Built with Ramps!",
             "Scientists believe ancient Egyptians built the Great Pyramid "
             "using enormous earthen ramps to drag 2.3 million stone blocks "
             "— each weighing 2.5 tonnes — up to their positions! "
             "Thousands of workers used ramps, sledges, and levers "
             "to build one of the greatest structures in human history. 🌍✨",
             bg="#fef9e7", border="#d4ac0d")

with col2:
    st.markdown("##### 🪜 Inclined Plane Facts")
    for icon, label, fact in [
        ("🏔️", "Mountain roads",   "Mountain roads zigzag back and forth (called SWITCHBACKS) to reduce the slope — a longer, gentler path up the mountain needs far less engine power! 🚗"),
        ("♿", "Wheelchair ramps", "Ramps allow wheelchair users to access buildings without needing to be lifted — a gentle gradient makes it possible to push up independently. ♿🏛️"),
        ("🚢", "Ship launch",      "Ships are launched sideways into water down enormous greased inclined planes — gravity and the slope do all the work of sliding the ship in! ⛴️"),
        ("🛝", "Playground slide",  "A playground slide is an inclined plane! Gravity pulls you down the slope — the shallower the slide, the slower and more controlled the descent. 🎢"),
        ("🔧", "Car ramps",        "Mechanics drive cars up metal ramps to work underneath them — much easier and safer than digging a pit or lifting the whole car! 🚙"),
        ("📦", "Warehouse ramps",  "Warehouses use ramps and roller conveyor systems to move heavy pallets from delivery lorries into storage — pure inclined plane physics! 🏭"),
    ]:
        fact_row(icon, label, fact, "#fef9e7", "#d4ac0d")

    if st.button("🪜 Reveal a Ramp Secret!", use_container_width=True, key="ramp_btn"):
        st.session_state.show_ramp_fact = not st.session_state.show_ramp_fact
    if st.session_state.show_ramp_fact:
        st.success("🎉 The steepest road in the world is Baldwin Street in Dunedin, New Zealand — "
                   "with a slope of 35 degrees! It is so steep that people have actually "
                   "rolled giant balls of chocolate down it for a charity race! 🍫🎉 "
                   "Most roads are kept below 6 degrees — any steeper and cars and lorries "
                   "struggle to climb in wet or icy conditions. 🚗❄️")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — WEDGE AND SCREW (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔩", "Wedge and Screw — The Last Two!",
               "The final two simple machines — and they are the sneakiest ones of all! 🤫")

machine_steps = [
    ("🔪", "The Wedge — Two Ramps Joined Together!",
     "A **wedge** is basically TWO inclined planes joined at their thin ends — forming a point or sharp edge! 🔪\n\n"
     "**How it works:** When you push a wedge INTO something, the sloping sides push the material SIDEWAYS and APART. "
     "A small downward force on the thick end creates a LARGE sideways force at the thin end! 💥\n\n"
     "**Everyday wedges you use every day:**\n"
     "- 🔪 **Knife and axe**: Push down on the thick back — the sharp wedge edge splits food and wood apart!\n"
     "- 📌 **Nail**: A nail is a wedge! The pointed tip splits wood fibres apart as you hammer it in.\n"
     "- ✏️ **Pencil tip**: A sharpened pencil is a wedge — the point splits paper fibres to make a mark!\n"
     "- 🚪 **Door wedge**: The thin end goes under the door, and the slope keeps it from closing! 🛑\n"
     "- ⛏️ **Chisel**: Stonemasons and woodworkers use wedge-shaped chisels to carve and split materials! 🪨",
     "#f5eef8", "#6c3483"),
    ("🔩", "The Screw — A Ramp in a Spiral!",
     "A **screw** is secretly an inclined plane (ramp) wrapped in a spiral around a cylinder! 🔩\n\n"
     "**How it works:** The spiral thread on a screw is actually a ramp going round and round. "
     "Each turn of the screw moves it a tiny bit forward — but turns a small rotational force "
     "into a HUGE forward force! This is why a small screwdriver can drive a screw deep into hard wood. 💪\n\n"
     "**Everyday screws everywhere:**\n"
     "- 🔩 **Wood screws**: The spiral thread grips wood fibres tightly — much stronger than a nail! 🪵\n"
     "- 🫙 **Jar lids**: The thread on a jar lid is a screw! Each turn moves the lid further on or off. 🫙\n"
     "- 💉 **Drill bit**: A drill bit is a screw — the spiral groove carries wood shavings out as it bores in! 🌀\n"
     "- 🚢 **Ship propeller**: A ship's propeller is a screw that pushes water backward, driving the ship forward! ⛴️\n"
     "- 🗜️ **Clamps and vices**: Workshop clamps use a screw thread to generate enormous gripping force from a simple turn of the handle! 🔧",
     "#e8f8f5", "#117a65"),
    ("⚙️", "How Wedge and Screw Are REALLY Ramps!",
     "Here is the beautiful secret that connects wedge, screw, and inclined plane together! 🤩\n\n"
     "**All three are the SAME machine in different form:**\n\n"
     "- 🪜 **Inclined Plane**: A flat ramp — you move a load along its surface upward.\n"
     "- 🔪 **Wedge**: Take two inclined planes and join them back-to-back — now it splits things sideways!\n"
     "- 🔩 **Screw**: Take an inclined plane and wrap it in a spiral around a cylinder — now it drills into materials!\n\n"
     "Scientists sometimes group all three together as **'the inclined plane family'** — "
     "they all use the same basic principle of trading a small force over a long path "
     "for a big force over a short distance. 🔄\n\n"
     "This is why knowing just **ONE** core principle of physics lets you understand "
     "three completely different-looking tools! Science is elegant! 🌟",
     "#fdf2e9", "#784212"),
    ("🏆", "Compound Machines — Simple Machines Working Together!",
     "The real magic happens when simple machines team up! A **compound machine** "
     "is just two or more simple machines working together. 🤝\n\n"
     "**Famous compound machines broken down:**\n\n"
     "- ✂️ **Scissors**: 2 LEVERS (the handles) + 2 WEDGES (the blades) joined at a FULCRUM (the bolt)!\n"
     "- 🚲 **Bicycle**: WHEEL AND AXLE (wheels) + LEVER (handlebars, brake levers) + PULLEY (gear chain) + WEDGE (brake pads)!\n"
     "- 🔨 **Hammer**: LEVER (handle multiplies force) + WEDGE (nail it drives in)!\n"
     "- 🪣 **Well bucket**: PULLEY (rope over wheel) + LEVER (handle you turn)!\n"
     "- 🏗️ **Crane**: PULLEY (lifting rope) + WHEEL AND AXLE (cab rotation) + LEVER (boom arm)!\n\n"
     "Every machine ever built — from a toaster to a spacecraft — is made of "
     "combinations of these same six simple machines! 🚀",
     "#eaf2ff", "#1a5276"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="mach_prev"):
        st.session_state.machine_step = max(0, st.session_state.machine_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="mach_next"):
        st.session_state.machine_step = min(len(machine_steps)-1, st.session_state.machine_step + 1)

idx   = st.session_state.machine_step
mstep = machine_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{mstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {mstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{mstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {mstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {mstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{mstep[4]}">●</span>'
                for i in range(len(machine_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            {idx+1} of {len(machine_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — SIMPLE MACHINES IN EVERYDAY LIFE (Topic selector)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🏠", "Simple Machines Are Everywhere!",
               "Tap each place to find all the hidden simple machines around you! 🔍")

everyday_machines = {
    "🏠 At Home": {
        "emoji": "🏠", "color": "#c0392b", "bg": "#fdedec",
        "tagline": "⚙️ Your home is a machine museum!",
        "body": (
            "Your home is packed with simple machines — you use them dozens of times a day without thinking! 🏡\n\n"
            "- 🪛 **Screws**: Holding your furniture together, your light switches on the wall, your door hinges — screws everywhere! Count the screws in just one room! 🔩\n"
            "- 🚪 **Door handle**: A lever! The handle multiplies your small turning force into enough force to retract the heavy latch bolt. 💪\n"
            "- 🪟 **Scissors**: Two levers + two wedges — cutting paper, fabric, and food! ✂️\n"
            "- 🔪 **Kitchen knives**: Wedges! Every knife, from bread knife to vegetable peeler, uses a wedge-shaped blade. 🥕\n"
            "- 🪣 **Blinds and curtains**: Pulley systems! Pull the cord down and the blind goes up — a simple fixed pulley! 🏠\n"
            "- 🪜 **Stairs**: A staircase is a series of inclined planes — each step is a tiny ramp that makes going upstairs much less effort than climbing straight up! 🧗"
        )
    },
    "🏫 At School": {
        "emoji": "🏫", "color": "#1a5276", "bg": "#eaf2ff",
        "tagline": "⚙️ Learning surrounded by machines!",
        "body": (
            "Your classroom is full of simple machines you use every single day! 📚\n\n"
            "- ✏️ **Pencil sharpener**: A wedge (the blade) + a wheel and axle (the turning handle)! The spinning wedge shaves wood and graphite. ✏️\n"
            "- 📌 **Stapler**: A second-class lever! The stapler body is the lever, the hinge is the fulcrum, and you press down (effort) to push the staple through paper (load). 📎\n"
            "- 🖊️ **Pencil tip**: A wedge! The sharp graphite tip is a tiny wedge that splits paper fibres and leaves graphite behind. ✍️\n"
            "- 🚪 **Classroom door**: Lever (handle) + screw (hinges) + wedge (latch)! Three machines in one door. 🚪\n"
            "- 📐 **Ruler (as lever)**: You can use a ruler as a first-class lever to pry open a paint tin lid — with a pencil as the fulcrum! 🎨\n"
            "- 🎒 **Zip**: A zip is a wedge! The sliding pull opens two rows of teeth by pushing them apart, or closes them by pushing them together. 🧳"
        )
    },
    "🏗️ Building Sites": {
        "emoji": "🏗️", "color": "#7d6608", "bg": "#fef9e7",
        "tagline": "⚙️ Simple machines building big things!",
        "body": (
            "Building sites are the ultimate simple machine playground — everything is being lifted, pushed, and moved! 🏙️\n\n"
            "- 🏗️ **Tower crane**: Pulley (lifting hook) + lever (the boom arm) + wheel and axle (the rotating cab) — three machines in one towering structure! 🌆\n"
            "- 🔩 **Concrete screws**: Enormous screws drill into rock to anchor buildings in place — the same principle as a tiny wood screw, just massive! 💪\n"
            "- 🛞 **Wheelbarrow**: A second-class lever — the wheel is the fulcrum, the load sits in the bucket (middle), and you lift the handles (effort). 💪\n"
            "- 🪛 **Impact driver**: A wheel and axle (the drill chuck) + screw (the fastener being driven)! 🔧\n"
            "- ⛏️ **Crowbar**: The most powerful first-class lever on a building site — used to pry apart floorboards, move heavy stones, and open sealed containers. 🏚️\n"
            "- 🪜 **Scaffolding ramps**: Inclined planes that allow workers to push heavy materials to different levels of the building without lifting! 📦"
        )
    },
    "🚗 In Transport": {
        "emoji": "🚗", "color": "#117a65", "bg": "#e8f8f5",
        "tagline": "⚙️ Getting you from A to B!",
        "body": (
            "Every vehicle you travel in uses multiple simple machines working together at high speed! 🚀\n\n"
            "- 🚗 **Car wheels**: Wheel and axle — the engine turns the axle, which spins the wheel! Four wheels, four axles, all spinning together. 🛞\n"
            "- 🛞 **Steering wheel**: A wheel and axle — turning the large wheel rotates the smaller steering column, which turns the front wheels! 🔄\n"
            "- ✈️ **Aeroplane propeller**: A screw! The spiral blade pushes air backward, driving the plane forward — same principle as a ship's propeller in water. ⛴️\n"
            "- 🚂 **Railway switches**: Giant levers! A lever changes the direction of the track — a small handle movement at one end moves a massive rail at the other. 🛤️\n"
            "- 🧰 **Car jack**: A screw! Turn the handle and the screw thread slowly lifts the car — a tiny rotational force lifting tonnes of metal! 🚙\n"
            "- 🛝 **Motorway on-ramps**: Inclined planes — long gentle ramps that let vehicles gradually accelerate to motorway speed! 🏎️"
        )
    },
    "🏥 In Medicine": {
        "emoji": "🏥", "color": "#6c3483", "bg": "#f5eef8",
        "tagline": "⚙️ Simple machines that heal!",
        "body": (
            "Simple machines play life-saving roles in hospitals and medicine every day! 🩺\n\n"
            "- 🩺 **Syringe plunger**: A lever principle — the handle lets you apply a controlled force to the plunger to draw or inject fluid precisely. 💉\n"
            "- 🦽 **Wheelchair ramp**: An inclined plane that allows wheelchair users to enter buildings — a gentle slope makes independence possible! ♿\n"
            "- 🔩 **Bone screws**: Surgeons use tiny titanium screws to hold broken bones together while they heal — same screw principle, just inside your body! 🦴\n"
            "- 🏥 **Hospital bed controls**: Lever mechanisms allow nurses to raise or lower sections of the bed with minimal effort for patient care. 🛏️\n"
            "- 🦷 **Dental tools**: Dental probes are levers — the dentist applies a small force at the handle, creating a precise force at the tip. The mouth mirror handle is a wheel and axle! 😬\n"
            "- 💊 **Pill cutter**: A lever and a wedge together — press the lever handle, the wedge blade cuts the pill cleanly in half! 🔪"
        )
    },
    "🌾 On a Farm": {
        "emoji": "🌾", "color": "#784212", "bg": "#fdf2e9",
        "tagline": "⚙️ The oldest machines on Earth!",
        "body": (
            "Farming was the first industry to use simple machines systematically — thousands of years ago! 🌱\n\n"
            "- ⛏️ **Plough**: A wedge that splits and turns soil as it is dragged forward — the same principle as a knife cutting through butter, just through hard earth! 🐂\n"
            "- 🪣 **Water wheel**: A wheel and axle used for thousands of years to lift water from rivers for irrigation, and to grind grain into flour. 💧\n"
            "- 🌾 **Pitchfork**: A lever! The handle multiplies the force of the farmer's arms to lift and throw heavy bundles of hay. 🐴\n"
            "- 🔪 **Scythe**: A lever (long handle) + wedge (sharp curved blade) — used to cut large areas of grain with a sweeping motion. 🌾\n"
            "- 🐓 **Pulley water wells**: Traditional wells used a pulley system to lower and raise a bucket of water — a simple but life-saving application! 🏡\n"
            "- 🧱 **Wedge-shaped plough tip**: The tip of a modern tractor plough is a precisely engineered wedge — splitting earth efficiently with minimum tractor power! 🚜"
        )
    },
}

m_cols = st.columns(len(everyday_machines))
for i, (mname, mdata) in enumerate(everyday_machines.items()):
    with m_cols[i]:
        short = mname.split(" ", 1)[1]
        if st.button(mdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"mplace_{i}"):
            st.session_state.machine_picked = mname

if st.session_state.machine_picked and st.session_state.machine_picked in everyday_machines:
    mname = st.session_state.machine_picked
    mdata = everyday_machines[mname]
    st.markdown(f"""
    <div style="background:{mdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {mdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{mdata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {mname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{mdata['color']}; font-weight:700;">
                    {mdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(mdata["body"])
else:
    st.info("👆 Tap any category above to find all its hidden simple machines!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — ANIMALS THAT USE SIMPLE MACHINES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Animals That Use Simple Machine Principles!",
               "Nature invented simple machines billions of years before humans did — tap to explore! 🌍")

animal_machines = {
    "🦦 Otter": {
        "emoji": "🦦", "color": "#795548", "bg": "#efebe9",
        "tagline": "🔨 The original hammer user!",
        "body": (
            "Sea otters are one of the few non-human animals that use tools — and they use them brilliantly! 🦦\n\n"
            "- 🪨 **Rock as hammer**: Sea otters float on their backs and place a flat rock on their chest as an anvil, then smash shellfish against it to break them open — a LEVER and WEDGE in action!\n"
            "- 💪 **Mechanical advantage**: By swinging the shellfish with their arms (levers!) and smashing against a hard surface (anvil), they generate far more force than their small paws could apply directly.\n"
            "- 🔧 **Personal tools**: Sea otters have favourite rocks they keep and reuse — sometimes carrying them under their arms for days! They select flat, heavy rocks for maximum effect.\n"
            "- 🦷 **Teeth as wedges**: Their powerful, flat molars are wedge-shaped — perfect for crushing hard shells with maximum crushing force per bite. 😬\n"
            "- 🌊 **Floating workshop**: They perform all this tool use while floating on their back in the ocean — perhaps the world's most impressive mobile workshop! 🛠️"
        )
    },
    "🐦 Woodpecker": {
        "emoji": "🐦", "color": "#c0392b", "bg": "#fdedec",
        "tagline": "⛏️ Nature's chisel and lever!",
        "body": (
            "A woodpecker is a flying compound machine — using lever, wedge, and spring all at once! 🐦\n\n"
            "- ⛏️ **Beak as wedge**: The woodpecker's beak is a precision-engineered wedge — hard, sharp, and pointed to split wood fibres with each strike. 🔪\n"
            "- 💪 **Neck as lever**: The neck muscles and skull act as a lever system that amplifies the small movement of the muscles into a powerful hammering blow of up to 20 Newtons!\n"
            "- 🏎️ **20 pecks per second**: A woodpecker can peck 20 times per second — each peck decelerating from 6 m/s to zero! The brain needs special cushioning to survive this. 🧠\n"
            "- 🪝 **Tongue as grappling hook**: After drilling a hole (wedge), the woodpecker extends a sticky barbed tongue to extract insects — a biological hook and pulley! 🪱\n"
            "- 🌲 **Structural engineering**: Woodpeckers engineer perfectly round, smooth-sided nest holes in trees — using their beak as both wedge and chisel. 🏡"
        )
    },
    "🦫 Beaver": {
        "emoji": "🦫", "color": "#6d4c41", "bg": "#efebe9",
        "tagline": "🪵 Nature's greatest engineer!",
        "body": (
            "Beavers are perhaps the most impressive animal engineers on Earth — and they use simple machine principles throughout! 🏗️\n\n"
            "- 🔪 **Teeth as wedges**: Beaver incisors are wedge-shaped and self-sharpening — the front layer is harder orange enamel, the back softer — so chewing keeps them razor-sharp! 🦷\n"
            "- 🌲 **Lever principle**: When felling a tree, beavers work around the trunk in a wedge pattern — each bite removes a wedge of wood, eventually making the trunk so thin it topples under gravity! 🌳\n"
            "- 🏊 **Tail as rudder lever**: The broad, flat tail acts as a steering lever in the water — small muscle movements create large directional changes. ⛵\n"
            "- 🏗️ **Dam engineering**: Beaver dams use an inclined plane principle — a sloped structure of branches and mud that redirects and slows water flow. 💧\n"
            "- 🏠 **Lodge building**: The beaver lodge entrance is underwater — the beaver must dive through a natural pulley-like tube structure to enter the dry living chamber above water! 🏡"
        )
    },
    "🦅 Eagle": {
        "emoji": "🦅", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "⚖️ Lever-powered flight and hunting!",
        "body": (
            "An eagle is a precision lever machine — every part of its body uses lever principles to hunt and fly! 🦅\n\n"
            "- 💪 **Wings as levers**: Eagle wings are curved levers — the wing root (fulcrum) and wing tip (effort and load) work together to generate lift and control direction with minimal muscle effort.\n"
            "- 🦅 **Talons as first-class levers**: When an eagle grips prey, the tendon arrangement in the foot locks the talons closed automatically — no muscle effort needed to maintain grip! Purely mechanical! 🔒\n"
            "- 🔪 **Beak as wedge**: The hooked beak is a curved wedge — perfectly designed to tear flesh by pushing the two cutting edges apart through meat. 🥩\n"
            "- 📐 **Thermal soaring**: Eagles exploit rising warm air columns (thermals) — circling upward for free, using the inclined plane principle of the wind rather than flapping! ☀️\n"
            "- 🎯 **Dive calculation**: A diving eagle calculates the precise angle of its dive — essentially solving a moving inclined-plane equation to intercept fast-moving prey. 🧮"
        )
    },
    "🐜 Leafcutter Ant": {
        "emoji": "🐜", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "✂️ Tiny compound machine!",
        "body": (
            "Leafcutter ants use multiple simple machine principles simultaneously — in a body weighing just 1 milligram! 🤯\n\n"
            "- ✂️ **Jaws as levers + wedges**: The ant's mandibles are curved levers with wedge-shaped cutting edges — they vibrate at 1,000 times per second to saw through leaves! 🌿\n"
            "- 💪 **Carrying as lever**: An ant carries a leaf fragment 50 times its own body weight over its head — using its legs as lever systems to maintain balance. 🏋️\n"
            "- 🔊 **Vibration tool**: Leafcutters stridulate (vibrate their bodies) while cutting — the vibration propagates through the leaf like a saw, making cutting 4x faster! 🪚\n"
            "- 🏗️ **Tunnel engineering**: Underground nest tunnels use inclined plane principles — sloped passages channel air for ventilation, and angle downward to drain water. 🌧️\n"
            "- 🍄 **Fungus farming**: Ants carry leaf fragments to underground chambers and use them to grow fungus — an agricultural system using simple machine principles that has run for 50 million years! 🌱"
        )
    },
    "🐘 Elephant": {
        "emoji": "🐘", "color": "#546e7a", "bg": "#eceff1",
        "tagline": "🌳 The living crane!",
        "body": (
            "Elephants are the largest land animal — and natural masters of simple machine physics! 🐘\n\n"
            "- 🪝 **Trunk as crane arm**: An elephant's trunk is a flexible lever and pulley system — it can exert over 800 Newtons of pulling force to uproot trees, and handle objects as delicate as a single grape. 🍇\n"
            "- 🌊 **Trunk as siphon**: The trunk sucks up to 8 litres of water at once — the elephant's lungs create a pressure difference (like a pulley in reverse) to draw water up the trunk. 💧\n"
            "- 🦷 **Tusks as levers**: Elephant tusks are first-class levers — used to pry bark from trees, lever boulders out of the ground, and dig for underground water. 🪨\n"
            "- 🦶 **Feet as shock absorbers**: Elephant feet contain fatty cushion pads that compress and release with each step — acting as natural spring systems that store and return energy. 🏃\n"
            "- 🌳 **Tree felling**: When an elephant pushes over a tree, it uses its forehead as a wedge and its enormous body weight as the effort force — pure lever and wedge mechanics on a massive scale! 💪"
        )
    },
}

an_cols = st.columns(len(animal_machines))
for i, (aname, adata) in enumerate(animal_machines.items()):
    with an_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"anim_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in animal_machines:
    aname = st.session_state.animal_picked
    adata = animal_machines[aname]
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
    st.info("👆 Tap any animal above to discover how it uses simple machine principles!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — SIMPLE MACHINE SAFETY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Using Simple Machines Safely!",
               "Simple machines are powerful — here is how to use them wisely! 🌟")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("🔪", "Using Cutting Tools Safely",
     "Knives, scissors, and chisels are all wedges — they are sharp by design! "
     "Always cut AWAY from your body, never toward yourself. "
     "Keep fingers curled away from the blade. "
     "Use a chopping board, not your hand, as a surface. "
     "Always put cutting tools down carefully — never leave them in a bag! ✂️🩹",
     "#fdedec", "#c0392b"),
    ("🔩", "Using Screws and Screwdrivers",
     "Always use the right size screwdriver for the screw head — a wrong-sized one can slip and injure your hand! "
     "Keep fingers well away from the screw tip when starting. "
     "Hold the work piece in a clamp — not in your hand — when drilling. "
     "Never use a screwdriver as a chisel or pry tool! 🪛⚠️",
     "#eaf2ff", "#1a5276"),
    ("⚖️", "Using Levers Safely",
     "A long lever can create enormous forces — much more than you expect! "
     "Make sure the lever cannot slip off the fulcrum and snap back. "
     "Keep fingers and toes away from the load end — the force there is huge. "
     "Never use a door as a lever — you can damage hinges and injure yourself. "
     "Always check the lever and fulcrum are stable before applying force. 💪🛑",
     "#fef9e7", "#d4ac0d"),
    ("🪝", "Using Ropes and Pulleys",
     "Rope and pulley systems can lift very heavy loads — treat them with respect! "
     "Never stand underneath a suspended load. "
     "Check ropes for fraying before use — a worn rope can snap suddenly. "
     "Keep hair, clothing, and fingers away from the pulley wheel. "
     "Lower loads slowly and under control — never let them drop freely. 🏗️🧤",
     "#e9f7ef", "#1e8449"),
    ("🎡", "Wheels and Axles Safety",
     "Moving wheels and axles can trap fingers — never reach near spinning parts! "
     "On a bicycle, keep clothes and laces away from the chain and sprocket. "
     "Always use guards and covers on machine wheels in workshops. "
     "Never oil a wheel while it is moving. "
     "Check wheels are properly attached before riding or using — a loose wheel is dangerous! 🚲⚠️",
     "#f5eef8", "#6c3483"),
    ("🧠", "Always Think First!",
     "Simple machines multiply FORCE — which means they can also multiply ACCIDENTS if used carelessly! "
     "Before using any tool, ask: Is it the right tool? Is it in good condition? "
     "Am I using it correctly? Is there anyone in the way? "
     "The greatest simple machine safety tool of all is your BRAIN — use it first! 🧠💡",
     "#e8f8f5", "#117a65"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Can you think of three simple machines you used today before even arriving at school? 🎒🚪🚲")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Simple Machines Quiz — Test What You Know!",
               "6 engineering questions — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 ⚖️ — What is the turning point of a lever called?",
        "opts": ["The effort", "The load", "The fulcrum", "The axle"],
        "ans":  "The fulcrum",
        "explain": "The FULCRUM is the pivot point of a lever — the fixed point that everything rotates around! Move the fulcrum and you change how easy or hard the lever is to use. ⚖️"
    },
    {
        "q":    "Q2 🔩 — A screw is really which simple machine wrapped in a spiral?",
        "opts": ["A lever", "A pulley", "A wheel and axle", "An inclined plane"],
        "ans":  "An inclined plane",
        "explain": "A SCREW is an inclined plane (ramp) wrapped in a spiral around a cylinder! The spiral thread is the ramp — each full turn advances the screw a tiny bit into the material. 🔩🪜"
    },
    {
        "q":    "Q3 ✂️ — A pair of scissors is a combination of which two simple machines?",
        "opts": ["Pulley and screw", "Lever and wedge", "Wheel and ramp", "Axle and fulcrum"],
        "ans":  "Lever and wedge",
        "explain": "Scissors are TWO LEVERS (the handles, joined at the bolt fulcrum) and TWO WEDGES (the sharp blades that slice through material)! A brilliant compound machine! ✂️"
    },
    {
        "q":    "Q4 🪝 — What does a single fixed pulley change about a force?",
        "opts": ["It makes the force much bigger", "It changes the direction of the force", "It makes the load lighter", "It adds extra force from nowhere"],
        "ans":  "It changes the direction of the force",
        "explain": "A single fixed pulley does NOT reduce the force needed — it changes DIRECTION! You pull DOWN to lift something UP. Pulling down is much easier for humans than lifting straight up! 🪝🔄"
    },
    {
        "q":    "Q5 🏔️ — Why do mountain roads zigzag back and forth instead of going straight up?",
        "opts": ["To make the road longer for fun", "To avoid rocks and trees", "A gentler slope needs less effort to climb — the ramp principle", "Because cars cannot turn sharp corners"],
        "ans":  "A gentler slope needs less effort to climb — the ramp principle",
        "explain": "Zigzag roads (switchbacks) create a LONGER but GENTLER slope — using the inclined plane principle! Less engine force needed, even though you travel further. 🏔️🚗"
    },
    {
        "q":    "Q6 🦦 — Which animal uses a rock as a simple machine tool to open shellfish?",
        "opts": ["A beaver 🦫", "A sea otter 🦦", "A woodpecker 🐦", "An elephant 🐘"],
        "ans":  "A sea otter 🦦",
        "explain": "Sea otters float on their backs and smash shellfish against a rock placed on their chest — using the rock as an anvil and their arms as levers! One of the few non-human tool users. 🦦🪨"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"sm_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="sm_quiz_submit"):
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
        (6, "🏆", "MASTER ENGINEER! ⚙️🛠️",             "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Machine Scientist! 🔩",    "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Simple Machine Explorer! ⚖️",  "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Machine Detective! 🔍",    "#7b1fa2", "#f3e5f5"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="sm_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?",
               "Simple Machines — your quick recap! 🎉")

summary_items = [
    ("⚖️", "Lever",          "A rigid bar on a fulcrum — multiplies force and changes direction!"),
    ("🎡", "Wheel & Axle",   "A wheel on a rod — reduces friction and multiplies force!"),
    ("🪝", "Pulley",         "A grooved wheel with rope — changes direction of force!"),
    ("🪜", "Inclined Plane", "A sloped ramp — less force needed over longer distance!"),
    ("🔪", "Wedge",          "Two ramps joined — splits and separates materials apart!"),
    ("🔩", "Screw",          "A ramp in a spiral — tiny turns create huge forward force!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #784212;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1b2631,#784212,#1a5276,#1b2631);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Amazing work, little engineer! You are a Simple Machines Master! ✨
    </div>
    <div style="color:#fad7a0; font-size:0.95rem;">
        Every tool you will ever use, every machine ever built — they all start with these six simple ideas!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        ⚖️ 🎡 🪝 🪜 🔪 🔩 ⚙️ 🛠️
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