import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

# --- 1. PAGE CONFIG & SESSION STATE ---
st.set_page_config(page_title="FactCheck AI 2026", page_icon="🛡️", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

# --- 2. THEME & STYLING ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #3b82f6; color: white; height: 3em; font-weight: bold; }
    .report-box { padding: 20px; border-radius: 15px; border: 1px solid #3b82f6; background-color: #1e293b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SYSTEM INITIALIZATION ---
try:
    # Pulling from .streamlit/secrets.toml
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
    
    search_tool = TavilySearchResults(k=5)
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    
    st.sidebar.success("✅ API Keys Loaded Successfully")
except Exception as e:
    st.error(f"❌ Initialization Error: {e}")
    st.info("Ensure .streamlit/secrets.toml exists with GOOGLE_API_KEY and TAVILY_API_KEY")
    st.stop()

# --- 4. SIDEBAR (HISTORY) ---
with st.sidebar:
    st.title("🛡️ System Info")
    st.success("Brain: Gemini 2.5 Online")
    st.info("Status: Live (March 2, 2026)")
    st.divider()
    
    st.header("📜 Search History")
    if st.session_state.history:
        for idx, item in enumerate(reversed(st.session_state.history)):
            if st.button(f"📄 {item['query'][:25]}...", key=f"hist_{idx}"):
                st.session_state.current_view = item['report']
        if st.sidebar.button("🗑️ Clear History"):
            st.session_state.history = []
            if "current_view" in st.session_state: del st.session_state.current_view
            st.rerun()
    else:
        st.write("No recent searches.")

# --- 5. MAIN UI & LOGIC ---
st.title("🛡️ FactCheck AI: 2026 Intelligence Portal")
st.write("Enter any claim to verify it against real-time 2026 global data.")

user_input = st.text_input("📝 News Headline:", placeholder="e.g., CBSE board exam cancellation circular in Middle East")

if st.button("🚀 Verify & Generate Report"):
    if user_input:
        with st.status("🔍 Researching live sources...", expanded=True) as status:
            try:
                # Get Search Data
                raw_data = search_tool.run(user_input)
                
                # Strict Prompt to ensure URLs are returned
                prompt = f"""
                You are a professional Fact-Checker. Use the following SEARCH DATA to verify the USER INPUT.
                
                USER INPUT: {user_input}
                SEARCH DATA: {raw_data}
                
                FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:
                
                # 🛡️ NEWS VERIFICATION DASHBOARD
                ---
                **USER CLAIM:** {user_input}
                **AI VERDICT:** [🔴 FAKE | 🟡 PARTIALLY REAL | 🟢 REAL]
                
                ### 📝 ACTUAL NEWS (THE TRUTH)
                (Provide a clear, 2-3 sentence summary of the verified facts.)
                
                ### 🔗 VERIFIED SOURCES
                (You MUST list the URLs from the SEARCH DATA here as clickable markdown links.)
                (Example: [Source Title](URL))
                
                ---
                *Status: Verified Live March 2, 2026*
                """
                
                report = llm.invoke(prompt).content
                
                # Update Session History
                st.session_state.history.append({"query": user_input, "report": report})
                st.session_state.current_view = report
                status.update(label="Research Complete!", state="complete")
            
            except Exception as e:
                st.error(f"Research Failed: {e}")
                status.update(label="Research Failed", state="error")
    else:
        st.warning("Please enter a headline.")

# --- 6. DISPLAY RESULTS ---
if "current_view" in st.session_state:
    st.divider()
    st.markdown(st.session_state.current_view)
    
    # Simple Download Button
    st.download_button(
        label="📂 Download This Report",
        data=st.session_state.current_view,
        file_name="fact_check_report.md",
        mime="text/markdown"
    )