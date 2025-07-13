# PropGuard
# Property Safety Predictor

## 📌 Overview

This project is designed to automate the process of predicting the safety of a property by analyzing documents and images. It uses text extraction from images, post-processing of extracted data, and an AI-driven prediction model to assess property safety.

## 🛠 Features

* **Image to Text Extraction**: Automatically extracts text from scanned images located in the `images/` folder.
* **Data Post-processing**: Cleans and formats the extracted text to prepare it for analysis.
* **Safety Prediction**: Uses the cleaned data to predict if a property is safe.

## 📂 Project Structure

```
organized/
├── images/                     # Folder containing input images of property documents
├── output/                     # Folder to store extracted text and prediction results
├── imgtotxt.py                 # Script to extract text from images
├── post_process.py             # Script to process and clean extracted text
└── property_safety_predictor.py # Script to analyze data and predict property safety
```

## ✅ How to Use

1. **Prepare Data**

   * Place your scanned property document images inside the `images/` folder.

2. **Extract Text**

```bash
python imgtotxt.py
```

This script will extract text from the images and save the results in the `output/` folder.

3. **Post-process Text**

```bash
python post_process.py
```

This script cleans and organizes the extracted text.

4. **Run Safety Prediction**

```bash
python property_safety_predictor.py
```

This script analyzes the processed text and predicts whether the property is safe.

## ⚙️ Requirements

Make sure you have the following installed (example):

* Python 3.x
* pytesseract
* OpenCV
* scikit-learn
* pandas

> Install dependencies using:
>
> ```bash
> pip install -r requirements.txt
> ```

## 📌 Note

* Make sure `output/` folder has write permissions.
* The prediction script may need to be updated with your own model or criteria.

## ✏️ Contributing

Feel free to contribute by improving scripts, adding documentation, or creating new features.

## 📄 License

This project is licensed under the MIT License.

---

**Author:** \[Your Name or Team]

