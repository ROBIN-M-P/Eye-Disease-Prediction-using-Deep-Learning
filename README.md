Eye Disease Prediction using Deep Learning – Full Setup Guide

# 👁️ Human Eye Disease Prediction using Deep Learning

This project uses a trained deep learning model (`.h5`) to classify and predict eye diseases from OCT (Optical Coherence Tomography) images through an interactive **Streamlit** web application.

---

## 🚀 Features

- ✅ TensorFlow‑based trained `.h5` model  
- ✅ Streamlit web interface for instant predictions  
- ✅ Upload OCT retinal images  
- ✅ Python 3.10 + TensorFlow 2.13 support  
- ✅ Git LFS support for large model files  

---

## 🖥️ How to Run (Verified Setup)

### ✅ 1. Clone the Repository with Git LFS

```bash
sudo apt update && sudo apt install -y git-lfs
git lfs install
git clone https://github.com/ROBIN-M-P/Eye-Disease-Prediction-using-Deep-Learning.git
cd Eye-Disease-Prediction-using-Deep-Learning
```

### ✅ 2. Install Python 3.10 (Ubuntu-based systems)

```bash
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-distutils
```

### ✅ 3. Create Virtual Environment and Install Dependencies

```bash
python3.10 -m venv .venv310
source .venv310/bin/activate
pip install --upgrade pip
pip install tensorflow==2.13.0 streamlit pillow
```

### ✅ 4. Download the Model File via Git LFS

```bash
cd Human_Eye_Disease_Prediction
git lfs pull
cd ..
```

### ✅ 5. Run the Streamlit App

```bash
streamlit run Human_Eye_Disease_Prediction/app.py
```

---

## 📂 Project Structure

```
Eye-Disease-Prediction-using-Deep-Learning/
├── Human_Eye_Disease_Prediction/
│   ├── app.py
│   ├── recommendation.py
│   ├── Trained_Model.h5
├── requirements.txt
├── environment.yml
└── README.md
```

---

# 📘 Eye Disease Prediction App – Environment Setup and Cross‑Platform Usage Guide

### 1. Why Python 3.10 + TensorFlow 2.13

The `Trained_Model.h5` file was saved with TensorFlow 2.13 and Keras 2.x.  
Keras 3 (bundled with TF ≥ 2.18) refuses layer names that contain slashes (e.g. “Conv/BatchNorm”).  
Running the model therefore requires the last Keras 2.x release, which in turn is only compiled for Python 3.10 or lower.

### 2. Why Git LFS

The model weighs ≈ 64 MB. Git Large File Storage keeps the main repo light and downloads the weight file on demand.  
Always run `git lfs install` once per machine and `git lfs pull` inside the repo to fetch the actual `.h5`.

### 3. Quick Setup – Ubuntu 24.04 / GitHub Codespaces

```bash
# 1. Install Python 3.10
sudo apt update && sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-distutils

# 2. Create a virtual environment
python3.10 -m venv .venv310 && source .venv310/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install tensorflow==2.13.0 streamlit pillow

# 4. Fetch model
git lfs install && git lfs pull

# 5. Run app
streamlit run Human_Eye_Disease_Prediction/app.py
```

### 4. Setup – Windows 10/11 (Anaconda)

- Install Anaconda or Miniconda.
- Create environment:
    ```bash
    conda create -n eyepred python=3.10 tensorflow=2.13 streamlit pillow git-lfs
    conda activate eyepred
    ```
- Clone repo with Git LFS enabled, then run the app with Streamlit.

### 5. Setup – macOS

- Install Homebrew + Python 3.10 (`brew install python@3.10`) or use Conda.
- Follow the Linux steps from section 3.

### 6. Optional: Convert Model for Keras 3+

Use the TF 2.13 environment to convert your model:

```python
import tensorflow as tf
m = tf.keras.models.load_model('Trained_Model.h5')
m.save('RetinoScan.keras', save_format='keras_v3')
```

Then in TF ≥ 2.18:

```python
tf.keras.models.load_model('RetinoScan.keras', safe_mode=False)
```

### 7. Troubleshooting

- `file signature not found` → run `git lfs pull`
- `name cannot contain character '/'` → You’re on Keras 3; either switch to TF 2.13 or use the converted model.

---

## 👨‍💻 Author

[ROBIN M P](https://github.com/ROBIN-M-P)
