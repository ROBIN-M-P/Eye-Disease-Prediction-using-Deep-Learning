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
                    sh 'sudo apt install -y python3 python3-pip'
                    sh 'python3 --version'

                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'

                    sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                }
            }
        }
        stage('Run Tests (Example)') {
            steps {
                script {
                    sh 'echo "Running placeholder tests for your Python project..."'
                }
            }
        }
        stage('Build/Package (Example)') {
            steps {
                script {
                    sh 'echo "No specific build step for this project, but you could add packaging here."'
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
