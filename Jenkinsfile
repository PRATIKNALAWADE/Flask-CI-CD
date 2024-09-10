pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-todo-app'
        APP_SERVER = 'ubuntu@54.158.215.63'
        APP_SERVER_DIR = '/home/ubuntu/p'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PRATIKNALAWADE/Flaskcicd.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    if (fileExists('Dockerfile')) {
                        docker.build(DOCKER_IMAGE)
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'python -m unittest discover'
                }
            }
        }
        stage('Deploy') {
            steps {
                sshagent(credentials: ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCXMTcCtFPBYtPOOBGXkFLSKYEGAmB6XgGTYTiAzewsZVpX3W/3qiIttnIzEtUcASzvNO2cygs4CICKaVSDgwocZJ44HWnuFdFqmek8+pZl3qFCtJdKBLuRrY80g0b/9K3/LIAmIiSgktkXHZiL17C9s4wB4jEkln1Norg/K2eI/P+11x/bRMM7rk/2QtT9HsLmR4v5Y60AhB6KnJyJWQojWj++hcNtEmLAcI160Eky4E8chtzCOCWvPoA1Pw311v+cu5UKhEYpOQJ1drD3Jc+4N6gufpn6YoXwfl+JHD0/xYG2nsB6WBTbIBerkcWH7xF8WGY/Eb2hdKHV5MAo1Y+ee9t6jze9EQeE0+sHjkOcEQ8nDvHzLhBMmhOGV6T0vSaqtBnF1Mj9oMhDrX0tS5GYSCq2+0AbbOPrwn5ghBI4e26ihU7uAmwDdwzERaYiTCdczxR4NancVBdbibhOWCu4C2BjopACc8KuETsaNYKTo4ZrnM2JF2D+2tW2sXGu6g64B4AobJP9G6CeW/qOvvSqayOd2Gg5yLSUydag9UCD21fGS46LrbLFgJUAlY3lW9d1Ka8VlB2EYDqe1TH6EDuiibBbtrx1MHmob8lWgxpPMJ8lq5795YDzUQLjdbigAEFwoQlyujYdTKsOlBZQBwsECmisoYTkH2qyWWk+/zQJ6w== ubuntu@ip-10-0-17-48']) {
                    sh """
                    ssh ${APP_SERVER} 'rm -rf ${APP_SERVER_DIR}'
                    scp -r . ${APP_SERVER}:${APP_SERVER_DIR}
                    ssh ${APP_SERVER} 'cd ${APP_SERVER_DIR} && docker-compose up -d'
                    """
                }
            }
        }
    }

     post {
        always {
            echo 'Pipeline execution finished!'
        }
    }
}
