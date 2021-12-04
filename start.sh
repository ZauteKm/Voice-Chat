echo "Cloning Repo, Please Wait..."
git clone https://github.com/lushaimusic/vc-userbot.git /vc-userbot
cd /vc-userbot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 main.py
