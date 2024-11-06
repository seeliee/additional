# prox gages


prox1_gages <- data.frame(whatNWISdata(siteNumber='0208706575',parameterCd='00060',service='dv'))

for (i in 1:nrow(prox1_gages)) {
  store1=whatNWISdata(siteNumber='0208706575',parameterCd='00060',service='dv')
  prox1_gages <- rbind(prox1_gages,store2)
}

for (row in 1:nrow(prox1_gages)){
  site_Number <- prox1_gages[row,"site_no"]
  startDate <- prox1_gages[row, "begin_date"]
  endDate <- prox1_gages[row, "end_date"]
  Daily3 <- readNWISDaily(site_Number,"00060",startDate,endDate)
}

prox1a <- data.frame(whatNWISdata(siteNumber='0208706575',parameterCd='00065',service='dv'))

for (i in 1:nrow(prox1a)) {
  store1=whatNWISdata(siteNumber='0208706575',parameterCd='00065',service='dv')
  prox1_gages <- rbind(prox1a,store1)
}

for (row in 1:nrow(prox1a)){
  site_Number <- prox1a[row,"site_no"]
  startDate <- prox1a[row, "begin_date"]
  endDate <- prox1a[row, "end_date"]
  Daily3a <- readNWISdv(site_Number,"00065",startDate,endDate)
}

# save
write.csv(Daily1, "D:\\skyla\\Documents\\Sync\\!! College Files\\! INLS 792\\dataretrieval\\gage_data\\neuse_proximity_gages\\prox_discharge1.csv", row.names=FALSE)
write.csv(Daily1a, "D:\\skyla\\Documents\\Sync\\!! College Files\\! INLS 792\\dataretrieval\\gage_data\\neuse_proximity_gages\\prox_height.csv", row.names=FALSE)