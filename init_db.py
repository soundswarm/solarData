from solarsystems import init_db, app

def main():
    with app.app_context():
        init_db()

if __name__ == '__main__':
    main()