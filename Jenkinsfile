pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Scan') {
            steps {
                withSonarQubeEnv('sq1') { 
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=sq1 \
                    -Dsonar.sources=. \
                    -Dsonar.language=py \
                    -Dsonar.python.version=3.x \
                    -Dsonar.host.url=http://10.10.141.175:9000 \
                    -Dsonar.login=squ_d2767690cdcc9507fde5c5a572278a20e390c707
                    '''
                }
            }
        }
    }
}
