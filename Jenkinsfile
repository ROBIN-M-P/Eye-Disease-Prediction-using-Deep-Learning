// Jenkinsfile for Python Project
pipeline {
    agent any

    stages {
        stage('Checkout Code & Git LFS') { // Stage name updated for clarity
            steps {
                script {
                    // Ensure git-lfs is installed on the agent
                    sh 'sudo apt update && sudo apt install -y git-lfs'
                    sh 'git lfs install --force'

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
                    // Explicitly install python3.10 and its venv module as per README
                    sh 'sudo apt install -y python3.10 python3.10-venv python3.10-distutils'
                    sh 'python3.10 --version' // Verify python3.10

                    // Create virtual environment using python3.10 and .venv310 name
                    sh 'python3.10 -m venv .venv310'
                    sh 'source .venv310/bin/activate' // Activate the venv

                    // Ensure pip is upgraded within the virtual environment
                    sh 'pip install --upgrade pip'

                    // Install core dependencies. Prefer requirements.txt if comprehensive.
                    // If your requirements.txt covers all these, keep the 'if [ -f requirements.txt ]' line.
                    // Otherwise, uncomment the specific pip install below or add to requirements.txt.
                    // sh 'pip install tensorflow==2.13.0 streamlit pillow'
                    sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi' // Keep this if requirements.txt is complete.
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment for this stage
                    sh 'source .venv310/bin/activate'

                    // --- CHOOSE ONE OF THE FOLLOWING TEST COMMANDS BASED ON YOUR PROJECT ---
                    // Option 1: If you are using pytest for your tests
                    // sh 'pytest'
                    // Option 2: If you are using Python's built-in unittest framework
                    // sh 'python -m unittest discover'
                    sh 'echo "Running placeholder tests for your Python project..."' // Revert to placeholder if tests aren't ready
                }
            }
        }
        stage('Build/Package') {
            steps {
                script {
                    // Activate the virtual environment for this stage if needed for packaging tools
                    sh 'source .venv310/bin/activate'

                    // Example: Packaging your application into a zip file, excluding the venv and git files
                    sh 'zip -r eye_disease_app.zip . -x ".venv310/*" -x ".git/*" -x "__pycache__/*" -x "venv/*"'
                    sh 'echo "Application packaged as eye_disease_app.zip"'
                }
            }
        }
        stage('Run Streamlit App (Manual/Deployment Example)') { // New stage for running the app
            steps {
                script {
                    // Activate the virtual environment
                    sh 'source .venv310/bin/activate'

                    // IMPORTANT: Running this command directly in Jenkins will keep the pipeline running indefinitely
                    // until the Streamlit app is stopped or the pipeline job is terminated.
                    // For actual deployment, you would typically deploy this to a dedicated server
                    // where it can run persistently, rather than within the CI/CD job itself.
                    sh 'echo "To run the Streamlit app manually after this pipeline completes, use: streamlit run Human_Eye_Disease_Prediction/app.py"'
                    // If you wanted to start it and then stop it as part of a test, you'd need background processes and a kill command.
                    // Example (for testing purposes, not for continuous service):
                    // sh 'nohup streamlit run Human_Eye_Disease_Prediction/app.py & > streamlit.log'
                    // sh 'sleep 30' // Give it time to start
                    // sh 'kill $(lsof -t -i:8501)' // Assuming it runs on 8501 and you want to kill it
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
