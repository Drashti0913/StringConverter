import re
import streamlit as st

def process_string(input_str):
    # Convert all letters to lowercase
    processed_str = input_str.lower()
    # Convert first letter of each word to lowercase
    processed_str = re.sub(r'\b\w', lambda x: x.group().lower(), processed_str)
    # Replace normal spaces and plus signs with underscore
    processed_str = re.sub(r'[\s+]', '_', processed_str)
     # Replace normal spaces with underscore
    processed_str = re.sub(r'\s', '_', processed_str)
    return processed_str

def main():
    st.title("String Processing App")
    input_str = st.text_input("Enter a string:")
    if st.button("Process"):
        processed_str = process_string(input_str)
        st.write("Processed String:", processed_str)

if __name__ == "__main__":
    main()
