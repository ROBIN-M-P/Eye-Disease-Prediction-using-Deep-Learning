# 👁️ Human Eye Disease Prediction using Deep Learning

This project uses a trained deep learning model (`.h5`) to classify and predict eye diseases from OCT (Optical Coherence Tomography) images through an interactive **Streamlit** web application.

---

## 🚀 Features

- ✅ TensorFlow‑based trained `.h5` model  
- ✅ Streamlit web interface for easy use  
- ✅ Upload OCT retinal images and receive instant predictions  
- ✅ Works with **Conda** or **pip/venv** environments  
- ✅ Git LFS support for large model files  

---

## 🖥️ How to Run

### 1️⃣ Clone the repository

```bash
git lfs install          # run once per system
git clone https://github.com/ROBIN-M-P/test.git
cd test
```

### 2️⃣ Set up the environment

**Using Conda**

```bash
conda env create -f environment.yml
conda activate tf213-env
```

**Using pip + venv**

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Launch the Streamlit app

```bash
streamlit run Human_Eye_Disease_Prediction/app.py
```

---

## 🧪 Requirements

| Library     | Version |
|-------------|---------|
| TensorFlow  | 2.13.0  |
| Streamlit   | 1.46.0  |
| Pillow      | 11.2.1  |

See **`requirements.txt`** or **`environment.yml`** for the full, pinned list.

---

## 📂 Project Structure

```text
test/
├── Human_Eye_Disease_Prediction/
│   ├── app.py
│   ├── recommendation.py
│   ├── Trained_Model.h5
│   └── ...
├── requirements.txt
├── environment.yml
└── README.md
```

---

## ⚠️ Notes

- The `.h5` model is tracked with **Git LFS**. Make sure `git lfs install` is executed **before** cloning so the model downloads correctly.
- The app is tested with **Python 3.10**. Newer versions (3.11/3.12) should work but are not officially validated.

---

## 👨‍💻 Author

[ROBIN M P](https://github.com/ROBIN-M-P)
