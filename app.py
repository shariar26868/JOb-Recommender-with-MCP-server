###################################################
import streamlit as st
from src.helper import extract_text_from_pdf, ask_groq
from src.job_api import fetch_linkedin_jobs
from fpdf import FPDF
import os
import tempfile
import unidecode

st.set_page_config(page_title="Job Recommender", layout="wide")
st.title("📄 AI Job Recommender")
st.markdown("Upload your resume and get job recommendations based on your skills and experience from LinkedIn.")

# Function to get a valid font path with fallback
def get_font_path():
    font_name = "DejaVuSans.ttf"
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "fonts", font_name),
        os.path.join(os.getcwd(), "fonts", font_name),
        os.path.join(tempfile.gettempdir(), font_name),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path, "DejaVu"
    # Fallback to a default font if DejaVuSans is not found
    st.warning("DejaVuSans.ttf not found. Using built-in Helvetica font (limited Unicode support).")
    return None, "Helvetica"

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Summarizing your resume..."):
        summary = ask_groq(f"Summarize this resume highlighting the skills, education, and experience: \n\n{resume_text}", max_tokens=500)

    with st.spinner("Finding skill gaps..."):
        gaps = ask_groq(f"Analyze this resume and highlight missing skills, certifications, and experiences needed for better job opportunities: \n\n{resume_text}", max_tokens=400)

    with st.spinner("Creating future roadmap..."):
        roadmap = ask_groq(f"Based on this resume, suggest a future roadmap to improve this person's career prospects (Skills to learn, certification needed, industry exposure): \n\n{resume_text}", max_tokens=400)

    st.markdown("---")
    st.header("📑 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)

    st.success("✅ Analysis Completed Successfully!")

    job_type = st.radio("Job Preference", ["remote", "onsite"], index=0)

    if st.button("🔎 Get Job Recommendations"):
        with st.spinner("Fetching job recommendations..."):
            keywords = ask_groq(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary: {summary}",
                max_tokens=100
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Extracted Job Keywords: {search_keywords_clean}")

        with st.spinner("Fetching jobs from LinkedIn..."):
            keyword_list = [k.strip() for k in search_keywords_clean.split(",")]
            linkedin_jobs = fetch_linkedin_jobs(keywords=keyword_list, location="Bangladesh", rows=5, job_type=job_type)

        st.markdown("---")
        st.header("💼 Top LinkedIn Jobs")

        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()
        font_path, font_name = get_font_path()
        if font_path:
            pdf.add_font(font_name, "", font_path, uni=True)
            pdf.set_font(font_name, "", size=12)
        else:
            pdf.set_font(font_name, "", size=12)  # Fallback to Helvetica

        # Corrected line: replaced 'new_x' and 'new_y' with 'ln=1'
        pdf.cell(200, 10, txt="Recommended Jobs", ln=1, align="C")

        if linkedin_jobs:
            for idx, job in enumerate(linkedin_jobs):
                job_title = job.get('title', 'N/A')
                company = job.get('companyName', 'N/A')
                location = job.get('location', 'N/A')
                link = job.get('link', '#')

                st.markdown(f"**{job_title}** at *{company}*")
                st.markdown(f"- 📍 {location}")
                st.markdown(f"- 🔗 <a href='{link}' target='_blank'>View Job</a>", unsafe_allow_html=True)
                st.markdown("---")

                # Clean text for PDF to handle Unicode issues
                job_text = f"{idx+1}. {job_title} at {company}\nLocation: {location}\nLink: {link}\n\n"
                if font_name == "Helvetica":
                    job_text = unidecode.unidecode(job_text)  # Transliterate Unicode to ASCII for Helvetica
                else:
                    job_text = job_text.replace("—", "-")  # Replace em dash for safety
                try:
                    pdf.multi_cell(0, 10, job_text)
                except Exception as e:
                    st.warning(f"Error adding job to PDF: {e}. Skipping this job.")
                    continue

            # Save PDF to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                pdf_path = tmp_file.name
                try:
                    pdf.output(pdf_path)
                    with open(pdf_path, "rb") as f:
                        st.download_button("📄 Download Job List as PDF", f, file_name="job_links.pdf")
                except Exception as e:
                    st.error(f"Error generating PDF: {e}")
                finally:
                    # Clean up temporary file
                    try:
                        os.unlink(pdf_path)
                    except Exception:
                        pass
        else:
            st.warning("No LinkedIn jobs found.")
