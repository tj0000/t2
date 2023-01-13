# t2 - Deploy a lambda function using aws cdk

Requirements:
- T1 - Setup an aws account to use aws cdk - [Tutorial](https://www.youtube.com/watch?v=q1Rwus-uioY) | [Repository](https://github.com/tj0000/t1)
- Install aws cli [Docs](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

        (linux)
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        unzip awscliv2.zip
        sudo ./aws/install

- Install aws cdk

        npm install -g aws-cdk

- python3.9

        sudo apt update
        sudo apt install software-properties-common
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt install python3.9
        python3.9 --version


Documentations:
- [Aws Lambda Container Image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)


Cleanup
        
        (run in root folder)
        cdk destroy