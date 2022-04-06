
pipeline {
    agent {
        label "ap-se-1-master"
    }
    stages {
        stage("Image build and push in China") {
            steps {
                script {
                    start {"node --max-old-space-size=8192"}
                    sh """
                    node -e 'console.log(v8.getHeapStatistics().heap_size_limit/(1024*1024))'
                    export NODE_OPTIONS="--max-old-space-size=8192"
                    echo $NODE_OPTIONS
                    """
                }
            }
        }
    }
}
