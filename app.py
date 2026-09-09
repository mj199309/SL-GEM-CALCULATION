import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- CUSTOM CSS FOR LUXURY BACKGROUND & PREMIUM STYLING ---
st.markdown(
    """
    <style>
    /* Premium Deep Sapphire Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #060c17 0%, #0b1528 50%, #03070e 100%);
    }
    
    /* Clean text styling over dark theme */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    
    /* Subtle neon border around input fields to lock premium look */
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"], div[data-baseweb="input-container"] {
        background-color: rgba(15, 27, 49, 0.6) !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Input element text color adjustment */
    input, select, textarea {
        color: #e2f1ff !important;
    }
    
    /* Metrics panel decoration */
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 25px;
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
st.caption("Adjusted Market Rates & Advanced Color Categories (40% Discount Enabled)")
st.write("---")

# DATA CONFIGURATION WITH SUB-CATEGORIES
gem_data = {
    "නිල් මැණික් (Blue Sapphire)": {
        "Royal Blue (රාජකීය තද නිල්)": (475000, 1150000),
        "Cornflower Blue (නිල් මානෙල් පැහැය)": (450000, 1000000),
        "Vivid Blue (දීප්තිමත් තද නිල්)": (420000, 950000),
        "Velvet Blue (වෙල්වට් නිල්)": (380000, 850000),
        "Peacock Blue (මොනර නිල්)": (350000, 750000),
        "Deep Blue (තද නිල් පැහැය)": (300000, 650000),
        "Medium Blue (සාමාන්‍ය නිල්)": (250000, 550000),
        "Light Blue (ලා නිල් පැහැය)": (120000, 300000)
    },
    "රතු කැට (Ruby)": {
        "Pigeon Blood Ruby (පරෙවි ලේ රතු)": (900000, 1850000),
        "Vivid Red Ruby (දීප්තිමත් රතු)": (800000, 1600000),
        "Deep Red Ruby (තද රතු කැට)": (650000, 1300000),
        "Light Pinkish Red (ලා රෝස රතු)": (350000, 800000)
    },
    "පුෂ්පරාග (Yellow Sapphire)": {
        "Mekong Whisky Yellow (විස්කි කහ)": (250000, 600000),
        "Vivid Canary Yellow (කැනරි කහ)": (200000, 500000),
        "Golden Yellow (රන්වන් කහ)": (180000, 450000),
        "Light Yellow (ලා කහ පැහැය)": (90000, 250000)
    },
    "පද්මරාග (Padparadscha)": {
        "Sunset Padparadscha (තැඹිලි-රෝස මිශ්‍ර)": (525000, 1500000),
        "Sunrise Padparadscha (රෝස-තැඹිලි මිශ්‍ර)": (500000, 1300000)
    },
    "රෝස සෆයාර් (Pink Sapphire)": {
        "Hot Pink (තද රෝස)": (180000, 420000),
        "Medium Pink (සාමාන්‍ය රෝස)": (140000, 320000),
        "Pastel/Light Pink (ලා රෝස)": (70000, 180000)
    },
    "පැණි වෛරෝඩි (Cat's Eye - Chrysoberyl)": {
        "Honey Colour (පැණි වර්ණය - Premium)": (550000, 1300000),
        "Apple Green (ඇපල් කොළ වෛරෝඩි)": (450000, 1000000),
        "Yellowish Green (කහ-කොළ වෛරෝඩි)": (350000, 800000)
    },
    "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite)": {
        "Strong Color Change (පැහැදිලි වර්ණ මාරුව)": (850000, 1950000),
        "Medium Color Change (සාමාන්‍ය වර්ණ මාරුව)": (600000, 1400000)
    },
    "මරකත (Emerald)": {
        "Vivid Green (දීප්තිමත් පච්ච)": (400000, 950000),
        "Deep Green (තද පච්ච බෙරිල්)": (350000, 800000),
        "Light Green (ලා කොළ පැහැය)": (150000, 400000)
    },
    "වෙනත් මැණික් වර්ග (Other Gemstones)": {
        "සුදු සෆයාර් (White Sapphire)": (65000, 150000),
        "කොළ සෆයාර් (Green Sapphire)": (75000, 180000),
        "දියමන්ති / වජ්‍ර (Diamond)": (1500000, 3500000),
        "මුතු (Pearl)": (100000, 450000),
        "ගෝමේද (Hessonite Garnet)": (45000, 90000),
        "දම් පළිඟු (Amethyst)": (30000, 65000)
    }
}

# 1. Main Gemstone Category Selection
st.markdown("### 1 මැණික් කුලය / ප්‍රධාන වර්ගය (GEMSTONE TYPE):")
main_gem = st.selectbox("තෝරන්න (Select Gem):", list(gem_data.keys()), label_visibility="collapsed")

# 2. Dynamic Sub-Category Selection based on Main Selection
st.markdown("### 2 වර්ණ ප්‍රභේදය / උප-වර්ගය (COLOR CATEGORY):")
sub_categories = gem_data[main_gem]
selected_sub = st.selectbox("තෝරන්න (Select Color Category):", list(sub_categories.keys()), label_visibility="collapsed")

# 3. Gemstone Cut
st.markdown("### 3 කැපුම / හැඩය (GEMSTONE CUT):")
cut_options = {
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (ප්‍රින්සස් / හතරැස් හැඩය) - 88%": 0.88,
    "Marquise Cut (මාර්කිස් / ඔරු හැඩය) - 82%": 0.82,
    "Oval Cut (ඕවල් / ප්‍රමිතිගත බිත්තර හැඩය) - 75%": 0.75,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 70%": 0.70,
    "Pear Cut (පෙයාර් / කඳුළු බිංදු හැඩය) - 68%": 0.68,
    "Emerald Cut (එමරල්ඩ් / පියගැටපෙළ හැඩය) - 62%": 0.62,
    "Native / Local Cut (සම්ප්‍රදායික දේශීය අත් කැපුම) - 40%": 0.40
}
selected_cut = st.selectbox("තෝරන්න (Select Cut):", list(cut_options.keys()), label_visibility="collapsed")

# 4. Weight in Carats
st.markdown("### 4 බර කැරට් ප්‍රමාණය (WEIGHT IN CARATS):")
weight = st.number_input("කැරට් ප්‍රමාණය ඇතුලත් කරන්න (Enter Carats):", min_value=0.05, max_value=50.0, value=1.0, step=0.05)

# --- PRICE CALCULATION LOGIC WITH 40% DISCOUNT ---
if st.button("💰 මිල ගණනය කරන්න (Calculate Value)"):
    min_base, max_base = sub_categories[selected_sub]
    cut_multiplier = cut_options[selected_cut]
    
    # Calculate original market price boundaries
    orig_min_price = min_base * weight * cut_multiplier
    orig_max_price = max_base * weight * cut_multiplier
    
    # Apply 40% discount (Multiply by 0.60)
    final_min_price = orig_min_price * 0.60
    final_max_price = orig_max_price * 0.60
    
    st.write("---")
    st.markdown("### 📊 ගණනය කරන ලද තක්සේරු මිල (Estimated Valuation):")
    
    # Custom stylized container for final results
    st.markdown(
        f"""
        <div class="metric-box">
            <span style='color: #ff5252; font-size: 14px; font-weight: bold; border: 1px solid #ff5252; padding: 2px 8px; border-radius: 4px;'>🔥 SPECIAL 40% DISCOUNT APPLIED</span>
            <h2 style='color: #00d2ff; margin: 15px 0 5px 0;'>LKR {final_min_price:,.2f} - LKR {final_max_price:,.2f}</h2>
            <p style='color: #a4c5e6; font-size: 13px; margin: 5px 0 0 0;'>
                වර්ගය: <b>{main_gem}</b> ({selected_sub}) | බර: <b>{weight} Cts</b><br>
                මුල් වෙළඳපොළ මිල: <del style='color: #ff8a8a;'>LKR {orig_min_price:,.0f} - LKR {orig_max_price:,.0f}</del>
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
