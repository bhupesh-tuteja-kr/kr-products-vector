# kr-products-vector
similarity search on product database


##########################
#Setup runtime environment

#first, #make sure you have python, pip, and mini-anaconda installed.
conda-env list

#if conda env doesn't exist
conda create --name <env-name> python=<desired-version>
conda init
source ~/.bash_profile

#if you want to remvoe a conda environment
conda remove --name <env-name> --all

#if python lower versin then upgrade it with this
conda python=3.10.0

#activate env
conda activate kr-products-vector

#install required packages
pip install -r requirements.txt

# install and start jupyter notebook
jupyter notebook
#if jupyter not installed then follow this
		conda install jupyter
		pip install ipykernel
		python -m ipykernel install --user --name=<myenv> --display-name "<Python (myenv)>"
        jupyter notebook


#Or skip above and use google collab to upload the notebooks and the csv and then run from there.
https://colab.research.google.com


################
#Running the applicaiton
#Execute "ingest" notebook first to ingest product data into a vector database to enable similarity search.
#Then execute "query" notebook to query data from the vector db for nearest matches.
