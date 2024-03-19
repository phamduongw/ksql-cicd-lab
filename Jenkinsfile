pipeline {
    agent any

    stages {    
        stage("Apply") {
            steps {
                script {
                    withCredentials([string(credentialsId: 'KSQLDB_URL', variable: 'KSQLDB_URL'),
                                     string(credentialsId: 'KSQLDB_USERNAME', variable: 'KSQLDB_USERNAME'),
                                     string(credentialsId: 'KSQLDB_PASSWORD', variable: 'KSQLDB_PASSWORD')]) {
                        sh "python3 main.py ${KSQLDB_URL} ${KSQLDB_USERNAME} ${KSQLDB_PASSWORD}"
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}