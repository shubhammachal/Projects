output "website_endpoint" {
  description = "Website endpoint"
  value       = aws_s3_bucket_website_configuration.website_config.website_endpoint
}
output "bucket_regional_domain_name" {
  description = "Regional domain name of the bucket"
  value       = aws_s3_bucket.website_bucket.bucket_regional_domain_name
}

