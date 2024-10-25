import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
# Use st.secrets to get the API key in Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

def main():
    st.title("ThinkAI")

    st.write("""
    **ThinkAI - AI Decision-Making Assistant**

    ThinkAI is an AI-powered decision-making assistant that helps users determine the most appropriate AI or machine learning approach based on their needs. Whether you’re looking to automate tasks, analyze data, or generate content, ThinkAI guides you through a series of questions to assess your goals, data availability, and business requirements. The app then provides AI-generated recommendations on suitable models, tools, and approaches to build your solution, empowering users to harness AI effectively even without extensive technical knowledge.
    """)
    

    # Step 1: Identify Your Main Goal
    st.header("Step 1: Identify Your Main Goal")
    goal = st.selectbox(
        "What are you trying to achieve?",
        [
            "Automate a task or make predictions based on data.",
            "Analyze data for insights.",
            "Create new content (e.g., text, images, music).",
            "None of the above."
        ]
    )

    if goal == "None of the above.":
        st.info("AI might not be necessary for your needs.")
        return

    # Allow users to enter a custom description of what they want to achieve
    st.header("Describe Your Objective")
    user_description = st.text_area("Please describe what you want to achieve:", height=100)

    if goal in ["Automate a task or make predictions based on data.", "Analyze data for insights."]:
        # Step 2: Assess Data Availability
        st.header("Step 2: Assess Data Availability")
        data_available = st.radio(
            "Do you have data related to your task?",
            ("Yes", "No")
        )

        if data_available == "No":
            st.warning("You may need to collect data before using AI.")
            return

        # Step 3: Describe Your Data
        st.header("Step 3: Describe Your Data")
        data_type = st.multiselect(
            "What types of data do you have? (Select all that apply)",
            [
                "Numerical data (e.g., sales figures, measurements)",
                "Categorical data (e.g., product categories, labels)",
                "Text data (e.g., reviews, articles)",
                "Image data (e.g., photos, scans)",
                "Audio data (e.g., recordings, speech)",
                "Time series data (e.g., stock prices over time)",
                "Geospatial data (e.g., location coordinates)"
            ]
        )

        if not data_type:
            st.warning("Please select at least one data type.")
            return

        # Step 4: Define Your Objective with the Data
        st.header("Step 4: Define Your Objective with the Data")
        objectives = st.multiselect(
            "What are your objectives? (Select all that apply)",
            [
                "Predict future values or trends",
                "Classify data into categories",
                "Detect anomalies or outliers",
                "Cluster data into groups",
                "Reduce data dimensionality",
                "Generate recommendations",
                "Perform sentiment analysis",
                "Recognize patterns or objects in data",
                "Other (please specify)"
            ]
        )

        if "Other (please specify)" in objectives:
            other_objective = st.text_input("Please specify your other objective:")
            if other_objective:
                objectives.append(other_objective)
            else:
                st.warning("Please specify your other objective.")
                return

        if not objectives:
            st.warning("Please select at least one objective.")
            return

        # Step 5: Consider Business Requirements
        st.header("Step 5: Consider Business Requirements")
        st.write("Consider the following when choosing a model:")

        interpretability = st.checkbox("Interpretability is important")
        accuracy = st.checkbox("High accuracy is critical")
        resources = st.checkbox("Limited computational resources")
        data_size = st.radio("What is the size of your dataset?", ("Small", "Medium", "Large"))
        time_constraints = st.checkbox("Need quick deployment")

        # Option to generate a prompt and get AI assistance
        if st.button("Get AI Assistance"):
            # Build the mega prompt
            prompt = "I am working on a project where I want to "
            if user_description:
                prompt += f"{user_description.strip()}. "
            else:
                prompt += "achieve the following objectives: "
                prompt += ", ".join(objectives).lower() + ". "
            prompt += "I have the following types of data: "
            prompt += ", ".join(data_type).lower() + ". "
            prompt += "Business considerations include: "
            considerations = []
            if interpretability:
                considerations.append("interpretability is important")
            if accuracy:
                considerations.append("high accuracy is critical")
            if resources:
                considerations.append("limited computational resources")
            considerations.append(f"dataset size is {data_size.lower()}")
            if time_constraints:
                considerations.append("need quick deployment")
            prompt += ", ".join(considerations) + ". "
            prompt += "Please provide a short but informative recommendation on suitable machine learning approaches and tools I can use to build this myself, or if I should consult a data scientist."

            st.subheader("Generated Prompt for AI Assistance:")
            st.write(prompt)

            # OpenAI API Call
            with st.spinner("Getting AI assistance..."):
                try:
                    if openai.api_key is None:
                        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
                    else:
                        response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are an expert data scientist providing concise and practical advice."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=600,  # Increased max_tokens to allow longer responses
                            n=1,
                            stop=None,
                            temperature=0.5
                        )

                        ai_response = response.choices[0].message['content'].strip()
                        st.subheader("AI Assistant's Response:")
                        st.write(ai_response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    elif goal == "Create new content (e.g., text, images, music).":
        # Step 2: Specify the Content to Create
        st.header("Step 2: Specify the Content to Create")
        content_type = st.selectbox(
            "What type of content do you want to generate?",
            [
                "Text (e.g., articles, stories)",
                "Images (e.g., artwork, designs)",
                "Audio (e.g., music, voiceovers)",
                "Video (e.g., animations)",
                "Other (please specify)"
            ]
        )

        if content_type == "Other (please specify)":
            content_type = st.text_input("Please specify the type of content:")
            if not content_type:
                st.warning("Please specify the content type.")
                return

        # Step 3: Determine the Complexity
        st.header("Step 3: Determine the Complexity")
        complexity = st.radio(
            "Is the content:",
            ("Simple", "Complex")
        )

        # Option to generate a prompt and get AI assistance
        if st.button("Get AI Assistance"):
            # Build the mega prompt
            prompt = "I want to create "
            if user_description:
                prompt += f"{user_description.strip()} "
            else:
                prompt += f"{complexity.lower()} {content_type.lower()} "
            prompt += "using AI tools. Please provide a short but informative recommendation on suitable AI tools or models I can use to build this myself, or if I should consult a specialist."

            st.subheader("Generated Prompt for AI Assistance:")
            st.write(prompt)

            # OpenAI API Call
            with st.spinner("Getting AI assistance..."):
                try:
                    if openai.api_key is None:
                        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
                    else:
                        response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are an expert AI assistant providing concise and practical advice on AI tools for content creation."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=600,  # Increased max_tokens to allow longer responses
                            n=1,
                            stop=None,
                            temperature=0.5
                        )

                        ai_response = response.choices[0].message['content'].strip()
                        st.subheader("AI Assistant's Response:")
                        st.write(ai_response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    # Final Note
    st.write("---")
    st.write("This application is designed to guide you through the AI decision-making process and provide AI-generated assistance. Use the information and recommendations to advance your AI projects.")

if __name__ == "__main__":
    main()

