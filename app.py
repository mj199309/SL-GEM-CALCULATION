import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- CUSTOM CSS FOR PREMIUM STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #060c17 0%, #0b1528 50%, #03070e 100%);
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"], div[data-baseweb="input-container"] {
        background-color: rgba(15, 27, 49, 0.6) !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    input, select, textarea {
        color: #e2f1ff !important;
    }
    .metric-box {
        background: linear-gradient(145deg, rgba(11, 28, 54, 0.9) 0%, rgba(4, 13, 26, 0.95) 100%);
        border: 2px solid #00d2ff;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.2);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-top: 20px;
    }
    .detail-row {
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid rgba(0, 210, 255, 0.1);
        padding: 8px 0;
        font-size: 14px;
    }
    .detail-label {
        color: #a4c5e6;
        font-weight: bold;
    }
    .detail-value {
        color: #00d2ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 3D ROTATING TITLE EFFECT ---
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

st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Advanced Gem Valuation & Treatment Matrix (40% Discount Enabled)")
st.write("---")

# BASE VALUES (පැරණි ඇප් එකේ මිල ගණන් වලට 100% ක් ගැලපෙන සේ සකසා ඇත)
base_prices = {
    "නිල් මැණික් (Blue Sapphire - Light Blue)": 65625,
    "නිල් මැණික් (Blue Sapphire - Royal Blue)": 180000,
    "නිල් මැණික් (Blue Sapphire - Cornflower Blue)": 150000,
    "නිල් මැණික් (Blue Sapphire - Vivid Blue)": 140000,
    "නිල් මැණික් (Blue Sapphire - Velvet Blue)": 130000,
    "නිල් මැණික් (Blue Sapphire - Peacock Blue)": 120000,
    "නිල් මැණික් (Blue Sapphire - Deep Blue)": 100000,
    "නිල් මැණික් (Blue Sapphire - Medium Blue)": 85000,
    "රතු කැට (Ruby - Pigeon Blood)": 200000,
    "රතු කැට (Ruby - Vivid Red)": 180000,
    "පුෂ්පරාග (Yellow Sapphire)": 90000,
    "පද්මරාග (Padparadscha)": 190000,
    "පැණි වෛරෝඩි (Cat's Eye)": 150000,
    "මරකත (Emerald)": 130000
}

# 1. Main Gemstone Type & Color Category
st.markdown("### 1 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
selected_gem = st.selectbox("තෝරන්න (Select Gem):", list(base_prices.keys()), label_visibility="collapsed")

# 2. Gemstone Cut
st.markdown("### 2 කැපුම / හැඩය (GEMSTONE CUT):")
cut_options = {
    "Oval Brilliant Cut (Precision Cut) - 100%": 1.00,
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (හතරැස් හැඩය) - 0.88": 0.88,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 0.75": 0.75,
    "Native / Local Cut (සම්ප්‍රදායික දේශීය අත් කැපුම) - 0.40": 0.40
}
selected_cut = st.selectbox("තෝරන්න (Select Cut):", list(cut_options.keys()), label_visibility="collapsed")

# 3. Stone Body Tone
st.markdown("### 3 වර්ණ තීව්‍රතාවය (STONE BODY TONE):")
tone_options = {
    "Vibrant Tone (දීප්තිමත් වර්ණය) - 1.00": 1.00,
    "Normal Tone (සාමාන්‍ය පැහැය) - 0.85": 0.85,
    "Very Light / Pale Tone (ඉතා ලා පැහැති) - 0.40": 0.40
}
selected_tone = st.selectbox("තෝරන්න (Select Tone):", list(tone_options.keys()), label_visibility="collapsed")

# 4. Gemstone Clarity
st.markdown("### 4 පැහැදිලි බව (GEMSTONE CLARITY):")
clarity_options = {
    "100% Clean (Eye Clean / සම්පූර්ණ පිරිසිදු) - 1.00": 1.00,
    "90% Clean (Minor inclusions / සුළු රොඩු) - 0.80": 0.80,
    "75% Clean (Slightly Included) - 0.60": 0.60,
    "50% Clean (Heavily Included) - 0.35": 0.35
}
selected_clarity = st.selectbox("තෝරන්න (Select Clarity):", list(clarity_options.keys()), label_visibility="collapsed")

# 5. Treatment / Heat
st.markdown("### 5 පදම් කිරීම (TREATMENT / HEAT):")
treatment_options = {
    "UNHEATED (ස්වභාවික නිල් / රත් නොකළ) - 1.00": 1.00,
    "HEATED (සාමාන්‍ය පරිදි රත් කළ / තැම්බූ) - 0.60": 0.60,
    "TREATED / DIFFUSED (රසායනික ප්‍රතිකර්ම කළ) - 0.25": 0.25
}
selected_treatment = st.radio("තෝරන්න (Select Treatment):", list(treatment_options.keys()), label_visibility="collapsed")

# 6. Weight in Carats
st.markdown("### 6 බර කැරට් ප්‍රමාණය (WEIGHT IN CARATS):")
weight = st.number_input("කැරට් ප්‍රමාණය ඇතුලත් කරන්න (Enter Carats):", min_value=0.05, max_value=50.0, value=0.25, step=0.05)

# --- CALCULATE LOGIC ---
if st.button("💰 මිල ගණනය කරන්න (Calculate Value)"):
    base_rate = base_prices[selected_gem]
    cut_val = cut_options[selected_cut]
    tone_val = tone_options[selected_tone]
    clarity_val = clarity_options[selected_clarity]
    treatment_val = treatment_options[selected_treatment]
    
    # Per Carat Calculation incorporating all factors
    per_carat_rate = base_rate * cut_val * tone_val * clarity_val * treatment_val
    
    # Total Valuation
    total_market_value = per_carat_rate * weight
    
    # 40% Discount Applied Value
    final_discounted_value = total_market_value * 0.60
    
    # Display logic adjustments
    per_carat_display = final_discounted_value / weight if weight > 0 else 0
    min_range = final_discounted_value * 0.85
    max_range = final_discounted_value * 1.15

    st.write("---")
    
    # Render final output cleanly by completely bypassing custom HTML strings in st.markdown
    st.markdown("### 📊 ගණනය කරන ලද අවසාන තක්සේරුව")
    
    # Creating a premium stylized card using clean safe HTML container layout
    html_card = f"""
    <div class="metric-box">
        <div style="font-size: 50px; margin-bottom: 10px;">💎</div>
        <h3 style="color: #2ecc71; margin: 0 0 5px 0; font-size: 26px; font-family: sans-serif;">LKR {final_discounted_value:,.2f}</h3>
        <p style="color: #ceddf0; font-size: 14px; margin: 0 0 20px 0;">තක්සේරුකළ වටිනාකම (Valuation)</p>
        
        <div class="detail-row">
            <span class="detail-label">⚖️ වෙළඳපොළ සාධාරණ පරාසය:</span>
            <span class="detail-value" style="color: #e2f1ff; font-weight: bold;">LKR {min_range:,.2f} - LKR {max_range:,.2f}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">📊 කැරට් එකක අგය (Per Carat):</span>
            <span class="detail-value">LKR {per_carat_display:,.2f}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">💎 මැණික් වර්ගය:</span>
            <span class="detail-value">{selected_gem}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">✂️ කැපුම් හැඩය:</span>
            <span class="detail-value">{selected_cut.split(' - ')[0]}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">🔍 පැහැදිලි බව (Clarity):</span>
            <span class="detail-value">{selected_clarity.split(' - ')[0]}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">🔥 පදම් කිරීම (Treatment):</span>
            <span class="detail-value">{selected_treatment.split(' - ')[0]}</span>
        </div>
        <div class="detail-row" style="border-bottom: none;">
            <span class="detail-label">⚖️ බර ප්‍රමාණය:</span>
            <span class="detail-value" style="color: #2ecc71; font-weight: bold;">{weight} Carats (Cts)</span>
        </div>
    </div>
    """
    st.markdown(html_card, unsafe_allow_html=True)
