import http.server
import socketserver
import os, argparse

PORT = 8000

def serve(port):
	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", port), Handler)
	print("serving on port", port)
	httpd.serve_forever()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Serve a local directory via HTTP')
	parser.add_argument('directory', type=str,
			help='directory to serve from (relative to current path)')
	parser.add_argument('-p', '--port', metavar='p', type=int, default=PORT,
			help='port to serve on')
	args = parser.parse_args()

	serve_from = os.path.join(os.getcwd(), args.directory)
	if not os.path.isdir(serve_from):
		print(f"'{args.directory}' not found, please make sure the directory exists.")
		quit(1)

	os.chdir(serve_from)
	serve(args.port)
