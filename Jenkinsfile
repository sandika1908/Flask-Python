pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git url: 'https://github.com/sandika1908/Flask-Python.git'
            }
        }
        stage('Scan') {
            steps {
                // Set the SonarQube environment
                withSonarQubeEnv(installationName: 'sonar01') {
                    // Run the SonarQube scanner for Python
                    sh '''
                        sonar-scanner \
                            -Dsonar.projectKey=flask-python \
                            -Dsonar.sources=. \
                            -Dsonar.language=py \
                            -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }
    }
}
