import streamlit as st
import spacy
import PyPDF2

def main():
    try:
        st.title("Resume Parser App")
        st.write("Hey there! You can now scan your resume here.")
        
        uploaded_file = st.file_uploader("Upload a resume here", type=["pdf"])
        
        if uploaded_file is not None:
            st.header("Parsed Resume:")
            extraction(uploaded_file)  # Call the extraction function
            
    except Exception as e:
        st.error(f"An error occurred: {e}")

def extraction(file):
    try:
        nlp = spacy.load('output/model-best') 
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            text = text.strip()   
            text = ' '.join(text.split()) 
       
        doc = nlp(text)
        displayed_entities = {}
        for ent in doc.ents:
            if ent.label_ not in displayed_entities:
                displayed_entities[ent.label_] = []
            displayed_entities[ent.label_].append(ent.text)

        for label, texts in displayed_entities.items():
            st.markdown(f'**{label} -**')
            for text in texts:
                if "," in text:
                    parts = text.split(",")
                    for part in parts:
                        st.text(part.strip())
                else:
                    st.text(text)

    except Exception as e:
        st.error(f"An error occurred during extraction: {e}")
                 
    
if __name__ == "__main__":
    main()
