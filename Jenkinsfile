pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false, url: 'https://github.com/MaksimPotrus/selenium_ide.git'
        }
    }
    
    stage('build') {
  steps {
        sh 'pip3 install --upgrade pip'
        sh 'pip3 install pytest selenium async-generator attrs certifi cffi charset-normalizer h11 idna iniconfig outcome packaging pluggy py pycparser PySocks pytest-html pytest-metadata python-dotenv requests selenium sniffio sortedcontainers tomli tqdm trio trio-websocket webdriver-manager wsproto six'
  }
}
    stage ('Test'){
        steps {
            sh 'pytest test_login.py'
        }
    }
}
}
