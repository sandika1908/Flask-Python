pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Scan') {
            steps {
                withSonarQubeEnv(installationName: 'sonar01') {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                    
                    // Run SonarQube analysis
                    sh '''
                        sonar-scanner \
                            -Dsonar.projectKey=jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://3.93.59.182:9000 \
                            -Dsonar.login=jenkins-sonar
                    '''
                }
            }
        }
    }
}
