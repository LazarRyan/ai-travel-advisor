import streamlit as st
import openai
import traceback

st.set_page_config(page_title="AI Tourism Advice", layout="wide")

# Debug information
st.sidebar.write("Debug Information:")
st.sidebar.write(f"Streamlit version: {st.__version__}")
st.sidebar.write(f"OpenAI library version: {openai.__version__}")

# Try to get the API key from Streamlit secrets
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.sidebar.write("OpenAI API Key: Found in secrets")
except KeyError:
    st.sidebar.error("OPENAI_API_KEY not found in Streamlit secrets.")
    openai.api_key = None

def get_ai_tourism_advice(destination):
    if not openai.api_key:
        return "OpenAI API key is not set. Unable to fetch tourism advice."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant providing detailed advice about tourist attractions."},
                {"role": "user", "content": f"Provide detailed information about {destination}, including must-visit attractions and cultural insights."}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error in get_ai_tourism_advice: {str(e)}")
        st.error(traceback.format_exc())
        return "Sorry, I couldn't retrieve tourism advice at the moment. Please try again later."

def main():
    st.title("🏛️ AI Tourism Advice")

    if not openai.api_key:
        st.warning("OpenAI API key is not set. The app will not be able to provide tourism advice.")
        st.stop()

    destination = st.text_input("Enter a destination:", "")

    if st.button("Get Tourism Advice"):
        if destination:
            with st.spinner("Fetching tourism advice..."):
                advice = get_ai_tourism_advice(destination)
                st.subheader(f"AI Tourism Advice for {destination}:")
                st.write(advice)
        else:
            st.warning("Please enter a destination.")

    st.info("This AI tourism advice is generated based on the destination you enter. For more accurate results, consider using specific city or country names.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred in the main function: {str(e)}")
        st.error(traceback.format_exc())

st.sidebar.write("Script executed to the end.")
