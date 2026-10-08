import time
import streamlit as st

from llm import ask_llm, DETAIL_LEVELS
from prompt_templates import TECHNIQUES, build_prompt


st.set_page_config(
    page_title="PromptLab AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

TECHNIQUE_COLORS = {
    "Zero-Shot": "#2563EB",
    "One-Shot": "#7C3AED",
    "Few-Shot": "#059669",
    "Chain of Thought (CoT)": "#D97706",
    "Tree of Thought (ToT)": "#DB2777",
}


st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: #F8FAFC;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] > div {
        background: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }

    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #0F172A !important;
    }

    section[data-testid="stSidebar"] label {
        color: #334155 !important;
    }

    section[data-testid="stSidebar"] .stCaption {
        color: #64748B !important;
    }

    /* MAIN TITLE */

    .main-title {
        font-size: 28px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 5px;
    }

    .main-subtitle {
        color: #64748B;
        font-size: 14px;
        margin-bottom: 25px;
    }

    /* SECTION */

    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #0F172A;
        margin-top: 10px;
        margin-bottom: 8px;
    }

    .section-description {
        color: #64748B;
        font-size: 13px;
        margin-bottom: 15px;
    }

    /* STAT CARDS */

    .stat-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
    }

    .stat-number {
        font-size: 25px;
        font-weight: 800;
        color: #2563EB;
    }

    .stat-label {
        font-size: 12px;
        color: #64748B;
        margin-top: 4px;
    }

    /* RESULT */

    .result-header {
        background: #0F172A;
        color: #FFFFFF !important;
        padding: 14px 16px;
        border-radius: 10px 10px 0 0;
        font-weight: 700;
        font-size: 15px;
    }

    .result-box {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-top: none;
        border-radius: 0 0 10px 10px;
        padding: 20px;
    }

    /* GENERATED PROMPT */

    .prompt-box {
        background: #F1F5F9;
        border: 1px solid #CBD5E1;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .prompt-title {
        font-size: 13px;
        font-weight: 700;
        color: #334155;
        margin-bottom: 8px;
    }

    /* FOOTER */

    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 12px;
        margin-top: 40px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:

    st.markdown(
        """
        <h2 style="
            margin-bottom:0;
            color:#0F172A !important;
        ">
            PromptLab
        </h2>

        <p style="
            font-size:12px;
            color:#64748B !important;
        ">
            Prompt Engineering Dashboard
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # MODEL SETTINGS

    st.markdown("### Model Settings")

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controls how creative or deterministic the model response is.",
    )

    detail = st.selectbox(
        "Response Detail",
        list(DETAIL_LEVELS.keys()),
        index=2,
    )

    show_prompt = st.checkbox(
        "Show generated prompt",
        value=False,
    )

    st.divider()

    # AVAILABLE STRATEGIES

    st.markdown("### Available Strategies")

    st.markdown(
        """
        **Zero-Shot** → Answer without examples.

        **One-Shot** → Answer using one example.

        **Few-Shot** → Answer using multiple examples.

        **Chain of Thought (CoT)** → Solve step by step.

        **Tree of Thought (ToT)** → Explore multiple approaches.
        """
    )
st.markdown(
    '<div class="main-title">Prompt Engineering Playground</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-subtitle">
        Test different prompting strategies and compare how they influence AI responses.
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# STAT CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">05</div>
            <div class="stat-label">Prompt Strategies</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">02</div>
            <div class="stat-label">Analysis Modes</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">01</div>
            <div class="stat-label">AI Workspace</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


with col4:

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-number">{temperature:.1f}</div>
            <div class="stat-label">Creativity Level</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("")

st.markdown(
    '<div class="section-title">Enter Your Task</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-description">
        Enter a question, problem, or instruction that you want the AI model to solve.
    </div>
    """,
    unsafe_allow_html=True,
)

task = st.text_area(
    "Task",
    height=150,
    placeholder="Example: Explain the difference between machine learning and deep learning.",
    label_visibility="collapsed",
)


st.markdown(
    '<div class="section-title">Choose Analysis Mode</div>',
    unsafe_allow_html=True,
)

mode = st.radio(
    "Analysis Mode",
    [
        "Single Strategy",
        "Compare Strategies",
    ],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown(
    '<div class="section-title">Choose Prompt Strategy</div>',
    unsafe_allow_html=True,
)

if mode == "Single Strategy":

    selected_technique = st.selectbox(
        "Prompt Strategy",
        list(TECHNIQUES.keys()),
    )

    selected_techniques = [
        selected_technique
    ]

else:

    selected_techniques = st.multiselect(
        "Prompt Strategies",
        list(TECHNIQUES.keys()),
        default=[
            "Zero-Shot",
            "Few-Shot",
            "Chain of Thought (CoT)",
        ],
    )
st.write("")

run_button = st.button(
    "Run Prompt Analysis",
    type="primary",
    use_container_width=True,
)

def render_response(technique):

    color = TECHNIQUE_COLORS.get(
        technique,
        "#2563EB",
    )

    generated_prompt = build_prompt(
        technique,
        task,
    )

    # SHOW GENERATED PROMPT

    if show_prompt:

        st.markdown(
            f"""
            <div class="prompt-box">

                <div class="prompt-title">
                    Generated Prompt — {technique}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.code(
            generated_prompt,
            language="text",
        )

    # GENERATE RESPONSE

    with st.spinner(
        f"Generating response using {technique}..."
    ):

        start_time = time.time()

        try:

            answer = ask_llm(
                generated_prompt,
                detail=detail,
                temperature=temperature,
            )

            elapsed = time.time() - start_time

        except Exception as e:

            st.error(
                f"Unable to generate the response: {e}"
            )

            return

    # RESULT HEADER

    st.markdown(
        f"""
        <div class="result-header"
             style="border-left:5px solid {color};">

            {technique}

        </div>
        """,
        unsafe_allow_html=True,
    )

    # RESULT BOX

    st.markdown(
        '<div class="result-box">',
        unsafe_allow_html=True,
    )

    st.markdown(answer)

    # RESPONSE METADATA

    st.markdown(
        f"""
        <div style="
            margin-top:15px;
            padding-top:10px;
            border-top:1px solid #E2E8F0;
            font-size:11px;
            color:#64748B;
        ">

            Strategy: {technique}
            &nbsp;&nbsp; | &nbsp;&nbsp;

            Response Detail: {detail}
            &nbsp;&nbsp; | &nbsp;&nbsp;

            Generation Time: {elapsed:.2f}s

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True,
    )


if run_button:

    if not task.strip():

        st.warning(
            "Please enter a task before running the analysis."
        )

    elif not selected_techniques:

        st.warning(
            "Please select at least one prompt strategy."
        )

    else:

        st.markdown(
            '<div class="section-title">AI Results</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="section-description">
                Results generated using the selected prompt engineering strategies.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # SINGLE STRATEGY

        if mode == "Single Strategy":

            render_response(
                selected_techniques[0]
            )

        # COMPARE STRATEGIES

        else:

            columns = st.columns(
                len(selected_techniques)
            )

            for column, technique in zip(
                columns,
                selected_techniques,
            ):

                with column:

                    render_response(
                        technique
                    )


st.markdown(
    """
    <div class="footer">
        PromptLab AI • Prompt Engineering Dashboard
    </div>
    """,
    unsafe_allow_html=True,
)