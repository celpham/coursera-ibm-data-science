
docker stop jupyter
docker run --rm -p 8888:8888 --name jupyter -v D:\Bexit\DataScience\coursera-ibm-data-science:/home/jovyan/work jupyter/scipy-notebook