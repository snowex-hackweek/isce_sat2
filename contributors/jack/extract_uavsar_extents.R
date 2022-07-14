# convert uavsar coherence data to shape files for isce_sat2 group work
# july 13th, 2022
# we have failed the group. we are using R

library(terra)

list_coherence_files <-list.files("/Users/jacktarricone/hackweek2022/isce_sat2/coherence", full.names = TRUE)
print(list_coherence_files)

# create shape file from cor data
rast_to_shp <-function(file){

  #import raster
  rast <-rast(file)
  
  # extract raster name
  name <-names(rast)
  
  # convert all values to 1
  rast[rast > 0] <- 1

  # convert to vector data
  rast_shp_file <-as.polygons(rast)

  ## aggregate polyongs up to just data extent
  rast_shp <- aggregate(rast_shp_file, dissolve = TRUE, fun = "mean", cores = 10)
  
  setwd("/Users/jacktarricone/hackweek2022/isce_sat2/")
  writeVector(rast_shp, paste(name,".shp"))
  return(rast_shp)
}

# apply our funciton to the list of rasters
lapply(list_coherence_files, rast_to_shp)
