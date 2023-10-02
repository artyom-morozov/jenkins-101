pipeline {
    agent any

    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          submoduleCfg: [],
                          userRemoteConfigs: [[url: 'https://github.com/artyom-morozov/jenkins-101.git']]
                ])
            }
        }

        stage('Run Python script') {


            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'test_id', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh """
                            python3 run.py $USERNAME $PASSWORD
                        """
                    }
                }
            }
        }
    }
}
