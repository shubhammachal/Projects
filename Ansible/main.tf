provider "aws" {
  region = "us-east-1"
  
}

resource "aws_key_pair" "ansible-key" {
  key_name   = "ansible-key" 
  public_key = file("~/.ssh/id_rsa.pub") 
}


resource "aws_instance" "server" {
    ami           = "ami-084568db4383264d4" 
    key_name      = "ansible-key" 
    instance_type = "t2.micro"
    count = 3
    
    tags = {
        Name = "server-${count.index + 1}"
    }
  
}