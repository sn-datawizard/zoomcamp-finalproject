variable "atlas_public_key" {
  type = string
  default = "$${var.lookup('ATLAS_PUBLIC_KEY')}"
}

variable "atlas_private_key" {
  type = string
  default = "$${var.lookup('ATLAS_PRIVATE_KEY')}"
}

variable "project_id" {
  type = string
  default = "$${var.lookup('PROJECT_ID')}"
}

variable "region" {
  type    = string
  default = "EUROPE_WEST"
}

variable "db_user" {
  type = string
  default = "$${var.lookup('DB_USER')}"
}

variable "db_password" {
  type = string
  default = "$${var.lookup('DB_PASSWORD')}"
}

variable "account" {
  type = string
  default = "<account-identifier>"
}

variable "snow_username" {
  type = string
  default = "$${var.lookup('snow_username')}"
}

variable "snow_password" {
  type = string
  default = "$${var.lookup('snow_password')}"
}

variable "snow_db_user" {
  type = string
  default = "$${var.lookup('SNOW_DB_USER')}"
}

variable "snow_db_password" {
  type = string
  default = "$${var.lookup('SNOW_DB_PASSWORD')}"
}
