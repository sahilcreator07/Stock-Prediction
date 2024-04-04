from app import make_app 

if __name__ == '__main__':
    app = make_app()
    app.run_server(host="127.0.0.1", debug=True)