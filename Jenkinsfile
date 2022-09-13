
pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
            }
    stages {
        stage('update apt cache') {
            steps {
                sh 'sudo apt update'
            }
        }
        stage('install apache') {
            steps {
                sh 'sudo apt install apache2 -y'
            }
        }
        stage('prune') {
            steps {
                sh 'sudo docker system prune -a -f'
            }
        }
        stage('Build') {
            steps {
                sh 'sudo docker-compose build'
            }
        }
        stage('Unit Test'){
            steps {
                sh '''
                      python3 -m pytest ./converter/tests/test_unit.py
                      
                   '''
            }
        }
    }
}
