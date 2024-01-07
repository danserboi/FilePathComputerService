import json
from flask import Flask, request, Response
from constants import FILE_PATH_COMPUTER_SERVICE_PORT, GET_FILEPATH_ENDPOINT

app = Flask(__name__)
root_path = "/"
imbrication_level = 3
storage_item_extension = ".extension"

@app.route(GET_FILEPATH_ENDPOINT, methods=['GET'])
def get_filepath():
    filename = request.args.get('filename')
    if not(filename):
        return Response(response=400)
    try:
        filepath = compute_filepath(filename)
    except:
        return Response(response=500)
    resp_body = {
        'filename': filename,
        'filepath': filepath
    }
    return Response(mimetype="application/json", response=json.dumps(resp_body), status=200)

def compute_filepath(filename):
    root_path_for_persistence = root_path
    current_directory_name = ""
    imbrication_levels_left = imbrication_level

    for i in range(len(filename)):
        current_directory_name += filename[i]

        if i % 2 == 1:
            root_path_for_persistence += current_directory_name + "/"
            current_directory_name = ""
            imbrication_levels_left -= 1

            if imbrication_levels_left == 0:
                break

    root_path_for_persistence += filename + storage_item_extension

    return root_path_for_persistence


if __name__ == '__main__':
   app.run(port=FILE_PATH_COMPUTER_SERVICE_PORT)