try:
    from api import (app, api, LoginController)
except Exception as e:
    print(f"Error in loading... {e}")

api.add_resource(LoginController, '/')

if __name__ == "__main__":
    app.run(debug=True)



