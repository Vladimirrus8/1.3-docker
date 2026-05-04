import argparse
import uvicorn
from fastapi_app import create_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', '-hn', help='Hostname', type=str, default='0.0.0.0')
    parser.add_argument('--port', '-p', help='Port', type=int, default=5050)
    args = parser.parse_args()

    app = create_app()
    uvicorn.run(app, host=args.host, port=args.port, log_level='info')
