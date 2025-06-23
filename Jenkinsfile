// Jenkinsfile for Python Project
pipeline {
    agent any

    stages {
        stage('Checkout Code & Git LFS') {
            steps {
                script {
                    // Ensure git-lfs is installed on the agent
                    sh 'sudo apt update && sudo apt install -y git-lfs'

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
                    // Use bash for this script block to ensure 'source' command is available
                    sh '''#!/bin/bash
                        sudo apt update
                        sudo apt install -y python3.10 python3.10-venv python3.10-distutils
                        python3.10 --version
                        python3.10 -m venv .venv310
                        source .venv310/bin/activate
                        pip install --upgrade pip
                        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Use bash for this script block
                    sh '''#!/bin/bash
                        source .venv310/bin/activate
                        echo "Running placeholder tests for your Python project..."
                    '''
                }
            }
        }
        stage('Build/Package') {
            steps {
                script {
                    // Use bash for this script block
                    sh '''#!/bin/bash
                        source .venv310/bin/activate
                        zip -r eye_disease_app.zip . -x ".venv310/*" -x ".git/*" -x "__pycache__/*" -x "venv/*"
                        echo "Application packaged as eye_disease_app.zip"
                    '''
                }
            }
        }
        stage('Run Streamlit App (Manual/Deployment Example)') {
            steps {
                script {
                    // Use bash for this script block
                    sh '''#!/bin/bash
                        source .venv310/bin/activate
                        echo "To run the Streamlit app manually after this pipeline completes, use: streamlit run Human_Eye_Disease_Prediction/app.py"
                    '''
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
