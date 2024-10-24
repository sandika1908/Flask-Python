pipeline {
    agent any
    stages {
        stage('Scan Code Quality') {
            steps {
                withSonarQubeEnv('sq1') {
                    withCredentials([string(credentialsId: 'jenkins-python', variable: 'JENKINS_PYTHON')]) {
                        sh '''
                        export PATH=/opt/sonar-scanner/bin:$PATH
                        sonar-scanner \
                        -Dsonar.projectKey=sq1 \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://10.10.141.175:9000 \
                        -Dsonar.login=$JENKINS_PYTHON
                        '''
                    }
                }
            }
        }
    }
}
