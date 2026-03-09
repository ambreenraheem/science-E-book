import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 4 · Amazing Animals", layout="wide", initial_sidebar_state="expanded")

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
if "show_mammal_fact"   not in st.session_state: st.session_state.show_mammal_fact   = False
if "show_bird_fact"     not in st.session_state: st.session_state.show_bird_fact     = False
if "show_fish_fact"     not in st.session_state: st.session_state.show_fish_fact     = False
if "show_insect_fact"   not in st.session_state: st.session_state.show_insect_fact   = False
if "show_reptile_fact"  not in st.session_state: st.session_state.show_reptile_fact  = False
if "show_amphibian_fact" not in st.session_state: st.session_state.show_amphibian_fact = False
if "animal_picked"      not in st.session_state: st.session_state.animal_picked      = None
if "habitat_picked"     not in st.session_state: st.session_state.habitat_picked     = None
if "food_chain_step"    not in st.session_state: st.session_state.food_chain_step    = 0
if "quiz_answers"       not in st.session_state: st.session_state.quiz_answers       = {}
if "quiz_submitted"     not in st.session_state: st.session_state.quiz_submitted     = False

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
    <div style="background:linear-gradient(135deg,#fff3e0,#fce4ec);
                border-radius:20px; padding:1rem 1.4rem; margin:0.8rem 0;
                border:2px dashed #ff8f00; text-align:center;">
        <span style="font-size:1.5rem;">🤔</span>
        <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;
                     font-size:0.97rem;">{question}</span>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#1a3a1a,#2e6b2e,#4e3b1a);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#c8e6c9; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 04 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🐘 Amazing Animals 🦁
    </h1>
    <p style="color:#dcedc8; font-size:1.05rem; margin:0.8rem 0 0;">
        Explore the incredible animal kingdom — from tiny ants to giant whales!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.4rem;">
        🐘 🦁 🐦 🐠 🦋 🐸 🦎 🐋
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What makes an animal an **animal**
        - ✅ The **6 animal groups** and their features
        - ✅ Where animals **live** (habitats)
        - ✅ What animals **eat** (food chains)
        """)
    with col2:
        st.markdown("""
        - ✅ How animals **protect** themselves
        - ✅ **Record-breaking** animals of the world
        - ✅ Why we must **protect** animals
        - ✅ A fun **quiz** with badges!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT IS AN ANIMAL?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌍", "What Is an Animal?",
               "Animals are living things — but what makes them special?")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Animals are **living things** — just like plants and people! But animals 
    are different from plants in some very important ways.

    Every animal on Earth — from a tiny ant to a gigantic whale — shares these things:
    """)
    icons = [
        ("🍽️", "They eat food",       "Animals cannot make their own food like plants. They must find and eat other things — plants, other animals, or both!"),
        ("🏃", "They can move",        "Most animals can move from place to place — by walking, flying, swimming, hopping, or slithering!"),
        ("👶", "They make babies",     "All animals reproduce — they make young ones (babies, eggs, or larvae) to keep their species alive."),
        ("🌬️", "They breathe",        "Every animal breathes — some breathe air with lungs, some breathe water through gills!"),
        ("💡", "They sense the world", "Animals have senses like sight, smell, hearing, taste and touch to understand their world."),
    ]
    for emoji, title, desc in icons:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.65rem 0.8rem; border-radius:12px; margin-bottom:0.4rem;
                    background:#fff8e1; border-left:4px solid #f9a825;">
            <span style="font-size:1.6rem; flex-shrink:0;">{emoji}</span>
            <div><strong style="color:#e65100;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("How many different animals can you name in 30 seconds? Give it a try! 🕐")

with col2:
    fun_card("🔢", "How Many Animals?",
             "Scientists have discovered about **8.7 million** different species of animals "
             "on Earth — and they find new ones every single year! Most we haven't even discovered yet. 🤯",
             bg="#fff3e0", border="#ff8f00")
    fun_card("🦠", "Smallest Animal",
             "The smallest animal on Earth is a tiny parasitic wasp called Dicopomorpha echmepterygis "
             "— it is smaller than a grain of sand! You would need a microscope to see it. 🔬",
             bg="#f3e5f5", border="#8e24aa")
    fun_card("🐋", "Biggest Animal",
             "The Blue Whale is the biggest animal **ever** — bigger than any dinosaur! "
             "It can grow to 30 metres long and weigh 180,000 kg. Its heart is the size of a small car! 🚗💙",
             bg="#e8f4fd", border="#1e88e5")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE 6 ANIMAL GROUPS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🐾", "The 6 Groups of Animals",
               "Scientists sort animals into 6 groups — let's explore each one!")

# ─── MAMMALS ──────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🦁 Group 1 — Mammals")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Mammals** are probably the group you know best — because **you are one!** 🙋

    All mammals share these features:
    """)
    for icon, label, desc in [
        ("🧸", "Warm-blooded",    "Their body temperature stays the same whether it is hot or cold outside — like your body always stays warm even in winter!"),
        ("🍼", "Feed babies milk","Mammal mothers make milk from their bodies to feed their newborn babies. Every mammal starts life drinking milk!"),
        ("🪮", "Have hair or fur","All mammals have at least some hair or fur on their bodies — even whales have a few hairs!"),
        ("🫁", "Breathe air",     "All mammals breathe air with lungs — even dolphins and whales must come to the surface to breathe!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fff8e1; border-left:3px solid #f9a825;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#e65100;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Are you a mammal? How do you know? Check the list above! 😄")

with col2:
    st.markdown("##### 🦁 Amazing Mammal Facts")
    for icon, label, fact in [
        ("🐘", "Elephants",   "Elephants never forget! They can remember other elephants and people they met many years ago. They even mourn their dead. 💔"),
        ("🦇", "Bats",        "Bats are the only mammals that can truly fly! They navigate in the dark using ECHOLOCATION — sending out sound waves and listening for the echo."),
        ("🐬", "Dolphins",    "Dolphins sleep with one eye open and half their brain awake — so they don't forget to breathe! They are also one of the smartest animals."),
        ("🦘", "Kangaroos",   "A baby kangaroo (called a joey) is born the size of a jellybean! It crawls straight into its mother's pouch and stays there for months. 🫘"),
        ("🦔", "Hedgehogs",   "Hedgehogs have about 6,000 spines on their back. When scared, they curl into a tight ball — the perfect prickly shield! 🛡️"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#fffde7;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#f57f17;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🦁 Reveal a Mammal Secret!", use_container_width=True, key="mammal_btn"):
        st.session_state.show_mammal_fact = not st.session_state.show_mammal_fact
    if st.session_state.show_mammal_fact:
        st.success("🎉 A giraffe's tongue is about 45 cm long and dark purple in colour! "
                   "It uses it to grab leaves from the tops of thorny trees. "
                   "The purple colour protects it from sunburn! 🦒💜")

# ─── BIRDS ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


### 🐦 Group 2 — Birds")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Birds** are the only animals in the world with **feathers** — 
    no other animal group has them!

    All birds share these features:
    """)
    for icon, label, desc in [
        ("🪶", "Have feathers", "Feathers keep birds warm, dry, and help them fly. Even flightless birds like penguins and ostriches have feathers!"),
        ("🥚", "Lay eggs",      "All birds lay eggs with a hard or tough shell. They sit on them to keep them warm until the baby hatches out. 🐣"),
        ("🦴", "Light bones",   "Birds have hollow bones filled with air — this makes them light enough to fly. Even big eagles have surprisingly light skeletons!"),
        ("🫁", "Breathe air",   "Birds have very efficient lungs — some birds can even breathe and sing at the same time! 🎶"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e3f2fd; border-left:3px solid #1e88e5;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#1565c0;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Not all birds can fly! Can you name a bird that stays on the ground? 🐧")

with col2:
    st.markdown("##### 🐦 Bird Wonders")
    for icon, label, fact in [
        ("🦅", "Eagle Eyes",    "Eagles can spot a rabbit from 3 km away! Their eyesight is 4–8 times sharper than a human's. 👁️"),
        ("🐧", "Penguins",      "Penguins cannot fly but they are brilliant swimmers — they use their wings like flippers and can swim at 36 km/h! 🏊"),
        ("🦜", "Parrots",       "African Grey Parrots can learn over 1,000 words and understand what they mean — not just copy sounds! They are as clever as a 5-year-old child. 🧠"),
        ("🦢", "Migration",     "Arctic Terns fly from the Arctic to the Antarctic and back every year — a round trip of 90,000 km! That's like flying around Earth twice. 🌍"),
        ("🦉", "Owls",          "Owls can turn their heads 270° — almost all the way around — because their eyes cannot move in their sockets like ours can. 👀"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#e8f4fd;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#1565c0;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🐦 Tap for a Bird Surprise!", use_container_width=True, key="bird_btn"):
        st.session_state.show_bird_fact = not st.session_state.show_bird_fact
    if st.session_state.show_bird_fact:
        st.success("🎉 A hummingbird's heart beats up to 1,260 times per MINUTE — "
                   "that's over 20 times per second! Your heart only beats about "
                   "80 times per minute. Hummingbirds also flap their wings "
                   "80 times every second! 🏃💨")

# ─── FISH ─────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

### 🐠 Group 3 — Fish")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Fish** are animals that spend their whole lives living in water — 
    in rivers, lakes, and oceans all over the world!

    All fish share these features:
    """)
    for icon, label, desc in [
        ("🌊", "Live in water",   "Fish are perfectly built for water — they are streamlined (smooth and pointed) so they can glide through water easily."),
        ("🫧", "Breathe with gills", "Fish breathe using special organs called GILLS. Water flows into their mouth, over the gills (which take oxygen out), and out through their sides."),
        ("🐟", "Have scales",     "Most fish are covered with overlapping scales — like a suit of tiny armour! Scales protect and help them move smoothly in water."),
        ("🏊", "Have fins",       "Fish use their fins to steer, balance, and push themselves through the water. It's like having built-in paddles! 🚣"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e0f7fa; border-left:3px solid #00838f;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#006064;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("How do YOU breathe? Is it similar to or different from how a fish breathes? 💭")

with col2:
    st.markdown("##### 🐠 Fish Fascinations")
    for icon, label, fact in [
        ("🦈", "Sharks",       "Sharks have been on Earth for 450 million years — that is longer than trees! They were swimming before the dinosaurs existed. 🦕"),
        ("🐡", "Clownfish",    "The clownfish (like Nemo!) lives inside sea anemones which would sting other fish. A special coat of slime protects them! 🏠"),
        ("🐙", "Octopus",      "Although it lives in water, an octopus is NOT a fish — it has no backbone! It's a mollusc, just like a snail, but much cleverer. 🧠"),
        ("🌊", "Flying Fish",  "Flying fish can leap out of the water and glide through the air for up to 200 metres using their large fins as wings! ✈️"),
        ("💡", "Anglerfish",   "Deep-sea anglerfish have a glowing lure dangling from their head to attract prey in the pitch-black deep ocean. 🔦"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#e0f7fa;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#006064;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🐠 Reveal a Fish Secret!", use_container_width=True, key="fish_btn"):
        st.session_state.show_fish_fact = not st.session_state.show_fish_fact
    if st.session_state.show_fish_fact:
        st.success("🎉 The seahorse is the only animal where the FATHER gets pregnant! "
                   "The mother puts her eggs into the father's special pouch, "
                   "and he carries and gives birth to up to 1,000 babies! 🐴💛")

# ─── INSECTS ──────────────────────────────────────────────────────────────────
st.markdown("""<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


st.markdown("### 🦋 Group 4 — Insects")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Insects** are the most numerous animals on Earth — there are more insects 
    alive right now than any other type of animal. By far!

    All insects share exactly these features — no exceptions!
    """)
    for icon, label, desc in [
        ("🦿", "6 legs",          "Every insect — from a tiny ant to a giant stick insect — has exactly 6 legs. If it has 8 legs (like a spider), it is NOT an insect!"),
        ("🔲", "3 body sections", "An insect's body is always divided into three parts: the HEAD, the THORAX (middle), and the ABDOMEN (back end)."),
        ("🦴", "Exoskeleton",     "Insects have no bones inside! Instead, they have a hard outer shell called an exoskeleton that protects them like armour. 🛡️"),
        ("🪲", "Antennae",        "Insects have two antennae on their head. They use them to smell, touch, taste and even hear the world around them!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#f3e5f5; border-left:3px solid #8e24aa;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#6a1b9a;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Is a spider an insect? Count its legs and find out! 🕷️")

with col2:
    st.markdown("##### 🦋 Incredible Insect Facts")
    for icon, label, fact in [
        ("🐜", "Ants",        "Ants can carry 50 times their own body weight! If YOU were that strong, you could lift a car. 🚗 They also never sleep!"),
        ("🐝", "Bees",        "A honeybee visits up to 1,500 flowers to make just ONE teaspoon of honey. A whole hive works together as one super-organism. 🍯"),
        ("🦋", "Butterflies", "A butterfly can taste with its FEET! It stands on a leaf to decide if it is good enough to lay eggs on for its caterpillars to eat. 👣"),
        ("🔦", "Fireflies",   "Fireflies produce their own cold light — called bioluminescence — using a chemical reaction in their abdomen. 💡"),
        ("🦗", "Crickets",    "Crickets hear with their KNEES! They have ears on their front legs, not on their heads! 🦵👂"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#f3e5f5;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#6a1b9a;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🦋 Tap for an Insect Surprise!", use_container_width=True, key="insect_btn"):
        st.session_state.show_insect_fact = not st.session_state.show_insect_fact
    if st.session_state.show_insect_fact:
        st.success("🎉 A caterpillar dissolves almost completely inside its chrysalis! "
                   "It basically turns into a liquid soup, and then rebuilds itself "
                   "into a completely different creature — a butterfly! 🫠🦋 "
                   "Scientists call this metamorphosis.")

# ─── REPTILES ─────────────────────────────────────────────────────────────────

st.markdown("""
    <hr style="border:2px solid lightblue;">""", unsafe_allow_html=True)

st.markdown("### 🦎 Group 5 — Reptiles")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Reptiles** are scaly, cold-blooded animals that mostly live on land — 
    though some, like crocodiles, love the water too!

    **Cold-blooded** means their body temperature changes with the weather — 
    they need the Sun to warm up and shade to cool down. 🌡️

    All reptiles share these features:
    """)
    for icon, label, desc in [
        ("🦎", "Dry, scaly skin",    "Reptile skin is covered in tough, dry scales that protect them and stop them from drying out in hot weather."),
        ("🥚", "Lay leathery eggs",  "Most reptiles lay eggs on land with a soft, leathery shell — not a hard shell like birds. 🐊"),
        ("❄️", "Cold-blooded",       "They cannot make their own body heat, so you often see lizards sunbathing on rocks to warm up in the morning. ☀️"),
        ("🫁", "Breathe air",        "Even water reptiles like sea turtles must come up to breathe air — they have lungs, not gills!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e8f5e9; border-left:3px solid #388e3c;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#1b5e20;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Why do reptiles love sitting in the sun? What does the sun do for them? ☀️")

with col2:
    st.markdown("##### 🦎 Reptile Records")
    for icon, label, fact in [
        ("🐊", "Crocodiles",   "Crocodiles have the strongest bite of any animal on Earth! Yet the muscles for OPENING their jaws are so weak, a person can hold them shut with their hands. 🤝"),
        ("🐢", "Sea Turtles",  "Sea turtles always return to the exact same beach where THEY were born to lay their own eggs. They navigate using Earth's magnetic field like a built-in compass. 🧭"),
        ("🦎", "Gecko",        "A gecko can walk upside down on smooth glass ceilings! Its toe pads have millions of tiny hairs that create a sticky grip using science called Van der Waals force. 🔬"),
        ("🐍", "Anaconda",     "The green anaconda is the world's heaviest snake — it can weigh as much as 250 kg and grow to 9 metres long! It squeezes its prey to catch it. 💪"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#e8f5e9;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#2e7d32;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🦎 Reveal a Reptile Secret!", use_container_width=True, key="reptile_btn"):
        st.session_state.show_reptile_fact = not st.session_state.show_reptile_fact
    if st.session_state.show_reptile_fact:
        st.success("🎉 A chameleon does NOT change colour to camouflage itself — "
                   "that's a myth! It changes colour to show its MOOD, like a face emoji. "
                   "Dark colours = stressed 😠, bright colours = happy and showing off! 😎🦎")

# ─── AMPHIBIANS ───────────────────────────────────────────────────────────────

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🐸 Group 6 — Amphibians")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Amphibians** are remarkable animals that live **double lives** — 
    they are born in water but can also live on land when they grow up!

    The word *amphibian* actually means **"double life"** in Greek! 🌊➡️🌿

    All amphibians share these features:
    """)
    for icon, label, desc in [
        ("🌊", "Born in water",    "Amphibians always lay their jelly-like eggs in water or damp places. Their babies (like tadpoles) live in water at first."),
        ("🔄", "Transform!",       "Amphibians go through METAMORPHOSIS — they change shape completely as they grow! A tadpole grows legs and lungs to become a frog. 🐸"),
        ("💧", "Moist skin",       "Their skin has no scales — it must stay moist to help them breathe through it! They soak up water through their skin too."),
        ("❄️", "Cold-blooded",     "Like reptiles, amphibians are cold-blooded and rely on their environment to stay warm."),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e8eaf6; border-left:3px solid #3949ab;">
            <span style="font-size:1.4rem;">{icon}</span>
            <div><strong style="color:#283593;">{label}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("A frog starts as a tadpole with a tail. What does it grow, and what does it lose, as it becomes a frog? 🐸")

with col2:
    st.markdown("##### 🐸 Amphibian Amazements")
    for icon, label, fact in [
        ("🐸", "Frogs",         "There are over 7,000 species of frogs! The tiniest is smaller than your fingernail, and the largest — the Goliath Frog — is the size of a small cat. 🐱"),
        ("🔴", "Poison Dart",   "The golden poison dart frog is one of the most toxic animals alive. Its bright colours are a WARNING to predators: 'Don't eat me!' ☠️"),
        ("🧊", "Wood Frog",     "The wood frog from North America can FREEZE SOLID in winter — no heartbeat, no breathing — and come back to life in spring! 🧊➡️🐸"),
        ("🌈", "Axolotl",       "The axolotl is a salamander that keeps its baby (larval) features its whole life — it never fully transforms! Scientists study it to understand healing. 🔬"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem; border-radius:10px; margin-bottom:0.35rem;
                    background:#e8eaf6;">
            <span style="font-size:1.3rem;">{icon}</span>
            <div><strong style="color:#283593;">{label}:</strong>
            <span style="font-size:0.9rem; color:#444;"> {fact}</span></div>
        </div>""", unsafe_allow_html=True)

    if st.button("🐸 Tap for an Amphibian Secret!", use_container_width=True, key="amphibian_btn"):
        st.session_state.show_amphibian_fact = not st.session_state.show_amphibian_fact
    if st.session_state.show_amphibian_fact:
        st.success("🎉 Frogs don't drink water with their mouth! "
                   "They absorb water directly through a special patch of thin skin "
                   "on their belly called the 'drinking patch'. "
                   "They basically drink through their tummy! 🐸💧")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — ANIMAL HABITATS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🗺️", "Where Do Animals Live? — Habitats!",
               "A habitat is an animal's home — tap each one to explore! 🏠")

habitats = {
    "🌳 Rainforest": {
        "emoji": "🌳", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "The richest habitat on Earth 🌿",
        "body": (
            "**Rainforests** cover only 6% of Earth's surface but are home to over **half of all animal species!** 🌍\n\n"
            "The rainforest has different layers — animals live at different heights:\n\n"
            "- 🌿 **Forest floor**: Gorillas, jaguars, giant anteaters\n"
            "- 🌱 **Understory**: Tree frogs, snakes, leopards\n"
            "- 🍃 **Canopy**: Monkeys, toucans, sloths, parrots\n"
            "- 🌤️ **Emergent layer**: Eagles, butterflies, bats\n\n"
            "Famous rainforest animals: 🦜 Macaw · 🐆 Jaguar · 🦥 Sloth · 🐍 Anaconda · 🐸 Poison Dart Frog"
        )
    },
    "🏔️ Arctic": {
        "emoji": "🏔️", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "The frozen world at the top of Earth ❄️",
        "body": (
            "The **Arctic** is one of the coldest, harshest places on Earth — yet animals have adapted brilliantly to survive! 🧊\n\n"
            "Animals here have special features:\n\n"
            "- 🧸 **Thick fur/blubber**: Polar bears have a layer of fat 10 cm thick to stay warm\n"
            "- ⬜ **White colour**: Many animals are white — perfect camouflage in the snow!\n"
            "- 🐾 **Wide paws**: Polar bear paws are huge and act like snowshoes\n"
            "- 💤 **Hibernation**: Some animals sleep through the coldest months\n\n"
            "Famous Arctic animals: 🐻‍❄️ Polar Bear · 🦭 Seal · 🦊 Arctic Fox · 🐋 Beluga Whale · 🦌 Reindeer"
        )
    },
    "🏜️ Desert": {
        "emoji": "🏜️", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "Surviving the scorching heat 🌵",
        "body": (
            "**Deserts** are extremely dry places — but clever animals have found amazing ways to survive! 🌵\n\n"
            "Desert survival tricks:\n\n"
            "- 🌙 **Nocturnal lifestyle**: Many desert animals sleep during the hot day and come out at cool night\n"
            "- 💧 **Water storage**: Some get all their water from their food — they never need to drink!\n"
            "- 🏖️ **Burrowing**: Animals dig into the cool sand to escape the scorching surface\n"
            "- 🦶 **Big ears**: Large ears (like fennec foxes) release body heat to stay cool\n\n"
            "Famous desert animals: 🐪 Camel · 🦂 Scorpion · 🦎 Monitor Lizard · 🦊 Fennec Fox · 🐍 Sidewinder Snake"
        )
    },
    "🌊 Ocean": {
        "emoji": "🌊", "color": "#00838f", "bg": "#e0f7fa",
        "tagline": "The largest habitat on Earth 🐋",
        "body": (
            "The **ocean** covers over 70% of Earth's surface and goes as deep as 11 km — deeper than Mount Everest is tall! 🌊\n\n"
            "The ocean has different zones too:\n\n"
            "- ☀️ **Sunlit zone**: Coral reefs, sharks, turtles, dolphins, most fish\n"
            "- 🌑 **Twilight zone**: Giant squid, lanternfish, weird bioluminescent creatures\n"
            "- 🖤 **Midnight zone**: Anglerfish, viperfish, dumbo octopus — total darkness!\n\n"
            "Famous ocean animals: 🐋 Blue Whale · 🦈 Shark · 🐠 Clownfish · 🐙 Octopus · 🐢 Sea Turtle"
        )
    },
    "🌾 Grassland": {
        "emoji": "🌾", "color": "#ff8f00", "bg": "#fff3e0",
        "tagline": "Wide open spaces with great herds 🦁",
        "body": (
            "**Grasslands** (like the African Savanna) are huge open plains with tall grass and scattered trees. "
            "They are home to the world's most famous wildlife! 🌍\n\n"
            "Life on the grassland is all about the great chase:\n\n"
            "- 🌿 **Grazers**: Huge herds of zebra, wildebeest, and elephant roam and eat grass\n"
            "- 🔍 **Hunters**: Lions, cheetahs, and leopards stalk the grazers\n"
            "- 🦅 **Scavengers**: Vultures and hyenas eat what the hunters leave behind\n"
            "- 🐜 **Decomposers**: Insects and bacteria break down what's left into nutrients for the grass\n\n"
            "Famous grassland animals: 🦁 Lion · 🦓 Zebra · 🐘 Elephant · 🦒 Giraffe · 🐆 Cheetah"
        )
    },
}

habitat_cols = st.columns(len(habitats))
for i, (hname, hdata) in enumerate(habitats.items()):
    with habitat_cols[i]:
        short = hname.split(" ")[1]
        if st.button(hdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"habitat_{i}"):
            st.session_state.habitat_picked = hname

if st.session_state.habitat_picked:
    hname = st.session_state.habitat_picked
    hdata = habitats[hname]
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
                <div style="font-size:0.9rem; color:{hdata['color']}; font-weight:600;">
                    {hdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(hdata["body"])
else:
    st.info("👆 Tap any habitat button above to explore the animals that live there!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — THE FOOD CHAIN
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🍃", "What Do Animals Eat? — The Food Chain!",
               "All living things are connected through food — step through the chain! ⛓️")

st.markdown("""
Animals eat different things, and this creates a **food chain** — a chain of 
who eats what! Every food chain starts with the **Sun** and plants.
Press the buttons to step through a real food chain! 🌿
""")

food_chain_steps = [
    ("☀️", "Step 1: The Sun",
     "Everything starts with the SUN! ☀️\n\n"
     "The Sun's energy powers all life on Earth. Without it, nothing could live. "
     "Plants capture this energy and use it to make food through photosynthesis.",
     "#fff8e1", "#f9a825"),
    ("🌿", "Step 2: Plants (Producers)",
     "Plants are called PRODUCERS because they PRODUCE (make) their own food. 🌿\n\n"
     "They capture the Sun's energy and turn it into leaves, fruits, seeds, and roots "
     "that animals can eat. Without plants, no animal could survive!",
     "#e8f5e9", "#43a047"),
    ("🦗", "Step 3: Plant-Eaters (Herbivores)",
     "Animals that eat ONLY plants are called HERBIVORES. 🦗\n\n"
     "Examples: Caterpillars, rabbits, cows, deer, elephants, and grasshoppers. "
     "They are also called PRIMARY CONSUMERS — the first animals in the food chain. "
     "They get their energy by eating the plants. 🌿➡️🐇",
     "#f3e5f5", "#7b1fa2"),
    ("🐸", "Step 4: Meat-Eaters (Carnivores)",
     "Animals that eat OTHER animals are called CARNIVORES. 🐸\n\n"
     "A frog eats the grasshopper. A snake eats the frog. An eagle eats the snake! "
     "Each one is a SECONDARY or TERTIARY CONSUMER — passing energy along the chain. "
     "🌿➡️🦗➡️🐸➡️🐍➡️🦅",
     "#fff3e0", "#e65100"),
    ("🦅", "Step 5: Top Predators (Apex Predators)",
     "At the TOP of the food chain are APEX PREDATORS — animals that no other animal hunts! 🦅\n\n"
     "Examples: Lions, eagles, orcas, and great white sharks. "
     "They are crucial for keeping ecosystems balanced — if there are too many deer, "
     "a wolf pack keeps the numbers in check so plants are not over-eaten. 🌿⚖️",
     "#fce4ec", "#c62828"),
    ("🍄", "Step 6: Decomposers",
     "When animals die, DECOMPOSERS break their bodies down into nutrients. 🍄\n\n"
     "Earthworms, fungi, and bacteria are nature's clean-up crew. "
     "They turn dead things into rich nutrients that go back into the soil — "
     "which plants then use to grow, and the whole chain starts again! 🔄\n\n"
     "The food chain is really a never-ending FOOD WEB of connections! 🕸️",
     "#efebe9", "#5d4037"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="fc_prev"):
        st.session_state.food_chain_step = max(0, st.session_state.food_chain_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="fc_next"):
        st.session_state.food_chain_step = min(len(food_chain_steps)-1, st.session_state.food_chain_step + 1)

idx   = st.session_state.food_chain_step
fstep = food_chain_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{fstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {fstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{fstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {fstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {fstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{fstep[4]}">●</span>'
                for i in range(len(food_chain_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Step {idx+1} of {len(food_chain_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

# Visual chain summary
st.markdown("##### 🔗 A Full Food Chain at a Glance:")
st.markdown("""
<div style="background:linear-gradient(135deg,#1a3a1a,#2e6b2e);
            border-radius:16px; padding:1.4rem 1.8rem; margin:0.5rem 0; color:#fff;
            text-align:center; font-size:1.15rem;">
    ☀️ Sun
    <span style="color:#a5d6a7;"> ➡️ </span>
    🌿 Plant
    <span style="color:#a5d6a7;"> ➡️ </span>
    🦗 Grasshopper
    <span style="color:#a5d6a7;"> ➡️ </span>
    🐸 Frog
    <span style="color:#a5d6a7;"> ➡️ </span>
    🐍 Snake
    <span style="color:#a5d6a7;"> ➡️ </span>
    🦅 Eagle
    <span style="color:#a5d6a7;"> ➡️ </span>
    🍄 Decomposer
    <br><span style="font-size:0.85rem; color:#c8e6c9; margin-top:0.5rem; display:block;">
    Energy flows from left to right — and nutrients return to the soil at the end! 🔄
    </span>
</div>""", unsafe_allow_html=True)

think_bubble("What would happen to eagles if all the frogs disappeared? Can you follow the chain? 🦅🐸")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — HOW ANIMALS PROTECT THEMSELVES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🛡️", "How Animals Stay Safe!",
               "Animals have clever tricks to avoid being eaten!")

col1, col2, col3 = st.columns(3)
defences = [
    ("🎨", "Camouflage",      "Blending in with surroundings to stay hidden",
     "A stick insect looks exactly like a twig. A snow leopard's spotted coat hides it in rocky mountains. A flounder fish matches the sandy sea floor perfectly. Can you spot them? 👀",
     "#e8f5e9", "#43a047"),
    ("⚠️", "Warning Colours", "Bright colours that scream DANGER!",
     "Poison dart frogs are neon blue, red, or yellow to warn predators: 'I taste terrible and I'm toxic!' 🔴 Many harmless animals copy these colours to trick predators too!",
     "#fce4ec", "#c62828"),
    ("🔵", "Mimicry",         "Copying something dangerous or disgusting",
     "The harmless hoverfly has yellow and black stripes — just like a wasp — so birds avoid it, even though it has no sting! Some moths have eye patterns on their wings to look like an owl. 🦉",
     "#e3f2fd", "#1e88e5"),
    ("🦔", "Armour & Spines", "Hard shells and sharp spikes",
     "A tortoise retreats into its shell when scared. A porcupine rattles its spines as a warning. A pangolin rolls into a ball covered in sharp scales — like a living pinecone! 🌲",
     "#fff8e1", "#f9a825"),
    ("💨", "Speed",           "Outrunning any predator!",
     "The cheetah is the fastest land animal at 120 km/h — it outruns everything! A springbok leaps and zigzags wildly to confuse chasing cheetahs. Speed and unpredictability save lives! ⚡",
     "#f3e5f5", "#8e24aa"),
    ("🔢", "Safety in Numbers","Herds, flocks, and schools confuse predators",
     "Thousands of starlings fly in swirling murmurations — impossible for a hawk to pick one target! Fish schools spin and flash, looking like one huge confusing creature. Together is safer! 🐟🐟🐟",
     "#e0f7fa", "#00838f"),
]

for i, (emoji, title, subtitle, body, bg, border) in enumerate(defences):
    col = [col1, col2, col3][i % 3]
    with col:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:14px; padding:1rem;
                    border-top:4px solid {border}; margin-bottom:0.8rem;
                    box-shadow:0 3px 10px rgba(0,0,0,0.06); height:100%;">
            <div style="font-size:2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; font-size:1rem;">{title}</div>
            <div style="font-size:0.82rem; color:{border}; font-weight:600;
                        margin-bottom:0.5rem;">{subtitle}</div>
            <div style="font-size:0.88rem; color:#555; line-height:1.6;">{body}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — RECORD-BREAKING ANIMALS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🏆", "Record-Breaking Animals!",
               "The most extreme animals on Earth — tap to explore! 🌍")

record_animals = {
    "🐋 Blue Whale": {
        "emoji": "🐋", "color": "#1565c0", "bg": "#e3f2fd",
        "record": "🏆 Biggest Animal Ever",
        "body": (
            "The **Blue Whale** is the largest animal to have **ever** existed on Earth — "
            "bigger than any dinosaur! 😱\n\n"
            "- 📏 Length: Up to **33 metres** (longer than two school buses end to end!)\n"
            "- ⚖️ Weight: Up to **180,000 kg** (heavier than 30 elephants!)\n"
            "- ❤️ Heart: As big as a small car — you could crawl through its arteries!\n"
            "- 🍼 Baby: A newborn calf is already 7 metres long and gains 90 kg per DAY\n"
            "- 🔊 Voice: Their call is the loudest of any animal — heard 800 km away underwater!"
        )
    },
    "🐆 Cheetah": {
        "emoji": "🐆", "color": "#e65100", "bg": "#fff3e0",
        "record": "🏆 Fastest Land Animal",
        "body": (
            "The **Cheetah** is the fastest animal on land — it accelerates faster than most sports cars! 🏎️\n\n"
            "- 💨 Top speed: **120 km/h** (from 0 to 96 km/h in just 3 seconds!)\n"
            "- 🏃 Stride: Each leap covers up to 8 metres — its feet are barely on the ground\n"
            "- 👁️ Eyes: Black 'tear marks' reduce sun glare — built-in sunglasses for hunting!\n"
            "- 😮‍💨 Exhaustion: A sprint lasts only 20–30 seconds before they must rest and pant\n"
            "- 📢 Voice: Unlike other big cats, cheetahs PURR — they cannot roar!"
        )
    },
    "🦅 Peregrine Falcon": {
        "emoji": "🦅", "color": "#4527a0", "bg": "#ede7f6",
        "record": "🏆 Fastest Animal on Earth",
        "body": (
            "The **Peregrine Falcon** is the fastest creature on the entire planet — nothing moves faster! ⚡\n\n"
            "- 💨 Diving speed: **389 km/h** — faster than a racing car!\n"
            "- 🎯 Hunting: It tucks its wings and dives from great height onto prey\n"
            "- 👁️ Eyes: Can spot a pigeon from 8 km away — the sharpest eyes in the animal kingdom\n"
            "- 🌍 Range: Found on every continent except Antarctica — the world's most widespread bird of prey\n"
            "- 💪 Recovery: Near-extinct in the 1970s, it made a remarkable comeback thanks to conservation! 🌟"
        )
    },
    "🐘 African Elephant": {
        "emoji": "🐘", "color": "#5d4037", "bg": "#efebe9",
        "record": "🏆 Biggest Land Animal",
        "body": (
            "The **African Elephant** is the largest animal living on land today — massive and magnificent! 🐘\n\n"
            "- ⚖️ Weight: Up to **7,000 kg** — heavier than a large truck!\n"
            "- 🦷 Tusks: Made of ivory — used for digging, lifting and defence\n"
            "- 👃 Trunk: Has over 40,000 muscles — used for breathing, smelling, drinking, and picking things up\n"
            "- 🧠 Memory: Exceptional memory — they remember water sources, friends, and enemies for decades\n"
            "- 👪 Family: Live in close family groups led by the oldest female — the matriarch. They even comfort each other when sad. 💕"
        )
    },
    "🐢 Galápagos Tortoise": {
        "emoji": "🐢", "color": "#33691e", "bg": "#f9fbe7",
        "record": "🏆 Longest-Living Animal",
        "body": (
            "The **Galápagos Tortoise** is the longest-living animal on Earth — some alive today were born before your great-great-grandparents! 👴\n\n"
            "- 📅 Lifespan: Can live for **175+ years**\n"
            "- ⚖️ Weight: Up to **400 kg** — the world's largest tortoise\n"
            "- 💧 Water storage: Can store water in their bladder and survive up to a year without drinking\n"
            "- 🐢 Growth: They grow very slowly — it takes 40 years to reach full size\n"
            "- 🏝️ Home: Found only on the Galápagos Islands in the Pacific Ocean — Charles Darwin studied them to develop his theory of evolution! 🔬"
        )
    },
    "🐜 Leafcutter Ant": {
        "emoji": "🐜", "color": "#827717", "bg": "#f9fbe7",
        "record": "🏆 World's Strongest Animal (relative to size)",
        "body": (
            "The **Leafcutter Ant** is the strongest animal on Earth relative to its size — and it runs one of nature's most sophisticated societies! 🐜\n\n"
            "- 💪 Strength: Can carry **50 times** its own body weight — equivalent to a human carrying a car!\n"
            "- 🍄 Farming: They don't eat the leaves — they carry them underground to grow FUNGUS, which they then eat. They are farmers! 🌾\n"
            "- 🏙️ Colony: A colony can have **8 million** ants — all working together as one superorganism\n"
            "- ✂️ Cutting: They use their jaws like scissors — vibrating them 1,000 times per second to cut through leaves\n"
            "- 👑 Queen: The queen can live for **20 years** and lays millions of eggs"
        )
    },
}

animal_cols = st.columns(len(record_animals))
for i, (aname, adata) in enumerate(record_animals.items()):
    with animal_cols[i]:
        short = aname.split(" ")[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"rec_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in record_animals:
    aname = st.session_state.animal_picked
    adata = record_animals[aname]
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
                    {adata['record']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(adata["body"])
else:
    st.info("👆 Tap any animal above to learn about its world record!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — PROTECTING ANIMALS
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Protecting Animals — Why It Matters!",
               "Every animal plays a role — when one disappears, everything changes.")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Extinction** means a type of animal has completely disappeared from Earth — 
    forever. Once an animal is gone, it is gone for good. 😢

    Sadly, animals are disappearing faster today than ever before in history — 
    and the main reason is **humans.**
    """)
    for icon, label, desc in [
        ("🌳", "Habitat Destruction", "When forests are cut down and wetlands are drained, animals lose their homes and food. With nowhere to live, they cannot survive."),
        ("🎯", "Hunting",             "Some animals have been hunted for their fur, horns, or tusks until almost none are left. Rhinos and elephants are threatened this way."),
        ("🌡️", "Climate Change",      "As Earth warms up, the habitats animals depend on are changing. Polar bears are losing their sea ice, coral reefs are dying, and seasons are shifting."),
        ("🏭", "Pollution",           "Plastic in the oceans kills whales and seabirds. Chemicals in rivers poison fish. What we throw away can end up hurting wild animals far away."),
    ]:
        fun_card(icon, label, desc, bg="#fce4ec", border="#c62828")

with col2:
    st.markdown("""
    #### But there is GOOD NEWS! 🌟 We CAN help!
    """)
    for icon, label, desc in [
        ("🏞️", "National Parks",    "Huge areas of land and sea are protected from hunting and building so animals can live safely. Kenya's national parks saved the elephant from extinction!"),
        ("🌱", "Conservation Breeding","Zoos carefully breed endangered animals and release them back into the wild. The Arabian Oryx and California Condor were saved this way!"),
        ("♻️", "Reduce Pollution",  "Using less plastic, recycling, and keeping rivers clean helps protect the animals that depend on clean water and habitats."),
        ("🧒", "Education",         "Learning about animals — like YOU are doing right now — helps people care about them. People protect what they love! 💚"),
    ]:
        fun_card(icon, label, desc, bg="#e8f5e9", border="#43a047")

    think_bubble("What is ONE thing YOU could do to help animals this week? 🌍💚")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Let's Test What You Know!",
               "6 big animal questions — then check your score! 🐾")

questions = [
    {
        "q":    "Q1 🦁 — What do we call animals that feed their babies with milk?",
        "opts": ["Reptiles", "Birds", "Mammals", "Fish"],
        "ans":  "Mammals",
        "explain": "Mammals are the only animals that make milk to feed their babies — and YOU are a mammal! 🍼🦁"
    },
    {
        "q":    "Q2 🐠 — How do fish breathe underwater?",
        "opts": ["With lungs", "With gills", "Through their skin", "They hold their breath"],
        "ans":  "With gills",
        "explain": "Fish breathe through gills — special organs that pull oxygen out of water. 🫧🐠"
    },
    {
        "q":    "Q3 🦋 — How many legs does every insect have?",
        "opts": ["4 legs", "8 legs", "6 legs", "10 legs"],
        "ans":  "6 legs",
        "explain": "ALL insects have exactly 6 legs — no more, no less! If it has 8 legs (like a spider), it's NOT an insect. 🦋"
    },
    {
        "q":    "Q4 🌿 — What is an animal called that eats ONLY plants?",
        "opts": ["Carnivore", "Omnivore", "Herbivore", "Predator"],
        "ans":  "Herbivore",
        "explain": "Herbivores eat only plants. Carnivores eat only meat. Omnivores eat BOTH — like bears and humans! 🌿🐇"
    },
    {
        "q":    "Q5 🐸 — What is special about amphibians?",
        "opts": ["They only live on land", "They live in the sky", "They are born in water but can live on land too", "They have dry, scaly skin"],
        "ans":  "They are born in water but can live on land too",
        "explain": "Amphibian means 'double life' — they start life in water as tadpoles and grow into land animals! 🌊🐸🌿"
    },
    {
        "q":    "Q6 🏆 — Which is the BIGGEST animal to ever live on Earth?",
        "opts": ["African Elephant", "Tyrannosaurus Rex", "Blue Whale", "Giraffe"],
        "ans":  "Blue Whale",
        "explain": "The Blue Whale is the largest animal EVER — bigger than any dinosaur! It can be 33 metres long. 🐋💙"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"animal_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="animal_quiz_submit"):
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
        (6, "🏆", "ANIMAL EXPERT!",         "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Naturalist!",   "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Wildlife Explorer!","#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Animal Lover!", "#43a047", "#e8f5e9"),
        (0, "🐾", "Keep Exploring! Try Again!","#e65100","#fff3e0"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="animal_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?", "A quick summary — well done for finishing! 🎉")

summary_items = [
    ("🦁", "Mammals",     "Warm-blooded, have fur, feed babies milk"),
    ("🐦", "Birds",       "Have feathers, lay hard-shelled eggs"),
    ("🐠", "Fish",        "Breathe with gills, have scales, live in water"),
    ("🦋", "Insects",     "6 legs, 3 body parts, exoskeleton"),
    ("🦎", "Reptiles",    "Cold-blooded, dry scales, lay leathery eggs"),
    ("🐸", "Amphibians",  "Double life — born in water, live on land"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #f9a825;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1a3a1a,#2e6b2e,#4e3b1a);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        🐘 Keep exploring, little naturalist! 🦁
    </div>
    <div style="color:#dcedc8; font-size:0.95rem;">
        Every animal — from the tiniest ant to the biggest whale — deserves our care and curiosity!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        🐘 🦁 🐦 🐠 🦋 🐸 🦎 🐋
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

