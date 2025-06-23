// Jenkinsfile for Python Project
pipeline {
    agent any

    stages {
        stage('Checkout Code & Git LFS') {
            steps {
                script {
                    // Explicitly define a standard PATH to avoid environmental issues
                    withEnv(["PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"]) {
                        sh 'sudo apt update && sudo apt install -y git-lfs'
                        sh 'git lfs install --force' // Keep the --force
                    }
                    // Clone the repository
                    git branch: 'main', url: 'https://github.com/ROBIN-M-P/Eye-Disease-Prediction-using-Deep-Learning.git'

                    // Download Git LFS files (the .h5 model)
                    sh 'cd Human_Eye_Disease_Prediction && git lfs pull && cd ..'
                }
            }
        }
        stage('Prepare Environment & Install Dependencies') {
            steps {
                script {
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3.10 python3.10-venv python3.10-distutils'
                    sh 'python3.10 --version'

                    sh 'python3.10 -m venv .venv310'
                    sh 'source .venv310/bin/activate'

                    sh 'pip install --upgrade pip'
                    sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'source .venv310/bin/activate'
                    sh 'echo "Running placeholder tests for your Python project..."'
                }
            }
        }
        stage('Build/Package') {
            steps {
                script {
                    sh 'source .venv310/bin/activate'
                    sh 'zip -r eye_disease_app.zip . -x ".venv310/*" -x ".git/*" -x "__pycache__/*" -x "venv/*"'
                    sh 'echo "Application packaged as eye_disease_app.zip"'
                }
            }
        }
        stage('Run Streamlit App (Manual/Deployment Example)') {
            steps {
                script {
                    sh 'source .venv310/bin/activate'
                    sh 'echo "To run the Streamlit app manually after this pipeline completes, use: streamlit run Human_Eye_Disease_Prediction/app.py"'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
