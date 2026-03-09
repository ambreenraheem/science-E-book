# 🔬 Science E-book for Young Explorers (Ages 5-7)

A multipage interactive science learning platform built with Streamlit, HTML, and CSS.

## 🌟 Features
- **10 Engaging Chapters:** Covering space, plants, animals, energy, and more.
- **Interactive Navbar:** Easy navigation for kids to jump between topics.
- **MCQ Assessment:** A fun quiz to test knowledge with instant scoring and balloons!
- **AI Science Assistant:** A conversational agent to help kids with their questions.
- **Kid-Friendly UI:** Light cream theme with scientific instrument background patterns.

## 🚀 How to Run the Website

### 1. Prerequisites
Make sure you have Python installed. You will also need `streamlit`.

```bash
pip install streamlit
```

### 2. Run the Application
Navigate to the project folder and run:

```bash
streamlit run Home.py
```

### 3. AI Assistant Configuration
To enable the AI Assistant, you can update `Home.py` to include your OpenAI API key using Streamlit secrets or environment variables.

## 📁 Project Structure
- `Home.py`: The landing page and AI Assistant entry point.
- `style.css`: Global styling for the entire website.
- `bg.png`: Custom background image with scientific motifs.
- `pages/`: Contains all 10 chapters and the final assessment quiz.

## 🎨 Design Notes
- **Color Palette:** Light Cream (`#fffdf5`) for a soft, readable feel.
- **Typography:** 'Outfit' font for a modern, rounded, kid-friendly look.
- **Assets:** Custom generated background and high-quality educational illustrations.

---
Created with ❤️ for the next generation of scientists!


#### New impementations
I have carefully checked the project files, and I can confirm that I have not deleted a style.css file.

While the README.md mentions a style.css file, it is not currently present in the project folder. Instead, the styling for the website is built directly into the Python files (like Home.py and the chapter pages) using the st.markdown("<style>...</style>") function. This is actually a very stable way to style Streamlit apps.

If you had a separate style.css file that you would like me to use, please let me know or provide its content, and I can move the internal styles back into it! Otherwise, the project is working perfectly with the current internal styles.