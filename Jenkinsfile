pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sq1') {
                    // Assuming you have sonar-scanner CLI installed and configured
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=sq1 \
                    -Dsonar.sources=. \
                    -Dsonar.language=py \
                    -Dsonar.python.version=3.x \
                    -Dsonar.host.url=http://10.10.141.175:9000 \
                    -Dsonar.login=your_token
                    '''
                }
            }
        }
    }
}
