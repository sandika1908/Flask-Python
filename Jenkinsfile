pipeline {
    agent any
    stages {
        stage('Scan Code Quality') {
            steps {
                withSonarQubeEnv('sq1') {
                    sh '''
                    export PATH=/opt/sonar-scanner/bin:$PATH
                    sonar-scanner \
                    -Dsonar.projectKey=sq1 \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://10.10.141.175:9000 \
                    -Dsonar.login=squ_d2767690cdcc9507fde5c5a572278a20e390c707
                    '''
                }
            }
        }
    }
}
