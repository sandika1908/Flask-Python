pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Scan') {
            steps {
                withSonarQubeEnv(installationName: 'sonar01') {
                    // Set up and activate virtual environment
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                        
                        # Run SonarQube analysis
                        sonar-scanner \
                            -Dsonar.projectKey=flask-python-project \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://3.93.59.182:9000 \
                            -Dsonar.login=jenkins-sonar
                    '''
                }
            }
        }
    }
}
