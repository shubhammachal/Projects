variable "aws_region" {
    description = "value of the region"
    type = string
    default = "us-east-1"
}

variable "bucket_name" {
    description = "Name of the bucket"
    type = string
    default = "shubham-static-website-bucket"

}
variable "environment" {
    description = "Environment of the bucket"
    type = string
    default = "dev"
  
}