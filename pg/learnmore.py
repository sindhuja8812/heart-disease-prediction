import streamlit as st

def show():
    st.title("📖 Learn More About Heart Health")

    tab1, tab2, tab3, tab4 = st.tabs(["🫀 Facts", "✅ Tips", "🧠 Quiz", "📊 Visual Guide"])

    # --- Tab 1: Facts ---
    with tab1:
        st.header("Important Facts")
        st.markdown("""
        <ul style='font-size: 1.2rem;'>
            <li>Heart disease is the <b>leading cause of death</b> globally.</li>
            <li>It can affect <b>anyone</b>, regardless of gender or age.</li>
            <li><b>Early lifestyle changes</b> can significantly reduce risk.</li>
            <li>High blood pressure, smoking, and obesity are major contributors.</li>
            <li>Physical activity and diet have a <b>huge impact</b> on heart health.</li>
        </ul>
        """, unsafe_allow_html=True)

        # You can still add a Lottie animation here if desired
        # lottie_json = load_lottieurl("your-lottie-url")
        # st_lottie(lottie_json, height=220)

    # --- Tab 2: Tips ---
    with tab2:
        st.header("Practical Prevention Tips")
        col1, col2 = st.columns(2)

        with col1:
            st.success("🥗 Eat a balanced diet (vegetables, fruits, whole grains)")
            st.info("🏃 Stay active daily (at least 30 minutes)")
            st.warning("🚫 Quit smoking and reduce alcohol intake")

        with col2:
            st.success("😴 Prioritize quality sleep (7–8 hours)")
            st.warning("🩺 Regularly monitor blood pressure and cholesterol")
            st.info("🧘 Manage stress with mindfulness and hobbies")

        # Load your existing PDF for download
        pdf_file = "heart_health_guide.pdf"

        with open(pdf_file, "rb") as f:
            st.download_button("📄 Download Heart Health Guide (PDF)", f, file_name="heart_health_guide.pdf")

    # --- Tab 3: Quiz ---
    with tab3:
        st.header("🧠 Test Your Heart Knowledge")
        score = 0
        with st.form("quiz_form"):
            q1 = st.radio("1. What is a major risk factor for heart disease?", ["Low cholesterol", "High blood pressure", "Young age"])
            q2 = st.radio("2. How much exercise is recommended daily?", ["10 minutes", "30 minutes", "2 hours"])
            q3 = st.radio("3. What does 'BMI' stand for?", ["Body Mass Index", "Blood Mass Intake", "Body Muscle Insight"])
            q4 = st.radio("4. Which type of fat is heart-healthy?", ["Trans fat", "Saturated fat", "Unsaturated fat"])
            q5 = st.radio("5. What's a healthy cholesterol level (mg/dL)?", ["Above 240", "Around 200", "Below 100"])
            q6 = st.radio("6. How does stress affect the heart?", ["No effect", "Increases risk", "Decreases blood pressure"])
            q7 = st.radio("7. What is considered high blood pressure?", ["120/80", "130/85", "140/90 or above"])
            q8 = st.radio("8. Which organ does the coronary artery supply?", ["Liver", "Heart", "Lungs"])
            q9 = st.radio("9. Is diabetes a heart disease risk factor?", ["Yes", "No"])
            q10 = st.radio("10. What's a common heart attack symptom?", ["Blurred vision", "Chest pain", "Sneezing"])
            submitted = st.form_submit_button("✅ Submit Answers")

        if submitted:
            if q1 == "High blood pressure": score += 1
            if q2 == "30 minutes": score += 1
            if q3 == "Body Mass Index": score += 1
            if q4 == "Unsaturated fat": score += 1
            if q5 == "Around 200": score += 1
            if q6 == "Increases risk": score += 1
            if q7 == "140/90 or above": score += 1
            if q8 == "Heart": score += 1
            if q9 == "Yes": score += 1
            if q10 == "Chest pain": score += 1

            st.success(f"🎉 You scored {score}/10!")
            if score < 7:
                st.info("📘 Review the Tips and Facts tabs to strengthen your understanding.")
            elif score == 10:
                st.balloons()
                st.success("🏆 Perfect! You're a heart health champion!")

    # --- Tab 4: Visual Guide ---
    with tab4:
        st.header("📊 Visual Summary of Key Factors")
        st.markdown("""
        This chart outlines how various lifestyle habits influence heart health. Green = good habits, Red = risky behaviors.
        """)

        st.markdown("""
        | Lifestyle Factor      | Impact on Heart | Category |
        |------------------------|------------------|----------|
        | Smoking               | 🚫 Increases risk | ❌ Risk   |
        | Regular Exercise      | ✅ Lowers risk    | ✔️ Healthy|
        | High Fat Diet         | 🚫 Increases risk | ❌ Risk   |
        | Balanced Diet         | ✅ Improves health| ✔️ Healthy|
        | Excessive Alcohol     | 🚫 Damaging       | ❌ Risk   |
        | Daily Walks           | ✅ Great for heart| ✔️ Healthy|
        """, unsafe_allow_html=True)

        st.caption("Note: Visual guides are for educational purposes only.")
