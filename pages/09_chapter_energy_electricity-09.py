import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 09 · Energy and Electricity", layout="wide", initial_sidebar_state="expanded")

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
    "show_sun_fact", "show_electric_fact",
    "show_circuit_fact", "show_renewable_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "energy_picked"  not in st.session_state: st.session_state.energy_picked  = None
if "animal_picked"  not in st.session_state: st.session_state.animal_picked  = None
if "energy_step"    not in st.session_state: st.session_state.energy_step    = 0
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
<div style="background:linear-gradient(135deg,#1a2a00,#f57f17,#e65100,#1a2a00);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#ffe082; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 09 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🔋 Energy and Electricity! ⚡
    </h1>
    <p style="color:#fff9c4; font-size:1.05rem; margin:0.8rem 0 0;">
        Energy makes every single thing in the universe happen —
        from the tiniest cell to the most powerful star!
        Let's discover where it comes from and how it powers your world!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        ☀️ ⚡ 🔋 💡 🌊 💨 🔥 ⚛️
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What **energy** is and why everything needs it
        - ✅ The many different **types of energy** around us
        - ✅ How the **Sun** powers almost all life on Earth
        - ✅ How **electricity** is made and how it flows
        """)
    with col2:
        st.markdown("""
        - ✅ How an **electric circuit** works
        - ✅ The difference between **renewable and non-renewable** energy
        - ✅ How **lightning** forms in thunderclouds
        - ✅ Animals that use electricity + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS ENERGY?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Is Energy?",
               "The invisible force behind absolutely everything that moves, grows, glows, or changes! ✨")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Right now, energy is doing something remarkable — it is powering the screen you are reading,
    the light in the room, your beating heart, and the thoughts in your brain — **all at once!** 🤩

    **Energy** is the ability to make something **happen** — to move things, heat things,
    light things up, or change them. Without energy, absolutely nothing in the universe
    would ever happen. Not a single thing. ✋

    The most important law in all of physics is this: **energy is never created and never destroyed —
    it only changes from one form to another!** A lump of coal burns and becomes heat and light.
    Heat boils water into steam. Steam spins a turbine. The turbine makes electricity.
    Electricity flows to your home and becomes light in a bulb. 💡
    Every step is just energy changing shape! 🔄
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #e65100;">
        <div style="font-weight:700; color:#e65100; font-size:1.05rem; margin-bottom:0.8rem;">
            ⚡ The Main Types of Energy — Know Them All!
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">☀️</div>
                <div style="font-weight:700; color:#f57f17;">Light</div>
                <div style="font-size:0.8rem; color:#666;">From the Sun, fires, light bulbs</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🔥</div>
                <div style="font-weight:700; color="#c62828;">Heat</div>
                <div style="font-size:0.8rem; color:#666;">From burning, friction, the Sun</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">⚡</div>
                <div style="font-weight:700; color:#1565c0;">Electrical</div>
                <div style="font-size:0.8rem; color:#666;">Powers your home and devices</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🏃</div>
                <div style="font-weight:700; color:#2e7d32;">Kinetic</div>
                <div style="font-size:0.8rem; color:#666;">Energy of movement</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🪨</div>
                <div style="font-weight:700; color:#6d4c41;">Potential</div>
                <div style="font-size:0.8rem; color:#666;">Stored, ready to be released</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🎵</div>
                <div style="font-weight:700; color:#7b1fa2;">Sound</div>
                <div style="font-size:0.8rem; color:#666;">Vibrations travelling through air</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("Look around the room — how many different forms of energy can you spot right now? Hint: light, heat, movement, sound… 🔍⚡")

with col2:
    fun_card("🔄", "Energy Never Disappears!",
             "Energy cannot be created from nothing — and it can never be destroyed. "
             "It only <strong>transforms</strong> from one type to another! "
             "This is called the Law of Conservation of Energy — "
             "one of the most important rules in all of science. "
             "Every energy transformation you see is just energy changing clothes! 👕🔋",
             bg="#fff8e1", border="#f57f17")
    fun_card("🍎", "Food Energy — Fuel for YOU!",
             "The food you eat is stored chemical energy! "
             "Your body breaks food down and releases that energy — "
             "to move your muscles (kinetic), keep you warm (heat), "
             "power your brain (electrical signals), and build new cells (chemical). "
             "A chocolate bar has enough energy to power a light bulb for 1.5 hours! 💡🍫",
             bg="#e8f5e9", border="#2e7d32")
    fun_card("⚛️", "The Biggest Energy Source of All",
             "Inside the Sun, hydrogen atoms <strong>fuse together</strong> to make helium — "
             "releasing <strong>380 trillion trillion watts</strong> of energy every second! "
             "Just one second of the Sun's energy would power all of human civilisation "
             "for 500,000 years. The Sun has been doing this for 4.6 billion years — "
             "and has enough hydrogen for 5 billion more! ☀️🌍",
             bg="#fce4ec", border="#c62828")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE SUN: EARTH'S ENERGY SOURCE
# ═══════════════════════════════════════════════════════════════════════════════
section_header("☀️", "The Sun — Earth's Gigantic Power Station!",
               "Almost every drop of energy on Earth originally came from our nearest star! 🌍")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Trace any source of energy on Earth back far enough —
    and you will almost always end up at the **Sun**! ☀️

    Coal, oil, and gas? They are the compressed remains of ancient plants and animals
    that stored the Sun's energy millions of years ago. Wind? The Sun heats air unevenly,
    causing wind. Rain and rivers? The Sun evaporates water, creating the water cycle.
    Food? Plants use sunlight to grow, and we eat plants (or animals that ate plants). 🌿

    **How the Sun's energy reaches and powers Earth — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "⚛️", "Nuclear fusion in the core",    "Deep inside the Sun, gravity is so strong it squeezes hydrogen atoms together — fusing them into helium and releasing enormous energy as light and heat! 🌡️"),
        (2, "🌈", "Radiation travels to Earth",     "Energy travels from the Sun as electromagnetic radiation — mostly visible light, infrared heat, and UV rays — across 150 million km of empty space in just 8 minutes! 🚀"),
        (3, "🌿", "Plants capture the energy",      "Plants absorb sunlight and use it to turn water and CO₂ into glucose sugar — storing the Sun's energy as chemical energy. This is PHOTOSYNTHESIS! 🍃"),
        (4, "🍽️", "Energy enters the food chain",  "Animals eat plants and absorb that stored energy. Other animals eat those animals. Energy flows up the entire food chain — all originally from the Sun! 🌻🐛🐦"),
        (5, "🔥", "Fossil fuels — ancient sunshine", "Dead plants and animals buried millions of years ago compressed into coal, oil, and gas — storing ancient sunlight as chemical energy. We release it by burning! ⛏️"),
        (6, "☀️", "Direct solar energy today",      "Solar panels capture sunlight and convert it directly into electricity — the fastest, cleanest way to use the Sun's extraordinary energy! ⚡🏠"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fff8e1;">
            <span style="background:#f57f17; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#e65100;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("You ate breakfast this morning — can you trace the energy in that food all the way back to the Sun? 🥣☀️🌿")

with col2:
    st.markdown("##### ☀️ Sun Energy Facts")
    for icon, label, fact in [
        ("📏", "Distance",        "The Sun is 150 million km from Earth — so far that even light (the fastest thing in the universe) takes 8 minutes and 20 seconds to reach us! 🚀"),
        ("🌡️", "Surface temp",    "The Sun's surface is about 5,500°C — hot enough to vaporise any material on Earth instantly. Its core reaches 15 million °C! 🔥"),
        ("⚡", "Solar power",     "The Sun delivers about 1,361 watts of energy per square metre to Earth's surface — a single square metre of solar panel can power a small television! 📺"),
        ("🌱", "Photosynthesis",  "Plants convert only about 1–2% of the sunlight hitting them into stored energy — yet this tiny fraction powers almost all life on Earth! 🌿"),
        ("🌍", "Earth's balance", "Earth absorbs the Sun's energy and radiates it back as infrared heat. Greenhouse gases trap some of this heat — keeping Earth warm enough for life! 🌡️"),
        ("🌑", "Without the Sun", "If the Sun suddenly switched off, Earth's surface would freeze to -18°C within a week and -73°C within a year. All surface life would end within months. ❄️😱"),
    ]:
        fact_row(icon, label, fact, "#fff8e1", "#e65100")

    if st.button("☀️ Reveal a Sun Energy Secret!", use_container_width=True, key="sun_btn"):
        st.session_state.show_sun_fact = not st.session_state.show_sun_fact
    if st.session_state.show_sun_fact:
        st.success("🎉 The energy in one hour of sunlight hitting Earth is enough to power "
                   "the ENTIRE WORLD's energy consumption for a whole year! 🌍⚡ "
                   "The challenge is not generating solar energy — "
                   "it is capturing and storing it efficiently. "
                   "Scientists are working on this problem right now — "
                   "and solar power is already the fastest-growing energy source on Earth! ☀️🚀")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — ELECTRICITY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("⚡", "Electricity — The Flow of Tiny Particles!",
               "The power behind almost every device in your home — and lightning in the sky! 🌩️")


st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### ⚡ What Is Electricity?")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Everything you can see is made of **atoms** — and atoms contain tiny
    particles called **electrons**. Electricity is what happens when
    electrons start moving from atom to atom! ⚛️

    When billions of electrons flow together in the same direction
    through a wire, that flow of electrons IS electricity —
    called an **electric current**! 🌊

    **How electricity works — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "⚛️", "Atoms and electrons",      "Every atom has a nucleus (centre) with protons (+) and neutrons, surrounded by electrons (-). In metal wires, outer electrons are loosely held and can move freely! 🔬"),
        (2, "🔋", "A source pushes electrons", "A battery or power station acts like a pump — it pushes electrons out one end and pulls them in the other, creating a continuous flow of electrons through the wire. 💪"),
        (3, "🌊", "Electrons flow as current",  "Billions of electrons cascade along the wire — this is ELECTRIC CURRENT, measured in AMPERES (Amps). The more electrons flowing, the higher the current! 🔢"),
        (4, "💪", "Voltage — the push",         "VOLTAGE is the force pushing the electrons — measured in VOLTS. Higher voltage = stronger push = more powerful electricity. A AA battery is 1.5V; your home socket is 230V! ⚠️"),
        (5, "🔆", "Energy is released",         "As electrons flow through devices (bulbs, motors, heaters) they transfer energy — making light, movement, or heat. The electrons keep flowing — the energy is used! 💡"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e3f2fd;">
            <span style="background:#1565c0; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1565c0;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### ⚡ Conductors and Insulators")
    ci = [
        ("🔌", "Conductors",  "#e3f2fd", "#1565c0",
         "Materials that let electrons flow through easily — metals (copper, silver, gold, aluminium)! Copper is used in almost all electrical wiring. 🪙",
         "Examples: copper wire, silver, iron, saltwater, your body! 🧍"),
        ("🛡️", "Insulators",  "#fce4ec", "#c62828",
         "Materials that block electron flow — keeping electricity safely contained! Rubber, plastic, glass, wood, and dry air are all excellent insulators. 🧱",
         "Examples: rubber gloves, plastic wire coating, glass, porcelain. 🧤"),
        ("🌡️", "Semiconductors", "#e8f5e9", "#2e7d32",
         "Materials that conduct electricity only under certain conditions — like silicon! Semiconductors are the foundation of all computers and smartphones! 💻",
         "Examples: silicon chips, transistors — inside every electronic device! 📱"),
    ]
    for icon, name, bg, color, desc, eg in ci:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:12px; padding:0.6rem 1rem;
                    border-left:4px solid {color}; margin-bottom:0.4rem;">
            <span style="font-size:1.3rem;">{icon}</span>
            <strong style="color:{color};"> {name}:</strong>
            <span style="font-size:0.87rem; color:#555;"> {desc}</span>
            <div style="font-size:0.82rem; color:#777; padding-left:1.8rem; margin-top:0.15rem;">
                📍 {eg}
            </div>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### ⚡ Electricity Facts")
    for icon, label, fact in [
        ("🚀", "Speed of electrons", "Electricity travels through wires at close to the speed of light — about 300,000 km per second! That is why the light comes on instantly when you flick the switch! 💡"),
        ("🔋", "Battery history",    "Alessandro Volta invented the first battery in 1800 using zinc and copper discs soaked in salt water — the VOLT is named after him! 🇮🇹"),
        ("⚡", "Static electricity", "When you rub a balloon on your hair, electrons transfer from hair to balloon — the balloon becomes negatively charged and sticks to the wall! That is static electricity! 🎈"),
        ("🏭", "Power stations",     "Most electricity is generated in power stations where fuel (coal, gas, nuclear, wind, water) spins enormous turbines — spinning magnets inside copper coils generate electricity! 🌀"),
        ("🌍", "Global use",         "The world uses about 25,000 TWh (terawatt-hours) of electricity per year — and demand grows every year as more people gain access to electricity! 📈"),
        ("⚠️", "Mains safety",      "Mains electricity (from your wall socket at 230V) is powerful enough to be very dangerous — NEVER put fingers or objects in sockets, and always follow adult guidance! 🛑"),
    ]:
        fact_row(icon, label, fact, "#e3f2fd", "#1565c0")

    if st.button("⚡ Reveal an Electricity Secret!", use_container_width=True, key="elec_btn"):
        st.session_state.show_electric_fact = not st.session_state.show_electric_fact
    if st.session_state.show_electric_fact:
        st.success("🎉 Your brain runs on electricity! "
                   "Every thought you have, every memory you recall, every movement you make "
                   "is caused by tiny electrical signals (just 0.1 volts!) "
                   "jumping between your 86 billion neurons. "
                   "Your brain generates about 20 watts of electrical power — "
                   "enough to dimly light a small LED bulb! 🧠💡 "
                   "You are literally powered by electricity right now! ⚡")


st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🔌 Electric Circuits — Making Electricity Useful")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Electricity can only flow when it has a **complete, unbroken path** to travel along.
    This continuous loop is called an **electric circuit**! 🔄

    Break the loop anywhere and the electricity stops — which is exactly how
    a light switch works! 💡

    **The parts of every electric circuit:**
    """)
    for step, icon, title, desc in [
        (1, "🔋", "Power source",          "Every circuit needs a source of electrical energy — a battery, solar cell, or connection to the mains electricity supply. This is the pump that pushes electrons! 💪"),
        (2, "🔌", "Conducting wires",      "Metal wires (usually copper) connect everything together — providing the path for electrons to flow along. Wires must form a COMPLETE LOOP! 🔄"),
        (3, "💡", "Component (load)",      "The device that USES the electrical energy — a light bulb, buzzer, motor, or LED. This is where electrical energy transforms into light, sound, or movement! 🎵"),
        (4, "🔀", "Switch",               "A switch opens (breaks) or closes (completes) the circuit. Open = gap in the circuit = electrons stop = device off. Closed = complete loop = electrons flow = device ON! ✅"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e3f2fd;">
            <span style="background:#1565c0; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1565c0;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### 🔌 Series vs Parallel Circuits")
    for icon, name, bg, color, desc in [
        ("➡️", "Series Circuit",   "#e3f2fd", "#1565c0",
         "All components are in ONE single loop — electrons must pass through every component in turn. If one bulb breaks, ALL go out! (Old Christmas lights worked this way — one went out and all went dark!) 🎄"),
        ("⑆", "Parallel Circuit", "#e8f5e9", "#2e7d32",
         "Each component has its OWN separate branch. If one bulb breaks, the others STAY ON! Your home is wired in parallel — you can switch one light off without affecting the others. 🏠💡"),
    ]:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:12px; padding:0.6rem 1rem;
                    border-left:4px solid {color}; margin-bottom:0.4rem;">
            <span style="font-size:1.3rem;">{icon}</span>
            <strong style="color:{color};"> {name}:</strong>
            <span style="font-size:0.87rem; color:#555;"> {desc}</span>
        </div>""", unsafe_allow_html=True)

    think_bubble("If you have a circuit with 3 bulbs in series and one breaks — what happens to the others? And what if they are in parallel? 💡🔌")

with col2:
    st.markdown("##### 🔌 Circuit Facts")
    for icon, label, fact in [
        ("💡", "Light bulb",      "When electricity flows through the very thin tungsten wire (filament) in a bulb, it gets so hot it glows white — reaching 2,500°C! Modern LEDs are far more efficient. 🌡️"),
        ("🔋", "Battery power",   "A battery stores chemical energy and converts it to electrical energy on demand. The chemicals inside react to push electrons around the circuit — until the chemicals are used up! ⚗️"),
        ("🏠", "Your home circuit","Your home has many parallel circuits — lighting circuit, socket circuit, cooker circuit. A fuse box protects each one — if too much current flows, the fuse blows and cuts the power safely! 🛡️"),
        ("🖥️", "Microchip",       "A modern computer chip contains over 50 BILLION tiny transistors — microscopic switches — on a piece of silicon the size of your thumbnail! Each one is a tiny circuit element! 🤯"),
        ("🔋", "Rechargeable",    "Rechargeable batteries reverse their chemical reaction when you charge them — storing electrical energy as chemical energy again! You can do this hundreds of times. ♻️"),
        ("🚗", "Electric cars",   "Electric vehicles use enormous rechargeable battery packs — some containing thousands of individual cells — to store energy for driving hundreds of kilometres! 🔋🚗"),
    ]:
        fact_row(icon, label, fact, "#e3f2fd", "#1565c0")

    if st.button("🔌 Reveal a Circuit Secret!", use_container_width=True, key="circuit_btn"):
        st.session_state.show_circuit_fact = not st.session_state.show_circuit_fact
    if st.session_state.show_circuit_fact:
        st.success("🎉 The first electrical circuit was built by Alessandro Volta in 1800 — "
                   "just a stack of zinc and copper discs with salty water between them! "
                   "Yet that simple pile of discs powered the first demonstrations of "
                   "electrical current and launched the entire electrical age. "
                   "Every circuit in every device in your home traces its ancestry "
                   "back to that humble pile of metal discs! 🔋⚡ Amazing! 🌍")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — LIGHTNING (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌩️", "Lightning — Nature's Giant Spark!",
               "Step through how the sky builds up and releases billions of volts of electricity! ⚡")

lightning_steps = [
    ("☁️", "Step 1 — The Storm Cloud Builds",
     "A CUMULONIMBUS storm cloud can tower up to 15 km high — like a giant electricity factory! ⛈️\n\n"
     "Inside, powerful updrafts and downdrafts carry ice crystals and water droplets "
     "crashing into each other at enormous speed. "
     "These constant high-speed collisions cause electrons to be knocked off ice crystals — "
     "just like rubbing a balloon on your hair, but on a colossal scale! 🎈\n\n"
     "This electron-knocking happens billions of times per second throughout the cloud.",
     "#eceff1", "#546e7a"),
    ("🔋", "Step 2 — Charge Separation",
     "As ice particles collide, something remarkable happens — charge SEPARATES! ⚡\n\n"
     "Larger ice particles lose electrons (become positively charged ➕) and fall to the "
     "**bottom** of the cloud. Smaller ice crystals gain electrons (become negatively "
     "charged ➖) and are carried to the **top** of the cloud by updrafts.\n\n"
     "Now the cloud bottom is hugely negative (➖) and the cloud top is hugely positive (➕). "
     "The negative bottom also repels electrons in the ground below — "
     "making the ground directly beneath the cloud positively charged! ➕🌍",
     "#fff8e1", "#f57f17"),
    ("⚡", "Step 3 — The Voltage Builds",
     "The separated charges create a massive VOLTAGE between the cloud bottom and the ground below. 🌩️\n\n"
     "Voltage is electrical pressure — the greater the charge difference, "
     "the higher the voltage and the stronger the 'urge' for electricity to flow and equalise.\n\n"
     "A single thundercloud can build up a potential difference of up to "
     "**300 MILLION VOLTS** between cloud and ground — "
     "that is 1.3 million times more powerful than your home electricity socket! 😱\n\n"
     "This enormous electrical pressure is desperately looking for a path to discharge…",
     "#e8f5e9", "#2e7d32"),
    ("🔀", "Step 4 — The Leader Stroke",
     "When the voltage is high enough, the air itself starts to break down — "
     "becoming a conductor! 💥\n\n"
     "An invisible channel of ionised (electrically charged) air called a "
     "**STEPPED LEADER** zigzags downward from the cloud in rapid 50-metre steps "
     "toward the ground — completely invisible to the human eye!\n\n"
     "Simultaneously, POSITIVE STREAMERS reach upward from tall objects on the ground "
     "(trees, buildings, lightning rods) toward the descending leader. "
     "When leader and streamer CONNECT — completing the circuit — "
     "the massive discharge begins! ⚡🔗",
     "#ede7f6", "#6a1b9a"),
    ("🌟", "Step 5 — The Return Stroke — The Flash You See!",
     "The moment leader meets streamer, a huge surge of electricity races UPWARD "
     "from ground to cloud — this is the RETURN STROKE and it is what you actually see! 🌟\n\n"
     "- ⚡ The return stroke carries up to **30,000 AMPERES** of current\n"
     "- 🌡️ The lightning channel heats to **30,000°C** — five times hotter than the Sun's surface!\n"
     "- 💥 This superheated air expands explosively — creating the **SHOCKWAVE we hear as THUNDER!** 🥁\n"
     "- 🏎️ The whole thing lasts just **0.2 seconds** — but may include 3–5 return strokes!\n"
     "- 🌍 Lightning strikes Earth about **100 times every second** — 8.6 million times per day! 🤯",
     "#fce4ec", "#c62828"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="lgtn_prev"):
        st.session_state.energy_step = max(0, st.session_state.energy_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="lgtn_next"):
        st.session_state.energy_step = min(len(lightning_steps)-1, st.session_state.energy_step + 1)

idx   = st.session_state.energy_step
lstep = lightning_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{lstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {lstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{lstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {lstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {lstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{lstep[4]}">●</span>'
                for i in range(len(lightning_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Step {idx+1} of {len(lightning_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

think_bubble("Count the seconds between lightning and thunder, then divide by 3 — that tells you how many kilometres away the storm is! Try it next time! ⛈️🔢")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — ENERGY SOURCES EXPLORER (Topic selector)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌍", "Explore All Energy Sources!",
               "Tap each energy source to discover exactly how it works and why it matters! ⚡")

energy_sources = {
    "☀️ Solar": {
        "emoji": "☀️", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "☀️ The most abundant energy source in the solar system!",
        "body": (
            "Solar energy is light and heat from the Sun converted directly into electricity or heat! ☀️\n\n"
            "- ⚡ **Solar panels (PV)**: Photovoltaic cells made of silicon absorb photons (light particles) and release electrons — generating direct current (DC) electricity with no moving parts and zero pollution! 🌿\n"
            "- 🌡️ **Solar thermal**: Mirrors concentrate sunlight to heat water or oil to extreme temperatures — generating steam that spins turbines to make electricity. Used in large desert power stations! 🏜️\n"
            "- 🏠 **Solar at home**: Over 1 billion solar panels are now installed on rooftops worldwide — homeowners generate their own electricity and sell surplus back to the grid! 💰\n"
            "- 🌍 **Growth rate**: Solar is the fastest-growing energy source on Earth — costs have dropped 90% in the last decade, making it cheaper than coal in most countries! 📉\n"
            "- ✅ **Renewable**: The Sun will provide energy for another 5 billion years — it will NEVER run out during human civilisation! ♾️\n"
            "- ❄️ **Works in winter**: Solar panels still work on cloudy days and in cold climates — they need light, not heat! Germany (not very sunny!) is a world leader in solar power. 🇩🇪"
        )
    },
    "💨 Wind": {
        "emoji": "💨", "color": "#0288d1", "bg": "#e1f5fe",
        "tagline": "💨 Harnessing moving air to power millions of homes!",
        "body": (
            "Wind turbines capture the kinetic energy of moving air and convert it to electricity! 💨\n\n"
            "- 🌀 **How a turbine works**: Wind pushes the aerofoil-shaped blades (like aeroplane wings!) causing them to rotate. The spinning shaft drives a generator — magnets spinning inside copper coils generate electricity! ⚡\n"
            "- 🌊 **Offshore wind**: Wind turbines built at sea capture stronger, more consistent winds than on land — a single large offshore turbine can power over 3,000 homes! 🏠\n"
            "- 📏 **Enormous scale**: Modern wind turbines can be 250m tall — taller than the Eiffel Tower! Their blades sweep an area larger than a football pitch! ⚽\n"
            "- 🌍 **Global leader**: China has more wind power than any other country — enough turbines to power a country the size of France entirely from wind! 🇨🇳\n"
            "- ✅ **Renewable**: Wind is caused by the Sun heating air unevenly — it will blow for as long as the Sun shines! Clean and free forever. ♾️\n"
            "- 🦅 **Wildlife concern**: Turbine blades can harm birds and bats — engineers design smarter placement and radar systems to detect and pause turbines when birds approach. 🔍"
        )
    },
    "💧 Hydro": {
        "emoji": "💧", "color": "#00695c", "bg": "#e0f2f1",
        "tagline": "💧 The power of falling water — clean and ancient!",
        "body": (
            "Hydroelectric power uses the kinetic energy of flowing or falling water to generate electricity! 💧\n\n"
            "- 🏗️ **How a dam works**: A dam blocks a river, creating a reservoir. Water flows through pipes (penstocks) deep in the dam, spinning turbines — which drive generators to make electricity! ⚡\n"
            "- 🌍 **Largest power source**: Hydropower is the world's largest source of RENEWABLE electricity — providing about 16% of global electricity! In some countries (Norway, 95%), it supplies almost everything. 🇳🇴\n"
            "- 🏔️ **Run of river**: Smaller hydro plants divert part of a river through turbines without a large dam — less environmental impact, perfect for mountain streams! ⛰️\n"
            "- 🔋 **Pumped storage**: Water can be pumped UPHILL using surplus electricity (e.g. from solar at noon) and released downhill to generate electricity when needed — the world's biggest battery! 💾\n"
            "- ✅ **Renewable**: Powered by the water cycle — which is powered by the Sun — hydro energy will last as long as rain falls! ♾️\n"
            "- ⚠️ **Ecosystem impact**: Large dams flood valleys and disrupt river ecosystems — fish migration can be blocked. Engineers now build fish ladders to help salmon and other fish pass! 🐟"
        )
    },
    "🔥 Fossil Fuels": {
        "emoji": "🔥", "color": "#c62828", "bg": "#ffebee",
        "tagline": "🔥 Ancient sunshine — powerful but running out!",
        "body": (
            "Fossil fuels (coal, oil, natural gas) are the compressed remains of ancient organisms — "
            "storing millions of years of solar energy! 🌿\n\n"
            "- 🌿 **How they formed**: Dead plants and sea creatures were buried under rock over millions of years. Immense heat and pressure transformed them into coal, oil, and gas — concentrated chemical energy! ⏳\n"
            "- ⚡ **How we use them**: Burning fossil fuels releases heat, which boils water into steam, which spins turbines, which drive generators — making electricity for homes and factories! 🏭\n"
            "- 🚗 **Transport fuel**: Petrol and diesel (from oil) power most cars, lorries, ships, and aeroplanes. Without oil, most modern transport would stop immediately! ✈️\n"
            "- 🌡️ **Climate problem**: Burning fossil fuels releases CO₂ — a greenhouse gas that traps heat in Earth's atmosphere, causing global warming and climate change. 🌍⚠️\n"
            "- ⏳ **Running out**: Fossil fuels took hundreds of millions of years to form — we are burning them in hundreds of years. Once gone, they are gone forever! 🚫\n"
            "- 🔄 **Transition**: The world is working to replace fossil fuels with renewable energy — but it is one of the biggest engineering and political challenges humanity has ever faced! 🌱"
        )
    },
    "⚛️ Nuclear": {
        "emoji": "⚛️", "color": "#6a1b9a", "bg": "#f3e5f5",
        "tagline": "⚛️ Splitting atoms to release unimaginable energy!",
        "body": (
            "Nuclear energy releases energy from the nucleus (centre) of atoms — the most concentrated energy source humans have ever used! ⚛️\n\n"
            "- 💥 **Fission**: In a nuclear power station, uranium atoms are split apart (FISSION) — releasing enormous heat. This heat boils water to steam, which spins turbines to generate electricity! ⚡\n"
            "- ⚖️ **Incredible density**: One uranium fuel pellet the size of your fingertip contains as much energy as 800 kg of coal or 3 barrels of oil! Nuclear is the most energy-dense fuel ever used. 🤯\n"
            "- ✅ **Low carbon**: Nuclear generates electricity with almost no CO₂ — making it very useful for fighting climate change! France gets 70% of its electricity from nuclear. 🇫🇷\n"
            "- ⚠️ **Radioactive waste**: Used nuclear fuel remains radioactive for thousands of years — it must be stored very carefully in deep underground facilities. 🏔️\n"
            "- ☀️ **Fusion — the future**: Scientists are working on NUCLEAR FUSION — the same process the Sun uses — which could provide virtually unlimited clean energy with almost no waste. 🌟\n"
            "- 🏭 **Safety record**: Modern nuclear power stations are extremely safe — per unit of energy generated, nuclear causes fewer deaths than coal, oil, or even solar! 📊"
        )
    },
    "🌿 Biomass": {
        "emoji": "🌿", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🌿 Energy from living and recently living things!",
        "body": (
            "Biomass energy uses organic material — plants, wood, and organic waste — as fuel! 🌱\n\n"
            "- 🌳 **Wood burning**: The oldest energy source humans have used — burning wood releases the solar energy stored during the tree's growth. Still used for heating by 2.4 billion people worldwide! 🔥\n"
            "- 🐄 **Biogas**: Bacteria break down organic waste (animal dung, food scraps, sewage) in sealed tanks, producing methane gas — which can be burned for cooking and electricity! 🍳\n"
            "- 🌽 **Biofuels**: Crops like corn, sugarcane, and oilseed are fermented or pressed to produce liquid fuels (ethanol, biodiesel) that can power vehicles — reducing oil dependence! 🚗\n"
            "- ♻️ **Waste to energy**: Burning household waste generates heat and electricity — keeping rubbish out of landfill while generating energy. Used widely in Scandinavia and Japan! 🗑️\n"
            "- 🌱 **Carbon neutral?**: Growing new plants absorbs CO₂ from the air — theoretically balancing the CO₂ released when biomass is burned. But this only works if forests are properly managed! ⚖️\n"
            "- 🌍 **Developing world**: In many developing countries, biomass is the PRIMARY energy source — but inefficient stoves cause indoor air pollution, a major health problem. 😷"
        )
    },
}

e_cols = st.columns(len(energy_sources))
for i, (ename, edata) in enumerate(energy_sources.items()):
    with e_cols[i]:
        short = ename.split(" ", 1)[1]
        if st.button(edata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"esrc_{i}"):
            st.session_state.energy_picked = ename

if st.session_state.energy_picked and st.session_state.energy_picked in energy_sources:
    ename = st.session_state.energy_picked
    edata = energy_sources[ename]
    st.markdown(f"""
    <div style="background:{edata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {edata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{edata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {ename.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{edata['color']}; font-weight:700;">
                    {edata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(edata["body"])
else:
    st.info("👆 Tap any energy source above to discover exactly how it works!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — ANIMALS AND ELECTRICITY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Amazing Animals That Use Electricity!",
               "Nature discovered electricity long before humans did — tap to explore! 🌍")

animal_energy = {
    "⚡ Electric Eel": {
        "emoji": "⚡", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "⚡ The living battery — up to 860 volts!",
        "body": (
            "The electric eel is one of nature's most astonishing electrical generators! ⚡\n\n"
            "- 🔋 **Living battery**: About 80% of an electric eel's body consists of specialised muscle cells called ELECTROCYTES — stacked like tiny batteries in series! Each generates a tiny voltage; together they produce enormous power.\n"
            "- ⚡ **860 volts**: A large electric eel can discharge up to 860 volts — nearly 4 times the voltage of your home socket! Enough to stun a horse or knock a human unconscious! 😱\n"
            "- 🎯 **Hunting weapon**: The eel uses high-voltage pulses to stun prey — fish and small animals are momentarily paralysed, making them easy to catch. 🐟\n"
            "- 📡 **Radar system**: Low-voltage pulses (under 10V) are used constantly for navigation and communication — detecting objects by the distortions in the electric field. 🔍\n"
            "- 🐍 **Not an eel**: Despite the name, electric eels are actually more closely related to catfish than true eels! They breathe air and must surface every 10 minutes! 🌊"
        )
    },
    "🦈 Sharks": {
        "emoji": "🦈", "color": "#0277bd", "bg": "#e1f5fe",
        "tagline": "🔌 Detecting your heartbeat from metres away!",
        "body": (
            "Sharks have one of nature's most extraordinary electrical senses! 🦈\n\n"
            "- 🔌 **Ampullae of Lorenzini**: Hundreds of tiny gel-filled pores around a shark's snout connect to sensory cells that detect minute electrical fields — as small as 0.000000005 volts! 🤯\n"
            "- 💓 **Detecting heartbeats**: Every living creature generates a tiny electric field from its heartbeat and muscle movements — sharks can detect a flatfish buried under sand from over a metre away!\n"
            "- 🧭 **Navigation**: Sharks also use Earth's magnetic field (detected through their electrical sense) to navigate across thousands of kilometres of open ocean — a biological GPS! 🌍\n"
            "- ⚡ **Hammerhead advantage**: The hammerhead shark's wide, flat head massively increases the area of electrical receptors — giving it extraordinary sensitivity to detect prey hidden in the sand! 🏖️\n"
            "- 🔬 **Inspiring technology**: The ampullae of Lorenzini are inspiring new underwater sensors and medical diagnostic devices — nature's design is still ahead of human engineering! 💡"
        )
    },
    "🐠 Platypus": {
        "emoji": "🐠", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🦆 The duck-billed electrical detective!",
        "body": (
            "The platypus is one of the strangest and most electrically sensitive mammals alive! 🦆\n\n"
            "- 🔌 **Electroreception**: The platypus's rubbery bill contains about 40,000 electroreceptors — detecting the tiny electrical signals generated by the muscles of shrimp and crayfish! 🦐\n"
            "- 🙈 **Hunts blind**: When diving, the platypus closes its eyes, ears, and nose — navigating and hunting ENTIRELY through electrical detection! Like having a superpower in the dark. 🌑\n"
            "- 🌊 **Sweeping motion**: The platypus sweeps its bill from side to side as it swims — triangulating the source of electrical signals to precisely locate hidden prey. 📡\n"
            "- 🧬 **Mammal mystery**: The platypus is one of only five mammals with electroreception (the others are four species of echidna). How mammals evolved this fish-like sense is still being researched! 🔬\n"
            "- ⚡ **Venomous too!**: Male platypuses have venomous spurs on their hind legs — making them the only venomous mammals that also have electroreception! Nature's most surprising combination! 😮"
        )
    },
    "🐟 Elephantfish": {
        "emoji": "🐟", "color": "#7b1fa2", "bg": "#f3e5f5",
        "tagline": "📡 Communicating with electric pulses in murky water!",
        "body": (
            "Weakly electric fish like the elephantfish use electricity for communication AND sensing! 📡\n\n"
            "- 🔋 **Weak electric organ**: Unlike electric eels, elephantfish generate only very weak electric fields (less than 1 volt) — not for hunting but for sensing and social communication! 🗣️\n"
            "- 📡 **Electrolocation**: By detecting how objects distort their own electric field, they build a complete 3D picture of their surroundings — perfect for murky river water where vision is useless! 🌊\n"
            "- 💬 **Electric language**: Each species has its own unique electric pulse pattern — frequency, shape, and rhythm communicate identity, mood, and readiness to mate! 🎵\n"
            "- 🧠 **Huge brain**: Elephantfish have a cerebellum (balance/coordination brain region) that is proportionally LARGER than in humans — reflecting the enormous processing power needed for electrosensory mapping! 🤯\n"
            "- 🌍 **African rivers**: Found in murky rivers and flooded forests of West Africa — where their electrical sense gives them a major survival advantage over visually oriented predators! 🌿"
        )
    },
    "🦑 Cuttlefish": {
        "emoji": "🦑", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🎨 Electricity in the skin for instant camouflage!",
        "body": (
            "Cuttlefish use electrical signals to control one of nature's most spectacular light shows! 🎨\n\n"
            "- 🌈 **Chromatophores**: Cuttlefish skin contains millions of tiny colour cells called CHROMATOPHORES — each controlled by a tiny muscle activated by an electrical nerve signal! 🔌\n"
            "- ⚡ **Instant camouflage**: Electrical signals from the brain cause specific chromatophores to expand or contract in milliseconds — creating complex patterns of colour and texture instantly! 🎭\n"
            "- 📺 **Living TV screen**: The cuttlefish can run different colour patterns across different parts of its body simultaneously — like having a 3D TV screen for skin! 🖥️\n"
            "- 🗣️ **Communication**: Male cuttlefish show elaborate side-specific patterns — one pattern showing to a rival male (aggressive display), a DIFFERENT pattern on the other side showing to a female (courtship)! 💕\n"
            "- 🧠 **Surprising intelligence**: Cuttlefish can solve puzzles, delay gratification, and have excellent memories — their brain-to-body ratio rivals many vertebrates! 🤔"
        )
    },
    "🐝 Bees": {
        "emoji": "🐝", "color": "#f9a825", "bg": "#fffde7",
        "tagline": "🌸 Using electric fields to find the best flowers!",
        "body": (
            "Bees have an extraordinary ability to detect and use electric fields in ways scientists only recently discovered! 🌸\n\n"
            "- 🌸 **Flower electric fields**: Flowers generate weak electric fields from the ground — and different flower species have different field shapes! Bees can detect these fields to identify flower types. 🌺\n"
            "- ⚡ **Bee charge**: As a bee flies through the air, friction builds up a positive static charge on its body — just like a balloon rubbed on hair! 🎈\n"
            "- 💛 **Electrostatic pollen transfer**: When a positively charged bee lands on a negatively charged flower, pollen leaps through the air and clings to the bee electrostatically — no touching needed! 🧲\n"
            "- 📝 **Flower memory**: Bees can sense whether a flower has recently been visited by another bee — depleted flowers lose some of their charge. This helps bees avoid empty flowers! ♻️\n"
            "- 🌍 **Pollination impact**: This electrical pollination mechanism is responsible for about one-third of all the food humans eat — bees' electrical superpower helps feed the world! 🍎🥦🌽"
        )
    },
}

an_cols = st.columns(len(animal_energy))
for i, (aname, adata) in enumerate(animal_energy.items()):
    with an_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"anen_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in animal_energy:
    aname = st.session_state.animal_picked
    adata = animal_energy[aname]
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
    st.info("👆 Tap any animal above to discover how it uses electricity!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — SAVING ENERGY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Using Energy Wisely — Saving Our Planet!",
               "Small actions at home add up to a huge difference for the Earth! 🌍")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("💡", "Switch Off Lights!",
     "When you leave a room, switch the light off! "
     "A single LED bulb uses about 10 watts — but if left on all day, that adds up to real energy and cost. "
     "Switching from old-style bulbs to LEDs saves about 90% of lighting energy. "
     "Natural daylight is free — open the curtains before switching lights on! ☀️🏠",
     "#fff8e1", "#f57f17"),
    ("🌡️", "Don't Heat Empty Rooms!",
     "Heating your home uses enormous energy — often the biggest energy cost of all! "
     "Turn radiators down in rooms you are not using. "
     "Closing doors keeps heat where you need it. "
     "A thick jumper and cosy socks can replace turning the heating up a degree — "
     "saving energy AND keeping you cosy! 🧥🧦",
     "#ffebee", "#c62828"),
    ("📱", "Unplug Devices on Standby!",
     "Devices left on standby still use electricity — up to 10% of your home's energy! "
     "TVs, games consoles, phone chargers left plugged in with no phone attached — all use power. "
     "Turn off at the socket or use a smart power strip that cuts standby power automatically. "
     "Small actions, big savings! 🔌♻️",
     "#e3f2fd", "#1565c0"),
    ("🚶", "Walk, Cycle, or Use Public Transport!",
     "Cars and lorries burning petrol and diesel are a major source of CO₂ emissions. "
     "Walking and cycling use only the energy from your food — with zero emissions! "
     "A bus or train carries many people, sharing the energy cost. "
     "For every 1 km you walk instead of drive, you save about 170g of CO₂! 🌿🚲",
     "#e8f5e9", "#2e7d32"),
    ("🍽️", "Reduce Food Waste!",
     "Growing, transporting, and cooking food uses enormous amounts of energy. "
     "When food is thrown away, ALL that energy is wasted! "
     "Plan meals carefully, use leftovers, and compost what cannot be eaten. "
     "Eating less meat also helps — producing 1 kg of beef uses 20x more energy than 1 kg of vegetables! 🥗🌱",
     "#e0f2f1", "#00695c"),
    ("♻️", "Recycle and Reuse!",
     "Making new products from raw materials uses FAR more energy than recycling! "
     "Recycling one aluminium can saves enough energy to run a TV for 3 hours! 📺 "
     "Buying second-hand items, repairing broken things, and choosing durable products "
     "all reduce the energy embedded in manufacturing. "
     "The greenest product is the one you never had to make! 🌍",
     "#f3e5f5", "#6a1b9a"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Which energy-saving action from above could you start doing TODAY? Could you challenge your family to try it together? 🌍💪")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)    

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Energy and Electricity Quiz — Test What You Know!",
               "6 electrifying questions — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 🔄 — What happens to energy when it is 'used up'?",
        "opts": ["It disappears completely", "It transforms into a different type of energy", "It goes back to the Sun", "It is stored underground"],
        "ans":  "It transforms into a different type of energy",
        "explain": "Energy is NEVER destroyed — it only transforms! This is the Law of Conservation of Energy. Electrical energy in a bulb becomes light and heat energy. Chemical energy in food becomes kinetic (movement) and heat energy! 🔄⚡"
    },
    {
        "q":    "Q2 ⚡ — What is an electric current?",
        "opts": ["Heat flowing through a wire", "Light moving along a cable", "Electrons flowing through a conductor", "Atoms vibrating in metal"],
        "ans":  "Electrons flowing through a conductor",
        "explain": "Electric current is the flow of electrons — tiny charged particles — through a conducting material like copper wire. The more electrons flowing per second, the higher the current, measured in Amperes (Amps)! ⚡🔌"
    },
    {
        "q":    "Q3 💡 — What must a circuit have for electricity to flow?",
        "opts": ["A battery and a red wire", "A complete unbroken loop with a power source", "At least three bulbs", "A switch in the ON position"],
        "ans":  "A complete unbroken loop with a power source",
        "explain": "Electricity can only flow in a COMPLETE, UNBROKEN LOOP called a circuit! Break the loop anywhere — like opening a switch — and the current stops immediately. A power source, wires, and a complete path are all essential! 🔄🔋"
    },
    {
        "q":    "Q4 🌩️ — What causes the SOUND of thunder?",
        "opts": ["Clouds crashing together", "Rain hitting the ground very fast", "Superheated air around lightning expanding explosively", "Electricity bouncing between clouds"],
        "ans":  "Superheated air around lightning expanding explosively",
        "explain": "Lightning heats the air around it to 30,000°C in an instant — five times hotter than the Sun's surface! This superheated air expands so violently it creates a shockwave we hear as THUNDER! You see lightning first because light travels faster than sound! 🌩️🥁"
    },
    {
        "q":    "Q5 ☀️💨💧 — Which of these is a RENEWABLE energy source?",
        "opts": ["Coal", "Natural gas", "Oil", "Wind"],
        "ans":  "Wind",
        "explain": "Wind is RENEWABLE — it is powered by the Sun heating air, which will keep happening for billions of years! Coal, oil, and gas are FOSSIL FUELS — they took millions of years to form and will run out once we burn them all! ♾️💨"
    },
    {
        "q":    "Q6 🦈 — How do sharks detect prey hidden under sand?",
        "opts": ["With super-sensitive smell", "By feeling vibrations in the water", "By detecting the tiny electrical fields from the prey's heartbeat", "Using echolocation like bats"],
        "ans":  "By detecting the tiny electrical fields from the prey's heartbeat",
        "explain": "Sharks have special organs called AMPULLAE OF LORENZINI — hundreds of gel-filled pores that detect electric fields as tiny as 0.000000005 volts! Every animal's heart generates a tiny electrical field — sharks can sense it through sand! 🦈⚡🔌"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"en_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="en_quiz_submit"):
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
        (6, "🏆", "ENERGY AND ELECTRICITY MASTER! ⚡☀️",    "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Energy Scientist! 🔋",          "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Electricity Explorer! 💡",          "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Energy Detective! 🔍",          "#7b1fa2", "#f3e5f5"),
        (0, "✨", "Keep Exploring — You Can Do It! 💪",      "#1565c0", "#e3f2fd"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="en_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()


st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?",
               "Energy and Electricity — your quick recap! 🎉")

summary_items = [
    ("🌟", "Energy",       "The ability to make things happen — it never disappears, only transforms!"),
    ("☀️", "The Sun",      "Earth's ultimate energy source — powers weather, food, and fossil fuels!"),
    ("⚡", "Electricity",  "Electrons flowing through conductors — powering everything around you!"),
    ("🔌", "Circuits",     "Complete loops that let electricity flow to do useful work!"),
    ("🌩️", "Lightning",    "300 million volts of static electricity — nature's giant spark!"),
    ("🌱", "Renewables",   "Solar, wind, water — clean energy sources that will never run out!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #e65100;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1a2a00,#f57f17,#e65100,#1a2a00);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Amazing work, little scientist! You are an Energy and Electricity Master! ✨
    </div>
    <div style="color:#fff9c4; font-size:0.95rem;">
        Energy flows through everything in the universe — including you! Use it wisely and help power a better world! 🌍
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        ☀️ ⚡ 🔋 💡 🌊 💨 🔥 ⚛️
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
