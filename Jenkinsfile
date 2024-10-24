pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sq1') {
                    // Run sonar-scanner with the Jenkins credential
                    script {
                        // Fetch the token from Jenkins credentials
                        def sonarToken = credentials('jenkins-python')
                        sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=sq1 \
                        -Dsonar.sources=. \
                        -Dsonar.language=py \
                        -Dsonar.python.version=3.x \
                        -Dsonar.host.url=http://10.10.141.175:9000 \
                        -Dsonar.login=${sonarToken}
                        '''
                    }
                }
            }
        }
    }
}
