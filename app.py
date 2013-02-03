from dustinrcdotcom import app


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        app.run(
                sys.argv[1],
                int(sys.argv[2]),
		int(sys.argv[3])
               )
    else:
        app.run()
