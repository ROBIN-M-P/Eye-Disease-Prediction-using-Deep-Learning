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

                    sh 'python3 -m venv venv' // Successfully creates virtual environment
                    sh '. venv/bin/activate' // This activates the venv for subsequent commands in THIS script block

                    // Ensure pip is upgraded within the virtual environment before installing requirements
                    sh 'pip install --upgrade pip'
                    sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi' // Installs dependencies if requirements.txt exists
                }
            }
        }
        stage('Run Tests') { // Stage name updated
            steps {
                script {
                    // Activate the virtual environment for this stage.
                    // It's good practice to reactivate, especially if stages could run in different shell contexts.
                    sh '. venv/bin/activate'

                    // --- CHOOSE ONE OF THE FOLLOWING TEST COMMANDS BASED ON YOUR PROJECT ---
                    // Option 1: If you are using pytest for your tests
                    sh 'pytest'
                    // Option 2: If you are using Python's built-in unittest framework
                    // sh 'python -m unittest discover'

                    sh 'echo "Tests completed."' // Placeholder indicating test execution
                }
            }
        }
        stage('Build/Package') { // Stage name updated
            steps {
                script {
                    // Activate the virtual environment for this stage if needed for packaging tools
                    sh '. venv/bin/activate'

                    // --- ADD YOUR ACTUAL BUILD/PACKAGING COMMANDS HERE ---
                    // Example: Packaging your application into a zip file, excluding the venv and git files
                    sh 'zip -r eye_disease_app.zip . -x "venv/*" -x ".git/*" -x "__pycache__/*"'
                    sh 'echo "Application packaged as eye_disease_app.zip"'

                    // Example: If you have a Dockerfile and want to build a Docker image
                    // (Ensure Docker is installed and configured on your Jenkins agent)
                    // sh 'docker build -t robinmp/eye-disease-prediction:latest .'
                    // sh 'echo "Docker image built: robinmp/eye-disease-prediction:latest"'
                    // sh 'docker push robinmp/eye-disease-prediction:latest' // Optional: Push to a registry
                }
            }
        }
    }
    post {
        always {
            cleanWs() // Cleans the workspace after every build
        }
    }
}
