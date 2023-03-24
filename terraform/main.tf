terraform {
  backend "local" {}
  required_providers {
    mongodbatlas = {
      source = "mongodb/mongodbatlas"
      version = "1.8.1"
    }
  }
}

resource "mongodbatlas_cluster" "zoomcamp-finalproject" {
  project_id   = var.project_id
  name         = "zoomcamp-finalproject"
  cluster_type = "REPLICASET"
  replication_specs {
    num_shards = 1
    regions_config {
      region_name     = var.region
      electable_nodes = 3
      priority        = 7
      read_only_nodes = 0
    }
  }
  cloud_backup                 = false
  auto_scaling_disk_gb_enabled = false
  auto_scaling_compute_scale_down_enabled = false

  //Provider Settings "block"
  provider_instance_size_name = "M0"
  provider_name               = "TENANT"
  backing_provider_name       = "AZURE"
  provider_region_name = var.region
}

resource "mongodbatlas_database_user" "admin_user" {
  project_id = var.project_id
  username = var.db_user
  password = var.db_password
  auth_database_name = "admin"
  roles {
    role_name = "readWrite"
    database_name = "worldpopulation"
  }
   roles {
    role_name = "readWrite"
    database_name = "continent_data"
  }
}
