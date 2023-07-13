import streamlit as st
import openai

# Set OpenAI credentials
openai.api_key = "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"

def get_drug_recommendations(user_input):
    # Implement your logic to get drug recommendations based on user_input
    # You can use GPT-3, GPT-3 embeddings, or any other approach

    # Return a list of drug recommendations
    return ["Drug 1", "Drug 2", "Drug 3"]

def main():
    # Initialize user input variables
    patient_name = ""
    health_condition = ""
    age = ""

    # Set Streamlit app title
    st.title("Drug Recommendation Chatbot")

    # Create a chatbox to take user input
    user_input = st.text_input("Enter your message")

    # Check if user submitted input
    if st.button("Submit"):
        # Store user input details
        details = user_input.split(",")
        if len(details) == 3:
            patient_name = details[0].strip()
            health_condition = details[1].strip()
            age = details[2].strip()

    # Display user input details on the left side of the UI
    st.sidebar.title("User Input Details")
    st.sidebar.write("Patient Name:", patient_name)
    st.sidebar.write("Health Condition:", health_condition)
    st.sidebar.write("Age:", age)

    # Show drug recommendations when the "Drug Recommendations" button is clicked
    if st.button("Drug Recommendations"):
        if patient_name != "" and health_condition != "" and age != "":
            recommendations = get_drug_recommendations(user_input)
            st.write("Drug Recommendations:")
            for drug in recommendations:
                st.write(drug)

if __name__ == "__main__":
    main()