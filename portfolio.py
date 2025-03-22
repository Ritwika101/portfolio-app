import streamlit as st
from PIL import Image
import base64
st.set_page_config(page_title="Ritwika's Portfolio", layout="wide")
# Custom CSS for Dark Mode and Animations
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")  # Ensure you create a styles.css file for styling

def main():
    
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Experience", "About"])
    
    if page == "Home":
        home()
    elif page == "Skills":
        skills()
    elif page == "Projects":
        projects()
    elif page == "Experience":
        experience()
    elif page == "About":
        about()

def home():
    st.title("👋 Hi, I'm Ritwika!")
    st.write("A Software Engineer with a passion for problem-solving, backend development, and machine learning applications.")
    
    # Image Placeholder (Optional)
    image = Image.open("profile_picture.JPEG")  # Add your profile image
    st.image(image, width=250)
    
    st.markdown("### Connect with me:")
    st.write("[GitHub](https://github.com/Ritwika101) | [LinkedIn](https://linkedin.com/in/your-profile) | [Portfolio](https://ritwika-movie-recommendation.streamlit.app/)")

def skills():
    st.title("🛠 Skills")
    skills_list = [
        ("💡 Problem Solving, Data Structures & Algorithms"),
        ("💻 Programming: C++, JavaScript, Python, Java"),
        ("🔧 Backend Development: Node.js, Spring, REST APIs"),
        ("📩 Message Queues: RabbitMQ, AWS SQS & SNS"),
        ("🗄️ Databases: MongoDB, SQL"),
        ("🛠 Tools: Git, GitHub, VSCode, OpenTelemetry, Google Secret Manager")
    ]
    
    for skill in skills_list:
        st.markdown(f"- {skill}")

def experience():
    st.title("💼 Experience")

    exp_data = [
        ("Software Engineer – Arcesium (March, 2024 - Present)", "arcesium.png", "https://www.arcesium.com/"),
        ("SDE I – LetsTransport (May, 2022 - Dec, 2023)", "lt.png", "https://letstransport.in/"),
        ("Intern – Dell Technologies (2021 - 2022)", "dell.jpg", "https://www.dell.com/")
    ]
    
    # CSS for card styling
    st.markdown("""
        <style>
            .exp-card {
                background-color: #1e1e1e;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 15px;
                box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
                display: flex;
                align-items: center;
            }
            .exp-text {
                font-size: 18px;
                font-weight: bold;
                color: white;
                margin: 0;
            }
            .exp-link {
                text-decoration: none;
                color: #FFCC00;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    for title, image, link in exp_data:
        col1, col2 = st.columns([1, 4])  # Adjust width (1 part image, 4 parts text)
        with col1:
            st.image(image, width=80)  # Properly load local image
        with col2:
            st.markdown(
                f"""
                <div class="exp-card">
                    <p class="exp-text">{title}</p>
                    <a href="{link}" class="exp-link">🔗 Visit Website</a>
                </div>
                """,
                unsafe_allow_html=True
            )

def projects():
    st.title("🚀 Projects")

    projects = [
        ("Payment Management System", "https://github-readme-stats.vercel.app/api/pin/?username=Ritwika101&repo=Payment-management&theme=dark", "https://github.com/Ritwika101/Payment-management"),
        ("Skin Cancer Detection App", "https://github-readme-stats.vercel.app/api/pin/?username=Ritwika101&repo=skin-cancer-detection-webapp&theme=dark", "https://github.com/Ritwika101/skin-cancer-detection-webapp"),
        ("Movie Recommendation System", "https://github-readme-stats.vercel.app/api/pin/?username=Ritwika101&repo=movie-recommendation-app&theme=dark", "https://ritwika-movie-recommendation.streamlit.app/"),
        ("Minimizing Space for Disk Servers", "https://github-readme-stats.vercel.app/api/pin/?username=Ritwika101&repo=Minimizing-space-requirement-for-disk-server&theme=dark", "https://github.com/Ritwika101/Minimizing-space-requirement-for-disk-server")
    ]

    # Inject better CSS styling
    st.markdown("""
        <style>
            .project-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 30px;  /* Space between cards */
                margin-top: 20px;
            }
            .project-card {
                background: #222;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                transition: transform 0.2s ease-in-out;
                box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.1);
                width: 420px;  /* Increased card width */
                height: auto;
            }
            .project-card:hover {
                transform: scale(1.03);
                box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.2);
            }
            .project-card img {
                border-radius: 10px;
                width: 100%;
            }
            .project-card h4 {
                font-size: 18px;
                color: #ddd;
                margin-top: 10px;
                font-weight: normal;
            }
            .project-card a {
                text-decoration: none;
                color: #66ccff;
                font-weight: bold;
                font-size: 15px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Use a single container for better alignment
    st.markdown('<div class="project-container">', unsafe_allow_html=True)

    for title, image_url, link in projects:
        st.markdown(
            f"""
            <div class="project-card">
                <img src="{image_url}" alt="{title}">
                <h4>{title}</h4>
                <a href="{link}" target="_blank">🔗 View Project</a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

def about():
    st.title("📖 About Me")
    st.write("I am passionate about backend development, distributed systems, and solving complex engineering problems.")
    st.write("Currently working at Arcesium, I specialize in Java, Node.js, and system optimizations.")
    
    st.markdown("### 📚 Research")
    st.write("- **IEEE Paper:** [Automation of Skin Cancer Detection with Image Processing Using Efficient and Lightweight CNN Models](https://ieeexplore.ieee.org/abstract/document/10265957)")
    
    st.markdown("### 🏆 Achievements")
    st.write("- **Vice Chancellor’s Award** – Rank 1 in KIIT CSE 2022")
    st.write("- **Finalist** – GE Healthcare Precision Challenge")
    st.write("- **Google Code Jam I/O 2022** – 896th place")

if __name__ == "__main__":
    main()
