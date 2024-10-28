pipeline {
    agent any
    stages {
        stage('Scan Code Quality') {
            steps {
                withSonarQubeEnv('sonar01') {
                    withCredentials([string(credentialsId: 'sonartoken', variable: 'SONAR_TOKEN')]) {
                        sh '''
                        export PATH=/opt/sonar-scanner/bin:$PATH
                        sonar-scanner \
                        -Dsonar.projectKey=sq1 \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://54.144.78.8:9000 \
                        -Dsonar.login=$SONAR_TOKEN
                        '''
                    }
                }
            }
        }
    }
}
