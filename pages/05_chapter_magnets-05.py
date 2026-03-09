import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 05 · Marvelous Magnets", layout="wide", initial_sidebar_state="expanded")

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
    "show_attract_fact", "show_poles_fact",
    "show_types_fact",   "show_earth_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "magnet_picked"  not in st.session_state: st.session_state.magnet_picked  = None
if "animal_picked"  not in st.session_state: st.session_state.animal_picked  = None
if "magnet_step"    not in st.session_state: st.session_state.magnet_step    = 0
if "quiz_answers"   not in st.session_state: st.session_state.quiz_answers   = {}

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
<div style="background:linear-gradient(135deg,#003366,#0d47a1,#b71c1c,#003366);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#90caf9; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 05 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🧲 Marvelous Magnets! 🧲
    </h1>
    <p style="color:#bbdefb; font-size:1.05rem; margin:0.8rem 0 0;">
        Discover the invisible pulling power hiding all around you — let's explore every magnetic secret!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        🧲 🔩 📎 🌍 🧭 ⚡ 🔴🔵
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What a **magnet** is and why it is special
        - ✅ The magic powers of **attract and repel**
        - ✅ What **magnetic materials** are
        - ✅ How **north and south poles** work
        """)
    with col2:
        st.markdown("""
        - ✅ Different **types of magnets** in real life
        - ✅ How magnets are used **every single day**
        - ✅ The amazing fact that **Earth is a giant magnet**
        - ✅ Animals that use magnets + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS A MAGNET?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧲", "What Is a Magnet?",
               "A special object with an invisible superpower!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Have you ever picked up a paper clip with a magnet and felt that little invisible pull? 🤩

    A **magnet** is a special object that has an amazing invisible power called **magnetism**.
    It can **pull certain things toward it** — without even touching them!
    That invisible pull is called a **magnetic force**, and you cannot see it, but you can definitely feel it!

    Magnets have been fascinating scientists and children for thousands of years.
    The very first magnets were discovered as a special natural rock called **lodestone** —
    a rock that could pull iron pieces all by itself! 🪨✨
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#fff3e0,#fce4ec);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #e65100;">
        <div style="font-weight:700; color:#b71c1c; font-size:1.05rem; margin-bottom:0.8rem;">
            🔑 Key Magnet Words — Remember These!
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.8); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🧲</div>
                <div style="font-weight:700; color:#0d47a1;">Magnet</div>
                <div style="font-size:0.82rem; color:#666;">Special object with magnetic force</div>
            </div>
            <div style="background:rgba(255,255,255,0.8); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">⚡</div>
                <div style="font-weight:700; color:#b71c1c;">Magnetism</div>
                <div style="font-size:0.82rem; color:#666;">The invisible pulling power</div>
            </div>
            <div style="background:rgba(255,255,255,0.8); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🤗</div>
                <div style="font-weight:700; color:#2e7d32;">Attract</div>
                <div style="font-size:0.82rem; color:#666;">Pull towards — come closer!</div>
            </div>
            <div style="background:rgba(255,255,255,0.8); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">💨</div>
                <div style="font-weight:700; color:#6a1b9a;">Repel</div>
                <div style="font-size:0.82rem; color:#666;">Push away — go further!</div>
            </div>
            <div style="background:rgba(255,255,255,0.8); border-radius:10px; padding:0.6rem; text-align:center; grid-column:1/3;">
                <div style="font-size:1.8rem;">🔴🔵</div>
                <div style="font-weight:700; color:#e65100;">Poles</div>
                <div style="font-size:0.82rem; color:#666;">The two ends of a magnet — North &amp; South</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("Can you think of something in your home that uses a magnet right now? Look around! 🏠")

with col2:
    fun_card("🪨", "Lodestone — Nature's Magnet!",
             "Before anyone made magnets, people found a special rock called "
             "<strong>LODESTONE</strong> in the ground! It could attract iron "
             "all by itself — completely natural, completely magical. "
             "Ancient sailors used it to build the very first compasses! 🧭",
             bg="#fff3e0", border="#e65100")
    fun_card("📎", "The Magnetic Force is Invisible!",
             "You cannot see the magnetic force — but you can feel it! "
             "It passes right through the air, through paper, and even through "
             "your hand. Hold a paper clip under a table and move a magnet on top — "
             "the clip will follow! 🤯✨",
             bg="#e8f5e9", border="#43a047")
    fun_card("🔩", "Not ALL Metals!",
             "Here is a surprise — magnets do NOT attract all metals! "
             "Magnets love <strong>iron</strong> and <strong>steel</strong>. "
             "But gold, silver, copper, and aluminium are not magnetic at all! "
             "Try testing coins and foil at home. 🥇🥈",
             bg="#e3f2fd", border="#1565c0")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — ATTRACT AND REPEL IN DETAIL
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔬", "The Two Big Magnet Powers!",
               "Every magnet can do two amazing things — let's explore both deeply!")

# ─── ATTRACT ───────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🤗 Power 1 — ATTRACT (Pull Together!)")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Attract** means to **pull something closer**! When a magnet attracts an object,
    it gives it an invisible hug and pulls it toward itself. 🤗

    **How does attracting happen — step by step?**
    """)
    for step, icon, title, desc in [
        (1, "🧲", "Magnet has a force field",    "Every magnet is surrounded by an invisible force called a MAGNETIC FIELD — like a bubble of invisible pulling power around it!"),
        (2, "🔩", "Iron object enters the field", "When something made of iron or steel comes near, it enters the magnetic field and starts to feel the pull."),
        (3, "⚡", "Atoms line up inside",         "The tiny particles inside the iron object (called ATOMS) spin around and line up — turning the iron into a temporary magnet too!"),
        (4, "🤗", "Objects snap together",        "Now both the magnet and the iron object are attracting each other — they pull together! The closer they get, the stronger the pull."),
        (5, "📏", "Distance matters",             "The magnetic force gets WEAKER the further away you are. Move it far enough away and the pull disappears completely — like magic! 🔮"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e8f5e9;">
            <span style="background:#2e7d32; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#2e7d32;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("What objects near you right now do you think a magnet would attract? Which ones would it NOT attract? 🔩")

with col2:
    st.markdown("##### 🤗 Amazing Attract Facts")
    for icon, label, fact in [
        ("📎", "Paper clips",    "A single bar magnet can attract a chain of many paper clips — each clip becomes a temporary magnet and attracts the next one! 📎📎📎"),
        ("💪", "Strongest part", "A magnet is strongest at its TWO ENDS (called poles) and weakest in the middle. That is why you hold it at the ends to pick things up!"),
        ("🧱", "Through walls",  "Magnets can attract iron objects THROUGH non-magnetic materials — paper, plastic, glass, and even your hand! The force passes right through! 🤯"),
        ("🏗️", "Giant magnets",  "The biggest electromagnets can lift entire CARS off the ground! Junkyards use giant crane magnets to move scrapped vehicles. 🚗⬆️"),
        ("🩺", "In medicine",    "Doctors use powerful magnets in a machine called an MRI scanner to look inside your body without any cutting — amazing medical technology! 🏥"),
        ("🌊", "Maglev trains",  "Some super-fast trains use magnetic attraction and repulsion to FLOAT above their tracks — no wheels, no friction, speeds over 600 km/h! 🚄"),
    ]:
        fact_row(icon, label, fact, "#e8f5e9", "#2e7d32")

    if st.button("🤗 Reveal an Attract Secret!", use_container_width=True, key="attract_btn"):
        st.session_state.show_attract_fact = not st.session_state.show_attract_fact
    if st.session_state.show_attract_fact:
        st.success("🎉 The magnetic force passes THROUGH your hand! "
                   "Place a paper clip on top of your palm and a magnet underneath — "
                   "the magnet will pull the clip right through your hand! "
                   "The force goes through non-magnetic things as if they were invisible. 🖐️🧲")

# ─── REPEL ─────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 💨 Power 2 — REPEL (Push Away!)")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Repel** means to **push away**! This is the superpower that makes magnets push
    each other apart — without even touching! It feels like pushing against an invisible wall. 🧱

    **How does repelling happen? It is all about POLES!**
    """)
    for step, icon, title, desc in [
        (1, "🔴🔵", "Every magnet has two poles", "Every single magnet has a NORTH POLE (usually marked N or red) and a SOUTH POLE (usually marked S or blue). They are the two ends of the magnet."),
        (2, "🤝",   "Opposite poles attract",    "Put a NORTH end near a SOUTH end — they snap together! Opposites attract! This is why the letters N and S pull toward each other."),
        (3, "💨",   "Same poles repel",          "Put a NORTH end near another NORTH end — they push apart! It feels like pushing through invisible jelly! Same poles always repel."),
        (4, "🧭",   "This never changes",        "This rule ALWAYS works — every time, with every magnet, anywhere in the universe! Opposite poles attract, same poles repel. Always. ✅"),
        (5, "🌍",   "Earth has poles too!",      "Our planet Earth has a magnetic North Pole and South Pole — just like a bar magnet! That is how compasses work. 🧭"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fce4ec;">
            <span style="background:#c62828; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#c62828;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("🎮", "The Invisible Wall Experiment!",
             "Take two magnets and slowly push the same-coloured ends toward each other. "
             "Can you feel the invisible pushing force? It gets STRONGER the closer they get! "
             "Try pushing them together under water — the repulsion still works! "
             "The force travels through everything except iron and steel. 🌊🧲",
             bg="#fce4ec", border="#e53935")

with col2:
    st.markdown("##### 💨 Repelling Wonders")
    for icon, label, fact in [
        ("🚄", "Floating trains",   "Maglev trains use REPULSION between same poles to float above the track — completely frictionless, super quiet, and incredibly fast! 💨"),
        ("🎡", "Magnetic top",      "Levitating spinning tops use repulsion to float in the air — the repulsion between magnet in the base and the top keeps it hovering! 🌀"),
        ("🏥", "MRI machines",      "The powerful magnets inside MRI scanners repel each other so strongly that the machine must be very carefully engineered — or it could collapse!"),
        ("🐦", "Bird navigation",   "Migratory birds use Earth's magnetic field to navigate — their brains can actually SENSE the direction of Earth's magnetic poles! 🌍"),
        ("🔋", "Electric motors",   "Every electric motor — in fans, cars, and washing machines — uses attract and repel forces between magnets to spin and create movement! 🔄"),
        ("😆", "Same-pole prank",   "If you ever push two same-pole magnets together in your hands, they will slide sideways to flip and attract — they really hate being same-pole to same-pole! 😄"),
    ]:
        fact_row(icon, label, fact, "#fce4ec", "#c62828")

    if st.button("💨 Tap for a Repel Surprise!", use_container_width=True, key="poles_btn"):
        st.session_state.show_poles_fact = not st.session_state.show_poles_fact
    if st.session_state.show_poles_fact:
        st.success("🎉 It is IMPOSSIBLE to have a magnet with only ONE pole! "
                   "If you cut a bar magnet in half, you do not get a North piece and a South piece — "
                   "each half grows its OWN new North and South pole immediately! "
                   "Cut it again — same thing! Scientists have never been able to separate them. 🤯🧲")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — MAGNETIC MATERIALS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔍", "Magnetic Materials — What Does a Magnet Love?",
               "Discover which materials magnets pull — and which ones they totally ignore! 🤷")

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Not everything in the world is attracted to magnets! Only certain materials are **magnetic**.
    The key is whether the material contains **iron, nickel, or cobalt** inside it.
    These three metals are the only ones that respond to magnetic forces. 🔩

    **Let's sort things into MAGNETIC and NON-MAGNETIC:**
    """)

    mag_yes = [
        ("🔩", "Iron nails",       "Iron is the most common magnetic material — nails, screws, and bolts are usually magnetic!"),
        ("📎", "Steel paper clips","Steel is mostly iron, so paper clips and staples are strongly magnetic."),
        ("🔧", "Steel tools",      "Spanners, scissors, and most kitchen knives are made of steel — magnetic!"),
        ("🥫", "Tin cans",         "Many food cans are made of steel with a thin tin coating — mostly magnetic! 🧃"),
        ("🔑", "Some keys",        "Iron or steel keys are magnetic. Try testing your house keys! 🏠"),
    ]
    mag_no = [
        ("🪵", "Wood",     "Wood has no iron atoms — a magnet slides right off! 🌳"),
        ("🧴", "Plastic",  "All plastics are completely non-magnetic — bottles, rulers, toys. 🧸"),
        ("🪟", "Glass",    "Glass contains no iron — windows, jars, and glasses ignore magnets completely."),
        ("🥄", "Aluminium","Aluminium cans and foil are NOT magnetic — even though they are metals! 🥤"),
        ("💍", "Gold & Silver", "These precious metals have no iron — they will not stick to a magnet! 💛"),
        ("🧻", "Paper",    "Paper is made from wood fibres — completely non-magnetic! 📄"),
    ]

    mc1, mc2 = st.columns(2)
    with mc1:
        st.markdown("""<div style="background:#e8f5e9; border-radius:12px;
                    padding:0.6rem 1rem; margin-bottom:0.5rem; border-top:4px solid #2e7d32;">
                    <strong style="color:#2e7d32;">✅ MAGNETIC — Magnets Love These!</strong></div>""",
                    unsafe_allow_html=True)
        for icon, name, desc in mag_yes:
            st.markdown(f"""
            <div style="background:#f1f8f1; border-radius:10px; padding:0.5rem 0.8rem;
                        margin-bottom:0.35rem; border-left:3px solid #66bb6a;">
                <span style="font-size:1.2rem;">{icon}</span>
                <strong style="color:#2e7d32;"> {name}</strong>
                <div style="font-size:0.84rem; color:#555; margin-top:0.15rem;">{desc}</div>
            </div>""", unsafe_allow_html=True)
    with mc2:
        st.markdown("""<div style="background:#fce4ec; border-radius:12px;
                    padding:0.6rem 1rem; margin-bottom:0.5rem; border-top:4px solid #c62828;">
                    <strong style="color:#c62828;">❌ NON-MAGNETIC — Magnets Ignore These!</strong></div>""",
                    unsafe_allow_html=True)
        for icon, name, desc in mag_no:
            st.markdown(f"""
            <div style="background:#fdf5f5; border-radius:10px; padding:0.5rem 0.8rem;
                        margin-bottom:0.35rem; border-left:3px solid #ef9a9a;">
                <span style="font-size:1.2rem;">{icon}</span>
                <strong style="color:#c62828;"> {name}</strong>
                <div style="font-size:0.84rem; color:#555; margin-top:0.15rem;">{desc}</div>
            </div>""", unsafe_allow_html=True)

    think_bubble("Find 5 objects near you and predict: MAGNETIC or NOT? Then test with a magnet! Were you right? 🎯")

with col2:
    fun_card("🧪", "The Sorting Test!",
             "Scientists do a simple <strong>magnetic sorting test</strong> — "
             "they move a magnet near the object. If it moves or sticks, it contains iron, "
             "nickel, or cobalt. If nothing happens, it is non-magnetic. "
             "You can do this exact test at home right now! 🏠🔬",
             bg="#e8f5e9", border="#43a047")
    fun_card("🥤", "The Drinks Can Trick!",
             "Try a magnet on a steel food tin and it will STICK! "
             "Then try it on an aluminium drinks can and it will NOT! "
             "Both are silver-coloured metals, but only one contains iron. "
             "This is how recycling centres sort cans automatically! ♻️",
             bg="#e3f2fd", border="#1565c0")
    fun_card("💎", "Iron in Your Blood!",
             "Some things are weakly magnetic — like certain stainless steels. "
             "Incredibly, <strong>your blood</strong> contains iron too — "
             "that is what gives blood its red colour and carries oxygen around your body. 🩸",
             bg="#fff3e0", border="#e65100")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — TYPES OF MAGNETS EXPLORER
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🏭", "Types of Magnets — An Explorer!",
               "Magnets come in all shapes and strengths — step through each type! 🧲")

magnet_types = [
    ("🏠", "Permanent Magnet",
     "A permanent magnet keeps its magnetism <strong>forever</strong> — it never loses its power on its own! "
     "These are the magnets you find on your fridge, inside compasses, and in toy magnets. "
     "They are usually made from very strong magnetic materials like neodymium (the strongest!) "
     "or regular iron and steel. The magnets in your classroom are almost certainly permanent magnets. "
     "Fun fact: a neodymium magnet the size of a coin can lift 10 kg! 💪",
     "#e8f5e9", "#2e7d32"),
    ("⚡", "Electromagnet",
     "An <strong>electromagnet</strong> only becomes a magnet when <strong>electricity flows through it</strong>! "
     "Wrap copper wire around an iron nail, connect it to a battery, and it becomes a magnet. "
     "Disconnect the battery and it stops immediately! "
     "Electromagnets can be switched on and off, which makes them incredibly useful — "
     "from doorbells and speakers to hospital MRI scanners and giant junkyard cranes. "
     "The more coils of wire, the stronger the magnet! 🔋🔌",
     "#e3f2fd", "#1565c0"),
    ("🐴", "Horseshoe Magnet",
     "A <strong>horseshoe magnet</strong> is shaped like the letter U — just like a horseshoe! 🐎 "
     "By bending the magnet into this shape, both poles face the SAME direction — "
     "which makes it much easier to pick things up because both poles work together. "
     "Horseshoe magnets are great for classroom experiments! "
     "They are also used in generators that make electricity. "
     "You might see them in cartoons — the classic red and silver U-shaped magnet! 🎨",
     "#fff3e0", "#e65100"),
    ("📊", "Bar Magnet",
     "The <strong>bar magnet</strong> is the most common shape — a simple rectangle or rod! "
     "One end is the North Pole and the other is the South Pole. "
     "Bar magnets are brilliant for science experiments because you can clearly see both poles. "
     "They are used inside compasses (a very small bar magnet floats on water to point North!), "
     "and inside the motors of many machines. "
     "The red end is usually North, and the blue end is usually South. 🔴🔵",
     "#f3e5f5", "#7b1fa2"),
    ("🪙", "Disc and Ring Magnets",
     "Magnets do not have to be long! <strong>Disc magnets</strong> are flat and round — like a coin, "
     "and <strong>ring magnets</strong> have a hole in the middle like a doughnut! 🍩 "
     "Disc magnets are used in speakers inside your phone and TV — they make the sound! "
     "Ring magnets are used in science toys — stack several on a pencil with the same poles facing "
     "and they will float apart, levitating above each other by repulsion! "
     "This is a great way to see repulsion in action! ✨",
     "#fce4ec", "#c62828"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Previous", use_container_width=True, key="mag_prev"):
        st.session_state.magnet_step = max(0, st.session_state.magnet_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="mag_next"):
        st.session_state.magnet_step = min(len(magnet_types)-1, st.session_state.magnet_step + 1)

idx   = st.session_state.magnet_step
mstep = magnet_types[idx]
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
                for i in range(len(magnet_types))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Magnet Type {idx+1} of {len(magnet_types)}
        </div>
    </div>""", unsafe_allow_html=True)

if st.button("🤫 Reveal a Magnet Types Secret!", use_container_width=False, key="types_btn"):
    st.session_state.show_types_fact = not st.session_state.show_types_fact
if st.session_state.show_types_fact:
    st.success("🎉 The world's strongest permanent magnets are called NEODYMIUM magnets — "
               "made from a mix of neodymium, iron, and boron! "
               "A neodymium magnet just 5cm wide can hold up more than 100 kg — "
               "that is the weight of a grown-up adult! 😱 "
               "They are used in headphones, hard drives, and electric car motors. 🚗⚡")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — MAGNETS IN EVERYDAY LIFE
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🏠", "Magnets Are Everywhere Around You!",
               "Tap each place to discover all the hidden magnets in daily life! 🔍")

everyday_magnets = {
    "🏠 At Home": {
        "emoji": "🏠", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "🧲 Magnets hiding in your house!",
        "body": (
            "Your home is FULL of hidden magnets! 🤯\n\n"
            "- 🧲 **Fridge magnets**: The fun decorations that hold notes — but also the rubber seal around the fridge door that keeps cold air in uses a magnetic strip!\n"
            "- 📢 **Speakers**: Every speaker in your TV, radio, and phone has a magnet inside that makes the sound vibrate. Music literally comes from magnets! 🎵\n"
            "- 🚪 **Cabinet doors**: Many cupboard doors close with a small magnetic latch instead of a spring — listen for the click!\n"
            "- 💻 **Laptop lid**: Many laptop lids use magnets to sense when they are closed and switch off the screen automatically.\n"
            "- 🔔 **Doorbell**: Your doorbell uses an electromagnet that buzzes when you press the button — the electricity makes the magnet vibrate and create sound! 🎶"
        )
    },
    "🏥 Medicine": {
        "emoji": "🏥", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🧲 Magnets that save lives!",
        "body": (
            "Magnets are absolutely essential in hospitals — they help doctors see inside bodies! 🩺\n\n"
            "- 🔬 **MRI Scanner**: A huge magnetic tube takes detailed pictures of the inside of your body — brain, heart, bones — without any surgery!\n"
            "- 💊 **Magnet pills**: Scientists have invented tiny magnetic capsules that doctors can guide through your body using external magnets to deliver medicine exactly where it is needed!\n"
            "- 🦾 **Prosthetic limbs**: Some artificial hands and arms attach to the body using powerful magnetic connections — making them easy to put on and take off.\n"
            "- 🧲 **Removing metal**: If a tiny metal fragment gets inside someone's eye, surgeons use a magnet to carefully pull it out safely! 👁️\n"
            "- 🧠 **Brain treatment**: TMS uses magnets near the skull to treat certain brain conditions — magnets truly heal! 💚"
        )
    },
    "🚂 Transport": {
        "emoji": "🚂", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🧲 Magnets that move you!",
        "body": (
            "Magnets help us travel faster and further than ever before! 🌍\n\n"
            "- 🚄 **Maglev trains**: Magnetic Levitation trains FLOAT above their tracks using repulsion and are propelled forward using attraction — no wheels, no friction, no noise! The fastest reach over 600 km/h!\n"
            "- ⚡ **Electric motors**: Every electric vehicle — cars, buses, scooters — uses electromagnetic motors to convert electrical energy into spinning movement.\n"
            "- 🧭 **Ship navigation**: Giant cargo ships still use magnetic compasses as a backup navigation system — a technology invented over 1,000 years ago!\n"
            "- ✈️ **Aeroplane instruments**: Aircraft rely on magnetic compasses and instruments to stay on course, especially when GPS is unavailable.\n"
            "- 🚗 **Car speedometer**: The needle in an old-fashioned speedometer is moved by a rotating magnet — the faster the car goes, the more the magnet pulls the needle! 🔄"
        )
    },
    "💻 Technology": {
        "emoji": "💻", "color": "#6a1b9a", "bg": "#f3e5f5",
        "tagline": "🧲 Magnets inside your gadgets!",
        "body": (
            "Almost every piece of technology you use is powered by magnets! 🤖\n\n"
            "- 💾 **Hard drives**: Computers store information by magnetising tiny spots on a spinning disc — billions of microscopic magnets storing all your photos and videos!\n"
            "- 🎧 **Headphones**: The sound in your headphones is made by a tiny magnet vibrating against a coil to push air and create sound waves! 🎵\n"
            "- 📱 **Phone speaker**: The same magnet-coil system makes your phone ring, play music, and let you hear voices in calls.\n"
            "- 🖥️ **Computer fans**: The spinning fans inside computers use electromagnetic motors to cool the circuits — tiny magnets spinning hundreds of times per second!\n"
            "- 🔋 **Wireless charging**: New wireless charging pads use magnetic induction — passing energy through the air using a changing magnetic field — no cable needed! 🌀"
        )
    },
    "🏫 At School": {
        "emoji": "🏫", "color": "#c62828", "bg": "#fce4ec",
        "tagline": "🧲 Magnets you use every day!",
        "body": (
            "You are surrounded by magnets at school too! 📚\n\n"
            "- 🖥️ **Interactive whiteboard**: The stylus pen on a smartboard often uses magnetic technology to detect its position on the screen with perfect accuracy.\n"
            "- 📌 **Magnetic whiteboard**: That white board in class? Many are magnetic — you can stick magnetic letters and numbers directly on them!\n"
            "- 🎒 **Bag clasps**: Many school bag closures use magnetic snaps — press them together and click! They use attract force.\n"
            "- ✏️ **Pencil cases**: Some pencil cases have magnetic closures instead of zips — open and close thousands of times without ever wearing out!\n"
            "- 🔬 **Science kit magnets**: The bar magnets and horseshoe magnets in your science kit are permanent magnets — you might use them today! 🧲"
        )
    },
    "🌍 In Nature": {
        "emoji": "🌍", "color": "#00695c", "bg": "#e0f2f1",
        "tagline": "🧲 Magnets in the natural world!",
        "body": (
            "Magnetism is not just invented by humans — nature uses it too! 🌿\n\n"
            "- 🧭 **Earth's magnetic field**: Our entire planet acts like a giant bar magnet! The core of Earth contains molten iron that creates a massive magnetic field around the whole planet.\n"
            "- 🐦 **Migrating birds**: Robins, swallows, and geese have tiny crystals of magnetite in their brains that act like a built-in compass — they navigate by feeling Earth's magnetic field! 🌏\n"
            "- 🐝 **Honeybees**: Bees also contain magnetite and use Earth's field to navigate back to their hive from miles away — every single time! 🍯\n"
            "- 🐠 **Fish navigation**: Salmon migrate thousands of kilometres back to the exact river where they were born — guided partly by the planet's magnetic field! 🌊\n"
            "- 🪨 **Lodestone**: Magnetite rocks called lodestones are found in the ground all over the world — completely natural permanent magnets made by the Earth itself! ✨"
        )
    },
}

sense_cols = st.columns(len(everyday_magnets))
for i, (aname, adata) in enumerate(everyday_magnets.items()):
    with sense_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"elife_{i}"):
            st.session_state.magnet_picked = aname

if st.session_state.magnet_picked and st.session_state.magnet_picked in everyday_magnets:
    aname = st.session_state.magnet_picked
    adata = everyday_magnets[aname]
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
    st.info("👆 Tap any category above to discover its hidden magnets!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — THE EARTH IS A GIANT MAGNET
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌍", "The Earth is a Giant Magnet!",
               "The most mind-blowing magnet fact of all — our whole planet is magnetic! 🤯")

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Here is the most incredible magnet fact of all — the planet you are standing on right now
    is **one enormous, spectacular magnet!** 🌍🧲

    **How is Earth a magnet?**
    """)
    for step, icon, title, desc in [
        (1, "🔥", "Hot liquid core",        "Deep at the centre of Earth — about 6,000 km down — there is a core of extremely hot LIQUID IRON swirling around slowly. This is Earth's engine!"),
        (2, "🌀", "Spinning creates field",  "As this liquid iron spins and flows, it creates electrical currents — and electrical currents always create MAGNETIC FIELDS! This is Earth's natural electromagnet."),
        (3, "🌐", "Field wraps the Earth",   "This magnetic field stretches out into space, wrapping all around our planet like a giant invisible bubble thousands of kilometres thick!"),
        (4, "🛡️", "Shields us from danger",  "Earth's magnetic field is our SUPERPOWER SHIELD — it deflects dangerous radiation and charged particles from the Sun (called solar wind) that would destroy life on Earth! ☀️"),
        (5, "🧭", "Creates compass North",   "The field creates a magnetic North and South Pole. Every compass needle is a tiny bar magnet that aligns itself with Earth's field and points North — it has worked for 1,000 years! 🧭"),
        (6, "🌌", "Aurora Borealis!",        "When some of the Sun's particles sneak through near the poles, they collide with air molecules and create the spectacular light show called the NORTHERN LIGHTS! 💚💜✨"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e0f2f1;">
            <span style="background:#00695c; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#00695c;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("If Earth lost its magnetic field, what do you think might happen to animals that use it to navigate — like birds and bees? 🐝🐦")

with col2:
    fun_card("🧭", "The Compass — 1,000 Years Old!",
             "The compass was invented in <strong>ancient China</strong> about 1,000 years ago! "
             "It is simply a tiny bar magnet balanced so it can spin freely — "
             "it always points toward Earth's magnetic North Pole. "
             "Sailors used compasses to cross oceans and find their way home. "
             "The same principle works to this day! 🌊⛵",
             bg="#e0f2f1", border="#00695c")
    fun_card("🌌", "The Northern Lights",
             "The <strong>Aurora Borealis</strong> (Northern Lights) is one of the most beautiful "
             "natural shows on Earth — stunning curtains of green, pink, and purple light "
             "dancing in the night sky. They happen when the Sun's particles "
             "follow Earth's magnetic field lines into the atmosphere near the poles. 💚💜",
             bg="#e8eaf6", border="#3949ab")
    fun_card("⚠️", "Magnetic Storms!",
             "Sometimes the Sun sends out an especially powerful burst of energy called "
             "a <strong>solar flare</strong>. This can disturb Earth's magnetic field and "
             "cause problems with satellites, radio signals, and even electricity grids on the ground! "
             "Earth's magnet is incredibly important for modern life. 📡",
             bg="#fff3e0", border="#e65100")

    if st.button("🌍 Reveal an Earth Magnet Secret!", use_container_width=True, key="earth_btn"):
        st.session_state.show_earth_fact = not st.session_state.show_earth_fact
    if st.session_state.show_earth_fact:
        st.success("🎉 Earth's magnetic poles are NOT in the same place as the geographic North and South Poles! "
                   "The MAGNETIC North Pole is actually located in northern Canada — not at the top of the globe! "
                   "And it moves about 50 km every single year as the liquid iron core shifts. "
                   "Scientists update all maps and navigation systems regularly to track it! 🗺️")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — ANIMALS WITH MAGNETIC SUPERPOWERS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Animals With Magnetic Superpowers!",
               "Some creatures can actually FEEL Earth's magnetic field — tap to explore! 🌍")

animal_magnets = {
    "🐦 Robin": {
        "emoji": "🐦", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "🏆 Magnetic Compass in the Eye!",
        "body": (
            "Tiny robins and migratory birds navigate thousands of kilometres using Earth's magnetic field! 🧭\n\n"
            "- 🔬 **Magnetite crystals**: Birds have tiny crystals of a magnetic mineral called magnetite in their beaks and brains — like a built-in compass!\n"
            "- 👁️ **Quantum compass**: Scientists believe robins may also see Earth's magnetic field through special molecules in their eyes — the field appears as patterns of light in their vision! 🌈\n"
            "- ✈️ **Epic journeys**: A tiny Arctic Tern migrates from the Arctic to the Antarctic and back every year — over 70,000 km — guided entirely by magnetism and stars!\n"
            "- 🌙 **Night flying**: Many birds migrate at night when skies are clearer — their magnetic sense works 24 hours a day, unlike vision.\n"
            "- 🐣 **Never gets lost**: Even young birds flying alone for the first time can find their destination — the magnetic map is built into their biology at birth!"
        )
    },
    "🐢 Sea Turtle": {
        "emoji": "🐢", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🏆 Ocean GPS Navigation!",
        "body": (
            "Sea turtles make one of the most incredible journeys in nature — guided entirely by Earth's magnetic field! 🌊\n\n"
            "- 🌍 **Magnetic address**: Each location in the ocean has a unique combination of magnetic field strength and angle — sea turtles memorise the magnetic address of their birth beach!\n"
            "- 🏖️ **Return journey**: After spending 20-30 years crossing the entire Atlantic Ocean, a female sea turtle navigates back to the exact beach where she was born to lay her own eggs!\n"
            "- 📍 **GPS precision**: The accuracy is remarkable — turtles find beaches within metres of where they hatched, using magnetic signatures as precise as GPS coordinates.\n"
            "- 🐣 **Hatchlings**: Baby turtles imprint their birth beach's magnetic signature the moment they hatch and enter the sea — they remember it for their entire 80-year life!\n"
            "- 🔬 **How it works**: Tiny magnetic crystals in the turtles' heads detect subtle differences in Earth's field strength and inclination angle. 🧲"
        )
    },
    "🐝 Honeybee": {
        "emoji": "🐝", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "🏆 Magnetic Hive Finder!",
        "body": (
            "Honeybees can navigate miles away from their hive and find their way back perfectly — using magnetism! 🍯\n\n"
            "- 🧲 **Magnetic crystals**: Bees have magnetite crystals in their abdomens — this helps them detect Earth's magnetic field with amazing precision.\n"
            "- 🏗️ **Hive building**: Bees orient the wax combs inside their hive in alignment with Earth's magnetic field — always at a consistent angle. Remove the queen and replace her — the new queen builds at the same magnetic angle! 🤯\n"
            "- 🌸 **Flower finding**: Bees use the magnetic field as one of several navigation tools — combined with the Sun's position, landmarks, and memory — to create 3D maps of the area.\n"
            "- 💃 **Waggle dance**: The famous waggle dance that bees use to tell each other where flowers are uses magnetic north as a reference direction! 🕺\n"
            "- 🛰️ **Better than GPS**: Scientists believe bees combine up to SIX different navigation systems — a feat of biology that human engineers are still trying to match! 🚀"
        )
    },
    "🦈 Hammerhead": {
        "emoji": "🦈", "color": "#c62828", "bg": "#fce4ec",
        "tagline": "🏆 Electrical + Magnetic Superpower!",
        "body": (
            "Sharks have an extraordinary magnetic sense — plus the ability to detect electricity — making them the ultimate hunters! ⚡\n\n"
            "- 🔌 **Ampullae of Lorenzini**: Sharks have hundreds of tiny gel-filled pores around their snout that detect electrical fields as weak as one billionth of a volt!\n"
            "- 🏖️ **Buried prey**: Sharks can find fish buried under sand — they detect the fish's heartbeat as a tiny electrical signal. No hiding from a shark! 💓\n"
            "- 🌍 **Ocean navigation**: Hammerhead sharks navigate across open oceans using Earth's magnetic field — their wide, hammer-shaped head increases the surface area for magnetic detection! The hammer shape is for navigation! 🤯\n"
            "- 🗺️ **Magnetic map**: Sharks build detailed magnetic maps of the ocean floor — identifying locations by unique magnetic signatures, returning to exact feeding grounds year after year.\n"
            "- 🧭 **Built-in compass**: Young sharks raised entirely in captivity can orient themselves correctly with Earth's poles even without ever experiencing the ocean — it's biological! 🌊"
        )
    },
    "🐟 Salmon": {
        "emoji": "🐟", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🏆 Magnetic River Finder!",
        "body": (
            "Atlantic and Pacific Salmon complete one of the most dramatic magnetic journeys in all of nature! 🌊\n\n"
            "- 🐣 **Magnetic imprinting**: The moment a young salmon hatches, it records the exact magnetic signature of its birth river in its brain — like saving a GPS coordinate!\n"
            "- 🌊 **Ocean wandering**: Salmon spend 2-7 years travelling thousands of kilometres across entire oceans, feeding and growing — never returning to rivers during this time.\n"
            "- 🏠 **The return**: When ready to spawn, something incredible happens — the salmon turns toward home, following Earth's magnetic field across the featureless ocean to find the right coast.\n"
            "- 🏞️ **River precision**: Once near the coast, they switch from magnetic navigation to smell — following the exact chemical signature of their birth river upstream, sometimes jumping 3-metre waterfalls! 💪\n"
            "- 🔄 **Generation to generation**: The salmon that survive lay eggs and die in the same spot — their babies imprint the same magnetic address and the cycle begins again! 🌱"
        )
    },
    "🦋 Monarch": {
        "emoji": "🦋", "color": "#7b1fa2", "bg": "#f3e5f5",
        "tagline": "🏆 Multi-Tool Magnetic Navigator!",
        "body": (
            "Monarch butterflies weigh less than a paperclip — yet they navigate 4,000 km across a continent! 🤯\n\n"
            "- 🌞 **Sun compass**: Monarchs primarily navigate using the Sun's position — with a built-in clock that corrects for the Sun's movement across the sky throughout the day!\n"
            "- 🧲 **Magnetic backup**: When the sky is cloudy and they cannot see the Sun, monarchs switch to their magnetic sense — they have magnetite in their antenna to feel Earth's field!\n"
            "- 🌲 **Winter home**: Every autumn, millions of Monarchs fly from Canada to a specific mountain forest in Mexico — landing on the same trees used by their great-great-grandparents!\n"
            "- 🗺️ **No GPS needed**: They have never made this journey before — no parents guide them. The entire route is encoded in their tiny brain at birth! 🧠\n"
            "- 🌡️ **Temperature sensors**: Monarchs also use temperature and wind patterns to navigate — combining at least FOUR navigation systems in a brain smaller than a pinhead! 📍"
        )
    },
}

animal_cols = st.columns(len(animal_magnets))
for i, (aname, adata) in enumerate(animal_magnets.items()):
    with animal_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"anim_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in animal_magnets:
    aname = st.session_state.animal_picked
    adata = animal_magnets[aname]
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
    st.info("👆 Tap any animal above to discover its magnetic superpower!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — LOOKING AFTER YOUR MAGNETS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Looking After Your Magnets!",
               "Magnets are wonderful — here is how to keep them strong! 🌟")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("🛡️", "Keep Them Away From Heat",
     "HEAT is a magnet's worst enemy! If you heat a magnet above a certain temperature, "
     "the atoms inside get so excited they lose their alignment — and the magnetism disappears FOREVER. "
     "Never put a magnet near a fire, oven, or radiator! 🔥",
     "#fce4ec", "#c62828"),
    ("💻", "Keep Away From Electronics",
     "Strong magnets can damage credit cards, computer hard drives, and old-fashioned TV screens. "
     "The magnetic field scrambles the stored information. Keep magnets away from phones, "
     "computers, bank cards, and tablets! 💳📱",
     "#e3f2fd", "#1565c0"),
    ("📦", "Store Them Correctly",
     "Store bar magnets in opposite pairs (North to South) so they hold each other. "
     "This actually helps them stay strong! Store horseshoe magnets with a small iron bar "
     "across the poles — called a keeper. It closes the magnetic circuit and prevents weakening. 🔩",
     "#e8f5e9", "#2e7d32"),
    ("🏃", "Avoid Dropping Them",
     "DROPPING a magnet hard can scramble the atoms inside and weaken it! "
     "The shock disrupts the carefully organised magnetic atoms. "
     "Treat your magnets gently — especially ceramic ones which can also crack and break! 🤕",
     "#fff3e0", "#e65100"),
    ("🔬", "Never Force Same Poles",
     "Trying to force the same poles of two strong magnets together can temporarily weaken "
     "both magnets through the vibration and stress. If two magnets need to be near each other, "
     "keep them in a tray or box so they do not crash together. 💥",
     "#f3e5f5", "#8e24aa"),
    ("🧹", "Keep Them Clean",
     "Magnets pick up tiny iron filings and dust that can cling to their surface! "
     "This does not harm the magnet but can scratch surfaces. "
     "Clean magnets gently with a soft cloth. Keep them in a pouch when not in use. 🧺",
     "#e0f2f1", "#00695c"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Can you think of a job that uses magnets every day? What would that job be like? 🤔")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Magnet Quiz — Let's Test What You Know!",
               "6 magnetic questions — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 🧲 — What do we call the invisible pulling power of a magnet?",
        "opts": ["Electricity", "Gravity", "Magnetism", "Friction"],
        "ans":  "Magnetism",
        "explain": "MAGNETISM is the special invisible force that magnets have! It can pull iron and steel objects toward them. 🧲✨"
    },
    {
        "q":    "Q2 💨 — What happens when you put the SAME poles of two magnets together?",
        "opts": ["They attract and snap together", "They repel and push apart", "They spin around", "Nothing happens"],
        "ans":  "They repel and push apart",
        "explain": "SAME poles always REPEL — they push each other away! It feels like pushing against an invisible wall. North+North = push apart! 💨"
    },
    {
        "q":    "Q3 🔩 — Which of these materials would a magnet be able to pick up?",
        "opts": ["A wooden pencil 🪵", "A plastic bottle 🧴", "A steel paper clip 📎", "A gold ring 💍"],
        "ans":  "A steel paper clip 📎",
        "explain": "Steel contains iron, so magnets LOVE paper clips! Wood, plastic, and gold contain no iron — magnets completely ignore them. ✅"
    },
    {
        "q":    "Q4 🌍 — Why does a compass needle always point North?",
        "opts": ["Because it is painted red", "Because Earth is a giant magnet", "Because of the wind", "Because of gravity"],
        "ans":  "Because Earth is a giant magnet",
        "explain": "Earth's liquid iron core creates a massive magnetic field around our planet — making Earth one enormous magnet! The compass needle aligns with this field. 🌍🧭"
    },
    {
        "q":    "Q5 ⚡ — What type of magnet only works when electricity flows through it?",
        "opts": ["Permanent magnet", "Horseshoe magnet", "Electromagnet", "Bar magnet"],
        "ans":  "Electromagnet",
        "explain": "An ELECTROMAGNET is created by passing electricity through a coil of wire around iron — turn off the electricity and the magnetism disappears! 🔋⚡"
    },
    {
        "q":    "Q6 🐦 — Which animal uses Earth's magnetic field to navigate during migration?",
        "opts": ["A goldfish 🐠", "A house cat 🐱", "A migratory bird 🐦", "A garden snail 🐌"],
        "ans":  "A migratory bird 🐦",
        "explain": "Migratory birds have tiny magnetite crystals in their brains that work like a built-in compass — they can FEEL Earth's magnetic field and follow it thousands of kilometres! 🤯"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"mag_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="mag_quiz_submit"):
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
        (6, "🏆", "MAGNET MASTER! 🧲",                "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Magnet Scientist! ⚡",    "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Magnetic Explorer! 🔩",       "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Magnet Detective! 🔍",    "#7b1fa2", "#f3e5f5"),
        (0, "✨", "Keep Exploring — You Can Do It! 💪","#1565c0", "#e3f2fd"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="mag_quiz_reset"):
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
               "Marvelous Magnets — your quick recap! 🎉")

summary_items = [
    ("🧲", "Magnets",   "Special objects with invisible magnetic force — called magnetism!"),
    ("🤗", "Attract",   "Pull iron and steel objects closer — opposite poles attract!"),
    ("💨", "Repel",     "Push same poles away — same poles always repel!"),
    ("🔩", "Materials", "Only iron, steel, nickel and cobalt are magnetic!"),
    ("⚡", "Types",     "Permanent, electromagnet, horseshoe, bar, disc and ring!"),
    ("🌍", "Earth",     "Our whole planet is a giant magnet — with North and South poles!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #0d47a1;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#003366,#0d47a1,#b71c1c,#003366);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Amazing work, little scientist! You are a Magnet Master! ✨
    </div>
    <div style="color:#bbdefb; font-size:0.95rem;">
        Magnets are all around you — in your fridge, your speakers, the Earth beneath your feet, and the birds in the sky!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        🧲 🔩 📎 🌍 🧭 ⚡ 🔴🔵
    </div>
    <div style="margin-top:0.8rem; color:#90caf9; font-size:0.85rem;">
        Science for Little Stars · Chapter 05 of 10
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


