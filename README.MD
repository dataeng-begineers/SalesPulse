

# Postgres Data Warehouse 


# Dbt buuild tools



# Minio S3 object storage 



# Apache Kafka 

# Fast API service 

# 



docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=ROOTNAME" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   quay.io/minio/minio server /data --console-address ":9001"



 docker run \
    -p 9000:9000 \
    -p 9001:9001 \
    --name minio \
    -v /mnt/drive-1:/mnt/drive-1 \
    -v /mnt/drive-2:/mnt/drive-2 \
    -v /mnt/drive-3:/mnt/drive-3 \
    -v /mnt/drive-4:/mnt/drive-4 \
    -e "MINIO_ROOT_USER=ROOTNAME" \
    -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
    quay.io/minio/minio server http://localhost:9000/mnt/drive-{1...4} --console-address ":9001"


    
