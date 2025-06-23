// Jenkinsfile for Python Project
pipeline {
    agent any

    stages {
        stage('Checkout Code & Git LFS') {
            steps {
                script {
                    // Ensure git-lfs is installed on the agent
                    // We will keep apt install as a general prerequisite
                    sh 'sudo apt update && sudo apt install -y git-lfs'

                    // REMOVED: sh 'git lfs install --force'
                    // The `git lfs pull` command below can work without the install hooks
                    // as long as git-lfs is installed on the system.

                    // Clone the repository
                    git branch: 'main', url: 'https://github.com/ROBIN-M-P/Eye-Disease-Prediction-using-Deep-Learning.git'

                    // Download Git LFS files (the .h5 model)
                    // This is the crucial step that actually fetches the LFS content.
                    sh 'cd Human_Eye_Disease_Prediction && git lfs pull && cd ..'
                }
            }
        }
        // ... rest of your stages remain the same ...
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
