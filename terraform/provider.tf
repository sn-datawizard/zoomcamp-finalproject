provider "mongodbatlas" {
  public_key  = var.atlas_public_key
  private_key = var.atlas_private_key
  region    = var.region
}

provider "snowflake" {
  account     = var.account
  username    = var.snow_username
  password    = var.snow_password
}

