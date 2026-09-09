import streamlit as st
import time

# 1. Page Configuration (Desktop & Mobile Scaling)
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- 2. LUXURY GEMSTONES ROTATING LOADER ANIMATION (5 SECONDS) ---
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    st.markdown(
        """
        <div id="loading-screen">
          <div class="gem-ring">
            <div class="gem-particle" style="top: 0px; left: 42px; background: #00d2ff;"></div>
            <div class="gem-particle" style="top: 12px; left: 72px; background: #ff5252;"></div>
            <div class="gem-particle" style="top: 42px; left: 84px; background: #ffeb3b;"></div>
            <div class="gem-particle" style="top: 72px; left: 72px; background: #e040fb;"></div>
            <div class="gem-particle" style="top: 84px; left: 42px; background: #00e676;"></div>
            <div class="gem-particle" style="top: 72px; left: 12px; background: #ff9100;"></div>
            <div class="gem-particle" style="top: 42px; left: 0px; background: #00b0ff;"></div>
            <div class="gem-particle" style="top: 12px; left: 12px; background: #ff4081;"></div>
          </div>
          <div class="loading-text">Loading Portal...</div>
        </div>
        <style>
          #loading-screen { position: fixed; top: 0px; left: 0px; width: 100vw; height: 100vh; background: linear-gradient(135deg, #060c17, #03070e); display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 99999; }
          .gem-ring { position: relative; width: 100px; height: 100px; animation: spinRing 2.5s linear infinite; transform-style: preserve-3d; perspective: 500px; }
          .gem-particle { position: absolute; width: 16px; height: 16px; border-radius: 50%; box-shadow: 0 0 15px rgba(0,210,255,0.6); }
          @keyframes spinRing { 0% { transform: rotate(0deg) rotateX(20deg); } 100% { transform: rotate(360deg) rotateX(20deg); } }
          .loading-text { margin-top: 25px; font-family: sans-serif; font-size: 20px; font-weight: 500; color: #e2f1ff; letter-spacing: 3px; text-transform: uppercase; }
        </style>
        """,
        unsafe_allow_html=True
    )
    time.sleep(5.0)
    st.session_state.loaded = True
    st.rerun()

# --- 3. CUSTOM CSS FOR LUXURY DARK THEME BACKGROUND ---
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(135deg, #060c17, #0b1528, #03070e); }
    h1, h2, h3, p, span, label, .stMarkdown { color: #e2f1ff !important; }
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"] { background-color: rgba(15, 27, 49, 0.8) !important; border: 1px solid rgba(0, 210, 255, 0.3) !important; border-radius: 8px !important; }
    div[data-baseweb="select"] span { white-space: normal !important; word-break: break-word !important; }
    .metric-box { background-color: rgba(0, 210, 255, 0.05); border: 1px solid rgba(0, 210, 255, 0.3); padding: 20px; border-radius: 12px; text-align: center; margin-top: 10px; }
    .rotating-title { font-size: 42px; font-weight: bold; color: #00d2ff; text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="rotating-title">💎 MJ GEMS 💎</div>', unsafe_allow_html=True)
st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Adjusted Market Rates & Gem Knowledge Framework")
st.write("---")

# 1. Main Category Select
categories = [
    "CORUNDUM (කුරුන්දු / කොරන්ඩම්)", "CHRYSOBERYL (කනක / වෛරෝඩි)", "ZIRCON (ජාගුන් තෝර)", 
    "SPINEL (කිරිංචි)", "GARNET (රබහ / ගෝමේද)", "TOURMALINE (තෝරමල්ලි)", 
    "BERYL (බෙරිල් / පඩියන්)", "TOPAZ (තෝපස්)", "QUARTZ (පළිඟු)", 
    "FELDSPAR & OTHER GEMS (පුෂ්පකාන්ත සහ අනෙකුත්)"
]
st.markdown("### 1 මැණික් කාණ්ඩය (GEMSTONE CATEGORY):")
selected_cat = st.selectbox("කාණ්ඩය තෝරන්න:", categories, label_visibility="collapsed")

# 100% BALANCED GOOGLE MARKET RATES FOR LKR MATRIX (1 USD = 300 LKR Conversion Benchmark)
gem_registry = {
    "CORUNDUM (කුරුන්දු / කොරන්ඩම්)": {
        "නිල් මැණික් (Blue Sapphire - Royal Blue)": (240000, 390000), 
        "නිල් මැණික් (Blue Sapphire - Cornflower)": (180000, 280000),
        "නිල් මැණික් (Blue Sapphire - Vivid Blue)": (210000, 320000), 
        "නිල් මැණික් (Blue Sapphire - Pastel Blue)": (60000, 110000),
        "පුෂ්පරාග (Yellow Sapphire - Golden Yellow)": (120000, 220000),
        "පුෂ්පරාග (Yellow Sapphire - Vivid Yellow)": (90000, 180000), 
        "පද්මරාග (Padparadscha - Lotus Pink)": (280000, 480000), 
        "රතු කැට (Ruby - Pigeon Blood Red)": (350000, 600000), 
        "රෝස සෆයාර් (Pink Sapphire)": (90000, 160000), 
        "සුදු සෆයාර් (White Sapphire)": (30000, 60000),
        "ආරුල් නිල් මැණික් (Star Sapphire)": (90000, 180000), 
        "ගෙවුඩ (Geuda)": (15000, 35000)
    },
    "CHRYSOBERYL (කනක / වෛරෝඩි)": {
        "පැණි වෛරෝඩි (Cat's Eye)": (220000, 380000), 
        "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite)": (300000, 550000), 
        "කහ කනක (Yellow Chrysoberyl)": (35000, 75000),
        "කොළ කනක (Green Chrysoberyl)": (40000, 85000)
    },
    "ZIRCON (ජාගුන් තෝර)": {
        "නිල් ජාගුන් (Blue Zircon)": (4500, 8500), 
        "පච්ච තෝර (Green Zircon)": (4000, 7500),
        "සුදු ජාගුන් (Colourless Zircon)": (3500, 6500)
    },
    "SPINEL (කිරිංචි)": {
        "රතු කිරිංචි (Red Spinel)": (45000, 95000), 
        "නිල් කිරිංචි (Blue Spinel)": (35000, 75000), 
        "දම් කිරිංචි (Purple Spinel)": (25000, 50000)
    },
    "GARNET (රබහ / ගෝමේද)": {
        "ගෝමේද (Hessonite Garnet)": (3500, 6500), 
        "රතු රබහ (Almandine)": (3000, 5500), 
        "වර්ණ මාරු ගානට් (Colour-change)": (8500, 18000)
    },
    "TOURMALINE (තෝරමල්ලි)": {
        "පච්ච තෝරමල්ලි (Green Tourmaline)": (6500, 14000), 
        "රෝස තෝරමල්ලි (Pink Tourmaline)": (8500, 18000), 
        "රූබිලයිට් (Rubellite)": (12000, 25000)
    },
    "BERYL (බෙරිල් / පඩියන්)": {
        "පච්ච පඩියන් (Aquamarine)": (12000, 25000), 
        "මරකත (Emerald)": (95000, 185000), 
        "රෝස බෙරිල් (Morganite)": (10000, 22000)
    },
    "TOPAZ (තෝපස්)": {
        "නිල් තෝපස් (Blue Topaz)": (4000, 8500), 
        "කහ තෝපස් (Yellow Topaz)": (4500, 9000),
        "ඉම්පීරියල් තෝපස් (Imperial Topaz)": (35000, 75000)
    },
    "QUARTZ (පළිඟු)": {
        "දම් පළිඟු (Amethyst)": (2500, 5500), 
        "කහ පළිඟු (Citrine)": (2000, 4500), 
        "පුෂ්පකාන්ත (Moonstone)": (2500, 5500)
    },
    "FELDSPAR & OTHER GEMS (පුෂ්පකාන්ත සහ අනෙකුත්)": {
        "පෙරිඩොට් (Peridot)": (5500, 12000), 
        "දියමන්ති / වජ්‍ර (Diamond)": (750000, 1450000), 
        "මුතු (Pearl)": (25000, 65000)
    }
}

st.markdown("### 2 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
available_gems = gem_registry.get(selected_cat, {})
selected_gem = st.selectbox("වර්ගය තෝරන්න:", list(available_gems.keys()), label_visibility="collapsed")

cut_options = {
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00, "Princess Cut (ප්‍රින්සස්) - 88%": 0.88,
    "Marquise Cut (මාර්කිස්) - 82%": 0.82, "Oval Cut (ඕවල් / බිත්තර හැඩය) - 75%": 0.75,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 70%": 0.70, "Pear Cut (පෙයාර් / කඳුළු හැඩය) - 68%": 0.68,
    "Emerald Cut (එමරල්ඩ්) - 62%": 0.62, "Native / Local Cut (දේශීය අත් කැපුම) - 40%": 0.40
}
st.markdown("### 3 කැපුම / හැඩය (GEMSTONE CUT):")
selected_cut = st.selectbox("කැපුම තෝරන්න:", list(cut_options.keys()), label_visibility="collapsed")

tone_options = { "Vibrant Body (දීප්තිමත් වර්ණය)": 1.10, "Normal Body (සාමාන්ය පැහැය)": 1.00, "Dark Body (අඳුරු පැහැය)": 0.65 }
st.markdown("### 4 වර්ණ තීව්රතාවය (STONE BODY TONE):")
selected_tone = st.selectbox("පැහැය තෝරන්න:", list(tone_options.keys()), label_visibility="collapsed")

clarity_options = {
    "Loop Clean Quality (උපරිම පිරිසිදු)": 1.00, "Eye Clean Quality (ඇසට පිරිසිදු)": 0.90,
    "Slight Inclusions (සුළු රොඩු සහිත)": 0.70, "Medium Inclusions (මධ්‍යස්ථ රොඩු සහිත)": 0.50,
    "High Inclusions / Lowest Grade (වැඩි රොඩු සහිත)": 0.20
}
st.markdown("### 5 පිරිසිදුතාව (STONE CLARITY):")
selected_clarity = st.selectbox("පිරිසිදුතාව තෝරන්න:", list(clarity_options.keys()), label_visibility="collapsed")

st.markdown("### 6 තත්ත්වය (TREATMENT / HEAT):")
treatment = st.radio("තත්ත්වය:", ["HEATED (පෝරණුව)", "UNHEATED (ස්වභාවික)"], index=0, label_visibility="collapsed")

st.markdown("### 7 කැරට් බර (CARAT WEIGHT):")
carat_weight = st.number_input("Carat Weight", min_value=0.01, value=1.00, step=0.01, label_visibility="collapsed")

st.write("")
calculate_btn = st.button("OK / මිල ගණනය කරන්න", use_container_width=True)
st.write("---")
st.markdown("### Estimated Reference Value")

if calculate_btn:
    is_unheated = "UNHEATED" in treatment
    rates = available_gems.get(selected_gem, (100000, 200000))
    
    # Selection base rate extraction mapping (Heated index vs Unheated index)
    base_rate = rates[1] if is_unheated else rates[0]
    discounted_base_factor = 1.00
    
    final_calculated_price = base_rate * discounted_base_factor * cut_options[selected_cut] * tone_options[selected_tone] * clarity_options[selected_clarity] * carat_weight
    st.markdown(f'<div class="metric-box"><span style="font-size: 16px; color: #a4c5e6; display: block;">ගණනය කරන ලද තක්සේරු මිල (LKR)</span><span style="font-size: 36px; font-weight: bold; color: #00ffcc;">Rs. {final_calculated_price:,.2f}</span></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="metric-box"><span style="font-size: 28px; font-weight: bold; color: #7f9bb3;">Rs. 0.00</span></div>', unsafe_allow_html=True)
