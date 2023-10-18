import logging

import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        app_dir='app',
        app='main:app',
        use_colors=True,
        log_level=logging.INFO,
        reload=True
    )
