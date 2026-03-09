import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 08 · Saving Our Planet", layout="wide", initial_sidebar_state="expanded")

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
    "show_recycle_fact", "show_water_fact",
    "show_trees_fact",   "show_climate_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "hero_picked"   not in st.session_state: st.session_state.hero_picked   = None
if "animal_picked" not in st.session_state: st.session_state.animal_picked = None
if "planet_step"   not in st.session_state: st.session_state.planet_step   = 0
if "quiz_answers"  not in st.session_state: st.session_state.quiz_answers  = {}

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
<div style="background:linear-gradient(135deg,#003300,#1b5e20,#0d47a1,#003300);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#a5d6a7; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 08 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🌍 Saving Our Planet! 🌱
    </h1>
    <p style="color:#c8e6c9; font-size:1.05rem; margin:0.8rem 0 0;">
        Earth is the only home we have — the most beautiful planet in the universe!
        Discover how it works, what is threatening it, and how YOU can be a hero! 💚
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        🌍 ♻️ 💧 🌳 🌡️ 🌊 🦋 💚
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What makes Earth so **uniquely special** in our solar system
        - ✅ What **climate change** is and how it is happening
        - ✅ How **recycling** saves energy and resources
        - ✅ Why every drop of **water** is precious
        """)
    with col2:
        st.markdown("""
        - ✅ Why **trees and forests** are the lungs of Earth
        - ✅ How **pollution** harms land, sea, and air
        - ✅ What **YOU** can do every single day to help
        - ✅ Animals endangered by human activity + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — OUR EXTRAORDINARY PLANET
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌍", "Earth — The Most Special Planet We Know!",
               "Of all the billions of planets in the universe, only one has YOU living on it! 🌟")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Look out of the window. Breathe in. Feel the warmth of light on your face.
    All of that — the air, the water, the warmth, the life — is a **miracle** that
    scientists have found nowhere else in the universe. Not yet. 🔭

    Earth formed **4.5 billion years ago** from a swirling cloud of dust and gas.
    Over millions of years, it cooled, oceans formed, and about **3.8 billion years ago**,
    the first tiny living cells appeared in the sea. From those microscopic beginnings,
    all the trees, fish, birds, dinosaurs, flowers, and humans on Earth descended! 🌱

    Earth is perfectly placed — not too hot, not too cold.
    It has liquid water, a protective atmosphere, and a magnetic field shielding it from
    deadly solar radiation. Scientists call this the **Goldilocks Zone** — just right for life! 🐻
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f5e9,#e3f2fd);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #1b5e20;">
        <div style="font-weight:700; color:#1b5e20; font-size:1.05rem; margin-bottom:0.8rem;">
            🌍 Earth's Vital Statistics — Our Home By The Numbers!
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">💧</div>
                <div style="font-weight:700; color:#0288d1;">71%</div>
                <div style="font-size:0.8rem; color:#666;">of Earth's surface covered by ocean</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🌿</div>
                <div style="font-weight:700; color:#2e7d32;">3 trillion</div>
                <div style="font-size:0.8rem; color:#666;">trees on Earth right now</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🦎</div>
                <div style="font-weight:700; color:#e65100;">8.7 million</div>
                <div style="font-size:0.8rem; color:#666;">estimated species of life on Earth</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🌡️</div>
                <div style="font-weight:700; color="#c62828;">+1.2°C</div>
                <div style="font-size:0.8rem; color:#666;">average warming since 1850</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🌊</div>
                <div style="font-weight:700; color:#0277bd;">97%</div>
                <div style="font-size:0.8rem; color:#666;">of Earth's water is salty ocean</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">♻️</div>
                <div style="font-weight:700; color:#6a1b9a;">9%</div>
                <div style="font-size:0.8rem; color:#666;">of all plastic ever made has been recycled</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("If Earth were the size of a marble — all the world's oceans would be just a thin film of moisture on its surface. How precious does water seem now? 💧🌍")

with col2:
    fun_card("🛡️", "Earth's Invisible Shields",
             "Earth has two extraordinary shields protecting life! "
             "The <strong>atmosphere</strong> — a 100 km blanket of gases — "
             "blocks dangerous UV radiation, keeps us warm, and gives us air to breathe. "
             "The <strong>magnetic field</strong> — generated by Earth's liquid iron core — "
             "deflects deadly solar wind particles that would strip our atmosphere away! 🧲☀️",
             bg="#e8f5e9", border="#1b5e20")
    fun_card("🌊", "The Oceans — Earth's Life Support",
             "The oceans produce over <strong>50% of Earth's oxygen</strong> — "
             "more than all the forests combined! Tiny ocean plants called phytoplankton "
             "photosynthesize in their trillions. "
             "The oceans also absorb 90% of the excess heat from climate change "
             "and 30% of all CO₂ emissions — acting as Earth's greatest buffer. 🐋🌿",
             bg="#e3f2fd", border="#0277bd")
    fun_card("🌡️", "The Right Temperature — Just Right!",
             "Earth's average surface temperature is about <strong>15°C</strong>. "
             "Without the natural greenhouse effect, it would be -18°C — too cold for most life. "
             "But too much greenhouse gas makes it dangerously hot. "
             "Earth has maintained a liveable temperature for billions of years "
             "through a delicate balancing act — which human activity is now disrupting. ⚠️",
             bg="#fff8e1", border="#f57f17")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — CLIMATE CHANGE
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌡️", "Climate Change — Why Our Planet Is Warming!",
               "Understanding the biggest challenge facing our generation — clearly and honestly! 🌍")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Our planet is getting warmer — and scientists around the world agree on why.
    The story starts with the **greenhouse effect**. 🌿

    **How climate change is happening — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "☀️", "Sun warms the Earth",          "Sunlight passes through Earth's atmosphere and warms the ground and oceans. The warmed Earth then radiates this heat back upward as infrared radiation (heat rays). 🌡️"),
        (2, "🛡️", "Greenhouse gases trap heat",   "Certain gases in the atmosphere — CO₂, methane, water vapour — act like a blanket, absorbing the outgoing heat and radiating it back to Earth. This is the natural GREENHOUSE EFFECT and keeps Earth liveable! 🏡"),
        (3, "🏭", "Humans add extra CO₂",          "Burning coal, oil, and gas for energy releases billions of tonnes of extra CO₂ into the atmosphere every year. Deforestation removes trees that absorb CO₂. The blanket gets thicker! 🔥"),
        (4, "🌡️", "Earth's temperature rises",    "The thicker blanket traps more heat. Earth's average temperature has already risen 1.2°C since 1850 — and is rising faster every decade. 📈"),
        (5, "🌊", "Knock-on effects everywhere",  "Warmer temperatures melt ice caps (raising sea levels), make weather more extreme (stronger storms, worse droughts), disrupt seasons, and shift habitats — threatening millions of species. 🐻‍❄️"),
        (6, "💚", "But we can change it!",         "The same human ingenuity that caused this problem can solve it! Renewable energy, electric transport, reforestation, and smarter farming can all reduce CO₂ — if we act fast! ⚡🌱"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e8f5e9;">
            <span style="background:#1b5e20; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1b5e20;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("If you could invent one thing to help stop climate change, what would it be? Scientists need ideas like yours! 🔬💡")

with col2:
    st.markdown("##### 🌡️ Climate Change Facts")
    for icon, label, fact in [
        ("🧊", "Ice caps melting",     "The Arctic is warming 4x faster than the global average — Arctic summer sea ice has shrunk by 40% since 1980. Polar bears, seals, and Arctic foxes are losing their habitat! 🐻‍❄️"),
        ("🌊", "Sea level rising",     "Global sea levels have risen about 20cm since 1900 — and the rate is accelerating. Low-lying islands and coastal cities like Miami, Mumbai, and Amsterdam face flooding! 🏙️"),
        ("🌪️", "Extreme weather",      "Climate change makes extreme weather events more frequent and intense — more powerful hurricanes, longer droughts, larger wildfires, and heavier rainfall events. 🔥"),
        ("🌸", "Seasons shifting",     "Spring arrives earlier and autumn later in many parts of the world — confusing migrating birds, hibernating animals, and flowering plants whose timing is now out of sync! 🐦"),
        ("🐠", "Ocean acidification",  "Oceans absorb CO₂, which dissolves to form carbonic acid — making the ocean 30% more acidic since the industrial revolution. Coral reefs and shellfish are dissolving! 🐚"),
        ("💚", "Paris Agreement",      "In 2015, almost every country in the world agreed to limit warming to 1.5°C above pre-industrial levels — the Paris Agreement. Meeting this goal requires urgent, massive action. 🌍🤝"),
    ]:
        fact_row(icon, label, fact, "#e8f5e9", "#1b5e20")

    if st.button("🌡️ Reveal a Climate Secret!", use_container_width=True, key="climate_btn"):
        st.session_state.show_climate_fact = not st.session_state.show_climate_fact
    if st.session_state.show_climate_fact:
        st.success("🎉 The last time Earth's atmosphere had this much CO₂ was over 3 MILLION YEARS AGO — "
                   "long before humans existed! At that time, sea levels were 20 metres higher "
                   "than today and forests grew in the Arctic! 🌳❄️ "
                   "But here is the hopeful part: renewable energy is now cheaper than fossil fuels "
                   "in most countries — and solar power capacity is doubling every 3 years. "
                   "The clean energy revolution is already happening! ☀️⚡")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — RECYCLING AND WASTE
# ═══════════════════════════════════════════════════════════════════════════════
section_header("♻️", "Recycling — Giving Materials a Second Life!",
               "One person's waste is another product's raw material! 🌱")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Every object you use was made from **materials** taken from the Earth —
    metals mined from rock, plastic made from oil, paper made from trees,
    glass made from sand. All of these resources are **finite** — they will run out! ⛏️

    **Recycling** collects these used materials and processes them back into
    new products — saving raw materials, energy, water, and reducing pollution! ♻️

    **How recycling works — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "🗑️", "Sorting at home",        "You separate your waste into different bins — paper, glass, metal, plastic, food waste. Getting the sorting right at home is the most important step! 🏠"),
        (2, "🚛", "Collection",             "Recycling lorries collect sorted waste separately from general rubbish — mixing them together would contaminate recyclables and send them to landfill! 😢"),
        (3, "🏭", "Materials Recovery",     "At a MATERIALS RECOVERY FACILITY (MRF), machines and workers sort materials further using conveyor belts, magnets (for metals!), air jets, and optical scanners. 🤖"),
        (4, "⚗️", "Processing",            "Each material is processed differently. Paper is pulped with water. Glass is crushed and melted. Metals are melted. Plastic is shredded and re-melted. 🔥"),
        (5, "🏗️", "Made into new products", "The recycled material is formed into new objects — recycled aluminium becomes new cans, recycled paper becomes new cardboard, recycled plastic becomes bottles, clothing, and even furniture! 🪑"),
        (6, "🛒", "You buy it again!",       "When you buy products made from recycled materials, you complete the circle — creating demand for recycling and closing the loop! ♻️🔄"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f3e5f5;">
            <span style="background:#6a1b9a; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#6a1b9a;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### ♻️ What Happens to Each Material?")
    mats = [
        ("📄", "Paper",     "#e8f5e9", "#2e7d32",   "Pulped with water → cleaned → pressed into sheets → new paper or cardboard! Saves 17 trees per tonne recycled. 🌳"),
        ("🥫", "Aluminium", "#fff8e1", "#f57f17",   "Melted down → poured into moulds → rolled into sheets → new cans! Uses 95% LESS energy than mining new aluminium! ⚡"),
        ("🍾", "Glass",     "#e3f2fd", "#0277bd",   "Crushed into cullet → melted at 1,500°C → moulded into new bottles! Can be recycled infinitely with no quality loss! ♾️"),
        ("🧴", "Plastic",   "#fce4ec", "#c62828",   "Shredded → melted → moulded into pellets → new bottles, fleece jackets, garden furniture! But quality degrades — most plastic can only be recycled 2–3 times. ⚠️"),
        ("🍌", "Food waste", "#e0f2f1", "#00695c",  "Composted into rich soil for gardens, or turned into BIOGAS for cooking and electricity! Food waste in landfill produces methane — a powerful greenhouse gas! 🌱"),
    ]
    for icon, name, bg, color, desc in mats:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:10px; padding:0.5rem 0.8rem;
                    margin-bottom:0.3rem; border-left:3px solid {color};
                    display:flex; align-items:flex-start; gap:0.5rem;">
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:{color};">{name}:</strong>
            <span style="font-size:0.85rem; color:#555;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### ♻️ Recycling Facts")
    for icon, label, fact in [
        ("💡", "Glass and energy",     "Recycling one glass bottle saves enough energy to power a light bulb for 4 hours — and glass can be recycled over and over forever without losing quality! 🍾"),
        ("🥤", "Aluminium can",        "A recycled aluminium can is back on the shelf as a new can in just 60 DAYS! And recycling it uses 95% less energy than making new aluminium from bauxite ore. ⚡"),
        ("🌲", "Paper and forests",    "Each tonne of recycled paper saves 17 trees, 32,000 litres of water, and enough electricity to power a home for 6 months! 📰"),
        ("🛍️", "Plastic problem",      "Only about 9% of all plastic ever produced has been recycled. The rest sits in landfills, oceans, or was burned. Plastic takes up to 500 YEARS to break down! ⏳😱"),
        ("🌊", "Ocean plastic",        "About 8 million tonnes of plastic enters the oceans EVERY YEAR — equivalent to a rubbish lorry emptying into the sea every minute. 🚛🌊"),
        ("♻️", "Reduce first!",        "The best recycling is the recycling you never need to do! REFUSE unnecessary packaging, REUSE containers and bags, REPAIR broken items — THEN recycle! 💪"),
    ]:
        fact_row(icon, label, fact, "#f3e5f5", "#6a1b9a")

    if st.button("♻️ Reveal a Recycling Secret!", use_container_width=True, key="recycle_btn"):
        st.session_state.show_recycle_fact = not st.session_state.show_recycle_fact
    if st.session_state.show_recycle_fact:
        st.success("🎉 A fleece jacket made from recycled plastic bottles needs about 25 bottles! "
                   "Companies like Patagonia make entire clothing ranges from ocean plastic — "
                   "turning pollution directly into warm, useful clothing! 🧥🌊 "
                   "And plastic collected from beaches has been turned into everything from "
                   "sunglasses to surfboards to car parts! ♻️😎 "
                   "Pollution can become fashion — if we collect and recycle it! 🌍")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — WATER AND TREES (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💧", "Water and Trees — Earth's Two Greatest Treasures!",
               "Step through why water and forests are the foundations of all life on Earth! 🌳")

planet_steps = [
    ("💧", "Water — The Rarest Treasure in the Universe",
     "Of all the planets we know — hundreds of billions in our galaxy alone — "
     "only Earth has **liquid water on its surface**. Everywhere else is too hot, too cold, or too barren. 🌍\n\n"
     "**Water facts that will change how you see every tap:**\n\n"
     "- 🌊 **97% of Earth's water is salty ocean** — undrinkable without expensive treatment!\n"
     "- 🧊 **2% is frozen** in ice caps and glaciers — most of it inaccessible\n"
     "- 💧 **Only 0.3%** of all Earth's water is fresh liquid water in rivers, lakes, and underground — this tiny fraction supports all land life on Earth! 😱\n"
     "- 🌍 **1 billion people** currently lack access to clean safe drinking water — it is the world's greatest resource inequality\n"
     "- ♻️ **Water is never new** — the water in your glass has existed for billions of years, cycling through oceans, clouds, glaciers, and living creatures countless times! 🦕💧",
     "#e3f2fd", "#0277bd"),
    ("💧", "How We Are Running Out of Freshwater",
     "Despite water covering 71% of Earth, **freshwater scarcity** is one of the world's biggest problems — and it is getting worse! 😟\n\n"
     "- 🌾 **Agriculture uses 70%** of all freshwater withdrawn by humans — irrigating crops to feed a growing world population. Much is lost to evaporation before reaching plant roots! 🌽\n"
     "- 🏭 **Industry uses 20%** — factories, power stations, and manufacturing all require enormous amounts of water for cooling and processing!\n"
     "- 🚰 **Homes use 10%** — drinking, cooking, washing, and garden watering. In many developed countries, the average person uses 150 litres per day!\n"
     "- 🧊 **Glaciers are shrinking** — mountain glaciers supply freshwater to billions of people's rivers during summer. As they melt from climate change, seasonal water supplies will fail!\n"
     "- 💦 **Simple savings matter**: Turning off the tap while brushing teeth saves 12 litres per minute. A shorter shower saves 10 litres per minute. Small habits, multiplied by millions, make a huge difference! 🪥",
     "#e1f5fe", "#0288d1"),
    ("🌳", "Trees — The Lungs, Kidneys, and Air Conditioning of Earth",
     "A single large tree is more than beautiful — it is a working machine that supports life in dozens of ways! 🌳\n\n"
     "- 🌬️ **Oxygen factory**: A mature tree produces enough oxygen for 2 people to breathe for an entire year — through photosynthesis! 🫁\n"
     "- 💧 **Water pump**: A large oak tree absorbs up to 450 litres of water from the soil per day and releases it as water vapour — helping create clouds and rain! ☁️\n"
     "- ❄️ **Air conditioning**: A row of trees can lower air temperature by up to 8°C through shade and evaporation — completely free, natural cooling! 🌡️\n"
     "- 🛡️ **Flood prevention**: Tree roots absorb rainfall and hold soil in place — preventing floods and landslides that kill thousands of people each year! 🌊\n"
     "- 🐾 **Habitat**: A single oak tree can support over 2,300 different species of insects, birds, fungi, and mammals — a single tree is an entire ecosystem! 🦉🐿️",
     "#e8f5e9", "#2e7d32"),
    ("🌲", "Deforestation — The Crisis in Our Forests",
     "Earth's forests are being cut down at an alarming rate — with devastating consequences for climate and biodiversity! 🚨\n\n"
     "- 🌎 **Scale of loss**: About 15 billion trees are cut down every year — and only 5 billion are replanted. Earth loses 10 billion trees annually — net! 😢\n"
     "- 🔥 **Amazon in danger**: The Amazon rainforest — home to 10% of ALL species on Earth — has lost 20% of its area since 1970 to farming, logging, and fires! It generates its own rainfall; if it shrinks too much, it could stop! ⚠️\n"
     "- 🌡️ **Carbon release**: When forests are cleared and burned, all the CO₂ stored in trees over decades is released instantly — deforestation accounts for about 10% of global CO₂ emissions! 🔥\n"
     "- 🌧️ **Rainfall collapse**: Trees create their own rain through transpiration — remove too many trees from a region and rainfall drops, turning forests into deserts! 🏜️\n"
     "- 🌱 **Reforestation heroes**: Organisations and countries are planting billions of trees — Ethiopia planted 350 million trees in a single day in 2019! The Bonn Challenge aims to restore 350 million hectares of forests by 2030. 🌍💪",
     "#e0f2f1", "#00695c"),
    ("💚", "What You Can Do — Every Action Counts!",
     "You might be young — but your actions genuinely matter! Here is why, and what to do: 🌟\n\n"
     "**The power of habit multiplication:**\n"
     "If you turn off the tap while brushing teeth — saving 12 litres — and inspire 10 friends to do the same — "
     "and they each inspire 10 more — within three steps that is 1,000 people saving 12,000 litres per day! "
     "**Your choices ripple outward!** 💧\n\n"
     "**10 things you can do TODAY:**\n"
     "1. 🚰 Turn off taps — don't let water run while brushing\n"
     "2. 🛁 Shorter showers — every minute saved = 10 litres!\n"
     "3. 💡 Switch off lights — when leaving any room\n"
     "4. ♻️ Sort your recycling — carefully, every time\n"
     "5. 🌱 Plant something — a seed, a bulb, any plant helps!\n"
     "6. 🚶 Walk or cycle — instead of short car journeys\n"
     "7. 🥗 Eat less meat — even one meat-free day a week helps\n"
     "8. 🛍️ Say no to plastic bags — bring a reusable one\n"
     "9. 🐦 Feed birds and build bug hotels — support local wildlife\n"
     "10. 📢 Tell others — the most powerful thing you can do is share what you know! 🗣️",
     "#f3e5f5", "#6a1b9a"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="planet_prev"):
        st.session_state.planet_step = max(0, st.session_state.planet_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="planet_next"):
        st.session_state.planet_step = min(len(planet_steps)-1, st.session_state.planet_step + 1)

idx   = st.session_state.planet_step
pstep = planet_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{pstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {pstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{pstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {pstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {pstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{pstep[4]}">●</span>'
                for i in range(len(planet_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            {idx+1} of {len(planet_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — BE A GREEN HERO! (Topic selector)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Be a Green Hero — Actions in Every Part of Life!",
               "Tap each area to discover exactly how to make a difference — starting today! 💚")

hero_actions = {
    "🏠 At Home": {
        "emoji": "🏠", "color": "#1b5e20", "bg": "#e8f5e9",
        "tagline": "💚 Your home is your most powerful place to start!",
        "body": (
            "Your home is where you have the most control — and where small changes add up fastest! 🏡\n\n"
            "- 💡 **Lighting**: Switch off lights every time you leave a room. Replace old bulbs with LEDs — they use 90% less energy and last 25 times longer! Ask a grown-up to check your home's bulbs. 🌟\n"
            "- 🌡️ **Heating**: Put on a jumper before turning up the heating! Draught-proofing doors and windows keeps heat in. A 1°C reduction in thermostat temperature cuts heating bills by 10%! 🧥\n"
            "- 🚿 **Water saving**: Shorter showers (4 minutes saves 40 litres!), turning off taps while brushing (saves 12 litres per minute), and fixing dripping taps (1 drip per second = 10,000 litres wasted per year!) 💧\n"
            "- ♻️ **Recycling at home**: Set up clearly labelled recycling stations — paper, plastic, glass, metal, food waste. Make it easy for everyone in the family to sort correctly every time! 📦\n"
            "- 🛍️ **Plastic reduction**: Switch to reusable bags, beeswax wraps instead of cling film, refillable bottles and coffee cups. Refuse single-use plastic wherever possible! 🌿\n"
            "- 🌱 **Food growing**: Even a small windowsill can grow herbs, tomatoes, or salad leaves — growing your own food uses zero food miles and no packaging! 🍅"
        )
    },
    "🏫 At School": {
        "emoji": "🏫", "color": "#0277bd", "bg": "#e3f2fd",
        "tagline": "📚 Learning AND saving the planet — together!",
        "body": (
            "School is where you spend much of your day — and where collective action is most powerful! 📚\n\n"
            "- 💡 **Energy monitors**: Ask your teacher if you can be the classroom energy monitor — checking lights and screens are off at lunchtime and end of day. One school saved £1,000/year this way! ⚡\n"
            "- 🍽️ **Food waste audit**: Many schools waste 30–40% of food served. A food waste audit project can identify what is being wasted and why — leading to real changes in portions and menus! 🥗\n"
            "- 🌿 **School garden**: A school garden teaches biology, science, and environmental care while producing real food! Growing vegetables for the school canteen closes the food loop beautifully! 🥬\n"
            "- ♻️ **Recycling champions**: Start a school recycling programme — separate bins for paper, plastic, and cans. Educate younger children about why sorting matters. 📊\n"
            "- 🚲 **Cycle to school**: Walking and cycling schemes reduce car congestion, improve fitness, and cut emissions. Many schools now have 'Walk on Wednesdays' or cycle challenges! 🚶🏼\n"
            "- 🐾 **Wildlife area**: A wild corner of the school field with native plants, a bug hotel, and bird feeders creates a living classroom and sanctuary for local wildlife! 🦋"
        )
    },
    "🛒 Shopping": {
        "emoji": "🛒", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🛍️ Every purchase is a vote for the world you want!",
        "body": (
            "What you buy (or don't buy!) is one of the most powerful environmental choices you make! 💰\n\n"
            "- 🌱 **Buy local and seasonal**: Food grown nearby uses far less fuel for transport — and seasonal food needs no heated greenhouses. A local apple has a carbon footprint 10x smaller than an air-freighted one! 🍎\n"
            "- 🥩 **Eat less meat**: Producing 1 kg of beef uses 15,000 litres of water and generates 27 kg of CO₂. 1 kg of lentils uses 50 litres and generates 0.9 kg. Swapping one meal a week makes a real difference! 🌿\n"
            "- 🧥 **Buy second-hand**: Fast fashion is enormously polluting — the fashion industry generates 10% of global CO₂! Buying second-hand clothes gives them a new life and saves all the resources to make new ones. 👗\n"
            "- 📦 **Less packaging**: Choose loose fruit and vegetables over pre-packaged. Choose products with minimal, recyclable packaging. Vote with your wallet for better packaging! 🥦\n"
            "- 🔋 **Choose rechargeable**: Rechargeable batteries replace hundreds of single-use batteries — saving money and reducing toxic heavy metals from entering landfill! ♻️\n"
            "- 🛠️ **Repair instead of replace**: Before buying new, can it be fixed? A repaired toy, phone, or bicycle saves all the resources and energy needed to manufacture a replacement! 🔧"
        )
    },
    "🌿 In Nature": {
        "emoji": "🌿", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🌿 Connecting with nature is the first step to protecting it!",
        "body": (
            "You cannot love what you do not know — spending time in nature builds the connection that drives action! 🌳\n\n"
            "- 🌱 **Plant something**: Every plant helps! Trees absorb CO₂, provide oxygen, shelter wildlife, cool the air. One tree planted = decades of environmental service! 🌳\n"
            "- 🐝 **Pollinator garden**: Plant wildflowers, lavender, and native plants in any space — even a pot on a balcony feeds bees, butterflies, and hoverflies essential to our food supply! 🌸\n"
            "- 🦔 **Leave wild corners**: A pile of logs, a patch of long grass, a compost heap — these create habitats for hedgehogs, beetles, frogs, and countless creatures! 🐸\n"
            "- 🚯 **Litter picking**: Organise a local litter pick — removing litter from parks, roadsides, and beaches directly protects wildlife from ingesting plastic and chemical contamination! 🧹\n"
            "- 🔭 **Nature journaling**: Record the birds, insects, and plants you see — you can upload sightings to citizen science apps like iNaturalist that help real scientists track biodiversity! 📱\n"
            "- 💧 **Water wildlife**: A shallow bowl of clean water in the garden or on a windowsill is a lifeline for birds, hedgehogs, and insects during hot dry spells! 🐦"
        )
    },
    "🚗 Transport": {
        "emoji": "🚗", "color": "#6a1b9a", "bg": "#f3e5f5",
        "tagline": "🚲 How you travel is one of your biggest environmental choices!",
        "body": (
            "Transport generates about 16% of global greenhouse gas emissions — and there are great alternatives! 🌍\n\n"
            "- 🚶 **Walk short journeys**: Any journey under 1 km is faster to walk than to drive once you factor in parking! Walking is free, healthy, and zero emissions. 👟\n"
            "- 🚲 **Cycle**: A bicycle produces zero emissions, costs almost nothing to run, and keeps you fit. E-bikes extend cycling range for longer journeys. The Netherlands has more bikes than people! 🇳🇱\n"
            "- 🚌 **Use public transport**: A full bus emits 80% less CO₂ per passenger than a single-occupancy car. A full train emits 90% less. Every passenger using public transport makes a difference! 🚂\n"
            "- ✈️ **Fly less**: Aviation is the most carbon-intensive form of travel — one return flight from London to New York emits as much CO₂ as 3 months of average driving! Video calls replace most business travel! 💻\n"
            "- ⚡ **Electric vehicles**: Electric cars emit zero exhaust emissions — and as the electricity grid gets greener, their lifetime emissions keep falling. Battery technology is improving rapidly! 🔋\n"
            "- 🏘️ **Live locally**: The greenest transport solution is not needing to travel far — walkable neighbourhoods with local shops, schools, and parks eliminate many journeys entirely! 🏡"
        )
    },
    "💬 Spread the Word": {
        "emoji": "💬", "color": "#c62828", "bg": "#ffebee",
        "tagline": "📢 Your voice is your most powerful green tool of all!",
        "body": (
            "Individual actions matter — but collective action, driven by communication, changes the world! 🌍\n\n"
            "- 🗣️ **Talk about it**: Share what you have learned with family, friends, and classmates. When Greta Thunberg started talking about climate change at age 15, she inspired millions worldwide! 🌱\n"
            "- 📝 **Write letters**: Writing to your local councillor, MP, or school headteacher about environmental issues is a powerful democratic act — politicians DO read letters from young people! ✉️\n"
            "- 📚 **Read and learn**: The more you know, the more powerfully you can act and speak. Read books, watch documentaries, follow scientists and environmental organisations. Knowledge is power! 🔬\n"
            "- 🎨 **Make art**: Environmental art, posters, stories, and videos communicate emotions that facts sometimes cannot reach. Creative expression changes minds and moves hearts! 🖼️\n"
            "- 🌍 **Join groups**: Environmental clubs at school, nature groups, youth climate organisations — collective action achieves what individuals cannot. Find your team! 🤝\n"
            "- 🌟 **Lead by example**: The most persuasive thing you can do is live your values visibly — when others see you turning off lights, cycling, and recycling, they notice and think about their own choices! 💚"
        )
    },
}

h_cols = st.columns(len(hero_actions))
for i, (hname, hdata) in enumerate(hero_actions.items()):
    with h_cols[i]:
        short = hname.split(" ", 1)[1]
        if st.button(hdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"hero_{i}"):
            st.session_state.hero_picked = hname

if st.session_state.hero_picked and st.session_state.hero_picked in hero_actions:
    hname = st.session_state.hero_picked
    hdata = hero_actions[hname]
    st.markdown(f"""
    <div style="background:{hdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {hdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{hdata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {hname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{hdata['color']}; font-weight:700;">
                    {hdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(hdata["body"])
else:
    st.info("👆 Tap any category above to discover exactly how to be a Green Hero there!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — ANIMALS IN DANGER
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦁", "Animals Endangered by Human Activity!",
               "Meet the incredible creatures whose futures depend on our choices — tap to discover! 🌍")

endangered_animals = {
    "🐻‍❄️ Polar Bear": {
        "emoji": "🐻‍❄️", "color": "#0277bd", "bg": "#e1f5fe",
        "tagline": "🧊 The living symbol of climate change!",
        "body": (
            "The polar bear is the most recognisable symbol of climate change — their survival is directly tied to Arctic sea ice! 🧊\n\n"
            "- 🌡️ **Shrinking sea ice**: Polar bears hunt seals from sea ice — swimming between ice floes. As Arctic temperatures rise 4x faster than the global average, summer sea ice is disappearing rapidly. 😢\n"
            "- 🍽️ **Starvation risk**: Without sea ice, polar bears cannot hunt seals — their primary food source. Bears are spending longer on land, losing weight, and producing fewer cubs.\n"
            "- 📊 **Population**: About 26,000 polar bears remain — a number that could fall dramatically by 2100 if warming continues on current trajectories. Some subpopulations are already declining critically.\n"
            "- 🔬 **Scientific monitoring**: Scientists tag and track polar bears by helicopter to monitor health and movement — essential data for understanding and predicting population changes.\n"
            "- 💚 **How you help**: Every action reducing CO₂ helps preserve the Arctic! Reducing energy use, supporting renewable energy, and choosing low-carbon transport all contribute to keeping polar bears' home frozen. ❄️"
        )
    },
    "🐋 Blue Whale": {
        "emoji": "🐋", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "🌊 The largest animal ever — still endangered!",
        "body": (
            "The blue whale is the largest animal ever to have lived on Earth — yet it is still recovering from near-extinction! 🌊\n\n"
            "- 🐋 **Hunted to near extinction**: Commercial whaling in the 20th century reduced blue whale populations from 350,000 to just 360–1,300 individuals by the 1960s — a 99.9% population collapse! 😱\n"
            "- 📈 **Slow recovery**: Since whaling was banned internationally in 1986, populations have slowly recovered to about 10,000–25,000 — but they are still endangered. Blue whales reproduce very slowly — a female gives birth only once every 2–3 years.\n"
            "- 🚢 **Ship strikes**: One of the biggest threats today is collision with large ships — blue whales surface to breathe in the same shipping lanes that criss-cross the ocean. 🚢\n"
            "- 🔊 **Noise pollution**: Sonar and engine noise from ships disrupts the whale's long-distance communication songs — which can travel thousands of kilometres in quiet ocean and are essential for finding mates. 🎵\n"
            "- 🌡️ **Climate impact**: Warming oceans shift the distribution of krill (their tiny prey) — forcing blue whales to travel further for food and disrupting established migration patterns.\n"
            "- 💚 **Whales fight climate change**: Each blue whale stores about 33 tonnes of CO₂ in its body — and whale faeces fertilise phytoplankton that absorbs CO₂! Protecting whales actually helps fight climate change! 🌿"
        )
    },
    "🦋 Monarch Butterfly": {
        "emoji": "🦋", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🌸 A 4,000 km migration — under threat!",
        "body": (
            "The monarch butterfly performs one of nature's most extraordinary migrations — and its population has crashed by 90%! 🌸\n\n"
            "- 🗺️ **Epic migration**: Every autumn, hundreds of millions of monarchs fly up to 4,000 km from Canada and the USA to overwinter in specific forests in central Mexico — a journey spanning 3 generations! 🌎\n"
            "- 📉 **Population collapse**: The eastern North American monarch population has fallen from an estimated 1 billion in the 1990s to about 100 million today — a 90% decline in 30 years. 😢\n"
            "- 🌿 **Milkweed loss**: Monarch caterpillars ONLY eat milkweed — but milkweed has been eliminated from farmland by herbicides and agricultural intensification, removing the butterflies' only food source!\n"
            "- 🌡️ **Climate disruption**: Warmer winters are disrupting the timing signals monarchs use to begin migration — they may leave too late, or arrive at overwintering sites that are no longer suitable.\n"
            "- 🏚️ **Forest loss**: The specific oyamel fir forests in Mexico where monarchs overwinter are being illegally logged — removing their only winter shelter.\n"
            "- 💚 **How to help**: Plant milkweed and native wildflowers! Even a small garden patch of the right native plants creates an essential feeding stop on the migration highway. 🌼"
        )
    },
    "🦏 Rhino": {
        "emoji": "🦏", "color": "#6d4c41", "bg": "#efebe9",
        "tagline": "🔱 Poaching has pushed them to the brink!",
        "body": (
            "Rhinoceroses have roamed Earth for 50 million years — but human activity has brought several species to the very edge of extinction in just decades! 😔\n\n"
            "- 🔱 **Horn poaching**: Rhino horn is illegally sold in some parts of Asia where it is falsely believed to have medicinal properties — despite being made of the same material as your fingernails (keratin)! The horn is worth more than gold by weight, driving relentless poaching.\n"
            "- 📊 **Numbers**: The Northern White Rhino has just 2 individuals remaining — both female. Scientists are attempting IVF using frozen sperm to save the subspecies from extinction! 🔬\n"
            "- 🏞️ **Habitat loss**: Agricultural expansion has destroyed most of the natural grasslands and forests rhinos need — confining surviving populations to small protected areas.\n"
            "- 🛡️ **Armed guards**: In some African reserves, rhinos are protected 24 hours a day by armed rangers — a heartbreaking reflection of how far human greed can reach.\n"
            "- 💉 **Dehorning**: Some conservation programmes safely remove rhino horns (which regrow!) to make the animals worthless to poachers — a drastic but pragmatic response.\n"
            "- 💚 **Hope**: Southern White Rhino numbers have recovered from under 50 in 1895 to over 20,000 today — proof that conservation works when given sufficient resources and commitment! 🌟"
        )
    },
    "🐸 Amphibians": {
        "emoji": "🐸", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "🌿 The most threatened animal group on Earth!",
        "body": (
            "Frogs, toads, salamanders, and newts are disappearing faster than any other animal group — they are Earth's ecological alarm system! 🌡️\n\n"
            "- 📉 **Crisis scale**: About 41% of all amphibian species are threatened with extinction — more than birds, mammals, or reptiles. Over 200 species have gone extinct since 1970! 😱\n"
            "- 🦠 **Chytrid fungus**: A devastating fungal disease (Batrachochytrium dendrobatidis) has spread globally — killing amphibians by infecting their skin and disrupting breathing and water absorption. It has caused the biggest disease-driven biodiversity loss in vertebrate history!\n"
            "- 💧 **Pollution sensitivity**: Amphibians breathe through their porous skin — making them extraordinarily sensitive to pesticides, herbicides, and water pollution. They are dying from chemicals that barely affect other animals.\n"
            "- 🌡️ **Climate vulnerability**: As cold-blooded animals dependent on specific temperature and moisture conditions, climate change disrupts every aspect of amphibian life — breeding, feeding, and hibernation timing.\n"
            "- 🏞️ **Wetland loss**: 35% of the world's wetlands have been drained since 1970 — destroying the breeding and feeding habitat that amphibians depend on.\n"
            "- 💚 **Why it matters**: Amphibians control insect populations (one frog eats thousands of mosquitoes per year!), are eaten by birds, snakes, and fish, and indicate ecosystem health. Lose the frogs and the whole food web wobbles! 🕸️"
        )
    },
    "🐘 Elephant": {
        "emoji": "🐘", "color": "#546e7a", "bg": "#eceff1",
        "tagline": "🌍 Ecosystem engineers — we cannot afford to lose them!",
        "body": (
            "Elephants are not just magnificent animals — they are **keystone species** that create and maintain entire ecosystems! 🌍\n\n"
            "- 🌳 **Forest architects**: African forest elephants disperse seeds of over 300 tree species across vast distances in their dung — many large trees can ONLY be dispersed this way. Lose the elephants, lose the forest. 💩🌱\n"
            "- 💧 **Water engineers**: Elephants dig water holes during dry seasons that dozens of other species drink from. They push over trees that die and create open clearings. They are literally building their neighbours' homes! 🏡\n"
            "- 📉 **Population loss**: African savanna elephant numbers have fallen from 3–5 million in the early 20th century to about 415,000 today. Forest elephants have declined by 86% in 31 years — classified as Critically Endangered! 😢\n"
            "- 🔱 **Ivory poaching**: Despite an international ivory trade ban since 1989, illegal poaching continues — an estimated 20,000 African elephants are killed every year for their tusks!\n"
            "- 🏞️ **Human-elephant conflict**: As human settlements expand into elephant habitat, conflicts increase — elephants raid crops, families suffer, and retaliatory killing occurs. Solving this conflict is essential for coexistence.\n"
            "- 💚 **Carbon heroes**: Each forest elephant contributes to storing about 9,500 tonnes of carbon by maintaining the forest ecosystem — making their protection a climate solution too! 🌡️"
        )
    },
}

an_cols = st.columns(len(endangered_animals))
for i, (aname, adata) in enumerate(endangered_animals.items()):
    with an_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"endg_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in endangered_animals:
    aname = st.session_state.animal_picked
    adata = endangered_animals[aname]
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
    st.info("👆 Tap any animal above to discover how human activity is affecting its survival!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — GREEN HERO PLEDGE
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🏅", "Your Green Hero Pledge!",
               "Six powerful commitments — choose yours and start today! 💚")

col1, col2 = st.columns(2, gap="large")
pledge_items = [
    ("💧", "I Will Save Water Every Day!",
     "I promise to turn off the tap while brushing my teeth, take shorter showers, "
     "and remind my family not to let water run unnecessarily. "
     "Every litre I save is a litre preserved for people, animals, and ecosystems that need it. "
     "Water is the most precious substance on Earth — I will treat it that way! 🚰💙",
     "#e3f2fd", "#0277bd"),
    ("♻️", "I Will Recycle Carefully!",
     "I promise to sort my recycling correctly every single time — paper, glass, metal, plastic separately. "
     "I will learn what can and cannot be recycled in my area. "
     "I will choose products with less packaging and carry a reusable bag. "
     "When I recycle correctly, I save energy, raw materials, and reduce landfill! 🌍",
     "#f3e5f5", "#6a1b9a"),
    ("🌱", "I Will Plant and Protect Nature!",
     "I promise to plant at least one thing this year — a seed, a bulb, a sapling. "
     "I will help create habitat for wildlife in my garden or community. "
     "I will learn the names of birds, trees, and insects near my home. "
     "You cannot protect what you do not know and love — and I will know and love nature! 🌳🐝",
     "#e8f5e9", "#1b5e20"),
    ("💡", "I Will Use Energy Wisely!",
     "I promise to switch off lights when I leave a room, unplug chargers not in use, "
     "and wear a jumper before asking for the heating to go up. "
     "I will learn about renewable energy and support the transition to clean power. "
     "Energy is precious — I will use only what I need! ⚡🏠",
     "#fff8e1", "#f57f17"),
    ("🥗", "I Will Make Climate-Friendly Food Choices!",
     "I promise to try new vegetables and plant-based foods with an open mind. "
     "I will eat less meat — even one meat-free day a week makes a real difference! "
     "I will reduce food waste by taking only what I will eat. "
     "The food I choose is one of my most powerful daily environmental decisions! 🌿🍽️",
     "#e0f2f1", "#00695c"),
    ("📢", "I Will Speak Up for Our Planet!",
     "I promise to share what I have learned about our planet with others — "
     "family, friends, classmates — kindly and with hope, not fear. "
     "I will vote with my choices, my voice, and when I am old enough, my vote. "
     "I am part of the generation that will define Earth's future — "
     "and I choose to be a Green Hero! 🌍💚✨",
     "#fce4ec", "#c62828"),
]
for i, (emoji, title, body, bg, border) in enumerate(pledge_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Which of the six pledges above means the most to you personally? What ONE action will you start tomorrow? 🌍💪💚")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Planet Quiz — Test What You Know!",
               "6 important questions about our Earth — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 💧 — What percentage of Earth's water is drinkable fresh liquid water in rivers, lakes, and underground?",
        "opts": ["About 50%", "About 25%", "About 3%", "About 0.3%"],
        "ans":  "About 0.3%",
        "explain": "Only about 0.3% of all Earth's water is fresh liquid water accessible in rivers, lakes, and underground aquifers! 97% is salty ocean and almost 2% is frozen in ice caps. Every drop of fresh water is extraordinarily precious! 💧😱"
    },
    {
        "q":    "Q2 🌡️ — What is the main cause of climate change?",
        "opts": ["Volcanoes erupting more often", "The Sun getting hotter", "Extra greenhouse gases from burning fossil fuels trapping more heat", "The oceans evaporating more water"],
        "ans":  "Extra greenhouse gases from burning fossil fuels trapping more heat",
        "explain": "Burning coal, oil, and gas releases extra CO₂ into the atmosphere — thickening the natural greenhouse gas blanket. This traps more of Earth's heat, raising global temperatures. It is the primary cause, confirmed by thousands of scientists worldwide! 🌡️🏭"
    },
    {
        "q":    "Q3 ♻️ — Recycling one aluminium can saves how much of the energy needed to make a new one?",
        "opts": ["About 10%", "About 50%", "About 75%", "About 95%"],
        "ans":  "About 95%",
        "explain": "Recycling aluminium saves a stunning 95% of the energy needed to mine and process new aluminium from raw ore! A recycled can is back on the shelf in just 60 days. Aluminium can also be recycled infinitely without losing quality! ♻️⚡"
    },
    {
        "q":    "Q4 🌳 — What important gas does a mature tree produce enough of to support 2 people per year?",
        "opts": ["Carbon dioxide", "Nitrogen", "Oxygen", "Hydrogen"],
        "ans":  "Oxygen",
        "explain": "A mature tree produces enough OXYGEN through photosynthesis to support approximately 2 people breathing for an entire year! Trees also absorb CO₂, regulate water, cool the air, prevent floods, and support thousands of species. 🌳🫁"
    },
    {
        "q":    "Q5 🐻‍❄️ — Why are polar bears endangered by climate change?",
        "opts": ["Their fur is too thick for warmer temperatures", "They cannot swim in warming oceans", "Melting sea ice removes the platform they hunt seals from", "Warmer weather means fewer fish to eat"],
        "ans":  "Melting sea ice removes the platform they hunt seals from",
        "explain": "Polar bears hunt seals from floating sea ice — swimming between floes. As climate change melts Arctic sea ice, the bears' hunting platform disappears! They cannot hunt, lose weight, produce fewer cubs, and face starvation on land. ❄️🐻‍❄️"
    },
    {
        "q":    "Q6 🌍 — Which of these actions saves the MOST water?",
        "opts": ["Drinking tap water instead of bottled", "Turning off the tap while brushing teeth", "Taking a 4-minute shower instead of a bath", "Watering plants in the evening instead of morning"],
        "ans":  "Taking a 4-minute shower instead of a bath",
        "explain": "A 4-minute shower uses about 36 litres of water — a typical bath uses 80 litres! That saves 44 litres every time. Turning off the tap while brushing also saves about 12 litres per minute — both are brilliant habits! 🚿💧"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"pl_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="pl_quiz_submit"):
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
        (6, "🏆", "ULTIMATE GREEN HERO! 🌍💚✨",           "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Planet Protector! 🌱",        "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Earth Guardian! ♻️",              "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Green Explorer! 🌿",          "#2e7d32", "#e8f5e9"),
        (0, "✨", "Keep Learning — Our Planet Needs You!", "#0277bd", "#e3f2fd"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="pl_quiz_reset"):
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
               "Saving Our Planet — your quick recap! 🎉")

summary_items = [
    ("🌍", "Our Earth",      "The most special planet we know — unique, fragile, and ours to protect!"),
    ("🌡️", "Climate Change", "Extra CO₂ from fossil fuels is warming Earth — but we can change it!"),
    ("♻️", "Recycling",      "Giving materials new life — saving energy, resources, and reducing waste!"),
    ("💧", "Water",          "Only 0.3% is fresh liquid water — every drop is precious!"),
    ("🌳", "Trees",          "The lungs of Earth — oxygen, water, carbon, habitat, all in one!"),
    ("💚", "YOU!",           "Every action counts — you are already a Green Hero in the making!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #1b5e20;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1a1a4e,#2d4a8c);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">🌍 Keep it green, little one,its our only Home! 🌟</div>
    <div style="color:#c8daff; font-size:0.95rem;">
        The Earth is our only Home, so let's take care of it!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.8rem;">
        ☀️ 🌍 🌡️ ♻️ 🌳 💧 💚
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
