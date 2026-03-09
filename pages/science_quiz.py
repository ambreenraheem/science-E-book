import streamlit as st
import streamlit.components.v1 as components

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Science.Game", layout="wide", initial_sidebar_state="expanded")
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
        <div style="font-size:0.8rem; color:#90caf9;">Grades 1-3 · Ages 5-8</div>
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
    unsafe_allow_html=True)
# Footer
with st.sidebar:st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True) 


# ─── Full Game HTML (vanilla JS — no build tools, no React) ──────────────────
GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Trebuchet MS', Georgia, serif; background: #F3F0EB; min-height: 100vh; }
  button { cursor: pointer; font-family: inherit; border: none; outline: none; }
  img { display: block; }

  /* ── Layout ── */
  .screen { display: none; }
  .screen.active { display: block; }

  /* ── Home Header ── */
  .home-header {
    background: linear-gradient(160deg, #0C1F35, #164066, #1B4F72);
    padding: 36px 22px 28px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .star { position: absolute; border-radius: 50%; background: white; }
  .home-header h1 { color: white; font-size: clamp(22px,5vw,36px); font-weight: 900; margin: 0 0 6px; text-shadow: 0 2px 14px rgba(0,0,0,.4); }
  .home-header p  { color: rgba(255,255,255,.62); margin: 0 0 18px; font-size: 14px; }
  .gold-badge-pill {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(255,210,60,.14); border: 1px solid rgba(255,210,60,.32);
    border-radius: 30px; padding: 5px 16px; margin-bottom: 14px;
    color: #FFD700; font-weight: 700; font-size: 12px; letter-spacing: 1.2px; text-transform: uppercase;
  }
  .type-pills { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
  .type-pill  { border-radius: 20px; padding: 3px 11px; font-size: 11px; font-weight: 700; }

  /* ── Topic Grid ── */
  .topic-grid {
    max-width: 900px; margin: 0 auto;
    padding: 28px 16px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(188px, 1fr));
    gap: 15px;
  }
  .topic-card {
    background: white; border-radius: 16px; overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,.07);
    border: 2px solid transparent;
    transition: transform .17s ease, box-shadow .17s ease, border-color .17s ease;
    text-align: left;
  }
  .topic-card:hover { transform: translateY(-5px); box-shadow: 0 10px 26px rgba(0,0,0,.13); }
  .topic-card-img   { position: relative; height: 94px; overflow: hidden; }
  .topic-card-img img { width: 100%; height: 100%; object-fit: cover; opacity: .87; }
  .topic-card-overlay { position: absolute; inset: 0; }
  .topic-card-icon {
    position: absolute; top: 8px; right: 8px;
    width: 30px; height: 30px; border-radius: 50%;
    background: white; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 8px rgba(0,0,0,.18);
  }
  .topic-card-body  { padding: 10px 13px 13px; }
  .topic-card-title { font-weight: 800; font-size: 13.5px; color: #1A2E4A; }
  .topic-card-count { font-size: 11.5px; color: #999; margin-top: 2px; }
  .topic-type-tags  { margin-top: 7px; display: flex; gap: 4px; flex-wrap: wrap; }
  .topic-type-tag   { font-size: 9px; font-weight: 700; padding: 2px 6px; border-radius: 10px; border: 1px solid; }
  .home-footer { text-align: center; padding-bottom: 28px; color: #BBB; font-size: 13px; }

  /* ── Quiz Topbar ── */
  .quiz-topbar {
    background: white; padding: 10px 18px;
    display: flex; align-items: center; gap: 10px;
    border-bottom: 3px solid var(--topic-color, #333);
    position: sticky; top: 0; z-index: 10;
  }
  .back-btn {
    display: flex; align-items: center; gap: 5px;
    color: #666; font-size: 13px; font-weight: 700;
    background: none; padding: 4px 8px; border-radius: 8px;
  }
  .back-btn:hover { background: #F3F3F3; }
  .progress-wrap { flex: 1; height: 7px; background: #EEE; border-radius: 4px; overflow: hidden; }
  .progress-bar  { height: 100%; border-radius: 4px; transition: width .45s ease; }
  .q-counter { font-weight: 700; font-size: 12px; padding: 3px 10px; border-radius: 20px; white-space: nowrap; }
  .score-pill { display: flex; align-items: center; gap: 4px; background: #FFFBEA; color: #B45309; font-weight: 700; font-size: 12px; padding: 3px 10px; border-radius: 20px; }

  /* ── Quiz Body ── */
  .quiz-body { max-width: 650px; margin: 0 auto; padding: 22px 18px 36px; }
  .chip-row  { display: flex; gap: 7px; margin-bottom: 14px; flex-wrap: wrap; }
  .chip      { border-radius: 20px; padding: 4px 12px; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: .7px; border: 1px solid; }
  .question  { color: #0D1D2F; font-size: clamp(15px, 2.7vw, 20px); font-weight: 800; margin-bottom: 18px; line-height: 1.42; }

  /* ── Images ── */
  .q-img-large { border-radius: 16px; overflow: hidden; margin-bottom: 20px; height: 230px; border: 2px solid rgba(0,0,0,.05); box-shadow: 0 4px 20px rgba(0,0,0,.1); }
  .q-img-small { border-radius: 13px; overflow: hidden; margin-bottom: 18px; height: 158px; }
  .q-img-large img, .q-img-small img { width: 100%; height: 100%; object-fit: cover; }

  /* ── Scramble ── */
  .scramble-box {
    border-radius: 16px; padding: 18px 20px; margin-bottom: 20px;
    text-align: center; border: 2px dashed;
  }
  .scramble-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 13px; }
  .tiles-row { display: flex; gap: 7px; justify-content: center; flex-wrap: wrap; }
  .letter-tile {
    width: 42px; height: 52px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; font-weight: 900; font-family: Georgia, serif;
    color: white; user-select: none;
    box-shadow: 0 4px 0 rgba(0,0,0,.28), 0 6px 14px rgba(0,0,0,.12);
  }
  .scramble-answer { margin-top: 14px; font-size: 13px; font-weight: 700; }
  .answer-pill { border-radius: 12px; padding: 2px 10px; color: white; margin-left: 4px; display: inline-block; }

  /* ── Choices ── */
  .choices-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .choice-btn {
    background: white; border: 2px solid #E5E7EB;
    border-radius: 12px; padding: 12px 14px;
    display: flex; align-items: center; gap: 9px;
    color: #0D1D2F; font-weight: 600; font-size: 13px;
    transition: border-color .12s ease;
    text-align: left; line-height: 1.3;
  }
  .choice-btn:hover:not(:disabled) { border-color: var(--topic-color, #333); }
  .choice-btn:disabled { cursor: default; }
  .choice-btn.correct { background: #F0FDF4; border-color: #22C55E; color: #15803D; box-shadow: 0 0 0 3px rgba(134,239,172,.28); }
  .choice-btn.wrong   { background: #FFF1F0; border-color: #EF4444; color: #DC2626; }
  .choice-letter {
    min-width: 24px; height: 24px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 11px; flex-shrink: 0;
  }

  /* ── Feedback ── */
  .feedback { margin-top: 16px; }
  .result-line {
    padding: 11px 16px; border-radius: 11px;
    font-weight: 700; font-size: 13px;
    display: flex; align-items: center; gap: 8px; margin-bottom: 12px;
    border: 1px solid;
  }
  .result-line.ok    { background: #F0FDF4; border-color: #86EFAC; color: #15803D; }
  .result-line.wrong { background: #FFF1F0; border-color: #FECACA; color: #DC2626; }
  .fact-box {
    padding: 14px 16px; border-radius: 13px; margin-bottom: 14px;
    background: linear-gradient(135deg, #FDF4FF, #F3E8FF);
    border: 1px solid #D8B4FE;
  }
  .fact-inner { display: flex; gap: 10px; align-items: flex-start; }
  .fact-icon  { width: 30px; height: 30px; border-radius: 50%; background: #7E22CE; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px; }
  .fact-label { font-weight: 800; font-size: 11px; color: #7E22CE; text-transform: uppercase; letter-spacing: .9px; margin-bottom: 5px; }
  .fact-text  { font-size: 13px; color: #4B0082; line-height: 1.55; }
  .next-btn {
    display: flex; align-items: center; justify-content: center; gap: 8px;
    width: 100%; padding: 13px 28px; border-radius: 12px;
    color: white; font-weight: 800; font-size: 14px;
  }

  /* ── Dot progress ── */
  .dot-row { display: flex; gap: 5px; justify-content: center; margin-top: 22px; flex-wrap: wrap; }
  .dot { height: 8px; border-radius: 4px; transition: all .25s ease; }

  /* ── Result Screen ── */
  .result-wrap {
    min-height: 100vh; display: flex; flex-direction: column;
    align-items: center; justify-content: center; padding: 26px 16px;
  }
  .result-card {
    background: white; border-radius: 24px; padding: 36px 30px;
    max-width: 440px; width: 100%;
    box-shadow: 0 8px 40px rgba(0,0,0,.1);
    border: 3px solid rgba(0,0,0,.06);
    text-align: center;
  }
  .result-topic-label { color: #AAA; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 1.3px; margin-bottom: 6px; }
  .badge-circle {
    width: 86px; height: 86px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 10px;
  }
  .badge-label { font-family: Georgia, serif; font-weight: 800; font-size: 17px; color: #1A2E4A; }
  .score-big   { font-size: 50px; font-weight: 900; line-height: 1; }
  .score-total { font-size: 22px; color: #CCC; }
  .score-bar-wrap { background: #F3F4F6; border-radius: 50px; height: 8px; overflow: hidden; margin: 12px 0 8px; }
  .score-bar  { height: 100%; border-radius: 50px; transition: width 1.1s ease; }
  .score-msg  { font-size: 13px; color: #666; }
  .breakdown  { background: #F8F7F5; border-radius: 14px; padding: 14px 16px; margin-bottom: 20px; }
  .breakdown-title { font-size: 10px; font-weight: 700; color: #BBB; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
  .breakdown-row { display: flex; align-items: center; gap: 9px; margin-bottom: 8px; }
  .breakdown-label { width: 72px; font-size: 10px; font-weight: 700; border-radius: 10px; padding: 2px 6px; text-align: center; white-space: nowrap; border: 1px solid; }
  .breakdown-bar-wrap { flex: 1; height: 7px; background: #E5E7EB; border-radius: 4px; overflow: hidden; }
  .breakdown-bar { height: 100%; border-radius: 4px; transition: width 1s ease; }
  .breakdown-score { font-size: 12px; font-weight: 700; color: #555; min-width: 28px; }
  .result-btns { display: flex; gap: 10px; }
  .btn-retry, .btn-home {
    flex: 1; padding: 13px; border-radius: 12px;
    font-weight: 800; font-size: 13px; text-align: center;
  }

  @media (max-width: 500px) {
    .choices-grid { grid-template-columns: 1fr; }
    .topic-grid   { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
  }
</style>
</head>
<body>

<!-- ═══════════════════════════ HOME SCREEN ═══════════════════════════════ -->
<div id="screen-home" class="screen active">
  <div class="home-header" id="home-header">
    <div class="gold-badge-pill">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="#FFD700"><path d="M12 2L14.5 9H22L16 13.5L18.5 21L12 17L5.5 21L8 13.5L2 9H9.5Z"/></svg>
      Science Explorer
    </div>
    <h1>The Big Science Quiz</h1>
    <p>10+ questions per topic &mdash; Multiple Choice &middot; Spot-It &middot; Spelling &middot; History</p>
    <div class="type-pills">
      <span class="type-pill" style="background:#EFF6FF;color:#1D4ED8;border:1px solid #BFDBFE">Multiple Choice</span>
      <span class="type-pill" style="background:#FFF7ED;color:#C2410C;border:1px solid #FED7AA">Spell It Right!</span>
      <span class="type-pill" style="background:#F0FDF4;color:#15803D;border:1px solid #BBF7D0">Spot It!</span>
      <span class="type-pill" style="background:#FDF4FF;color:#7E22CE;border:1px solid #E9D5FF">History Fact</span>
    </div>
  </div>
  <div class="topic-grid" id="topic-grid"></div>
  <div class="home-footer">Pick any topic above to begin your adventure</div>
</div>

<!-- ═══════════════════════════ QUIZ SCREEN ════════════════════════════════ -->
<div id="screen-quiz" class="screen">
  <div class="quiz-topbar" id="quiz-topbar">
    <button class="back-btn" onclick="showHome()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
      Topics
    </button>
    <div class="progress-wrap"><div class="progress-bar" id="progress-bar"></div></div>
    <span class="q-counter" id="q-counter"></span>
    <span class="score-pill">
      <svg width="11" height="11" viewBox="0 0 24 24" fill="#B45309"><path d="M12 2L14.5 9H22L16 13.5L18.5 21L12 17L5.5 21L8 13.5L2 9H9.5Z"/></svg>
      <span id="score-display">0</span>
    </span>
  </div>
  <div class="quiz-body">
    <div class="chip-row" id="chip-row"></div>
    <div class="question" id="question-text"></div>
    <div id="q-img-container"></div>
    <div id="scramble-container"></div>
    <div class="choices-grid" id="choices-grid"></div>
    <div class="feedback" id="feedback" style="display:none"></div>
    <div class="dot-row" id="dot-row"></div>
  </div>
</div>

<!-- ═══════════════════════════ RESULT SCREEN ═════════════════════════════ -->
<div id="screen-result" class="screen">
  <div class="result-wrap">
    <div class="result-card" id="result-card">
      <div class="result-topic-label" id="result-topic-label"></div>
      <div style="text-align:center;margin-bottom:4px">
        <div class="badge-circle" id="badge-circle">
          <svg width="44" height="44" viewBox="0 0 48 48" fill="white"><path d="M24 4L29.5 17H44L32.5 26L37 40L24 32L11 40L15.5 26L4 17H18.5Z"/></svg>
        </div>
        <div class="badge-label" id="badge-label"></div>
      </div>
      <div style="margin:20px 0 16px">
        <div style="font-size:11px;color:#AAA;margin-bottom:3px">Your Score</div>
        <div class="score-big" id="score-big"></div>
        <div class="score-bar-wrap"><div class="score-bar" id="score-bar"></div></div>
        <div class="score-msg" id="score-msg"></div>
      </div>
      <div class="breakdown" id="breakdown"></div>
      <div class="result-btns">
        <button class="btn-retry" id="btn-retry" onclick="retryQuiz()"></button>
        <button class="btn-home"  onclick="showHome()" style="color:white">All Topics</button>
      </div>
    </div>
  </div>
</div>

<script>
// ─── DATA ─────────────────────────────────────────────────────────────────────
const TOPICS = [
  { id:"body",     title:"Our Body",        color:"#C0392B", bg:"#FDF0EE",
    img:"https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><circle cx="20" cy="8" r="4"/><path d="M13 16h14M20 16v12M13 28l-3 7M27 28l3 7M13 21l-3 4M27 21l3 4"/></svg>` },
  { id:"senses",   title:"Five Senses",     color:"#6C3483", bg:"#F5EEF8",
    img:"https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><ellipse cx="20" cy="20" rx="15" ry="9"/><circle cx="20" cy="20" r="5"/><circle cx="20" cy="20" r="2" fill="currentColor"/></svg>` },
  { id:"animals",  title:"Animals",         color:"#1E8449", bg:"#EAFAF1",
    img:"https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><ellipse cx="20" cy="24" rx="11" ry="8"/><circle cx="10" cy="13" r="4"/><circle cx="30" cy="13" r="4"/><circle cx="16" cy="22" r="1.5" fill="currentColor"/><circle cx="24" cy="22" r="1.5" fill="currentColor"/><path d="M18 27 Q20 30 22 27"/></svg>` },
  { id:"plants",   title:"Plants",          color:"#27AE60", bg:"#EDFAF1",
    img:"https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><path d="M20 36V18"/><path d="M20 26 Q11 18 11 8 Q20 8 20 18"/><path d="M20 21 Q29 15 31 5 Q22 5 20 15"/><path d="M15 34 Q20 32 25 34"/></svg>` },
  { id:"magnet",   title:"Magnets",         color:"#1A5276", bg:"#EBF5FB",
    img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><path d="M10 8 L10 22 Q10 32 20 32 Q30 32 30 22 L30 8"/><path d="M8 8 L16 8M24 8 L32 8"/><line x1="3" y1="16" x2="9" y2="16"/><line x1="31" y1="16" x2="37" y2="16"/></svg>` },
  { id:"space",    title:"Space",           color:"#154360", bg:"#EAF2FF",
    img:"https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><circle cx="20" cy="20" r="7"/><path d="M20 3v4M20 33v4M3 20h4M33 20h4M8 8l3 3M29 29l3 3M32 8l-3 3M11 29l-3 3"/></svg>` },
  { id:"machines", title:"Simple Machines", color:"#784212", bg:"#FEF5E7",
    img:"https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><circle cx="20" cy="20" r="9"/><circle cx="20" cy="20" r="3"/><path d="M20 11v-5M20 29v5M11 20H6M29 20h5M13.5 13.5l-3.5-3.5M26.5 26.5l3.5 3.5M26.5 13.5l3.5-3.5M13.5 26.5l-3.5 3.5"/></svg>` },
  { id:"weather",  title:"Water & Weather", color:"#0E6655", bg:"#E8F8F5",
    img:"https://images.unsplash.com/photo-1504608524841-42584120d693?w=420&h=230&fit=crop",
    iconSvg:`<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" width="22" height="22"><path d="M6 24 Q6 17 13 17 Q13 10 20 10 Q27 10 27 17 Q34 17 34 24 Q34 31 20 31 Q6 31 6 24Z"/><path d="M15 33L13 38M20 33L20 38M25 33L23 38"/></svg>` },
];

const TYPE_CFG = {
  mcq:      { label:"Multiple Choice", bg:"#EFF6FF", color:"#1D4ED8", border:"#BFDBFE" },
  scramble: { label:"Spell It Right!", bg:"#FFF7ED", color:"#C2410C", border:"#FED7AA" },
  image:    { label:"Spot It!",        bg:"#F0FDF4", color:"#15803D", border:"#BBF7D0" },
  history:  { label:"History Fact",   bg:"#FDF4FF", color:"#7E22CE", border:"#E9D5FF" },
};

const QUESTIONS = {
  body: [
    { type:"mcq",     q:"Which organ pumps blood around your body?", choices:["Brain","Heart","Lungs","Stomach"], ans:1, img:"https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many bones does an adult human body have?", choices:["106","206","306","406"], ans:1, img:"https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What is the main job of our lungs?", choices:["Digest food","Pump blood","Help us breathe","Move our arms"], ans:2 },
    { type:"mcq",     q:"How many chambers does the human heart have?", choices:["Two","Three","Four","Five"], ans:2 },
    { type:"mcq",     q:"What carries oxygen through the blood?", choices:["White blood cells","Red blood cells","Platelets","Plasma"], ans:1 },
    { type:"mcq",     q:"Which organ cleans the blood and removes waste from the body?", choices:["Stomach","Liver","Kidneys","Heart"], ans:2 },
    { type:"history", q:"William Harvey discovered in 1628 that the heart pumps blood in a continuous ___ around the body.", choices:["Zigzag","Loop / Circle","Straight line","Spiral"], ans:1, fact:"In 1628, William Harvey published proof that the heart pumps blood in a continuous loop. Before this, people believed blood was made fresh every day! He changed medicine forever." },
    { type:"history", q:"Ancient Egyptians believed that thinking happened in the heart, not the ___.", choices:["Stomach","Lungs","Brain","Liver"], ans:2, fact:"Ancient Egyptians thought the heart was the seat of thought and feeling. When making mummies, they threw the brain away but kept the heart! It was not until ancient Greece that the brain's role was understood." },
    { type:"image",   q:"What part of the body is shown in this X-ray picture?", choices:["Skull","Spine","Full Skeleton","Ribcage"], ans:2, img:"https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=440&h=270&fit=crop" },
    { type:"image",   q:"Which important organ does this model show?", choices:["Stomach","Kidney","Heart","Liver"], ans:2, img:"https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"RATHE", choices:["HEART","LUNGS","BRAIN","LIVER"], ans:0 },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"GULNS", choices:["BONES","LUNGS","SPINE","HEART"], ans:1 },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"NIABR", choices:["BRAIN","HEART","SPINE","NERVE"], ans:0 },
  ],
  senses: [
    { type:"mcq",     q:"Which sense do we use when we smell a flower?", choices:["Sight","Hearing","Smell","Touch"], ans:2, img:"https://images.unsplash.com/photo-1490750967868-88df5691cc27?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which body part helps us see the world?", choices:["Nose","Ears","Eyes","Tongue"], ans:2 },
    { type:"mcq",     q:"What sense do we use when we listen to music?", choices:["Taste","Hearing","Smell","Sight"], ans:1, img:"https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which sense tells us if food is sweet, salty or sour?", choices:["Touch","Smell","Sight","Taste"], ans:3 },
    { type:"mcq",     q:"What body part do we use to feel if something is hot, cold or rough?", choices:["Eyes","Ears","Skin","Nose"], ans:2 },
    { type:"mcq",     q:"How many main senses does the human body have?", choices:["3","4","5","6"], ans:2 },
    { type:"history", q:"The ancient Greek thinker Aristotle was the first to name the five senses. He lived roughly ___ years ago.", choices:["About 100","About 500","About 2,300","About 5,000"], ans:2, fact:"Aristotle (384-322 BC) was the first thinker to formally describe and name the five senses. That was over 2,300 years ago!" },
    { type:"history", q:"Louis Braille lost his sight at age 3 and went on to invent a reading system for blind people using raised ___.", choices:["Lines","Dots","Squares","Arrows"], ans:1, fact:"Louis Braille (1809-1852) became blind at age 3. By age 15 he invented the Braille system - a code of raised dots that blind people can read by touch. Today it is used worldwide!" },
    { type:"image",   q:"Which sense organ is shown in this close-up picture?", choices:["Ear","Nose","Eye","Tongue"], ans:2, img:"https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?w=440&h=270&fit=crop" },
    { type:"image",   q:"We use this sense to feel textures like rough or smooth. What sense is being used?", choices:["Smell","Taste","Hearing","Touch"], ans:3, img:"https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this sense word!", scrambled:"LEMLS", choices:["SMELL","TASTE","SIGHT","TOUCH"], ans:0 },
    { type:"scramble", q:"Unscramble this sense word!", scrambled:"HTOUC", choices:["TASTE","SMELL","TOUCH","SIGHT"], ans:2 },
  ],
  animals: [
    { type:"mcq",     q:"Which animal is known as the King of the Jungle?", choices:["Tiger","Lion","Elephant","Giraffe"], ans:1, img:"https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How do fish breathe underwater?", choices:["Lungs","Skin","Gills","Nose"], ans:2, img:"https://images.unsplash.com/photo-1524704796725-9fc3044a58b2?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which animal can change its skin colour to hide from enemies?", choices:["Dog","Chameleon","Horse","Deer"], ans:1 },
    { type:"mcq",     q:"Which animal has the longest neck in the whole world?", choices:["Elephant","Giraffe","Camel","Horse"], ans:1 },
    { type:"mcq",     q:"What do caterpillars turn into after their chrysalis stage?", choices:["Birds","Worms","Butterflies","Spiders"], ans:2 },
    { type:"mcq",     q:"What is the fastest land animal on Earth?", choices:["Lion","Horse","Cheetah","Leopard"], ans:2 },
    { type:"mcq",     q:"What is a group of wolves called?", choices:["Herd","Pack","Flock","Pride"], ans:1 },
    { type:"history", q:"Aristotle wrote the world's first book about animals around 350 BC. He described roughly how many species?", choices:["About 50","About 500","About 50,000","About 5,000"], ans:1, fact:"Around 350 BC, Aristotle wrote 'History of Animals,' describing about 500 species. He is called the Father of Zoology!" },
    { type:"history", q:"Charles Darwin discovered that animals change slowly over many generations. This idea is called ___.", choices:["Gravity","Evolution","Photosynthesis","Migration"], ans:1, fact:"In 1859, Charles Darwin published 'On the Origin of Species,' explaining that all animals evolved slowly over millions of years. One of the most important ideas in all of science!" },
    { type:"image",   q:"Which big cat is shown in this photo?", choices:["Tiger","Cheetah","Lion","Leopard"], ans:2, img:"https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=440&h=270&fit=crop" },
    { type:"image",   q:"Name this tall African animal!", choices:["Camel","Horse","Giraffe","Zebra"], ans:2, img:"https://images.unsplash.com/photo-1547721064-da6cfb341d50?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this animal name!", scrambled:"LAEGE", choices:["EAGLE","SNAKE","WHALE","TIGER"], ans:0 },
    { type:"scramble", q:"Unscramble this animal name!", scrambled:"LHAEW", choices:["SHARK","EAGLE","HORSE","WHALE"], ans:3 },
  ],
  plants: [
    { type:"mcq",     q:"What do plants use sunlight to make?", choices:["Water","Food (Sugar)","Air","Soil"], ans:1, img:"https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which part of the plant is found underground and absorbs water?", choices:["Leaf","Flower","Root","Stem"], ans:2 },
    { type:"mcq",     q:"What do seeds need to start growing (germinating)?", choices:["Sunlight only","Water, Soil & Sunlight","Just water","Just soil"], ans:1 },
    { type:"mcq",     q:"Which gas do plants produce during photosynthesis that we need to breathe?", choices:["Carbon dioxide","Nitrogen","Oxygen","Hydrogen"], ans:2 },
    { type:"mcq",     q:"What is the process that plants use to make food from sunlight called?", choices:["Digestion","Respiration","Photosynthesis","Pollination"], ans:2 },
    { type:"mcq",     q:"Which colourful part of the plant attracts bees and butterflies for pollination?", choices:["Root","Stem","Leaf","Flower"], ans:3 },
    { type:"mcq",     q:"A plant that stores water in its thick trunk and survives in hot deserts is a ___.", choices:["Fern","Cactus","Moss","Mushroom"], ans:1 },
    { type:"history", q:"Jan Ingenhousz discovered in 1779 that plants only produce food and release oxygen when exposed to ___.", choices:["Water","Soil","Light","Wind"], ans:2, fact:"In 1779, Jan Ingenhousz discovered photosynthesis - that plants make food using light. He noticed plants in sunlight produced tiny bubbles (oxygen), but stopped in the dark!" },
    { type:"history", q:"Gregor Mendel, a monk from Austria, discovered the rules of inheritance by studying which plant?", choices:["Roses","Pea plants","Sunflowers","Wheat"], ans:1, fact:"In the 1860s, Gregor Mendel grew thousands of pea plants in his garden and discovered how traits are passed from parents to children. He is called the Father of Genetics!" },
    { type:"image",   q:"What type of tall yellow flowering plant is this?", choices:["Rose","Tulip","Sunflower","Daisy"], ans:2, img:"https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=440&h=270&fit=crop" },
    { type:"image",   q:"This spiky plant stores water and grows in deserts. What is it?", choices:["Fern","Palm tree","Cactus","Bamboo"], ans:2, img:"https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this plant part!", scrambled:"TSOOR", choices:["SHOOT","ROOTS","SEEDS","STEMS"], ans:1 },
    { type:"scramble", q:"Unscramble this plant word!", scrambled:"EDESS", choices:["WEEDS","TREES","SEEDS","LEAFS"], ans:2 },
  ],
  magnet: [
    { type:"mcq",     q:"Which material is attracted to a magnet?", choices:["Plastic","Wood","Iron & Steel","Glass"], ans:2, img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many poles does every magnet have?", choices:["One","Two","Three","Four"], ans:1 },
    { type:"mcq",     q:"What happens when two North poles of magnets face each other?", choices:["They attract","They repel (push away)","They stick together","Nothing happens"], ans:1 },
    { type:"mcq",     q:"Which of these metals is NOT attracted to a magnet?", choices:["Iron","Steel","Aluminium","Nickel"], ans:2 },
    { type:"mcq",     q:"A magnet made by passing electricity through a coil of wire is called an ___.", choices:["Bar magnet","Horseshoe magnet","Electromagnet","Natural magnet"], ans:2 },
    { type:"mcq",     q:"What does the letter N stand for on a magnet?", choices:["Neutral","North","Negative","Normal"], ans:1 },
    { type:"history", q:"William Gilbert (1544-1603) was the first scientist to prove that the Earth itself acts like a giant ___.", choices:["Battery","Magnet","Electric wire","Volcano"], ans:1, fact:"In 1600, William Gilbert published 'De Magnete,' the first great scientific book in English history. He proved Earth is a giant magnet and also coined the word 'electricity'!" },
    { type:"history", q:"Ancient sailors used lodestones (natural magnets) to navigate. A compass always points towards which direction?", choices:["South","East","West","North"], ans:3, fact:"Over 2,000 years ago, Chinese sailors discovered that lodestone always points North - the world's first compass! By the 12th century, sailors everywhere used magnetic compasses." },
    { type:"image",   q:"This instrument uses a magnetic needle to show direction. What is it called?", choices:["Thermometer","Barometer","Compass","Ruler"], ans:2, img:"https://images.unsplash.com/photo-1465101046530-73398c7f28ca?w=440&h=270&fit=crop" },
    { type:"image",   q:"The two coloured ends of this magnet are called what?", choices:["Tips","Poles","Ends","Points"], ans:1, img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this magnet word!", scrambled:"HNORT", choices:["NORTH","SOUTH","FORCE","STEEL"], ans:0 },
    { type:"scramble", q:"Unscramble this magnet word!", scrambled:"SOELP", choices:["STEEL","POWER","POLES","FORCE"], ans:2 },
  ],
  space: [
    { type:"mcq",     q:"What is the closest star to planet Earth?", choices:["The Moon","Mars","The Sun","Venus"], ans:2, img:"https://images.unsplash.com/photo-1532693322450-2cb5c511067d?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many planets are in our Solar System?", choices:["7","8","9","10"], ans:1 },
    { type:"mcq",     q:"Which planet is known as the Red Planet?", choices:["Jupiter","Venus","Saturn","Mars"], ans:3, img:"https://images.unsplash.com/photo-1614728423169-3f65fd722b7e?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What do we call the curved path a planet takes as it travels around the Sun?", choices:["Revolution","Orbit","Rotation","Axis"], ans:1 },
    { type:"mcq",     q:"Which planet is famous for having beautiful rings around it?", choices:["Jupiter","Mars","Saturn","Neptune"], ans:2 },
    { type:"mcq",     q:"What is a shooting star actually made of?", choices:["A falling star","A meteor burning in the atmosphere","A comet tail","A broken satellite"], ans:1 },
    { type:"mcq",     q:"What is the name of the galaxy our Solar System lives in?", choices:["Andromeda","Black Hole","The Milky Way","Nebula"], ans:2 },
    { type:"history", q:"Neil Armstrong became the first human to walk on the Moon on 20 July ___.", choices:["1959","1969","1979","1989"], ans:1, fact:"On 20 July 1969, Neil Armstrong stepped onto the Moon and said: 'That's one small step for man, one giant leap for mankind.' The Apollo 11 mission was watched by over 600 million people!" },
    { type:"history", q:"Galileo Galilei used a telescope in 1609 to look at space. What did he discover around Jupiter?", choices:["Rings","Craters","Four large moons","A giant storm"], ans:2, fact:"In 1609, Galileo pointed his telescope at Jupiter and discovered four large moons orbiting it - proving not everything in space orbits the Earth. He was put under house arrest for his discoveries!" },
    { type:"image",   q:"Which planet with spectacular rings is shown here?", choices:["Jupiter","Uranus","Neptune","Saturn"], ans:3, img:"https://images.unsplash.com/photo-1630839437035-dac17da580d0?w=440&h=270&fit=crop" },
    { type:"image",   q:"What natural object in our night sky is shown in this photo?", choices:["Planet","Comet","Full Moon","Star cluster"], ans:2, img:"https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this space word!", scrambled:"TCEMO", choices:["COMET","ORBIT","STARS","SPACE"], ans:0 },
    { type:"scramble", q:"Unscramble this space word!", scrambled:"RASST", choices:["ORBIT","SPACE","STARS","VENUS"], ans:2 },
  ],
  machines: [
    { type:"mcq",     q:"A sloping ramp used to move heavy things upward is called an ___.", choices:["Lever","Pulley","Inclined Plane","Wedge"], ans:2, img:"https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"A seesaw in the playground is an example of which simple machine?", choices:["Pulley","Lever","Wheel & Axle","Screw"], ans:1 },
    { type:"mcq",     q:"Which simple machine uses a wheel with a groove and a rope to lift heavy loads?", choices:["Lever","Wedge","Pulley","Screw"], ans:2 },
    { type:"mcq",     q:"A knife blade or an axe is an example of which simple machine?", choices:["Screw","Wedge","Pulley","Lever"], ans:1 },
    { type:"mcq",     q:"What does a wheel and axle help us do?", choices:["Cut things","Move things more easily","Lift water","Climb up walls"], ans:1 },
    { type:"mcq",     q:"A screw is actually a twisted version of which other simple machine?", choices:["Lever","Wheel","Wedge","Inclined Plane"], ans:3 },
    { type:"mcq",     q:"Scissors are made from two ___ joined at a pivot point.", choices:["Pulleys","Screws","Levers","Wheels"], ans:2 },
    { type:"history", q:"The ancient Greek scientist Archimedes (287-212 BC) famously said: 'Give me a long enough lever and I can move ___'", choices:["A mountain","The whole Earth","A building","The sea"], ans:1, fact:"Archimedes discovered the principles of the lever and pulley. He once used pulleys to move an entire warship on land by himself! He said he could move the Earth with a long enough lever." },
    { type:"history", q:"The wheel was invented in ancient Mesopotamia (modern Iraq) around ___ years ago.", choices:["500","1,000","5,500","10,000"], ans:2, fact:"The wheel was invented around 3,500 BC - about 5,500 years ago! It was first used for pottery, then for carts. It is considered one of the most important inventions in human history." },
    { type:"image",   q:"A playground slide is an example of which simple machine?", choices:["Lever","Pulley","Wedge","Inclined Plane"], ans:3, img:"https://images.unsplash.com/photo-1575783970733-1aaedde1db74?w=440&h=270&fit=crop" },
    { type:"image",   q:"These interlocking toothed wheels that transfer motion are called ___.", choices:["Screws","Gears","Pulleys","Levers"], ans:1, img:"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this simple machine name!", scrambled:"RVELE", choices:["WHEEL","LEVER","SCREW","RAMP"], ans:1 },
    { type:"scramble", q:"Unscramble this simple machine name!", scrambled:"LWEHE", choices:["LEVER","WEDGE","WHEEL","SCREW"], ans:2 },
  ],
  weather: [
    { type:"mcq",     q:"What causes rain to fall down from clouds?", choices:["Wind pushing it down","Water droplets becoming too heavy","The Sun heating it","Cold air rising up"], ans:1, img:"https://images.unsplash.com/photo-1504608524841-42584120d693?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What are clouds actually made of?", choices:["Cotton fibres","Smoke","Tiny water droplets","Floating dust"], ans:2, img:"https://images.unsplash.com/photo-1444930694458-01babf71ab07?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What is the continuous movement of water between the Earth and sky called?", choices:["Water cycle","Rain cycle","Cloud cycle","Wind cycle"], ans:0 },
    { type:"mcq",     q:"What do we call precipitation that falls as tiny ice crystals?", choices:["Rain","Sleet","Snow","Hail"], ans:2 },
    { type:"mcq",     q:"What causes wind to blow?", choices:["Movement of clouds","Differences in air pressure","The Sun rising","Water evaporating"], ans:1 },
    { type:"mcq",     q:"Which instrument measures the temperature of the air?", choices:["Barometer","Compass","Thermometer","Ruler"], ans:2 },
    { type:"mcq",     q:"A violent spinning column of wind that touches the ground is called a ___.", choices:["Hurricane","Tornado","Blizzard","Monsoon"], ans:1 },
    { type:"history", q:"Gabriel Fahrenheit invented the mercury thermometer in 1714. What does a thermometer measure?", choices:["Wind speed","Air pressure","Temperature","Rainfall"], ans:2, fact:"In 1714, Gabriel Fahrenheit invented the first accurate mercury thermometer. Later in 1742, Anders Celsius invented the Celsius scale. Both scales are still used today!" },
    { type:"history", q:"Robert FitzRoy made the world's first official weather forecast in 1861. What word did he invent for his predictions?", choices:["Weather map","Rain report","Weather forecast","Storm signal"], ans:2, fact:"In 1861, British admiral Robert FitzRoy made the world's first official weather forecast in a newspaper. He invented the word 'forecast' for weather! He also designed the Fitzroy Barometer." },
    { type:"image",   q:"What beautiful natural phenomenon appears after rain when sunlight passes through water droplets?", choices:["Aurora","Lightning","Rainbow","Sunset glow"], ans:2, img:"https://images.unsplash.com/photo-1501630834273-4b5604d2ee31?w=440&h=270&fit=crop" },
    { type:"image",   q:"What type of dramatic weather is shown in this picture?", choices:["Sunny day","Snowstorm","Thunderstorm","Foggy morning"], ans:2, img:"https://images.unsplash.com/photo-1472145246862-b24cf25495bf?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this weather word!", scrambled:"DOLCU", choices:["FLOOD","CLOUD","STORM","FROST"], ans:1 },
    { type:"scramble", q:"Unscramble this weather word!", scrambled:"MORTS", choices:["FROST","FLOOD","SLEET","STORM"], ans:3 },
  ],
};

// ─── STATE ────────────────────────────────────────────────────────────────────
let curTopic   = null;
let qIdx       = 0;
let score      = 0;
let answered   = false;
let gameLog    = [];

// ─── BOOT ─────────────────────────────────────────────────────────────────────
window.addEventListener('DOMContentLoaded', () => {
  buildStars();
  buildTopicGrid();
});

function buildStars() {
  const hdr = document.getElementById('home-header');
  for (let i = 0; i < 24; i++) {
    const s = document.createElement('div');
    s.className = 'star';
    const sz = i % 4 === 0 ? 3 : 2;
    s.style.cssText = `width:${sz}px;height:${sz}px;opacity:${0.12 + (i*7%5)*0.09};top:${(i*43+5)%90}%;left:${(i*61+9)%96}%`;
    hdr.appendChild(s);
  }
}

function buildTopicGrid() {
  const grid = document.getElementById('topic-grid');
  grid.innerHTML = '';
  TOPICS.forEach(t => {
    const types = ['mcq','image','scramble','history'].filter(tp => QUESTIONS[t.id].some(q => q.type === tp));
    const tagsHtml = types.map(tp => {
      const c = TYPE_CFG[tp];
      const lbl = tp==='mcq'?'MCQ':tp==='image'?'Spot It':tp==='scramble'?'Spell It':'History';
      return `<span class="topic-type-tag" style="background:${c.bg};color:${c.color};border-color:${c.border}">${lbl}</span>`;
    }).join('');

    const card = document.createElement('button');
    card.className = 'topic-card';
    card.innerHTML = `
      <div class="topic-card-img">
        <img src="${t.img}" alt="${t.title}" onerror="this.style.display='none'"/>
        <div class="topic-card-overlay" style="background:linear-gradient(to bottom,transparent 25%,${t.color}CC)"></div>
        <div class="topic-card-icon" style="color:${t.color}">${t.iconSvg}</div>
      </div>
      <div class="topic-card-body">
        <div class="topic-card-title">${t.title}</div>
        <div class="topic-card-count">${QUESTIONS[t.id].length} questions</div>
        <div class="topic-type-tags">${tagsHtml}</div>
      </div>`;
    card.addEventListener('mouseenter', () => { card.style.borderColor = t.color; });
    card.addEventListener('mouseleave', () => { card.style.borderColor = 'transparent'; });
    card.addEventListener('click', () => startQuiz(t));
    grid.appendChild(card);
  });
}

// ─── NAVIGATION ───────────────────────────────────────────────────────────────
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-' + id).classList.add('active');
  window.scrollTo(0, 0);
}

function showHome() { showScreen('home'); }

// ─── QUIZ ─────────────────────────────────────────────────────────────────────
function startQuiz(topic) {
  curTopic = topic;
  qIdx     = 0;
  score    = 0;
  answered = false;
  gameLog  = [];
  renderQuestion();
  showScreen('quiz');
}

function renderQuestion() {
  const qs  = QUESTIONS[curTopic.id];
  const cur = qs[qIdx];
  const tc  = TYPE_CFG[cur.type] || TYPE_CFG.mcq;

  // Topbar
  document.getElementById('quiz-topbar').style.borderBottomColor = curTopic.color;
  document.getElementById('progress-bar').style.cssText =
    `width:${(qIdx/qs.length)*100}%;background:linear-gradient(90deg,${curTopic.color},${curTopic.color}88)`;
  document.getElementById('q-counter').textContent = `${qIdx+1}/${qs.length}`;
  document.getElementById('q-counter').style.cssText =
    `background:${curTopic.bg};color:${curTopic.color};border:1px solid ${curTopic.color}30;font-weight:700;font-size:12px;padding:3px 10px;border-radius:20px;white-space:nowrap`;
  document.getElementById('score-display').textContent = score;

  // Chips
  document.getElementById('chip-row').innerHTML = `
    <span class="chip" style="background:${tc.bg};color:${tc.color};border-color:${tc.border}">${tc.label}</span>
    <span class="chip" style="background:${curTopic.bg};color:${curTopic.color};border-color:${curTopic.color}28">${curTopic.title}</span>`;

  // Question text
  document.getElementById('question-text').textContent = cur.q;

  // Image
  const imgBox = document.getElementById('q-img-container');
  if (cur.type === 'image' && cur.img) {
    imgBox.innerHTML = `<div class="q-img-large" style="background:${curTopic.bg}"><img src="${cur.img}" alt="identify" onerror="this.parentElement.style.display='none'"/></div>`;
  } else if (cur.type !== 'image' && cur.type !== 'scramble' && cur.img) {
    imgBox.innerHTML = `<div class="q-img-small" style="background:${curTopic.bg};border:2px solid ${curTopic.color}18"><img src="${cur.img}" alt="question" onerror="this.parentElement.style.display='none'"/></div>`;
  } else {
    imgBox.innerHTML = '';
  }

  // Scramble tiles
  const scBox = document.getElementById('scramble-container');
  if (cur.type === 'scramble') {
    const tiles = cur.scrambled.split('').map(ch =>
      `<div class="letter-tile" style="background:${curTopic.color}">${ch}</div>`
    ).join('');
    scBox.innerHTML = `
      <div class="scramble-box" style="background:${tc.bg};border-color:${tc.border}">
        <div class="scramble-label" style="color:${tc.color}">Unscramble the Letters</div>
        <div class="tiles-row">${tiles}</div>
        <div id="scramble-ans" class="scramble-answer" style="display:none;color:${curTopic.color}">
          Answer: <span class="answer-pill" style="background:${curTopic.color}">${cur.choices[cur.ans]}</span>
        </div>
      </div>`;
  } else {
    scBox.innerHTML = '';
  }

  // Choices
  const grid = document.getElementById('choices-grid');
  grid.innerHTML = '';
  cur.choices.forEach((c, i) => {
    const btn = document.createElement('button');
    btn.className = 'choice-btn';
    btn.dataset.idx = i;
    btn.innerHTML = `
      <span class="choice-letter" style="background:${curTopic.color}18;color:${curTopic.color}">${String.fromCharCode(65+i)}</span>
      ${c}`;
    btn.addEventListener('mouseenter', () => { if (!answered) btn.style.borderColor = curTopic.color; });
    btn.addEventListener('mouseleave', () => { if (!answered) btn.style.borderColor = '#E5E7EB'; });
    btn.addEventListener('click', () => pickAnswer(i));
    grid.appendChild(btn);
  });

  // Feedback hidden
  const fb = document.getElementById('feedback');
  fb.style.display = 'none';
  fb.innerHTML = '';

  // Dots
  renderDots();
  answered = false;
}

function pickAnswer(i) {
  if (answered) return;
  answered = true;
  const qs  = QUESTIONS[curTopic.id];
  const cur = qs[qIdx];
  const ok  = i === cur.ans;
  if (ok) score++;
  document.getElementById('score-display').textContent = score;
  gameLog.push({ ok, type: cur.type });

  // Style buttons
  document.querySelectorAll('.choice-btn').forEach((btn, bi) => {
    btn.disabled = true;
    const letter = btn.querySelector('.choice-letter');
    if (bi === cur.ans) {
      btn.classList.add('correct');
      letter.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#22C55E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>`;
      letter.style.background = '#22C55E'; letter.style.color = 'white';
    } else if (bi === i && !ok) {
      btn.classList.add('wrong');
      letter.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="3" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>`;
      letter.style.background = '#EF4444'; letter.style.color = 'white';
    }
  });

  // Show scramble answer
  const sa = document.getElementById('scramble-ans');
  if (sa) sa.style.display = 'block';

  // Feedback
  const fb = document.getElementById('feedback');
  fb.style.display = 'block';
  let html = ok
    ? `<div class="result-line ok"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>Excellent! That is correct!</div>`
    : `<div class="result-line wrong"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>Correct answer: <strong style="margin-left:4px">${cur.choices[cur.ans]}</strong></div>`;

  if (cur.fact) {
    html += `<div class="fact-box">
      <div class="fact-inner">
        <div class="fact-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></div>
        <div><div class="fact-label">Did You Know?</div><div class="fact-text">${cur.fact}</div></div>
      </div>
    </div>`;
  }

  const isLast = qIdx + 1 >= QUESTIONS[curTopic.id].length;
  html += `<button class="next-btn" onclick="${isLast ? 'showResult()' : 'nextQ()'}"
    style="background:${curTopic.color};box-shadow:0 4px 18px ${curTopic.color}50">
    ${isLast ? 'See My Results' : 'Next Question'}
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  </button>`;

  fb.innerHTML = html;
  renderDots();
}

function nextQ() {
  qIdx++;
  renderQuestion();
}

function renderDots() {
  const qs = QUESTIONS[curTopic.id];
  const row = document.getElementById('dot-row');
  row.innerHTML = qs.map((_, i) => {
    let bg, width;
    if (i < gameLog.length)    { bg = gameLog[i].ok ? '#22C55E' : '#EF4444'; width = '8px'; }
    else if (i === qIdx)       { bg = curTopic.color; width = '22px'; }
    else                       { bg = '#DDD'; width = '8px'; }
    return `<div class="dot" style="width:${width};background:${bg}"></div>`;
  }).join('');
}

// ─── RESULT ───────────────────────────────────────────────────────────────────
function showResult() {
  const qs    = QUESTIONS[curTopic.id];
  const total = qs.length;
  const pct   = score / total;

  // Badge
  const circle = document.getElementById('badge-circle');
  const lbl    = document.getElementById('badge-label');
  if (pct >= 0.85) {
    circle.style.background = 'linear-gradient(135deg,#FFD700,#FF8C00)';
    circle.style.boxShadow  = '0 6px 24px rgba(255,195,0,0.5)';
    lbl.textContent = 'Gold Star Explorer!';
  } else if (pct >= 0.65) {
    circle.style.background = 'linear-gradient(135deg,#C0C0C0,#707070)';
    circle.style.boxShadow  = '0 6px 24px rgba(130,130,130,0.4)';
    lbl.textContent = 'Silver Explorer!';
  } else {
    circle.style.background = 'linear-gradient(135deg,#CD7F32,#8B4513)';
    circle.style.boxShadow  = '0 6px 24px rgba(150,80,20,0.35)';
    lbl.textContent = 'Bronze Explorer!';
  }

  // Result card border
  document.getElementById('result-card').style.borderColor = curTopic.color + '33';
  document.getElementById('result-topic-label').textContent = curTopic.title + ' — Quiz Complete';

  // Score
  document.getElementById('score-big').innerHTML =
    `<span style="color:${curTopic.color}">${score}</span><span class="score-total">/${total}</span>`;
  setTimeout(() => {
    document.getElementById('score-bar').style.cssText =
      `width:${pct*100}%;background:linear-gradient(90deg,${curTopic.color},${curTopic.color}80)`;
  }, 100);

  const msg = score===total ? 'Perfect! You are a true Science Explorer!'
    : pct>=0.8 ? 'Brilliant! Almost perfect!'
    : pct>=0.6 ? 'Great effort! Keep learning!'
    : 'Good try — review and try again!';
  document.getElementById('score-msg').textContent = msg;

  // Breakdown
  const byType = {};
  gameLog.forEach(h => {
    if (!byType[h.type]) byType[h.type] = { total:0, correct:0 };
    byType[h.type].total++;
    if (h.ok) byType[h.type].correct++;
  });
  let breakHtml = '<div class="breakdown-title">By Question Type</div>';
  Object.entries(byType).forEach(([tp, d]) => {
    const tc2 = TYPE_CFG[tp] || TYPE_CFG.mcq;
    const p   = d.correct / d.total;
    const barColor = p>0.7?'#22C55E':p>0.4?'#F59E0B':'#EF4444';
    breakHtml += `<div class="breakdown-row">
      <span class="breakdown-label" style="background:${tc2.bg};color:${tc2.color};border-color:${tc2.border}">${tc2.label.split(' ')[0]}</span>
      <div class="breakdown-bar-wrap"><div class="breakdown-bar" style="width:${p*100}%;background:${barColor}"></div></div>
      <span class="breakdown-score">${d.correct}/${d.total}</span>
    </div>`;
  });
  document.getElementById('breakdown').innerHTML = breakHtml;

  // Retry button
  const retry = document.getElementById('btn-retry');
  retry.textContent = 'Try Again';
  retry.style.cssText = `flex:1;padding:13px;border-radius:12px;font-weight:800;font-size:13px;text-align:center;background:${curTopic.bg};color:${curTopic.color};border:2px solid ${curTopic.color}38`;

  // Home button
  const homeBtn = document.querySelector('.btn-home');
  homeBtn.style.cssText = `flex:1;padding:13px;border-radius:12px;font-weight:800;font-size:13px;text-align:center;background:${curTopic.color};color:white;box-shadow:0 4px 16px ${curTopic.color}48`;

  showScreen('result');
}

function retryQuiz() { startQuiz(curTopic); }
</script>
</body>
</html>
"""

# ─── Render the game ──────────────────────────────────────────────────────────
components.html(GAME_HTML, height=900, scrolling=True)
