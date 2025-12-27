terraform {
  backend "s3" {
    bucket = "ankul-terraform-state"
    key    = "pre/eks.tfstate"
    region = "us-east-1"
  }
}
