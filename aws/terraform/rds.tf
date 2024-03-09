provider "aws" {
  region = "us-west-2"
}

/* resource "aws_db_instance" "encrypted_rds" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "encrypteddb"
  username             = "admin"
  password             = "yoursecurepassword"
  parameter_group_name = "default.mysql8.0"
  delete_automated_backups = true
  skip_final_snapshot  = true
  publicly_accessible  = true
  storage_encrypted    = true

  # Specify the KMS key for encryption - use default RDS key or specify your own
  kms_key_id           = "alias/aws/rds"
} */

resource "aws_db_instance" "non_encrypted_rds" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "nonencrypteddb"
  username             = "admin"
  password             = "yoursecurepassword"
  parameter_group_name = "default.mysql8.0"
  delete_automated_backups = true
  skip_final_snapshot  = true
  publicly_accessible  = true
  storage_encrypted    = false
}
