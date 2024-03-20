pipeline {
    agent any
    
    environment {
        LOG_FOLDER = "/tmp/ksql-cicd-lab"
    }

    stages {    
        stage("Apply") {
            steps {
                script {
                    def GIT_DIFF = sh(script: "git diff --name-only HEAD^ HEAD", returnStdout: true).trim()

                    withCredentials([string(credentialsId: 'KSQLDB_URL', variable: 'KSQLDB_URL'),
                                     string(credentialsId: 'KSQLDB_USERNAME', variable: 'KSQLDB_USERNAME'),
                                     string(credentialsId: 'KSQLDB_PASSWORD', variable: 'KSQLDB_PASSWORD')]) {
                        sh """
                            python3 main.py \
                            ${KSQLDB_URL} ${KSQLDB_USERNAME} \
                            ${KSQLDB_PASSWORD} ${LOG_FOLDER} \
                            "${GIT_DIFF}"
                        """
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