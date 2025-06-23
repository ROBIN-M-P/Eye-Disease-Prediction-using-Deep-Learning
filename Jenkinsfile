// Jenkinsfile for Python Project
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ROBIN-M-P/Eye-Disease-Prediction-using-Deep-Learning.git'
            }
        }
        stage('Prepare Environment & Install Dependencies') {
            steps {
                script {
                    sh 'sudo apt update'
                    // IMPORTANT: Added python3.10-venv to fix virtual environment creation
                    sh 'sudo apt install -y python3 python3-pip python3.10-venv'
                    sh 'python3 --version'

                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate' // This activates the venv for subsequent commands in THIS script block

                    // Ensure pip is upgraded within the virtual environment before installing requirements
                    sh 'pip install --upgrade pip'
                    sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                }
            }
        }
        stage('Run Tests (Example)') {
            steps {
                script {
                    // You might need to reactivate the venv here if this stage runs in a new shell context
                    // sh '. venv/bin/activate'
                    sh 'echo "Running placeholder tests for your Python project..."'
                    // Add your actual test commands here, e.g., 'pytest' or 'python3 -m unittest discover'
                }
            }
        }
        stage('Build/Package (Example)') {
            steps {
                script {
                    sh 'echo "No specific build step for this project, but you could add packaging here."'
                    // Add your build/packaging commands here if any
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
