# FilePathComputerService

## Project setup
```
apt update
```
```
apt install python3-pip
```
```
pip install flask 
```

### Start FilePathComputerService
```
python3 main.py
```

### Request Example
```
curl -X GET "http://0.0.0.0:8087/filepathcomputer/get_filepath?filename=cartea_noua" -H "accept: application/json"
```