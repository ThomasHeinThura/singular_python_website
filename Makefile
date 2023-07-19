# command for mlflow prefect and setupfile

run :
	# run mlflow add docker network as host `--host 172.18.0.2:5000` to show in docker
	mlflow server --backend-store-uri sqlite:///pages/reports/test.db --host 127.0.0.1:5000 &

	# run streamlit 
	streamlit run Home.py




