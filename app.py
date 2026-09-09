<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>MJ GEMS Admin Portal</title>
    <!-- stlite CSS -->
    <link rel="stylesheet" href="https://jsdelivr.net" />
    <style>
      /* --- PREMIUM FULL-SCREEN LOADING SCREEN (5 SECONDS) --- */
      #loading-screen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #060c17 0%, #03070e 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 99999;
      }

      /* 3D Rotating Gem Ring Spinner */
      .gem-ring {
        position: relative;
        width: 100px;
        height: 100px;
        animation: spinRing 2.5s linear infinite;
        transform-style: preserve-3d;
        perspective: 500px;
      }

      .gem-particle {
        position: absolute;
        width: 16px;
        height: 16px;
        background: #00ffcc;
        border-radius: 50%;
        box-shadow: 0 0 15px #00ffcc, 0 0 25px #00d2ff;
      }

      /* Placing gems in a perfect ring layout */
      .gem-particle:nth-child(1) { top: 0; left: 42px; background: #00d2ff; }
      .gem-particle:nth-child(2) { top: 12px; left: 72px; background: #ff5252; }
      .gem-particle:nth-child(3) { top: 42px; left: 84px; background: #ffeb3b; }
      .gem-particle:nth-child(4) { top: 72px; left: 72px; background: #e040fb; }
      .gem-particle:nth-child(5) { top: 84px; left: 42px; background: #00e676; }
      .gem-particle:nth-child(6) { top: 72px; left: 12px; background: #ff9100; }
      .gem-particle:nth-child(7) { top: 42px; left: 0; background: #00b0ff; }
      .gem-particle:nth-child(8) { top: 12px; left: 12px; background: #ff4081; }

      @keyframes spinRing {
        0% { transform: rotate(0deg) rotateX(20deg); }
        100% { transform: rotate(360deg) rotateX(20deg); }
      }

      /* Premium Text Glow for Loading Label */
      .loading-text {
        margin-top: 25px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 20px;
        font-weight: 500;
        color: #e2f1ff;
        letter-spacing: 3px;
        text-transform: uppercase;
        animation: pulseText 1.5s ease-in-out infinite;
      }

      @keyframes pulseText {
        0%, 100% { opacity: 0.5; text-shadow: 0 0 5px rgba(0,210,255,0.2); }
        50% { opacity: 1; text-shadow: 0 0 15px rgba(0,210,255,0.6); }
      }
    </style>
  </head>
  <body>
    <!-- Luxury Loader Interface -->
    <div id="loading-screen">
      <div class="gem-ring">
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
        <div class="gem-particle"></div>
      </div>
      <div class="loading-text">Loading...</div>
    </div>

    <div id="root"></div>

    <!-- Script to fade out loader after exactly 5 seconds -->
    <script>
      setTimeout(function() {
        var loader = document.getElementById('loading-screen');
        if (loader) {
          loader.style.transition = 'opacity 0.5s ease';
          loader.style.opacity = '0';
          setTimeout(function() { loader.style.display = 'none'; }, 500);
        }
      }, 5000);
    </script>

    <!-- stlite JS -->
    <script src="https://jsdelivr.net"></script>
    <script>
      stlite.mount({
        requirements: ["streamlit"],
        entrypoint: "app.py",
        files: {
          "app.py": `
import streamlit as st
import streamlit.components.v1 as components

# Page configuration for desktop and mobile scaling
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- CUSTOM CSS FOR LUXURY BACKGROUND & MOBILE STYLING (FIXED SYNTAX) ---
st.markdown(
    """
    <style>
    /* Fixed Python Decimal Literal Error by avoiding percentage symbols inside gradient */
    .stApp {
        background: linear-gradient(135deg, #060c17, #0b1528, #03070e);
    }
    
    /* Clean text styling over dark theme */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    
    /* Neon border applied to all viewports (Mobile Optimized) */
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"] {
        background-color: rgba(15, 27, 49, 0.8) !important;
        border: 1px solid rgba(0, 210, 255, 0.3) !important;
        border-radius: 8px !important;
    }
    
    /* Mobile select elements enhancement to prevent text overflow cutting */
    div[data-baseweb="select"] span {
        white-space: normal !important;
        word-break: break-word !important;
    }
    
    /* Premium metrics box decoration */
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 100% WORKING PURE HTML/CSS 3D ROTATING TITLE EFFECT ---
components.html(
    """
    <div style="display: flex; justify-content: center; align-items: center; background: transparent; height: 140px; overflow: hidden;">
        <div class="rotating-title">💎 MJ GEMS 💎</div>
        <style>
            .rotating-title {
                font-size: 42px;
                font-weight: bold;
                color: #00d2ff;
                font-family: 'Helvetica Neue', Arial, sans-serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                animation: rotateTitle 4s linear infinite;
                transform-style: preserve-3d;
                perspective: 1000px;
            }
            @keyframes rotateTitle {
                0% { transform: rotateY(0deg); text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc; }
                50% { transform: rotateY(180deg); text-shadow: 0 0 20px #00ffff, 0 0 30px #00d2ff; }
                100% { transform: rotateY(360deg); text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc; }
            }
        </style>
    </div>
    """,
    height=140,
)

# Subheader and Header
st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Adjusted Market Rates & Gem Cut Analytics")
st.write("---")

# --- GROUPING DATA INTO LOGICAL CATEGORIES TO FIX PHONE OVERFLOW ---
st.markdown("### 1 මැණික් කාණ්ඩය (GEMSTONE CATEGORY):")
categories = [
    "CORUNDUM (කුරුන්දු / සෆයාර්)",
    "CHRYSOBERYL (කනක / වෛරෝඩි)",
    "SPINEL (කිරිංචි / ස්පිනෙල්)",
    "GARNET (රබහ / ගෝමේද)",
    "TOURMALINE (තෝරමල්ලි)",
    "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)",
    "QUARTZ & FELDSPAR (පළිඟු / පුෂ්පකාන්ත)",
    "OTHER GEMS (දුර්ලභ සහ අනෙකුත් මැණික් වර්ග)"
]
selected_cat = st.selectbox("කාණ්ඩය තෝරන්න (Select Group):", categories, label_visibility="collapsed")

# Dynamic mapping arrays defined from Aruna Gems Chart
gem_registry = {
    "CORUNDUM (කුරුන්දු / සෆයාර්)": {
        "නිල් මැණික් (Blue Sapphire)": (475000, 1150000),
        "පුෂ්පරාග (Yellow Sapphire)": (250000, 600000),
        "රෝස සෆයාර් (Pink Sapphire)": (180000, 420000),
        "සුදු සෆයාර් (White Sapphire)": (65000, 150000),
        "කොළ සෆයාර් (Green Sapphire)": (75000, 180000),
        "පද්මරාග (Padparadscha)": (525000, 1500000),
        "රතු කැට (Ruby)": (900000, 1850000),
        "ආරුල් නිල් මැණික් (Star Sapphire)": (220000, 650000),
        "ආරුල් රතු කැට (Star Ruby)": (350000, 850000),
        "ගෙවුඩ (Geuda)": (50000, 120000),
        "ඔට්ටු මැණික් (Ottu Sapphire)": (120000, 300000)
    },
    "CHRYSOBERYL (kනක / වෛරෝඩි)": {
        "කහ කනක (Yellow Chrysoberyl)": (150000, 350000),
        "කොළ කනක (Green Chrysoberyl)": (160000, 380000),
        "පැණි වෛරෝඩි (Cat's Eye - Chrysoberyl)": (550000, 1300000),
        "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite)": (850000, 1950000),
        "ඇලෙක්සැන්ඩ්‍රයිට් වෛරෝඩි (Alexandrite Cat's Eye)": (950000, 2200000)
    },
    "SPINEL (කිරිංචි / ස්පිනෙල්)": {
        "රතු kිරිංචි (Red Spinel)": (360000, 360000),
        "රෝස kිරිංචි (Pink Spinel)": (150000, 150000),
        "නිල් kිරිංචි (Blue Spinel)": (180000, 180000),
        "දම් kිරිංචි (Purple Spinel)": (120000, 120000),
        "කළු kිරිංචි (Black Spinel)": (25000, 25000)
    },
    "GARNET (රබහ / ගෝමේද)": {
        "රතු රබහ (Almandine Garnet)": (35000, 75000),
        "ගෝමේද (Hessonite Garnet)": (45000, 90000),
        "රතු ගානට් (Pyrope Garnet)": (40000, 80000),
        "තැඹිලි ගානට් (Spessartine Garnet)": (60000, 130000),
        "වර්ණ මාරු ගානට් (Colour-change Garnet)": (95000, 210000),
        "ආරුල් ගානට් (Star Garnet)": (50000, 110000)
    },
    "TOURMALINE (තෝරමල්ලි)": {
        "පච්ච තෝරමල්ලි (Green Tourmaline)": (75000, 160000),
        "දුඹුරු තෝරමල්ලි (Brown Tourmaline)": (45000, 95000),
        "කළු තෝරමල්ලි (Black Tourmaline)": (15000, 35000),
        "රෝස තෝරමල්ලි (Pink Tourmaline)": (85000, 180000),
        "රූබිලයිට් (Rubellite)": (125000, 270000),
        "බහු වර්ණ තෝරමල්ලි (Multicoloured Tourmaline)": (90000, 195000)
    },
    "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)": {
        "පච්ච පඩියන් (Aquamarine)": (110000, 250000),
        "මරකත (Emerald)": (400000, 950000),
        "රන් පඩියන් (Golden Beryl)": (85000, 190000),
        "රෝස බෙරිල් (Morganite)": (95000, 210000),
        "සුදු බෙරිල් (Goshenite)": (35000, 75000),
        "සුදු තෝපස් (Colourless Topaz)": (20000, 45000),
        "කහ තෝපස් (Yellow Topaz)": (45000, 95000),
        "ඉම්පීරියල් තෝපස් (Imperial Topaz)": (180000, 400000),
        "නිල් තෝපස් (Blue Topaz)": (35000, 75000),
        "රෝස තෝපස් (Pink Topaz)": (75000, 160000)
    },
