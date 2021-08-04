from app import app
import views, models




if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5000, debug=True) 