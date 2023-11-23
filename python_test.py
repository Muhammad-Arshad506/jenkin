print("jenkins pipelines is runing")


"""
pipeline {
    agent {label 'my-node'}
    
    stages{
        stage('Bulid') {
            steps {
                 git url:'https://github.com/Muhammad-Arshad506/jenkin.git', branch:'main'
            }
        }
        stage('Run JOb') {
            steps {
            sh "python /home/muhammadarshad/workspace/test/python_test.py"
        }
            
        }
        
    }
}


"""
