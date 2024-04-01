# Resume Parsing using Spacy 3

This repository contains code for parsing resumes (CVs) using Spacy 3 and Scikit-learn. The goal is to extract information such as names, contact details, education, work experience, and other relevant details from resumes in a structured format.




https://github.com/SShadabHussain/Resume-Parsing/assets/93070562/7f65b1e7-7b11-4d11-834c-453dea46334c



## Installation

To get started, make sure you have the required libraries installed. You can install them using pip:

```bash
pip install spacy_transformers
pip install -U spacy
pip install -U scikit-learn
```

## Getting Started

Follow these steps to parse resumes using this code:

1. Clone the GitHub repository:

```bash
git clone https://github.com/SShadabHussain/Resume-Parsing.git
```

2. Load Resume Data

   You will need a dataset of resumes for training and testing. Make sure your resume data is in a JSON format similar to the one provided in the "train_data.json" file within the "data/training" directory.

3. Initialize Configuration

   Run the following command to initialize a configuration file based on your dataset:

```bash
python -m spacy init fill-config /data/training/base_config.cfg /data/training/config.cfg
```

4. Training

   Train the Spacy model on your resume dataset using the following command:

```bash
python -m spacy train /content/Resume-Parsing/data/training/config.cfg --output ./output --paths.train ./train_data.spacy --paths.dev ./test_data.spacy
```

5. Model Testing

   Once the model is trained, you can use it for parsing resumes. Load the trained model and provide a sample resume for parsing:

```python
import spacy

nlp = spacy.load('output/model-best')

resume_text = "My name is Syed Shadab Hussain. I am a data enthusiast. Check out this resume parsing project"
doc = nlp(resume_text)

for ent in doc.ents:
    print(ent.text, "   ->>>>> ", ent.label_)
```


![Pipeline initialization](https://github.com/SShadabHussain/Resume-Parsing/assets/93070562/8aab5adb-20ee-4946-a7e2-41e092f136b5)



6. Parsing PDF Resumes

   If you have resumes in PDF format, you can use the following code to parse them:

```python
!pip install PyMuPDF
import sys
import fitz

fname = 'data/test/Alice Clark CV.pdf'
doc = fitz.open(fname)
text = " "
for page in doc:
    text = text + str(page.get_text())
text = text.strip()
text = ' '.join(text.split())

doc = nlp(text)

for ent in doc.ents:
    print(ent.label_, "   ->>>>> ", ent.text)
```

Please note that this code is provided as a starting point for resume parsing. You may need to customize and fine-tune it based on your specific requirements and the structure of your resume data.

## Issues

If you encounter any issues or have questions about this project, please feel free to open an issue on the GitHub repository: [https://github.com/SShadabHussain/Resume-Parsing](https://github.com/SShadabHussain/Resume-Parsing)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
