while true
do
	echo "Press [CTRL+C] to stop.."
	sleep 1
    git pull
    gunicorn --bind 0.0.0.0:2083 index:app
done