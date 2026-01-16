variable "aws_region" {
  type        = string
  description = "AWS region"
}

variable "db_name" {
  type        = string
  description = "Postgres database name"
}

variable "db_username" {
  type        = string
  description = "Postgres master username"
}

variable "db_password" {
  type        = string
  description = "Postgres master password"
  sensitive   = true
}
