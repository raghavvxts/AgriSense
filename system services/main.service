[Unit]
Description=Python Script Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/user/main.py
WorkingDirectory=/home/user
Restart=always
User=user
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target