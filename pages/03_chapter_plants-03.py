import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 03 · Parts of a Plant", layout="wide", initial_sidebar_state="expanded")

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
if "show_root_fact"    not in st.session_state: st.session_state.show_root_fact    = False
if "show_stem_fact"    not in st.session_state: st.session_state.show_stem_fact    = False
if "show_leaf_fact"    not in st.session_state: st.session_state.show_leaf_fact    = False
if "show_flower_fact"  not in st.session_state: st.session_state.show_flower_fact  = False
if "show_seed_fact"    not in st.session_state: st.session_state.show_seed_fact    = False
if "plant_picked"      not in st.session_state: st.session_state.plant_picked      = None
if "growth_step"       not in st.session_state: st.session_state.growth_step       = 0
if "quiz_answers"      not in st.session_state: st.session_state.quiz_answers      = {}
if "quiz_submitted"    not in st.session_state: st.session_state.quiz_submitted    = False

# ─── Helpers ─────────────────────────────────────────────────────────────────
def fun_card(emoji, title, body, bg="#f1f8e9", border="#66bb6a"):
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
    <div style="background:linear-gradient(135deg,#e8f5e9,#f1f8e9);
                border-radius:20px; padding:1rem 1.4rem; margin:0.8rem 0;
                border:2px dashed #66bb6a; text-align:center;">
        <span style="font-size:1.5rem;">🤔</span>
        <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;
                     font-size:0.97rem;">{question}</span>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#1b5e20,#388e3c,#1b5e20);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#a5d6a7; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 03 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.3);">
        🌱 Parts of a Plant 🌸
    </h1>
    <p style="color:#c8e6c9; font-size:1.05rem; margin:0.8rem 0 0;">
        Discover how amazing plants really are — let's explore together!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        🌿 🌻 🌱 🍀 🌺 🌿
    </div>
</div>
""", unsafe_allow_html=True)

# Learning goals
with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ Why plants are **living things**
        - ✅ The **5 main parts** of a plant
        - ✅ What **roots, stems & leaves** do
        - ✅ How plants make their own **food**
        """)
    with col2:
        st.markdown("""
        - ✅ How flowers make **seeds**
        - ✅ How a seed grows into a **plant**
        - ✅ Amazing **weird & wonderful** plants
        - ✅ A fun **quiz** with badges!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — PLANTS ARE ALIVE!
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌿", "Plants Are Living Things!",
               "They grow, breathe, eat, and make babies — just like us!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Look around you — in your garden, at the park, in pots at home. 
    **Plants are everywhere!** 🌍

    Plants are **living things**, just like you, your pet, and the birds outside.
    That means they can:
    """)
    c1, c2, c3, c4 = st.columns(4)
    for col, icon, word in zip(
        [c1, c2, c3, c4],
        ["🌱", "🍽️", "💧", "🌰"],
        ["Grow", "Make Food", "Need Water", "Make Seeds"]
    ):
        with col:
            st.markdown(f"""
            <div style="background:#f1f8e9; border-radius:12px; padding:0.8rem;
                        text-align:center; border:2px solid #a5d6a7;">
                <div style="font-size:2rem;">{icon}</div>
                <div style="font-weight:700; font-size:0.9rem; color:#2e7d32;">{word}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-top:0.8rem;"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
    Unlike you and me, plants **cannot walk to a shop** to buy food. 
    Instead, they are super clever — they **make their own food** using sunlight, 
    water, and air! Isn't that amazing? 🌟
    """)
    think_bubble("Can you name 3 plants you have seen today?")

with col2:
    fun_card("🌳", "Plants & Trees",
             "All trees are plants! The enormous oak tree in the park and the tiny "
             "daisy on the grass are both plants — just very different sizes.",
             bg="#f1f8e9", border="#43a047")
    fun_card("🌊", "Plants Need Water",
             "Just like you get thirsty and need to drink water, plants get thirsty too! "
             "They drink water through their roots underground.",
             bg="#e8f4fd", border="#4a90e2")
    fun_card("☀️", "Plants Need Sunlight",
             "Put a plant in a dark room and it will slowly get sick and turn yellow. "
             "Sunlight is like a plant's energy drink!",
             bg="#fff8e1", border="#f9a825")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE 5 PARTS OF A PLANT
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌻", "The 5 Main Parts of a Plant",
               "Every part has an important job to do!")

# Visual plant diagram using columns
st.markdown("""
<div style="background:linear-gradient(180deg,#e3f2fd 0%,#e8f5e9 50%,#d7ccc8 100%);
            border-radius:20px; padding:1.5rem; margin-bottom:1rem; text-align:center;">
    <div style="font-size:0.85rem; color:#5d4037; font-weight:600; margin-bottom:0.3rem;">
        SKY ☁️
    </div>
    <div style="font-size:3.5rem; line-height:1.1;">🌸</div>
    <div style="font-size:0.85rem; font-weight:600; color:#6a1b9a;">← FLOWER</div>
    <div style="font-size:2.5rem; line-height:1.1;">🍃🍃</div>
    <div style="font-size:0.85rem; font-weight:600; color:#2e7d32;">← LEAVES</div>
    <div style="font-size:1.5rem; line-height:1.5; color:#795548; font-weight:700;">|</div>
    <div style="font-size:0.85rem; font-weight:600; color:#795548;">← STEM</div>
    <div style="font-size:1.5rem; line-height:1.0; color:#795548; font-weight:700;">|</div>
    <div style="background:#d7ccc8; border-radius:0 0 16px 16px; padding:0.6rem;
                margin: 0 -1.5rem -1.5rem -1.5rem; border-top:3px dashed #a1887f;">
        <div style="font-size:0.85rem; color:#4e342e; font-weight:600;">UNDERGROUND 🌍</div>
        <div style="font-size:1.8rem;">〰️〰️〰️</div>
        <div style="font-size:0.85rem; font-weight:600; color:#5d4037;">← ROOTS</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("#### 👇 Learn about each part to discover what it does!")

# ─── ROOTS ────────────────────────────────────────────────────────────────────

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🪱 Part 1 — The Roots")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Roots are hidden underground where we can't normally see them.
    They spread out in the soil like fingers reaching out in all directions!

    **Roots have two very important jobs:**
    """)
    fun_card("💧", "Job 1: Drink Water",
             "Roots are like drinking straws! They suck up water and minerals from the soil "
             "and send them all the way up to the leaves. A plant with no roots would dry up and die.",
             bg="#e8f4fd", border="#1e88e5")
    fun_card("⚓", "Job 2: Hold the Plant",
             "Roots grip the soil tightly so the plant doesn't fall over in the wind. "
             "The bigger the tree, the deeper and wider its roots grow!",
             bg="#efebe9", border="#795548")
with col2:
    st.markdown("""
    ##### 🌱 Amazing Root Facts
    """)
    for icon, label, fact in [
        ("🌳", "Tree Roots", "A large oak tree can have roots that spread out as wide as the tree is tall — sometimes 30 metres!"),
        ("🥕", "Eating Roots", "Carrots, radishes, and sweet potatoes are all roots that we eat — yummy! 😋"),
        ("🏜️", "Desert Roots", "Cactus roots spread out very wide but not deep, to catch every drop of rain before it disappears."),
        ("💪", "Strong Grip", "Roots of one large tree can hold tonnes of soil in place, stopping it from washing away in rain."),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f9fbe7;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#558b2f;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🪱 Reveal a Root Secret!", use_container_width=True, key="root_btn"):
        st.session_state.show_root_fact = not st.session_state.show_root_fact
    if st.session_state.show_root_fact:
        st.success("🎉 The roots of a single rye grass plant, if laid end to end, "
                   "would stretch for over 600 kilometres — longer than the whole of Pakistan from north to south! 🤯")

think_bubble("If you water a plant, where does the water go first — roots or leaves?")

# ─── STEM ─────────────────────────────────────────────────────────────────────

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🌱 Part 2 — The Stem")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    The **stem** is the tall, strong part of the plant that holds everything up.
    Look at a sunflower — its long green stalk is the stem!

    **The stem has two brilliant jobs:**
    """)
    fun_card("🏗️", "Job 1: Support",
             "The stem holds up the leaves and flowers so they can reach the sunlight. "
             "Without the stem, the plant would just be a pile on the ground!",
             bg="#f9fbe7", border="#8bc34a")
    fun_card("🚿", "Job 2: Transport Water",
             "The stem works like a network of tiny pipes. Water travels UP the stem "
             "from the roots to the leaves, and food travels DOWN from the leaves to the roots.",
             bg="#e8f4fd", border="#29b6f6")
with col2:
    st.markdown("##### 🌿 Stem Surprises")
    for icon, label, fact in [
        ("🌵", "Cactus Stems", "A cactus stores water inside its thick, juicy stem — that is its secret for surviving in the desert with no rain!"),
        ("🎋", "Bamboo", "Bamboo is actually a grass with a very thick, hollow stem. It is one of the fastest-growing plants on Earth — it can grow 90cm in ONE day!"),
        ("🥔", "Potato!", "A potato is actually an underground stem — not a root! It stores food that the plant can use later."),
        ("🌹", "Rose Thorns", "The sharp thorns on a rose stem help protect the plant from animals that want to eat it."),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f1f8e9;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#33691e;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌿 Tap for a Stem Surprise!", use_container_width=True, key="stem_btn"):
        st.session_state.show_stem_fact = not st.session_state.show_stem_fact
    if st.session_state.show_stem_fact:
        st.success("🎉 If you put a white flower (like a white carnation) in coloured water, "
                   "the stem drinks the coloured water and the petals slowly turn that colour! "
                   "You can try this experiment at home! 🌸🔵")

think_bubble("Why do you think tall trees need such thick, strong stems?")

# ─── LEAVES ───────────────────────────────────────────────────────────────────

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🍃 Part 3 — The Leaves")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Leaves are flat and green and they are the most important part of the plant for 
    making food. Most plants have lots of leaves spread out to catch as much sunlight as possible.

    **Leaves do something magical called PHOTOSYNTHESIS** (say it: *fo-to-SIN-the-sis*) 🌟
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f5e9,#f9fbe7);
                border-radius:16px; padding:1.2rem 1.4rem; margin:0.6rem 0;
                border:2px solid #81c784;">
        <div style="font-weight:700; color:#2e7d32; font-size:1rem; margin-bottom:0.8rem;">
            🧪 The Recipe for Leaf Food:
        </div>
        <div style="display:flex; align-items:center; justify-content:center;
                    flex-wrap:wrap; gap:0.5rem; font-size:1rem; text-align:center;">
            <span>☀️ Sunlight</span>
            <span style="color:#aaa;">+</span>
            <span>💧 Water</span>
            <span style="color:#aaa;">+</span>
            <span>💨 Air (CO₂)</span>
            <span style="color:#aaa;">=</span>
            <span style="font-weight:700; color:#2e7d32;">🍬 Food for the Plant!</span>
        </div>
        <div style="font-size:0.87rem; color:#558b2f; margin-top:0.7rem; text-align:center;">
            And as a bonus, leaves release OXYGEN — the fresh air that WE breathe! 🌬️
        </div>
    </div>
    """, unsafe_allow_html=True)

    fun_card("🟢", "Why Are Leaves Green?",
             "Leaves have a special green stuff called CHLOROPHYLL inside them. "
             "Chlorophyll is what captures sunlight and helps make food. "
             "It also gives leaves their beautiful green colour!",
             bg="#f1f8e9", border="#43a047")
with col2:
    st.markdown("##### 🍂 Leaf Facts")
    for icon, label, fact in [
        ("🌬️", "Breathing",   "Leaves have tiny invisible holes called stomata that breathe in air — just like your nose!"),
        ("🍂", "Autumn",      "In autumn, trees stop making chlorophyll. Without green, we can see the hidden red, orange and yellow colours in the leaves!"),
        ("🌵", "Needles",     "Pine tree needles are actually very thin leaves! Their thin shape helps them survive cold winters."),
        ("🐛", "Eating Bugs", "The Venus Flytrap has special leaves that snap shut to catch and eat insects! It gets minerals from bugs that it can't get from the soil."),
        ("📐", "Patterns",    "Leaves have lines called veins that carry water around the leaf — just like the veins in your hand!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f9fbe7;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#558b2f;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🍃 Leaf Secret — Click Me!", use_container_width=True, key="leaf_btn"):
        st.session_state.show_leaf_fact = not st.session_state.show_leaf_fact
    if st.session_state.show_leaf_fact:
        st.success("🎉 Trees give us the air we breathe! One large tree produces enough "
                   "oxygen for 2–4 people to breathe for an entire year. "
                   "Trees are our best friends! 🌳💚")

think_bubble("If you covered a leaf with black paper so no sunlight could reach it, what do you think would happen?")

# ─── FLOWERS ──────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🌸 Part 4 — The Flowers")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Flowers are the colourful, beautiful part of a plant. But they are not just 
    pretty to look at — they have a very important job!

    **A flower's job is to make SEEDS** 🌱 — so that new plants can grow!

    Here is how it works — it's like a team effort between flowers and bees! 🐝
    """)
    for step, icon, title, desc in [
        (1, "🌸", "Flowers Bloom",       "The flower opens up and makes a sweet liquid called NECTAR inside it."),
        (2, "🐝", "Bees Visit",           "Bees fly to the flower to collect nectar. They accidentally pick up tiny yellow dust called POLLEN."),
        (3, "✈️", "Pollen Travels",       "The bee flies to another flower, carrying the pollen with it on its fluffy body."),
        (4, "🌱", "Seeds Form",           "The pollen reaches the new flower and seeds begin to grow inside it!"),
        (5, "💨", "Seeds Spread",         "Seeds travel by wind, water, or animals to find new soil where new plants can grow."),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.5rem 0.7rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fce4ec;">
            <span style="background:#e91e63; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#880e4f;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### 🌺 Flower Facts")
    for icon, label, fact in [
        ("🌈", "Colours",   "Flowers are bright to attract bees, butterflies and birds who help spread their pollen!"),
        ("👃", "Smell",     "Many flowers make sweet smells to attract insects from far away. Roses and jasmine are famous for their perfume!"),
        ("🌻", "Sunflower", "A sunflower is not one flower — it is actually made of up to 2,000 tiny flowers packed together!"),
        ("🌷", "Food",      "We eat some flowers! Broccoli is actually a flower that we harvest before it fully opens. 🥦"),
        ("⏱️", "Timing",   "Some flowers only open at certain times of day. The morning glory opens in the morning and closes at night!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fce4ec;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#ad1457;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌸 Discover a Flower Secret!", use_container_width=True, key="flower_btn"):
        st.session_state.show_flower_fact = not st.session_state.show_flower_fact
    if st.session_state.show_flower_fact:
        st.success("🎉 The world's BIGGEST flower is the Rafflesia from Asia. "
                   "It can be 1 metre wide — as big as your whole body stretched out! "
                   "But it smells like rotting meat to attract flies. 🪰🌺 Yuck and wow!")

think_bubble("Why do bees visit flowers? What do the bees and flowers each get from each other?")

# ─── SEEDS ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🌰 Part 5 — The Seeds")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    A **seed** is like a tiny baby plant in a protective coat, waiting to wake up and grow! 
    Inside every seed is everything needed to start a brand new plant. 🌱

    Seeds come in all sorts of shapes and sizes:
    """)
    c1, c2, c3 = st.columns(3)
    for col, emoji, name, eg in zip(
        [c1, c2, c3],
        ["🌰", "🌻", "🍇"],
        ["Big Seeds", "Medium Seeds", "Tiny Seeds"],
        ["Like a coconut or mango stone", "Like a sunflower or apple pip", "Like a poppy or orchid seed"]
    ):
        with col:
            st.markdown(f"""
            <div style="background:#fff8e1; border-radius:12px; padding:0.8rem;
                        text-align:center; border:2px solid #ffd54f;">
                <div style="font-size:2rem;">{emoji}</div>
                <div style="font-weight:700; font-size:0.85rem; color:#f57f17;">{name}</div>
                <div style="font-size:0.78rem; color:#666; margin-top:0.2rem;">{eg}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("")
    fun_card("✈️", "How Do Seeds Travel?",
             "Seeds are amazing travellers! Some float on the wind (like dandelion fluff 🌬️), "
             "some float on water (like coconuts 🌊), some stick to animal fur (like burrs 🐾), "
             "and some are inside juicy fruits that animals eat and then drop elsewhere! 🍎",
             bg="#fff8e1", border="#ffa000")

with col2:
    st.markdown("##### 🌱 Seed Secrets")
    for icon, label, fact in [
        ("💤", "Sleeping Seeds",   "Seeds can wait in the soil for years — even decades! — before they wake up and start growing. They wait for just the right conditions."),
        ("🍎", "Fruit is a Seed Box", "A fruit is actually the plant's way of protecting its seeds. The juicy apple around the pip, the fuzzy skin around the peach stone — all protecting seeds inside!"),
        ("🌾", "We Eat Seeds",    "Rice, wheat, corn, and oats are all seeds that we eat every day — in bread, rice dishes, and cereal! 🥣"),
        ("🌲", "Giant from Tiny", "A giant sequoia tree — one of the biggest living things on Earth — grows from a seed no bigger than a grain of rice!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fffde7;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#f57f17;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🌰 Tap to reveal a Seed Secret!", use_container_width=True, key="seed_btn"):
        st.session_state.show_seed_fact = not st.session_state.show_seed_fact
    if st.session_state.show_seed_fact:
        st.success("🎉 Scientists found seeds buried in the Arctic ice that were 32,000 years old — "
                   "and they managed to grow plants from them! Seeds really are tiny time capsules! 🧊🌱")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — PLANT GROWTH JOURNEY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌱", "From Seed to Plant — The Growth Journey!",
               "Watch a plant grow step by step! Press Next to move forward 🌿")

growth_stages = [
    ("🌰", "Stage 1: A Dry Seed",
     "It all begins with a tiny seed sitting in dry soil. "
     "It looks like nothing is happening — but the seed is waiting! It needs water, warmth, and air to wake up.",
     "#fff8e1", "#f9a825"),
    ("💧", "Stage 2: The Seed Drinks Water",
     "When rain falls (or we water the soil), the seed soaks up water. "
     "It begins to swell and soften. The tough outer coat starts to crack open!",
     "#e8f4fd", "#1e88e5"),
    ("🌱", "Stage 3: A Tiny Root Appears",
     "The very first thing to grow is a tiny root that pushes DOWN into the soil. "
     "Even before the plant can be seen above ground, the root is already searching for water!",
     "#f1f8e9", "#43a047"),
    ("🌿", "Stage 4: The Shoot Pushes Up",
     "Next, a tiny green shoot pushes UP through the soil, reaching toward the light. "
     "This is called GERMINATION (say it: jer-mih-NAY-shun). "
     "The seed is now a seedling — a baby plant! 🎉",
     "#e8f5e9", "#388e3c"),
    ("🍃", "Stage 5: Leaves Open Up",
     "The seedling grows taller and tiny leaves unfold. "
     "As soon as the leaves reach sunlight, they start making food through photosynthesis. "
     "Now the plant can feed itself!",
     "#f9fbe7", "#7cb342"),
    ("🌻", "Stage 6: The Plant Grows Flowers",
     "Weeks or months later, the plant is strong and big. "
     "Beautiful flowers appear — bright and colourful to attract bees and butterflies. "
     "The flowers will soon make seeds!",
     "#fce4ec", "#e91e63"),
    ("🌰", "Stage 7: Seeds Are Made and Spread",
     "The flowers create new seeds. The seeds travel away by wind, water, or animals. "
     "Each seed lands in soil and the whole amazing journey starts all over again! 🔄 "
     "This never-ending circle is called the PLANT LIFE CYCLE.",
     "#fff3e0", "#fb8c00"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="grow_prev"):
        st.session_state.growth_step = max(0, st.session_state.growth_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="grow_next"):
        st.session_state.growth_step = min(len(growth_stages)-1, st.session_state.growth_step + 1)

idx   = st.session_state.growth_step
stage = growth_stages[idx]
with col2:
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,{stage[3]},{stage[3]}cc);
                border-radius:20px; padding:2rem; text-align:center;
                border:3px solid {stage[4]}; box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{stage[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {stage[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.7;">{stage[2]}</div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{stage[4]}">●</span>'
                for i in range(len(growth_stages))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Step {idx+1} of {len(growth_stages)}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — AMAZING WEIRD PLANTS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌿", "Weird & Wonderful Plants!",
               "Tap a plant to discover what makes it extraordinary!")

weird_plants = {
    "🪤 Venus Flytrap": {
        "emoji": "🪤", "color": "#c62828", "bg": "#ffebee",
        "tagline": "The Plant That Eats Bugs! 🐛",
        "body": (
            "The **Venus Flytrap** is a plant that catches and **eats insects and spiders!** 🕷️\n\n"
            "Its leaves have two sides that snap shut like a mouth when an insect touches the tiny hairs inside. "
            "SNAP! 🫱 The insect is trapped!\n\n"
            "The plant then slowly digests the insect over several days to get minerals "
            "that it cannot get from the poor soil it lives in. It's a plant with a stomach! 🤯\n\n"
            "📍 Found in: Bogs and swamps in North and South Carolina, USA"
        )
    },
    "🌵 Cactus": {
        "emoji": "🌵", "color": "#2e7d32", "bg": "#f1f8e9",
        "tagline": "The Desert Survivor! 🏜️",
        "body": (
            "The **cactus** is a master of surviving with almost NO water! 🌵\n\n"
            "Its thick, spongy stem stores water inside — like a big water bottle. "
            "Some large cacti can store hundreds of litres of water after heavy rain!\n\n"
            "Its leaves have turned into **sharp spines** (needles) to stop animals eating it "
            "and to reduce water loss from the plant.\n\n"
            "Some cacti live for over **200 years** and grow as tall as a house! 🏠\n\n"
            "📍 Found in: Deserts in America, Africa, and Australia"
        )
    },
    "🌊 Seaweed": {
        "emoji": "🌊", "color": "#00838f", "bg": "#e0f7fa",
        "tagline": "A Plant That Lives Underwater! 🐠",
        "body": (
            "**Seaweed** is a plant that grows in the ocean! 🌊 "
            "It doesn't have roots in soil — instead it clings to rocks on the sea floor.\n\n"
            "Seaweed is incredibly important — it produces about **50% of the world's oxygen.** "
            "That means HALF of every breath you take comes from seaweed! 🌬️\n\n"
            "Seaweed is also food for fish, turtles, and even some people — "
            "in Japan and Korea, people love eating seaweed in soups and sushi! 🍣\n\n"
            "📍 Found in: Oceans and seas all around the world"
        )
    },
    "🎋 Bamboo": {
        "emoji": "🎋", "color": "#558b2f", "bg": "#f9fbe7",
        "tagline": "The World's Fastest-Growing Plant! ⚡",
        "body": (
            "**Bamboo** is a type of grass — but it can grow as tall as a tree! 🎋\n\n"
            "It is the **fastest-growing plant on Earth.** Some bamboo species can grow "
            "**90 cm in just ONE day** — you could almost watch it grow!\n\n"
            "Bamboo is incredibly strong — stronger than many types of wood and even some metals! "
            "People use it to build houses, make furniture, and pandas eat it for every meal. 🐼\n\n"
            "📍 Found in: Asia, Africa, and South America"
        )
    },
    "🌸 Baobab Tree": {
        "emoji": "🌳", "color": "#6a1b9a", "bg": "#f3e5f5",
        "tagline": "The Upside-Down Tree! 🙃",
        "body": (
            "The **Baobab tree** looks so strange that people call it the **'upside-down tree'** — "
            "its bare branches look like roots pointing up to the sky! 🌳\n\n"
            "Like a cactus, the Baobab stores thousands of litres of water in its huge trunk "
            "to survive long dry seasons.\n\n"
            "Baobabs can live for **over 2,000 years** — some are alive today that were already "
            "ancient trees when dinosaurs walked nearby! They are also called 'The Tree of Life' "
            "because animals rely on them for food and water. 🦁\n\n"
            "📍 Found in: Africa and Madagascar"
        )
    },
    "🌺 Rafflesia": {
        "emoji": "🌺", "color": "#ad1457", "bg": "#fce4ec",
        "tagline": "The World's Biggest Flower! 🤯",
        "body": (
            "**Rafflesia** is the world's **largest single flower** — it can grow up to "
            "**1 metre across** and weigh up to 10 kg! 😱\n\n"
            "But here's the strange part — Rafflesia has **no leaves, no stem, and no roots!** "
            "It lives as a parasite inside another plant, hidden and invisible, until suddenly "
            "a giant flower bursts out of the ground!\n\n"
            "Its nickname is the **'corpse flower'** because it smells like rotting meat — "
            "on purpose! The smell attracts flies that carry its pollen. 🪰\n\n"
            "📍 Found in: Rainforests of Southeast Asia"
        )
    },
}

plant_cols = st.columns(len(weird_plants))
for i, (pname, pdata) in enumerate(weird_plants.items()):
    with plant_cols[i]:
        short = pname.split(" ")[1]
        if st.button(pdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"weird_{i}"):
            st.session_state.plant_picked = pname

if st.session_state.plant_picked and st.session_state.plant_picked in weird_plants:
    pname = st.session_state.plant_picked
    pdata = weird_plants[pname]
    st.markdown(f"""
    <div style="background:{pdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {pdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{pdata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {pname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{pdata['color']}; font-weight:600;">
                    {pdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(pdata["body"])
else:
    st.info("👆 Tap any plant above to discover what makes it amazing!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Let's Test What You Know!",
               "6 questions about plants — answer them all then check your score! 🌱")

questions = [
    {
        "q":    "Q1 🌱 — What do plant roots do?",
        "opts": ["Make flowers", "Drink water from soil and hold the plant", "Make sunlight", "Breathe in air"],
        "ans":  "Drink water from soil and hold the plant",
        "explain": "Roots are like drinking straws AND anchors — they drink water AND hold the plant firm! 💧⚓"
    },
    {
        "q":    "Q2 🍃 — What do leaves use to make food for the plant?",
        "opts": ["Rain, wind and soil", "Sunlight, water and air", "Flowers, roots and seeds", "Insects and mud"],
        "ans":  "Sunlight, water and air",
        "explain": "Leaves use sunlight + water + air (CO₂) to make food in a process called photosynthesis! ☀️💧🌬️"
    },
    {
        "q":    "Q3 🌱 — What is the job of the stem?",
        "opts": ["To make seeds", "To absorb sunlight", "To hold the plant up and carry water", "To attract bees"],
        "ans":  "To hold the plant up and carry water",
        "explain": "The stem is the plant's backbone AND its pipe system — it holds everything up and carries water! 🏗️🚿"
    },
    {
        "q":    "Q4 🐝 — Why do bees visit flowers?",
        "opts": ["To sleep there", "To collect sweet nectar", "To eat the petals", "To hide from the rain"],
        "ans":  "To collect sweet nectar",
        "explain": "Bees visit for nectar — and while doing so, they accidentally carry pollen that helps make seeds! 🐝🌸"
    },
    {
        "q":    "Q5 🌵 — Which plant stores water in its thick stem?",
        "opts": ["Rose", "Cactus", "Daisy", "Oak Tree"],
        "ans":  "Cactus",
        "explain": "A cactus stores water inside its thick, spongy stem to survive in the dry desert! 🌵🏜️"
    },
    {
        "q":    "Q6 🌰 — What does a seed need to start growing?",
        "opts": ["Ice and darkness", "Water, warmth and air", "Wind and sand", "Flowers and bees"],
        "ans":  "Water, warmth and air",
        "explain": "Seeds need water, warmth and air to wake up and start growing — then the magic begins! 🌱✨"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"plant_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="plant_quiz_submit"):
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

    badge_data = [
        (6, "🏆", "PLANT GENIUS!",         "#ffd700", "#fffde7"),
        (5, "🥇", "Amazing Botanist!",      "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Nature Explorer!", "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Gardener!",    "#43a047", "#e8f5e9"),
        (0, "🌱", "Keep Growing! Try Again!","#8e24aa", "#f3e5f5"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="plant_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?", "A quick summary card for you!")

summary_items = [
    ("🪱", "Roots",   "Underground — drink water, hold plant firm"),
    ("🌱", "Stem",    "Holds plant up, carries water like a pipe"),
    ("🍃", "Leaves",  "Make food using sunlight, water and air"),
    ("🌸", "Flowers", "Make seeds with help from bees 🐝"),
    ("🌰", "Seeds",   "Baby plants that grow into new plants"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #66bb6a;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1b5e20,#388e3c,#1b5e20);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">🌿 Keep growing, little scientist! 🌸</div>
    <div style="color:#c8e6c9; font-size:0.95rem;">
        Every tree, flower, and blade of grass has an amazing story — go outside and explore!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.8rem;">
        🌱 🌻 🍃 🌺 🌳 🌿
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