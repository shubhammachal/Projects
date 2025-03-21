
terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
    }
  }
  required_version = ">=1.2.0"
}
provider "aws" {
  region = var.aws_region
  
}
#s3 bucket for webiste hosting
resource "aws_s3_bucket" "website_bucket" {
  bucket = var.bucket_name
  tags = {
    Name = "Static Website Bucket"
    Environment = "var.environment"
  }
}

#Bucket ownership control
resource "aws_s3_bucket_ownership_controls" "website_bucket" {
  bucket = aws_s3_bucket.website_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }

}

#website hosting
resource "aws_s3_bucket_website_configuration" "website_config" {

  bucket = aws_s3_bucket.website_bucket.id
  index_document {
    suffix = "index.html"
  }
  error_document {
    key = "error.html"
  }
  
}

#set bucket ACL to public Read
resource "aws_s3_bucket_acl" "website_bucket_acl" {
  depends_on = [aws_s3_bucket_ownership_controls.website_bucket]
  bucket = aws_s3_bucket.website_bucket.id
  acl = "public-read"
}
#public access block
resource "aws_s3_bucket_public_access_block" "website_access_block" {
  bucket = aws_s3_bucket.website_bucket.id
  block_public_acls = false
  block_public_policy = false
  ignore_public_acls = false
  restrict_public_buckets = false
  
}
#allowing public read access
resource "aws_s3_bucket_policy" "website_bucket_policy" {
  bucket = aws_s3_bucket.website_bucket.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid = "PublicReadGetObject",
        Effect = "Allow",
        Principal = "*",
        Action = "s3:GetObject",
        Resource = "${aws_s3_bucket.website_bucket.arn}/*"
      }
    ]
  })
  
}
#index.html
resource "aws_s3_object" "index_html" {
  bucket = aws_s3_bucket.website_bucket.id
  key = "index.html"
  source = "${path.module}/website/index.html"  
  content_type = "text/html"
  etag = filemd5("${path.module}/website/index.html")
}

#error.html
resource "aws_s3_object" "error_html" {
  bucket = aws_s3_bucket.website_bucket.id
  key = "error.html"
  source = "${path.module}/website/error.html"  
  content_type = "text/html"
  etag = filemd5("${path.module}/website/error.html")
}
