pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Scan') {
            steps {
                withSonarQubeEnv(installationName: 'sq1') { 
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=sq1 \
                    -Dsonar.sources=. \
                    -Dsonar.language=py \
                    -Dsonar.python.version=3.x \
                    -Dsonar.host.url=http://10.10.141.175:9000 \
                    -Dsonar.login=${{ env.JENKINS_PYTHON_TOKEN }}  # Replace with your environment variable if needed
                    '''
                }
            }
        }
    }
}
